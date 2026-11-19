# CoppeliaSim user manual (Markdown)

The CoppeliaSim user manual, maintained as Markdown and published as a static
site with [VitePress](https://vitepress.dev).

This edition covers the core manual (170 pages). Plugin pages and the versioned
API reference pages (`sim-2`, `sim-1`, `sim`, plugin APIs) are not part of it;
links to those pages point to the
[original HTML manual](https://github.com/CoppeliaRobotics/manual).

## Layout

```
docs/
├── README.md              # table of contents — also the source of the sidebar
├── screenshot.jpg         # illustration for this README
├── screenshot-tabs.jpg
├── .vitepress/            # VitePress config + theme
└── en/
    ├── index.md           # home page (same TOC, site-relative links)
    ├── *.md               # one file per page
    └── images/            # screenshots referenced by the pages

tools/portable.mjs         # turns a build into a file://-friendly folder
verify.py                  # Markdown checks: links, images, fences, stray HTML
CMakeLists.txt             # build orchestration
CMakePresets.json          # portable / hosted / subpath presets
package.json               # VitePress dependency pinning
```

## Static HTML site

Two build modes:

| Mode | Links | Client JS | Use it for |
|---|---|---|---|
| **portable** (default) | all relative (`./assets/…`, `./foo.html`) | one tiny inline script (sidebar only) | opening `index.html` from disk, shipping the manual with an application, any web host or sub-directory, offline use |
| **hosted** | absolute, `base` configurable | yes | a full VitePress site with local search, dark-mode switch, collapsible sidebar and client-side navigation |

### Portable build (default)

```bash
cmake --preset default
cmake --build --preset default     # -> build/html
```

`build/html/index.html` opens directly in a browser (`file://`), with the
sidebar, styling, images and tabbed code blocks intact. It can be copied
anywhere, served from any sub-directory, or zipped and shipped with the
application — no web server and no configuration needed.

A portable build is produced in three steps: VitePress renders with
`base: './'` and starts every sidebar group expanded,
[tools/portable.mjs](tools/portable.mjs) post-processes the result, and a small
inline script is injected into every page. The post-processor

* removes the client bundle and `modulepreload` links (module scripts are
  blocked under `file://`, and `history.pushState()` throws there);
* rewrites the root-absolute image URLs VitePress emits (`/assets/…`) to
  `./assets/…`;
* hides the SPA-only controls (search box, theme switch, mobile menu) via the
  `no-spa` class;
* verifies that every local `href`/`src` resolves on disk, failing the build
  otherwise.

The injected script is a classic (non-module) inline script, so it does run from
`file://`. It restores the sidebar behaviour of the full site: groups are
**collapsed by default**, the path to the current page is expanded, the current
page is highlighted, and the sidebar is scrolled so the current page and its
siblings are visible. Clicking a caret expands/collapses that group (keyboard
accessible); without JavaScript everything stays expanded.

The trade-off is no client-side search and no instant page transitions in this
mode — pages still link to each other normally.

### Hosted build

```bash
cmake --preset hosted
cmake --build --preset hosted      # -> build-hosted/html
```

This is the regular VitePress output (absolute URLs, client bundle) with local
search and client-side navigation. For a sub-path deployment — e.g. a GitHub
Pages *project* site served from `/manual/` — use:

```bash
cmake --preset subpath             # MANUAL_PORTABLE=OFF, MANUAL_BASE=/manual/
cmake --build --preset subpath
```

`-DMANUAL_BASE=/some/path/` works with any base URL, and
`-DMANUAL_OUTPUT_DIR=...` changes the output directory.

### Other targets

| Target | What it does |
|---|---|
| `cmake --build build --target serve` | VitePress dev server with hot reload on <http://localhost:5173> (`-DMANUAL_PORT=` to change) |
| `cmake --build build --target verify` | runs `verify.py` on the Markdown (also part of the default build) |
| `cmake --install build --prefix DIR` | installs the built site |

### What the site config adds

The Markdown carries no site metadata, so
[docs/.vitepress/config.mts](docs/.vitepress/config.mts) does four things:

* **Sidebar** — parsed at build time from `docs/README.md` (see *Editing the
  manual* below), so the navigation follows that table of contents.
* **Legacy link rewriting** — links to the plugin/API pages (`*.htm`) are
  rewritten at render time to the corresponding file in the
  [upstream HTML manual](https://github.com/CoppeliaRobotics/manual), so the
  site has no dead links while the Markdown keeps its relative `.htm` links.
* **Multi-language code tabs** — the manual shows the same snippet once per
  language (mostly Python + Lua, sometimes C++). Consecutive code blocks in
  *different* languages are merged at build time into one VitePress code group
  with tabs, so a page shows a single block with `Python | Lua` tabs instead of
  two stacked listings. Runs are split where a language repeats (two
  consecutive examples each in Python + Lua stay two groups), and blocks
  without a language are left alone. In the portable build the tabs are
  switched by CSS from the underlying radio inputs (`:has()`), so they work
  without the client bundle.
* **Presentation** — images are centred, `[caption]` lines are styled as
  captions, and inline code never breaks identifiers (see
  `docs/.vitepress/theme/custom.css`).

Screenshots are bundled by Vite (hashed file names in `assets/`);
`assetsInlineLimit` is set to 0 so they are not inlined into the HTML.

The tab merging happens only for the rendered site: the Markdown keeps plain,
consecutive fenced blocks, which renders fine on GitHub or in any other
Markdown viewer.

![Multi-language code tabs](docs/screenshot-tabs.jpg)

## Editing the manual

* **Pages** live in `docs/en/`. Links between pages are relative and keep the
  `.md` extension (`[Cameras](cameras.md)`, `[states](simulation.md#states)`).
* **Navigation** comes from [docs/README.md](docs/README.md), a nested bullet
  list: `- [Label](en/page.md)`, with **2 spaces per level**. Entries without a
  link are ignored unless they have linked children. The site reads this file
  at build time; `docs/en/index.md` is the same table of contents with
  site-relative links and is the home page — keep the two in sync when adding
  or moving pages.
* **Images** live in `docs/en/images/` and are referenced from the pages as
  `images/<file>`.
* **Code** is written as plain fenced blocks; consecutive blocks in different
  languages are turned into tabs when the site is built (no special syntax
  needed).
* Cross-references to pages that are not part of this edition stay as `.htm`
  links; they are rewritten to the upstream manual when the site is built.

## Verification

```bash
python3 verify.py        # broken links, missing images, fences, leftover HTML
```

The same check runs automatically as part of the CMake build (before the site is
rendered; disable with `-DMANUAL_VERIFY=OFF`). Current result: 171 files checked,
0 hard errors, 32 anchor warnings (cross-references that were already broken in
the original HTML manual).
