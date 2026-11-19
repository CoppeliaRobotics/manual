// VitePress configuration for the CoppeliaSim manual.
//
// The Markdown pages live in docs/; docs/index.md is the manual's table of
// contents and the source of the sidebar. This config adds the pieces of glue
// that the plain Markdown cannot carry:
//
//   * a sidebar built from that table of contents (docs/index.md);
//   * a markdown-it rule that turns links to the plugin/API pages (*.htm),
//     which are not part of this Markdown edition, into links to the original
//     HTML manual on GitHub, so the site does not ship dead links;
//   * a markdown-it rule that merges consecutive per-language code blocks into
//     one tabbed code group.

import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { defineConfig, type DefaultTheme } from 'vitepress'

const here = path.dirname(fileURLToPath(import.meta.url))
const htmlRoot = path.resolve(here, '..')
const docsRoot = path.resolve(htmlRoot, '..', 'docs')

const UPSTREAM_BLOB = 'https://github.com/CoppeliaRobotics/manual/blob/master/en/'
const UPSTREAM_REPO = 'https://github.com/CoppeliaRobotics/manual'

// Set by the portable build (MANUAL_PORTABLE=1): no client JS is shipped, so
// sidebar groups must start expanded and dead controls are hidden.
const PORTABLE = process.env.MANUAL_PORTABLE === '1'

type TocItem = { text: string; link?: string; items?: TocItem[] }

