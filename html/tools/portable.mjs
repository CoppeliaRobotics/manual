#!/usr/bin/env node
/**
 * Make a VitePress build self-contained: usable straight from file:// and
 * from any sub-directory of a web server, without configuration.
 *
 * VitePress is a single-page application. Its HTML ships module scripts and a
 * router that calls history.pushState(); module scripts are blocked when a
 * page is opened from disk (origin "null") and pushState throws on file://
 * URLs. The pages themselves are fully server-rendered, so removing the client
 * bundle leaves a working document: static sidebar, static content, plain
 * <a href> links and relative assets.
 *
 * The script also rewrites the root-absolute URLs VitePress emits for
 * Markdown images ("/assets/…") to "./assets/…" — every page sits at the site
 * root, so that is correct from any page and any location.
 *
 * Usage: node tools/portable.mjs <output-dir>
 */

import fs from 'node:fs'
import path from 'node:path'

const outDir = path.resolve(process.argv[2] ?? 'docs/.vitepress/dist')

if (!fs.existsSync(outDir)) {
  console.error(`portable: ${outDir} does not exist`)
  process.exit(1)
}

const SCRIPT_RE = /<script\b[^>]*>[\s\S]*?<\/script>/gi
const MODULE_PRELOAD_RE = /<link\b[^>]*\brel="modulepreload"[^>]*>/gi
const ROOT_ABSOLUTE_URL_RE = /\b(src|href|poster)="\/(?!\/)([^"]*)"/g
const REMAINING_ABSOLUTE_RE = /\b(?:src|href|poster)="\/(?!\/)/

/**
 * Classic inline script (not a module, so it runs from file://). It gives the
 * static sidebar the behaviour of the VitePress one: groups collapse, all are
 * collapsed except the ancestors of the current page, and the current page is
 * scrolled into view.
 */
const SIDEBAR_SCRIPT = `<script>
(function () {
  var sidebar = document.querySelector('.VPSidebar');
  if (!sidebar) return;

  var groups = Array.prototype.slice.call(
    sidebar.querySelectorAll('.VPSidebarItem.collapsible')
  );

  function caretOf(group) {
    var item = group.querySelector(':scope > .item');
    return item ? item.querySelector(':scope > .caret') : null;
  }

  function setCollapsed(group, collapse) {
    group.classList.toggle('collapsed', collapse);
    var caret = caretOf(group);
    if (caret) caret.setAttribute('aria-expanded', String(!collapse));
  }

  groups.forEach(function (group) {
    var caret = caretOf(group);
    if (!caret) return;
    caret.addEventListener('click', function (event) {
      event.preventDefault();
      event.stopPropagation();
      setCollapsed(group, !group.classList.contains('collapsed'));
    });
    caret.addEventListener('keydown', function (event) {
      if (event.key === 'Enter' || event.key === ' ') {
        event.preventDefault();
        setCollapsed(group, !group.classList.contains('collapsed'));
      }
    });
  });

  var links = Array.prototype.slice.call(sidebar.querySelectorAll('a.VPLink'));
  var here = decodeURIComponent(location.pathname);
  var current = null;
  for (var i = 0; i < links.length; i++) {
    try {
      if (decodeURIComponent(new URL(links[i].href).pathname) === here) {
        current = links[i];
        break;
      }
    } catch (error) {
      /* ignore malformed hrefs */
    }
  }

  groups.forEach(function (group) { setCollapsed(group, true); });

  if (!current) return;

  // Expand the path to the current page (its ancestors), and let VitePress'
  // own styles highlight the active item and its parent groups.
  var item = current.closest('.VPSidebarItem');
  if (item) item.classList.add('is-active');

  var node = item && item.parentElement
    ? item.parentElement.closest('.VPSidebarItem')
    : null;
  while (node) {
    if (node.classList.contains('collapsible')) setCollapsed(node, false);
    node.classList.add('has-active');
    var parent = node.parentElement;
    node = parent ? parent.closest('.VPSidebarItem') : null;
  }

  requestAnimationFrame(function () {
    var view = current.getBoundingClientRect();
    var box = sidebar.getBoundingClientRect();
    sidebar.scrollTop +=
      view.top - box.top - (sidebar.clientHeight - view.height) / 2;
  });
})();
</script>`

