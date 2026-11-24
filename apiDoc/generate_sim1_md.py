#!/usr/bin/env python3
"""Generate the Markdown reference pages of the legacy regular API (``sim-1``).

The sim-1 pages are static HTML files in :file:`en/sim-1` (they are no longer
generated from an XML description, unlike the sim-2 pages). This script converts
them to the Markdown layout used by the sim-2 reference pages, written by
:file:`generate_md.py`: title, description, ``Synopsis``, ``Parameters``,
``Return values`` and ``See also`` sections. The HTML fragments are converted by
the same converter (``generate_md.Converter``), and the links are rewritten by a
resolver derived from ``generate_md.LinkResolver``, so that both API versions
read the same way.

The pages indicate that they are deprecated in their description. Such a page is
reduced to a stub: the synopsis, parameters, return values and see-also sections
are dropped, and the description only keeps the deprecation note that points at
the replacement, e.g.::

    # sim.addObjectToCollection

    Deprecated. See [sim.addItemToCollection](simAddItemToCollection.md) instead.

Pages that have no synopsis at all (e.g. ``sim.setDebugWatchList``) are reduced
to their title and description as well, since there is nothing else to convert.

Links to the index pages of the API version (``apiFunctions.htm`` and
``apiConstants.htm`` in the HTML manual) point to :file:`docs/apiFunctions-1.md`
and :file:`docs/apiConstants-1.md`, the index pages of this API version. Links to
the pages of the current API version (``../sim/...`` in the HTML manual,
``../sim-2/...`` here) are rewritten when the sim-2 pages were already generated
by the ``genRegularApiMd`` CMake target (see ``--sim2-dir``); otherwise they stay
``.htm`` links, as do links to pages that have no Markdown counterpart.

The pages are written to :file:`docs/sim-1`, which is part of the Markdown
manual sources: the result is meant to be committed, unlike the sim-2 pages,
which are generated into the build directory and installed at build time.

Example::

    python3 generate_sim1_md.py --verbose
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString, Tag

from generate_md import LinkResolver, PageBuilder

# The section headings used by the static HTML pages, mapped to the kind of
# content they hold. The Markdown section titles are chosen when the page is
# assembled, so that both "Return" and "Return values" end up in the same place.
sectionKinds = {
    'synopsis': 'synopsis',
    'c++ synopsis': 'synopsis',
    'arguments': 'parameters',
    'return': 'returns',
    'return values': 'returns',
    'example': 'example',
    'xml example': 'example',
}

# Fenced code block languages, as in the HTML pages.
fenceLanguages = {
    'c++': 'cpp',
    'c#': 'csharp',
}

# The index pages of the API version, keyed by the page name used by the static
# HTML pages. The Markdown manual keeps one index page per API version, and the
# sim-1 pages must link to the sim-1 ones.
indexPages = {
    'apifunctions': 'apiFunctions-1.md',
    'apiconstants': 'apiConstants-1.md',
}

indexPageRe = re.compile(r'(?:^|/)(apiFunctions|apiConstants)\.html?$', re.IGNORECASE)

# The language tabs of the site list Lua first (see generate_md.py).
synopsisLanguageOrder = {'lua': 0, 'python': 1}


# ---------------------------------------------------------------------------
# HTML helpers
# ---------------------------------------------------------------------------

def unwrapTags(soup, name, className):
    """Replace all matching elements with their content (in place)."""
    for tag in soup.find_all(name, class_=className):
        tag.unwrap()


def plainText(element):
    return ' '.join(element.get_text(' ', strip=True).split()) if element is not None else ''


def sectionHtml(section, heading):
    """The HTML content of a section, without its heading."""
    return ''.join(str(child) for child in section.children if child is not heading)


def codeLanguage(code):
    """The language of a <code> element, as used by the HTML pages."""
    classes = ' '.join(code.get('class') or [])
    match = re.search(r'language-([A-Za-z0-9+#.-]+)', classes)
    language = match.group(1) if match else ''
    return fenceLanguages.get(language, language)


def splitName(li):
    """Split a list item that starts with a ``<strong>`` name.

    The HTML pages write parameters and return values as
    ``<li><strong>name</strong>: description</li>``. Returns ``(name, rest)``
    where ``rest`` is the HTML of the description, or ``(None, None)`` when the
    item does not start with a name.
    """
    children = list(li.children)
    index = 0
    while index < len(children) and isinstance(children[index], NavigableString) \
            and not str(children[index]).strip():
        index += 1
    if index == len(children):
        return None, None
    child = children[index]
    if not isinstance(child, Tag) or child.name != 'strong':
        return None, None
    name = ' '.join(child.get_text(' ', strip=True).split())
    rest = ''.join(str(item) for item in children[index + 1:])
    rest = re.sub(r'^\s*:\s*', '', rest, count=1)
    return name, rest


# ---------------------------------------------------------------------------
# Deprecation notes
# ---------------------------------------------------------------------------

def splitSentences(text):
    """Split a paragraph of Markdown into sentences.

    Dots of link targets (``[label](../page.md)``) do not end a sentence, and
    neither do dotted identifiers when they are not followed by a capitalised
    word or an opening parenthesis.
    """
    sentences = []
    start = 0
    index = 0
    linkDepth = 0
    while index < len(text):
        char = text[index]
        if char == ']' and index + 1 < len(text) and text[index + 1] == '(':
            linkDepth += 1
            index += 2
            continue
        if char == ')' and linkDepth:
            linkDepth -= 1
        elif char == '.' and not linkDepth:
            following = index + 1
            while following < len(text) and text[following] == ' ':
                following += 1
            if following == len(text) or (text[following].isupper()
                                          or text[following] in '("'):
                sentences.append(text[start:index + 1].strip())
                start = following
                index = following
                continue
        index += 1
    tail = text[start:].strip()
    if tail:
        sentences.append(tail)
    return sentences


functionToken = re.compile(r'\bsim(?:\.[A-Za-z_]\w*|[A-Z]\w*)')
markdownLink = re.compile(r'(\[[^\]]*\]\([^)]*\))')


def linkTarget(name, pageName, pagesByTitle):
    """Return the Markdown page that documents ``name``, if there is one."""
    candidates = pagesByTitle.get(name)
    if not candidates or pageName in candidates:
        return None
    if len(candidates) == 1:
        return candidates[0]
    # Prefer the page of the same flavour (C/C++ vs Lua/Python) when a name is
    # used as a title more than once.
    cppPage = pageName.endswith('_cpp.md')
    preferred = [page for page in candidates
                 if page.endswith('_cpp.md') == cppPage]
    return preferred[0] if len(preferred) == 1 else None


def linkFunctionNames(note, pageName, pagesByTitle):
    """Link the replacement functions that the page only names as plain text."""
    parts = markdownLink.split(note)
    for index in range(0, len(parts), 2):  # the odd parts are existing links
        def replace(match):
            name = match.group(0)
            target = linkTarget(name, pageName, pagesByTitle)
            return f'[{name}]({target})' if target else name
        parts[index] = functionToken.sub(replace, parts[index])
    return ''.join(parts)


def deprecationNote(description, pageName, pagesByTitle):
    """Reduce a deprecated page's description to its deprecation note.

    The note is the "Deprecated. ..." sentence, extended with the sentence that
    points at the replacement ("See ... instead."), when there is one. The
    wording is normalized to "Deprecated. See ... instead.", as used by the other
    reference pages. Replacement functions that the page only mentions by name
    are linked to their own page. A description that only says "Deprecated" is
    left without a replacement, since none is mentioned in the page.
    """
    text = ' '.join(description.split())
    if not text:
        return 'Deprecated.'
    sentences = splitSentences(text)
    kept = sentences[:1]
    for sentence in sentences[1:]:
        if re.match(r'(?:see|use)\b', sentence, re.IGNORECASE):
            kept.append(sentence)
            break

    note = ' '.join(kept).strip()
    # "Deprecated Use ..." -> "Deprecated. Use ..." ("Deprecated (yes, ...)" is
    # left alone: it already reads as a sentence).
    note = re.sub(r'^Deprecated(?=\s+[^(\s])', 'Deprecated.', note, count=1)
    # Unify the wording of the replacement sentence.
    note = re.sub(r'^(Deprecated[^.]*\.\s+)(?:use|see)\b', r'\1See', note,
                  flags=re.IGNORECASE)
    note = linkFunctionNames(note, pageName, pagesByTitle)
    note = note.rstrip()
    # A few pages have a typo in the note: "instead)" or "instead..".
    if note.endswith(')') and note.count(')') > note.count('('):
        note = note[:-1].rstrip()
    if not note.endswith(('.', '!', '?')):
        note += '.'
    note = re.sub(r'\.{2,}$', '.', note)
    return note


# ---------------------------------------------------------------------------
# Page building
# ---------------------------------------------------------------------------

class Sim1LinkResolver(LinkResolver):
    """Rewrite links to the local Markdown pages, including the sim-2 pages.

    The static HTML pages link to the index pages of their own API version as
    ``apiFunctions.htm`` and ``apiConstants.htm``, which are ``apiFunctions-1.md``
    and ``apiConstants-1.md`` in the Markdown manual (``apiFunctions.md`` and
    ``apiConstants.md`` index the current API version). They also sometimes link
    to a page of the current API version (``../sim/foo.htm`` in the HTML manual,
    ``../sim-2/foo.md`` here) or to one of its property pages
    (``property_foo.htm``), which live in the sim-2 Markdown directory rather
    than in the sim-1 one.
    """

    def __init__(self, docsDir, pageNames, sim2Names):
        super().__init__(docsDir, pageNames)
        self.sim2Names = sim2Names

    def __call__(self, href):
        path, _, fragment = href.partition('#')
        suffix = '#' + fragment if fragment else ''
        match = indexPageRe.search(path)
        if match:
            return '../' + indexPages[match.group(1).lower()] + suffix

        resolved = super().__call__(href)
        if resolved != href:
            return resolved

        if not re.search(r'\.html?$', path, re.IGNORECASE):
            return href
        if path.startswith('../'):
            if not path[3:].startswith('sim/'):
                return href
        elif '/' in path:
            return href
        name = path.rsplit('/', 1)[-1][:-4]
        for candidate in (name + '.md', name + '_cpp.md'):
            if candidate in self.sim2Names:
                return '../sim-2/' + candidate + suffix
        return href


class Sim1PageBuilder(PageBuilder):
    """Build one Markdown page from its static HTML counterpart."""

    def __init__(self, docsDir, pageNames, sim2Names):
        super().__init__(docsDir, pageNames)
        self.resolveLink = Sim1LinkResolver(docsDir, pageNames, sim2Names)

    # -- sections -----------------------------------------------------------
    def codeBlocks(self, section, sortLanguages=False):
        codes = section.find_all('code')
        if sortLanguages:
            codes = sorted(
                codes,
                key=lambda code: synopsisLanguageOrder.get(codeLanguage(code), 2))
        blocks = []
        for code in codes:
            text = code.get_text().strip('\n')
            if not text.strip():
                continue
            # The HTML pages keep alignment spaces at the end of some synopsis
            # lines; they are invisible and only add noise to the source.
            text = '\n'.join(line.rstrip() for line in text.split('\n'))
            blocks.append(f'```{codeLanguage(code)}\n{text}\n```')
        return '\n\n'.join(blocks)

    def listItems(self, listElement):
        items = []
        for item in listElement.find_all('li', recursive=False):
            name, rest = splitName(item)
            if name is None:
                items.append(self.descriptionBullet(
                    self.convert(item.decode_contents())))
            else:
                items.append(self.bullet(f'- **{name}**', self.convert(rest)))
        return '\n'.join(items)

    def itemsSection(self, section, heading, title, emptyText):
        listElement = section.find('ul')
        if listElement is not None:
            body = self.listItems(listElement)
        else:
            body = self.convert(sectionHtml(section, heading))
        return self.section(title, body or emptyText)

    # -- pages --------------------------------------------------------------
    def pageTitle(self, soup, pageName):
        if soup.find('div', class_='regApiSection') is not None:
            return self.newStyleTitle(soup)
        return self.oldStyleTitle(soup, pageName)

    def build(self, soup, title, pagesByTitle):
        """Return the Markdown page and whether it is a deprecated stub."""
        if soup.find('div', class_='regApiSection') is not None:
            description, sections, seeAlso = self.newStyleContent(soup)
        else:
            description = self.oldStyleDescription(soup)
            sections, seeAlso = {}, None

        deprecated = description.lower().startswith('deprecated')
        if deprecated:
            note = deprecationNote(description, title + '.md', pagesByTitle)
            return self.title(title, note) + '\n', True
        if 'synopsis' not in sections:
            # Nothing else to convert (e.g. a page that only documents that the
            # function is not supported anymore).
            return self.title(title, description) + '\n', False

        blocks = [
            self.title(title, description),
            self.section('Synopsis',
                         self.codeBlocks(sections['synopsis'][0][1],
                                         sortLanguages=True)),
        ]

        if 'parameters' in sections:
            heading, section = sections['parameters'][0]
            blocks.append(self.itemsSection(section, heading, 'Parameters',
                                            'No parameters.'))
        if 'returns' in sections:
            heading, section = sections['returns'][0]
            blocks.append(self.itemsSection(section, heading, 'Return values',
                                            'No return values.'))
        for heading, section in sections.get('example', []):
            exampleTitle = 'XML example' if 'xml' in plainText(heading).lower() \
                else 'Example'
            blocks.append(self.section(exampleTitle, self.codeBlocks(section)))
        blocks.append(self.seeAlsoSection(seeAlso))
        return '\n\n'.join(block for block in blocks if block) + '\n', False

    # -- titles and descriptions -------------------------------------------
    def newStyleTitle(self, soup):
        heading = soup.find('h2')
        if heading is None:
            return ''
        span = heading.find('span')
        title = plainText(span if span is not None else heading)
        return re.sub(r'\s*sim-1\s*$', '', title).strip()

    def oldStyleTitle(self, soup, pageName):
        bar = soup.find('p', class_='subsectionBar')
        if bar is None:
            return ''
        bar = BeautifulSoup(str(bar), 'html.parser').find('p')
        for small in bar.find_all('small'):
            small.decompose()
        # The older pages list both the C/C++ and the Lua/Python name, e.g.
        # "simAddBanner / sim.addBanner".
        title = plainText(bar)
        parts = [part.strip() for part in title.split('/') if part.strip()]
        if len(parts) <= 1:
            return parts[0] if parts else ''
        return parts[0] if pageName.endswith('_cpp') else parts[-1]

    def newStyleContent(self, soup):
        sections = {}
        titleSection = soup.find('div', class_='regApiSection')
        descriptionElement = titleSection.find('p') if titleSection else None
        description = self.convert(descriptionElement.decode_contents()) \
            if descriptionElement is not None else ''
        for section in soup.find_all('div', class_='regApiSection'):
            heading = section.find('h3')
            if heading is None:
                continue
            kind = sectionKinds.get(plainText(heading).lower())
            if kind is not None:
                sections.setdefault(kind, []).append((heading, section))
        return description, sections, self.seeAlsoParagraph(soup)

    def oldStyleDescription(self, soup):
        cell = soup.find('td', class_='apiTableRightDescr')
        if cell is None:
            return ''
        return self.convert(cell.decode_contents())

    def seeAlsoParagraph(self, soup):
        """The paragraph that holds the "See also" list, if any."""
        for paragraph in soup.find_all('p'):
            if paragraph.find_parent('div', class_='regApiSection') is not None:
                continue
            if plainText(paragraph).lower().startswith('see also'):
                return paragraph
        return None

    def seeAlsoSection(self, paragraph):
        if paragraph is None:
            return None
        links = []
        for item in paragraph.find_all('li'):
            anchor = item.find('a')
            if anchor is not None and anchor.get('href'):
                label = plainText(anchor)
                if label:
                    links.append(f'- [{label}]({self.resolveLink(anchor["href"])})')
                    continue
            text = self.convert(item.decode_contents())
            if text:
                links.append('- ' + text.replace('\n', '\n  '))
        uniqueLinks = []
        for link in links:
            if link not in uniqueLinks:
                uniqueLinks.append(link)
        return self.section('See also', '\n'.join(uniqueLinks))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def sim2PageNames(sim2Dir):
    """The sim-2 Markdown page names, or an empty set if they do not exist."""
    if sim2Dir.is_dir():
        return {page.name for page in sim2Dir.glob('*.md')}
    return set()


def parseArgs():
    parser = argparse.ArgumentParser(
        description='Generate the Markdown reference pages of the legacy regular '
                    'API (sim-1) from the static HTML pages.')
    parser.add_argument('--source-dir', default=None,
                        help='directory with the sim-1 .htm pages '
                             '(default: <repository>/en/sim-1)')
    parser.add_argument('--output-dir', default=None,
                        help='directory where the .md pages are written '
                             '(default: <repository>/docs/sim-1)')
    parser.add_argument('--docs-dir', default=None,
                        help='the Markdown manual directory, used to rewrite links '
                             'to manual pages (default: <repository>/docs)')
    parser.add_argument('--sim2-dir', default=None,
                        help='the directory with the sim-2 Markdown pages, used to '
                             'rewrite links to the current API version '
                             '(default: <repository>/build/generated/docs/sim-2, '
                             'when it exists)')
    parser.add_argument('--verbose', action='store_true',
                        help='print each generated page')
    return parser.parse_args()


def main():
    args = parseArgs()
    repository = Path(__file__).resolve().parent.parent
    sourceDir = Path(args.source_dir) if args.source_dir else repository / 'en' / 'sim-1'
    outputDir = Path(args.output_dir) if args.output_dir else repository / 'docs' / 'sim-1'
    docsDir = Path(args.docs_dir) if args.docs_dir else repository / 'docs'
    sim2Dir = Path(args.sim2_dir) if args.sim2_dir \
        else repository / 'build' / 'generated' / 'docs' / 'sim-2'

    if not sourceDir.is_dir():
        raise SystemExit(f'HTML page directory not found: {sourceDir}')
    if not docsDir.is_dir():
        raise SystemExit(f'Markdown manual directory not found: {docsDir}')
    pages = sorted(sourceDir.glob('*.htm'))
    if not pages:
        raise SystemExit(f'No .htm page found in {sourceDir}')

    # Pages that will exist: links to anything else stay .htm links.
    pageNames = {page.stem + '.md' for page in pages}

    # Start from a clean directory so that pages of removed HTML pages do not
    # survive. Only a directory that holds Markdown pages is cleaned.
    if outputDir.exists():
        entries = list(outputDir.iterdir())
        if any(entry.suffix != '.md' for entry in entries):
            raise SystemExit(
                f'{outputDir} contains files other than .md: refusing to clean it')
        for stalePage in entries:
            stalePage.unlink()
    outputDir.mkdir(parents=True, exist_ok=True)

    builder = Sim1PageBuilder(docsDir, pageNames, sim2PageNames(sim2Dir))
    parsed = []
    for page in pages:
        soup = BeautifulSoup(page.read_text(encoding='utf-8', errors='ignore'),
                             'html.parser')
        unwrapTags(soup, 'span', 'apiTableRightCSyn')
        parsed.append((page, soup, builder.pageTitle(soup, page.stem)))

    # Page titles double as the function names that deprecated pages mention in
    # their deprecation note; collect them so that those can be linked.
    pagesByTitle = {}
    for page, _, title in parsed:
        pagesByTitle.setdefault(title, []).append(page.stem + '.md')

    counts = {'page': 0, 'deprecated': 0}
    for page, soup, title in parsed:
        markdown, deprecated = builder.build(soup, title, pagesByTitle)
        if deprecated:
            counts['deprecated'] += 1
        destination = outputDir / (page.stem + '.md')
        destination.write_text(markdown, encoding='utf-8')
        counts['page'] += 1
        if args.verbose:
            print(f'  wrote {destination}')

    print(f'Generated {counts["page"]} Markdown pages '
          f'({counts["deprecated"]} of them deprecated) in {outputDir}')


if __name__ == '__main__':
    main()