/** Map a Markdown link from docs/index.md to a VitePress route. */
function routeFor(target: string): string | undefined {
  const clean = target.replace(/^\.\//, '').replace(/\.md$/, '')
  if (!clean || clean.includes('://')) return undefined
  return clean === 'index' ? '/' : `/${clean}`
}

function parseToc(markdown: string): TocItem[] {
  const lines = markdown.split('\n')
  const root: TocItem[] = []
  const stack: { depth: number; items: TocItem[] }[] = [{ depth: -1, items: root }]

  for (const line of lines) {
    const match = /^( *)- (.*)$/.exec(line)
    if (!match) continue
    const depth = Math.floor(match[1].length / 2)
    const body = match[2].trim()
    const link = /^\[(.+?)\]\((.+?)\)$/.exec(body)
    const item: TocItem = link
      ? { text: link[1], link: routeFor(link[2]) }
      : { text: body }

    while (stack.length > 1 && stack[stack.length - 1].depth >= depth) stack.pop()
    const parent = stack[stack.length - 1].items
    parent.push(item)
    item.items = []
    stack.push({ depth, items: item.items })
  }
  return prune(root)
}

/** Drop nodes that point at no page; keep groups that still have children. */
function prune(items: TocItem[]): TocItem[] {
  const out: TocItem[] = []
  for (const item of items) {
    const children = prune(item.items ?? [])
    if (item.link) {
      out.push(children.length ? { ...item, items: children } : { text: item.text, link: item.link })
    } else if (children.length) {
      out.push({ text: item.text, items: children })
    }
  }
  return out
}

function toSidebar(items: TocItem[], depth = 0): DefaultTheme.SidebarItem[] {
  return items.map((item) => {
    const node: DefaultTheme.SidebarItem = { text: item.text }
    if (item.link) node.link = item.link
    if (item.items?.length) {
      node.items = toSidebar(item.items, depth + 1)
      node.collapsed = PORTABLE ? false : depth > 0
    }
    return node
  })
}

function buildSidebar(): DefaultTheme.SidebarItem[] {
  const index = path.join(docsRoot, 'index.md')
  if (!fs.existsSync(index)) return []
  const markdown = fs.readFileSync(index, 'utf-8')
  const [contentsPart, extraPart] = markdown.split(/^## Additional pages$/m)
  const sidebar = toSidebar(parseToc(contentsPart))
  const extra = extraPart ? toSidebar(parseToc(extraPart)) : []
  if (extra.length) sidebar.push({ text: 'Additional pages', collapsed: true, items: extra })
  return sidebar
}

/** Rewrite links to the plugin/API *.htm pages to the upstream HTML manual. */
function legacyLinksPlugin(md: any) {
  const rewrite = (href: string | null): string | null => {
    if (!href || /^(?:https?:|mailto:|#)/.test(href)) return href
    const [pathPart, hash] = href.split('#', 2)
    if (!/\.html?$/i.test(pathPart)) return href
    const clean = pathPart.replace(/^\.\//, '').replace(/^\.\.\//, '')
    if (clean === 'index.html') return UPSTREAM_REPO
    const url = UPSTREAM_BLOB + clean.replace(/\.html$/i, '.htm')
    return hash ? `${url}#${hash}` : url
  }

  md.core.ruler.push('coppelia-legacy-links', (state: any) => {
    for (const token of state.tokens) {
      if (token.type !== 'inline' || !token.children) continue
      for (const child of token.children) {
        if (child.type !== 'link_open') continue
        const href = child.attrGet('href')
        const next = rewrite(href)
        if (next !== href) child.attrSet('href', next)
      }
    }
  })
}

/** Human labels for the languages used by the manual's code samples. */
const CODE_LABELS: Record<string, string> = {
  python: 'Python',
  lua: 'Lua',
  cpp: 'C++',
  c: 'C',
  xml: 'XML',
  java: 'Java',
  javascript: 'JavaScript',
  matlab: 'MATLAB',
  rust: 'Rust',
  bash: 'Bash',
  shell: 'Shell',
  console: 'Console',
  text: 'Text',
}

const langOf = (fence: any): string =>
  String(fence.info || '').trim().split(/\s+/)[0] || ''

/**
 * The manual shows the same snippet in several languages as consecutive code
 * blocks (mostly Python + Lua, sometimes C++). Merge such runs into one
 * VitePress code group ("::: code-group"), which renders CSS-only tabs.
 *
 * VitePress parses code groups as a container, so the tokens are synthesised
 * here: the container renderer takes care of the tab markup, and it needs a
 * "[Label]" in every fence info string to create a tab per language.
 */
function codeTabsPlugin(md: any) {
  md.core.ruler.after('inline', 'coppelia-code-tabs', (state: any) => {
    const tokens = state.tokens
    const result: any[] = []
    let index = 0

    while (index < tokens.length) {
      if (tokens[index].type !== 'fence') {
        result.push(tokens[index])
        index += 1
        continue
      }

      // A run is a sequence of adjacent fences (blank lines in between do not
      // produce tokens), i.e. no paragraph or heading separating them.
      let end = index
      while (end < tokens.length && tokens[end].type === 'fence') end += 1
      const run = tokens.slice(index, end)
      index = end

      // Split the run where a language repeats: "python, lua, python, lua" is
      // two separate examples, not one four-tab group.
      const groups: any[][] = []
      let current: any[] = []
      for (const fence of run) {
        const lang = langOf(fence)
        if (current.length && current.some((f) => langOf(f) === lang)) {
          groups.push(current)
          current = []
        }
        current.push(fence)
      }
      if (current.length) groups.push(current)

      for (const group of groups) {
        const langs = group.map(langOf)
        const mergeable =
          group.length >= 2 &&
          langs.every(Boolean) &&
          new Set(langs).size === langs.length

        if (!mergeable) {
          result.push(...group)
          continue
        }

        const open = new state.Token('container_code-group_open', 'div', 1)
        open.block = true
        const close = new state.Token('container_code-group_close', 'div', -1)
        close.block = true

        for (const fence of group) {
          const lang = langOf(fence)
          fence.info = `${lang} [${CODE_LABELS[lang] ?? lang}]`
        }
        result.push(open, ...group, close)
      }
    }

    state.tokens = result
  })
}

export default defineConfig({
  // The Markdown sources live next to the build system, in ../docs.
  srcDir: '../docs',
  // Keep VitePress' cache out of the source tree (set by the CMake build).
  cacheDir: process.env.MANUAL_CACHE_DIR || '.vitepress/cache',
  // Set MANUAL_BASE when the site is served from a sub-path, e.g.
  // MANUAL_BASE=/manual/ for a GitHub Pages project site.
  base: process.env.MANUAL_BASE || '/',
  lang: 'en-US',
  title: 'CoppeliaSim User Manual',
  description:
    'CoppeliaSim robot simulator manual: scene objects, scripts, APIs, calculation modules and tutorials.',
  cleanUrls: false,
  lastUpdated: false,
  themeConfig: {
    outline: { level: [2, 3], label: 'On this page' },
    nav: [
      { text: 'Manual', link: '/' },
      { text: 'HTML manual', link: UPSTREAM_REPO },
    ],
    sidebar: buildSidebar(),
    search: { provider: 'local' },
    docFooter: { prev: 'Previous page', next: 'Next page' },
    footer: {
      message: 'Converted from the CoppeliaSim HTML manual.',
      copyright: 'Coppelia Robotics',
    },
    returnToTopLabel: 'Back to top',
    sidebarMenuLabel: 'Menu',
    darkModeSwitchLabel: 'Appearance',
  },
  markdown: {
    config: (md) => {
      legacyLinksPlugin(md)
      codeTabsPlugin(md)
    },
  },
  vite: {
    resolve: {
      // The VitePress project lives in html/ and the pages in ../docs, so the
      // page modules cannot walk up to html/node_modules. Point the two
      // runtime imports they need at the installed copies.
      alias: [
        { find: /^vue$/, replacement: path.resolve(htmlRoot, 'node_modules/vue') },
        {
          find: /^vue\/server-renderer$/,
          replacement: path.resolve(htmlRoot, 'node_modules/vue/server-renderer'),
        },
      ],
    },
    build: {
      // The generated pages are large but static; raise the chunk warning limit.
      chunkSizeWarningLimit: 2000,
      // Keep screenshots as real files rather than base64 blobs inside the HTML.
      assetsInlineLimit: 0,
    },
  },
})