const stats = {
  pages: 0,
  scripts: 0,
  preloads: 0,
  urls: 0,
  bundles: 0,
  bytes: 0,
  leftovers: [],
}

/** Marks the page as "no VitePress SPA", for CSS that hides SPA-only controls. */
function markNoSpa(html) {
  return html.replace(/<html\b([^>]*)>/i, (match, attrs) => {
    if (/\bclass\s*=/.test(attrs)) {
      return `<html${attrs.replace(/\bclass\s*=\s*"([^"]*)"/, 'class="$1 no-spa"')}>`
    }
    return `<html${attrs} class="no-spa">`
  })
}

function convert(file) {
  const original = fs.readFileSync(file, 'utf8')
  let html = original

  html = html.replace(SCRIPT_RE, () => {
    stats.scripts++
    return ''
  })
  html = html.replace(MODULE_PRELOAD_RE, () => {
    stats.preloads++
    return ''
  })
  html = html.replace(ROOT_ABSOLUTE_URL_RE, (_match, attr, rest) => {
    stats.urls++
    return `${attr}="./${rest}"`
  })
  html = markNoSpa(html)
  if (html.includes('</body>')) {
    html = html.replace('</body>', SIDEBAR_SCRIPT + '</body>')
  }

  if (REMAINING_ABSOLUTE_RE.test(html)) {
    stats.leftovers.push(path.relative(outDir, file))
  }
  if (html !== original) {
    fs.writeFileSync(file, html)
    stats.pages++
  }
}

function walk(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name)
    if (entry.isDirectory()) walk(full)
    else if (entry.name.endsWith('.html')) convert(full)
  }
}

/** Drop the client bundle and its lazy page chunks. */
function pruneScripts(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name)
    if (entry.isDirectory()) {
      pruneScripts(full)
      if (fs.readdirSync(full).length === 0) fs.rmdirSync(full)
    } else if (entry.name.endsWith('.js')) {
      stats.bytes += fs.statSync(full).size
      fs.rmSync(full)
      stats.bundles++
    }
  }
}

walk(outDir)

const assetsDir = path.join(outDir, 'assets')
if (fs.existsSync(assetsDir)) pruneScripts(assetsDir)

/**
 * Every local link must resolve on disk, otherwise the site only looks
 * portable. This catches stale asset hashes and wrong relative prefixes.
 */
function checkLinks(dir) {
  const missing = []
  const ATTR_RE = /\b(?:href|src)="([^"]+)"/g
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name)
    if (entry.isDirectory()) {
      missing.push(...checkLinks(full))
      continue
    }
    if (!entry.name.endsWith('.html')) continue
    const html = fs.readFileSync(full, 'utf8')
    for (const match of html.matchAll(ATTR_RE)) {
      const url = match[1]
      if (
        !url ||
        url.startsWith('#') ||
        url.startsWith('data:') ||
        url.startsWith('mailto:') ||
        /^[a-z]+:\/\//i.test(url)
      ) {
        continue
      }
      const target = path.resolve(full, '..', url.split('#')[0].split('?')[0])
      if (!fs.existsSync(target)) {
        missing.push(`${path.relative(outDir, full)} -> ${url}`)
      }
    }
  }
  return missing
}

const missing = checkLinks(outDir)

console.log(
  `portable: ${stats.pages} pages patched, ` +
    `${stats.scripts} scripts and ${stats.preloads} module preloads removed, ` +
    `${stats.urls} absolute URLs rewritten, ` +
    `${stats.bundles} client bundles dropped ` +
    `(${(stats.bytes / 1024 / 1024).toFixed(1)} MB)`
)

if (missing.length) {
  console.error(
    `portable: ${missing.length} local link(s) do not resolve, e.g. ` +
      missing.slice(0, 5).join(', ')
  )
  process.exit(1)
}

if (stats.leftovers.length) {
  console.error(
    `portable: absolute URLs remain in ${stats.leftovers.length} page(s): ` +
      stats.leftovers.slice(0, 5).join(', ')
  )
  process.exit(1)
}
