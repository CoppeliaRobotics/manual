#!/usr/bin/env python3
"""Generate the Markdown reference pages of the regular API (``sim-2``).

This is the Markdown counterpart of :file:`generate.py`, which generates the
HTML pages of the regular API from the same XML sources. One Markdown file is
written per page, with the same base name as the HTML page it corresponds to
(e.g. ``sceneObject_getObject.htm`` -> ``sceneObject_getObject.md``).

The page layout follows ``simStubsGen/generate_docs_md.py``, which generates the
Markdown reference of the plugins: title, description, a ``Synopsis`` with one
fenced code block per supported language, ``Parameters``, ``Return values`` and
``See also`` lists. Property pages use ``Type``/``Flags`` sections instead of a
synopsis, as in the HTML pages. Since each page is standalone, the sections use
``##`` headings (the manual's pages do the same); the Lua/Python code blocks are
adjacent, so the site merges them into language tabs, as it does elsewhere.

The HTML fragments found in the XML files (``<a>``, ``<b>``, ``<em>``, ``<br>``,
``<ul>``/``<li>``, ``<code>``, ...) are converted to Markdown. Links to manual
pages (``../foo.htm``) are rewritten to the local Markdown pages as soon as they
exist (see ``--docs-dir``); only links to API pages with no Markdown counterpart
stay ``.htm`` links.

The CMakeLists.txt of this repository runs the script (``genRegularApiMd``
target) and installs the result into ``${COPPELIASIM_MANUAL_DIR}/docs/sim-2``.

Example::

    python3 generate_md.py \\
        --objects-xml=.../sim/objects.xml \\
        --functions-xml=.../sim/functions.xml \\
        --docs-dir=.../manual/docs \\
        --output-dir=.../generated/docs/sim-2
"""

from __future__ import annotations

import argparse
import re
import xml.etree.ElementTree as ET
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString, Tag

# Human-readable names of the API categories (also used by generate.py).
# Maintained here rather than derived from the XML, which only stores the ids.
categories = {
    'c_main': 'Main',
    'c_property': 'Properties',
    'c_stack': 'Stack',
    'c_aux': 'Auxiliary functions',
    'object': 'object',
    'app': 'app',
    'scene': 'scene',
    'collection': 'collection',
    'customObject': 'customObject',
    'script': 'script',
    'mesh': 'mesh',
    'textureData': 'textureData',
    'sceneObject': 'sceneObject',
    'shape': 'shape',
    'joint': 'joint',
    'dummy': 'dummy',
    'marker': 'marker',
    'scriptObject': 'scriptObject',
    'camera': 'camera',
    'light': 'light',
    'graph': 'graph',
    'proximitySensor': 'proximitySensor',
    'visionSensor': 'visionSensor',
    'forceSensor': 'forceSensor',
    'pointCloud': 'pointCloud',
    'ocTree': 'ocTree',
    'customSceneObject': 'customSceneObject',
    'Path': 'Path',
    'file': 'File operations',
    'main': 'General functionality handling',
    'dynamics': 'Dynamics',
    'property': 'Properties',
    'collision': 'Collision detection',
    'distance': 'Distance calculation',
    'rendering': 'Rendering',
    'customization': 'Customization',
    'model': 'Models',
    'selection': 'Selection',
    'creation': 'Object creation',
    'scriptRelated': 'Script related',
    'simulation': 'Simulation',
    'thread': 'Threads',
    'blocking': 'Blocking methods',
    'transformation': 'Coordinates and transformations',
    'hierarchy': 'Scene hierarchy',
    'messaging': 'Messaging',
    'console': 'console',
    'textEditor': 'textEditor',
    'importExport': 'Import/export',
    'Motion': 'Motion functionality',
    'MoveToConfig': 'MoveToConfig',
    'MoveToPose': 'MoveToPose',
    'TimeOptimalTrajectory': 'TimeOptimalTrajectory',
    'RuckigPosition': 'RuckigPosition',
    'RuckigVelocity': 'RuckigVelocity',
    'packing': 'Packing/unpacking',
    'stack': 'Stacks',
    'IK': 'IK',
    'IKObject': 'IKObject',
    'IKJoint': 'IKjoint',
    'IKGroup': 'IKGroup',
    'IKElement': 'IKElement',
    'other': 'Other',
    'drawingObject': 'drawingObject (deprecated, see marker instead)',
}

# Anchors in docs/commonTypes.md, keyed by generic API type.
commonTypeAnchors = {
    'vector': 'vector',
    'vector3': 'vector3',
    'quaternion': 'quaternion',
    'pose': 'pose',
    'matrix': 'matrix',
    'color': 'color',
    'func': 'function',
    'map': 'map',
    'bool': 'bool',
    'int': 'int',
    'long': 'int',
    'float': 'float',
    'string': 'string',
    'any': 'any',
    'handle': 'handle',
    'buffer': 'buffer',
    'enum': 'enum',
    'luaObject': 'luaObject',
}

pythonTypes = {
    'vector': 'numpy.ndarray<float>[]',
    'vector3': 'numpy.ndarray<float>[3,1]',
    'quaternion': 'numpy.ndarray<float>[4]',
    'pose': 'numpy.ndarray<float>[7]',
    'matrix': 'numpy.ndarray<float>[,]',
    'color': 'tuple[4]',
    'func': 'function',
    'map': 'dict',
    'bool': 'bool',
    'int': 'int',
    'long': 'int',
    'float': 'float',
    'string': 'str',
    'any': 'any',
    'handle': 'sim.Object',
    'buffer': 'bytes',
    'enum': 'enum',
    'luaObject': 'luaObject',
}

luaTypes = {
    'vector': 'simEigen.Vector',
    'vector3': 'simEigen.Vector<3>',
    'quaternion': 'simEigen.quaternion',
    'pose': 'simEigen.pose',
    'matrix': 'simEigen.Matrix',
    'color': 'Color',
    'func': 'function',
    'map': 'table',
    'bool': 'bool',
    'int': 'int',
    'long': 'int',
    'float': 'float',
    'string': 'string',
    'any': 'any',
    'handle': 'sim.Object',
    'buffer': 'buffer',
    'enum': 'enum',
    'luaObject': 'luaObject',
}


# ---------------------------------------------------------------------------
# XML helpers (mirror the ones in generate.py)
# ---------------------------------------------------------------------------

def getTxt(node, n):
    node = node.find(n)
    if node is not None:
        # preserve HTML tags (node.text would drop them):
        txt = ET.tostring(node, 'unicode').strip()
        return re.sub(f'^<{n}>(.*)</{n}>$', r'\1', txt, flags=re.DOTALL)
    return None


def parseParams(paramsNode):
    arguments = []
    if paramsNode is None:
        return arguments
    for param in paramsNode.findall('param'):
        arguments.append({
            'name': param.get('name', '').strip(),
            'type': param.get('type', '').strip(),
            'default': param.get('default', '').strip(),
            'description': (getTxt(param, 'description') or '').strip(),
        })
    return arguments


def getPropertyFlags(node):
    retVal = []
    flags = node.find('flags')
    if flags is not None:
        for flag in ('deprecated', 'readable', 'writable', 'removable', 'silent', 'constant'):
            if flags.get(flag) is not None:
                retVal.append(flag)
    if not retVal or retVal[0] == 'deprecated':
        return []
    return retVal


def getDescription(item, fallbackTag):
    """The item's 'description', falling back to another tag when empty."""
    description = (getTxt(item, 'description') or '').strip()
    if not description:
        description = (getTxt(item, fallbackTag) or '').strip()
    return description


def getEnum(node):
    enum = node.find('enum')
    if enum is not None:
        return enum.get('name', '')
    return None


def parseCategories(catNode):
    if catNode is None:
        return []
    return [cat.get('name', '') for cat in catNode.findall('category')]


def fmpToFilename(name, docItemType, objName, auxType=None):
    """Return the (HTML) page name of a function, method or property."""
    name = name.replace('.', '_').replace(':', '_')
    if auxType is None:
        auxType = docItemType
    if auxType == 'function':
        name = name + '_cpp'
    if auxType == 'method':
        if objName:
            name = objName + '_' + name
    if auxType == 'property':
        if objName:
            name = objName + '_' + name
        name = 'property_' + name
    return name + '.htm'


# ---------------------------------------------------------------------------
# Types
# ---------------------------------------------------------------------------

def transformTypeForLanguage(paramType, language):
    baseType = paramType.split('[', 1)[0]
    typeMap = luaTypes if language == 'lua' else pythonTypes
    if baseType not in typeMap:
        raise ValueError(f"Unsupported type '{paramType}' for language '{language}'")
    retVal = typeMap[baseType]
    if baseType != paramType and '[' in paramType:
        suffix = paramType.split('[', 1)[1]
        if language == 'python' and baseType not in ('int', 'float'):
            retVal = 'list<' + retVal + '>[' + suffix
        else:
            retVal = retVal + '[' + suffix
    return retVal


def transformTypeForLanguages(paramType, languages):
    retVal = ''
    cnt = 0
    if 'lua' in languages:
        cnt += 1
        retVal += transformTypeForLanguage(paramType, 'lua')
    if 'python' in languages:
        cnt += 1
        pythonType = transformTypeForLanguage(paramType, 'python')
        if pythonType != retVal:
            if cnt == 2:
                retVal += '/'
            retVal += pythonType
    return retVal or paramType


def escapeAngles(txt):
    return txt.replace('<', '&lt;').replace('>', '&gt;')


def typeLink(display, rawType):
    """Link a type name to docs/commonTypes.md, like the HTML pages do."""
    baseType = rawType.split('[', 1)[0].strip()
    anchor = None
    for genericType in sorted(commonTypeAnchors, key=len, reverse=True):
        if baseType == genericType:
            anchor = commonTypeAnchors[genericType]
            break
    if anchor is None:
        return display
    if '[' in rawType:
        anchor += 'Array'
    return f'[{display}](../commonTypes.md#{anchor})'


def inlineCode(txt):
    txt = txt.strip()
    if not txt:
        return ''
    if '`' in txt:
        return '`` ' + txt + ' ``'
    return '`' + txt + '`'


# ---------------------------------------------------------------------------
# Synopsis
# ---------------------------------------------------------------------------

def transformDefaultForLanguage(default, paramType, language):
    if language == 'python':
        if '[' in paramType:
            default = default.replace('{', '[').replace('}', ']')
        elif paramType.startswith(('map', 'table')):
            if default.startswith('{') and default.endswith('}'):
                content = default[1:-1].strip()
                if not content:
                    return '{}'
                pythonPairs = []
                for pair in content.split(','):
                    if '=' in pair:
                        key, value = pair.split('=', 1)
                        value = value.strip()
                        value = (value.replace('true', 'True')
                                      .replace('false', 'False')
                                      .replace('nil', 'None'))
                        pythonPairs.append(f"'{key.strip()}': {value}")
                    else:
                        pythonPairs.append(pair.strip())
                default = '{' + ', '.join(pythonPairs) + '}'
        elif paramType.startswith('bool'):
            default = default.replace('true', 'True').replace('false', 'False')
        if default == 'nil':
            default = 'None'
    return default


def prepareSynopsis(funcName, inputParams, outputParams, language, module=None):
    if language != 'c':
        inputParams = [dict(p, type=transformTypeForLanguage(p['type'], language),
                            default=transformDefaultForLanguage(p['default'], p['type'], language))
                       for p in inputParams]
        outputParams = [dict(p, type=transformTypeForLanguage(p['type'], language))
                        for p in outputParams]

    outputPart = ''
    if outputParams:
        if language == 'c':
            outputPart = outputParams[0]['type'] + ' '
        else:
            outputPart = ', '.join(f"{p['type']} {p['name']}" for p in outputParams) + ' = '

    inputArgs = []
    for param in inputParams:
        arg = f"{param['type']} {param['name']}"
        if param.get('default'):
            arg += f" = {param['default']}"
        inputArgs.append(arg)

    synopsis = f"{outputPart}{funcName}({', '.join(inputArgs)})"
    if module:
        synopsis = module.partition('-')[0] + " = require('" + module + "')\n" + synopsis
    return synopsis


def isArgumentSeparatorComma(s, pos):
    parenDepth = bracketDepth = braceDepth = 0
    for i in range(pos + 1):
        char = s[i]
        if char == '(':
            parenDepth += 1
        elif char == ')':
            parenDepth -= 1
        elif char == '[':
            bracketDepth += 1
        elif char == ']':
            bracketDepth -= 1
        elif char == '{':
            braceDepth += 1
        elif char == '}':
            braceDepth -= 1
    return parenDepth == 1 and bracketDepth == 0 and braceDepth == 0


def formatSynopsis(synopsis, maxLength):
    """Break a synopsis after argument-separator commas, like generate.py."""
    firstParen = synopsis.find('(')
    if firstParen == -1:
        return synopsis
    indentStr = ' ' * (firstParen + 1)

    result = []
    currentLine = ''
    i = 0
    while i < len(synopsis):
        char = synopsis[i]
        currentLine += char
        if char == ',' and isArgumentSeparatorComma(synopsis, i):
            j = i + 1
            while j < len(synopsis) and synopsis[j] == ' ':
                j += 1
            nextBreak = j
            parenDepth = bracketDepth = braceDepth = 0
            for k in range(i + 1, len(synopsis)):
                c = synopsis[k]
                if c == '(':
                    parenDepth += 1
                elif c == ')':
                    if parenDepth == 0:
                        nextBreak = k
                        break
                    parenDepth -= 1
                elif c == '[':
                    bracketDepth += 1
                elif c == ']':
                    bracketDepth -= 1
                elif c == '{':
                    braceDepth += 1
                elif c == '}':
                    braceDepth -= 1
                elif c == ',' and parenDepth == 0 and bracketDepth == 0 and braceDepth == 0:
                    nextBreak = k
                    break
            nextSegment = synopsis[j:nextBreak].strip()
            if len(currentLine) + 1 + len(nextSegment) > maxLength:
                result.append(currentLine.rstrip())
                currentLine = indentStr
                while i + 1 < len(synopsis) and synopsis[i + 1] == ' ':
                    i += 1
        i += 1
    if currentLine.strip():
        result.append(currentLine.rstrip())
    return '\n'.join(result)


# ---------------------------------------------------------------------------
# HTML -> Markdown
# ---------------------------------------------------------------------------

class Converter:
    """Convert the small subset of HTML found in the XML to Markdown."""

    # A hard line break; replaced with two trailing spaces at the very end,
    # once trailing whitespace has been stripped from the lines.
    BR = '\x00'

    def __init__(self, resolveLink, headingOffset=0):
        self.resolveLink = resolveLink
        self.headingOffset = headingOffset

    def convert(self, fragment):
        soup = BeautifulSoup(fragment or '', 'html.parser')
        text = self._children(soup, 0)
        lines = [line.rstrip() for line in text.split('\n')]

        def isBlank(line):
            return not line.replace(self.BR, '').strip()

        # A hard break at the end of a paragraph is invisible: drop it.
        for index, line in enumerate(lines):
            while line.endswith(self.BR) and \
                    (index + 1 >= len(lines) or isBlank(lines[index + 1])):
                line = line[:-1].rstrip()
            if line.endswith(self.BR):
                line = line[:-1].rstrip() + self.BR
            lines[index] = line

        # Whitespace at the beginning of a line that follows a break is XML
        # indentation; keep it only for (nested) list items.
        listMarker = re.compile(r'^\s+(?:[-*+]|\d+\.) ')
        fixed = []
        for line in lines:
            if fixed and (isBlank(fixed[-1]) or fixed[-1].endswith(self.BR)) \
                    and not listMarker.match(line):
                line = line.lstrip(' ')
            fixed.append(line)
        text = '\n'.join(fixed)

        text = text.replace(self.BR, '  ')
        text = '\n'.join('' if not line.strip() else line for line in text.split('\n'))
        text = re.sub(r'\n{3,}', '\n\n', text)

        # A list needs a blank line before it when it follows a paragraph,
        # otherwise the renderer keeps it in the paragraph.
        lines = text.split('\n')
        fixed = []
        marker = re.compile(r'^[-*+] |^\d+\. ')
        for line in lines:
            if fixed and marker.match(line) and fixed[-1].strip() \
                    and not marker.match(fixed[-1]):
                fixed.append('')
            fixed.append(line)
        return '\n'.join(fixed).strip()

    # -- text ---------------------------------------------------------------
    def _text(self, txt):
        txt = re.sub(r'\s+', ' ', txt)
        return txt.replace('\\', '\\\\').replace('<', '&lt;').replace('>', '&gt;')

    # -- tree ---------------------------------------------------------------
    def _children(self, node, indent):
        return ''.join(self._node(child, indent) for child in node.children)

    def _wrap(self, delimiter, node, indent):
        raw = self._children(node, indent)
        core = raw.strip()
        if not core:
            return raw
        lead = raw[:len(raw) - len(raw.lstrip())]
        trail = raw[len(raw.rstrip()):]
        return f'{lead}{delimiter}{core}{delimiter}{trail}'

    def _code(self, node):
        text = node.get_text()
        classes = ' '.join(node.get('class') or [])
        match = re.search(r'language-([A-Za-z0-9+#.-]+)', classes)
        if match or '\n' in text.strip():
            language = match.group(1) if match else ''
            language = {'c++': 'cpp', 'c#': 'csharp'}.get(language, language)
            return '\n\n```' + language + '\n' + text.strip('\n') + '\n```\n\n'
        return inlineCode(text)

    def _list(self, node, indent):
        lines = []
        items = [child for child in node.children
                 if isinstance(child, Tag) and child.name == 'li']
        ordered = (node.name == 'ol')
        for index, item in enumerate(items):
            marker = f'{index + 1}.' if ordered else '-'
            anchors = ''
            if item.get('id'):
                anchors = f'<a id="{item["id"]}"></a> '
            raw = self._children(item, indent + len(marker) + 1)
            rawLines = [line for line in raw.split('\n') if line.strip()]
            if not rawLines:
                lines.append(' ' * indent + marker + (' ' + anchors if anchors else ''))
                continue
            first, rest = rawLines[0].strip(), rawLines[1:]
            lines.append(' ' * indent + f'{marker} {anchors}{first}')
            continuation = ' ' * (indent + len(marker) + 1)
            for line in rest:
                if line.startswith(continuation):
                    lines.append(line)
                else:
                    lines.append(continuation + line.strip())
        return '\n'.join(lines)

    def _table(self, node, indent):
        rows = []
        for row in node.find_all('tr'):
            cells = [self._children(cell, indent).strip()
                     for cell in row.find_all(['td', 'th'])]
            if cells:
                rows.append('| ' + ' | '.join(cells) + ' |')
        return '\n\n' + '\n'.join(rows) + '\n\n'

    def _node(self, node, indent):
        if isinstance(node, NavigableString):
            return self._text(str(node))
        if not isinstance(node, Tag):
            return ''

        name = (node.name or '').lower()

        if name in ('script', 'style'):
            return ''
        if name == 'br':
            return self.BR + '\n'
        if name == 'hr':
            return '\n\n---\n\n'
        if name in ('b', 'strong'):
            return self._wrap('**', node, indent)
        if name in ('em', 'i'):
            return self._wrap('*', node, indent)
        if name == 'code':
            return self._code(node)
        if name == 'pre':
            return '\n\n```\n' + node.get_text().strip('\n') + '\n```\n\n'
        if name == 'a':
            href = (node.get('href') or '').strip()
            label = self._children(node, indent).strip()
            if not label:
                return ''
            if not href:
                return label
            target = self.resolveLink(href)
            # Links to pages outside the manual stay as plain text.
            return label if target is None else f'[{label}]({target})'
        if name in ('ul', 'ol'):
            return '\n' + self._list(node, indent) + '\n'
        if name == 'li':
            return self._children(node, indent)
        if re.fullmatch(r'h[1-6]', name):
            level = min(6, max(1, int(name[1]) + self.headingOffset))
            return f'\n\n{"#" * level} {self._children(node, indent).strip()}\n\n'
        if name == 'p':
            return '\n\n' + self._children(node, indent).strip() + '\n\n'
        if name in ('table', 'thead', 'tbody'):
            return self._table(node, indent)
        if name == 'div':
            return '\n' + self._children(node, indent) + '\n'
        return self._children(node, indent)


# ---------------------------------------------------------------------------
# Links
# ---------------------------------------------------------------------------

class LinkResolver:
    """Rewrite links to manual pages to their local Markdown pages.

    A link is rewritten as soon as its Markdown page exists; links whose page
    has no Markdown counterpart return ``None`` and are emitted as plain text,
    so the generated pages never link to a page that is not part of the manual.

    Resolution is deliberately forgiving, because the XML cross-references are
    not maintained as carefully as the pages themselves:

    * page names are matched case-insensitively (``scene_getobject`` ->
      ``scene_getObject``);
    * a page whose name is not found as written is looked up by its item name
      (``shape.dynamicallyEnabled`` -> ``property_sceneObject_dynamicallyEnabled``);
    * same-directory links may point at a page of the ``sim-1`` set
      (``simGetScript`` -> ``../sim-1/simGetScript.md``).

    A ``#fragment`` is kept even when the local page does not define it: the
    Markdown pages are abridged in places (e.g. apiConstants.md has fewer
    constants than apiConstants.htm), and the site no longer falls back to the
    HTML manual, so an anchor that lands at the top of the page beats a link
    that goes nowhere.
    """

    def __init__(self, docsDir, generatedNames, itemIndex=None):
        self.generatedNames = generatedNames
        self.generatedByLower = {name.lower(): name for name in generatedNames}
        # (kind, item name, class name) -> page name
        self.itemIndex = itemIndex or {}
        self.docsByLowerName = {}
        self.sim1ByLowerName = {}
        if docsDir is not None and docsDir.is_dir():
            for page in docsDir.glob('*.md'):
                self.docsByLowerName[page.name.lower()] = page.name
            sim1 = docsDir / 'sim-1'
            if sim1.is_dir():
                for page in sim1.glob('*.md'):
                    self.sim1ByLowerName[page.name.lower()] = page.name

    def _byItemName(self, stem):
        """Page whose item name is the trailing part of ``stem``, if unique."""
        best, hits = '', set()
        for (kind, name, className), page in self.itemIndex.items():
            if not stem.lower().endswith('_' + name.lower()):
                continue
            if len(name) > len(best):
                best, hits = name, {page}
            elif len(name) == len(best):
                hits.add(page)
        return next(iter(hits)) if len(hits) == 1 else None

    def resolveRef(self, itemKind, refName, refObjName, auxType):
        """Resolve a see-also reference, tolerating a stale class prefix."""
        resolved = self(fmpToFilename(refName, itemKind, refObjName, auxType))
        if resolved is not None:
            return resolved
        kind = 'property' if auxType == 'property' else 'method'
        matches = [(className, page) for (k, name, className), page in self.itemIndex.items()
                   if k == kind and name.lower() == refName.lower()]
        if len(matches) > 1 and refObjName:
            wanted = refObjName.lower()
            matches = [m for m in matches
                       if m[0].lower() == wanted or m[0].lower().startswith(wanted)
                       or wanted.startswith(m[0].lower())]
        return matches[0][1] if len(matches) == 1 else None

    def __call__(self, href):
        if not href:
            return href
        if re.match(r'^(?:https?:|mailto:|#)', href):
            return href

        path, _, fragment = href.partition('#')
        suffix = '#' + fragment if fragment else ''
        if not re.search(r'\.html?$', path, re.IGNORECASE):
            return href

        if path.startswith('../'):
            name = path[3:]
            if '/' in name:
                return None
            markdown = name[:-4] + '.md'
            # Use the directory listing rather than a file-system probe: the
            # manual pages are matched case-insensitively (e.g. ocTrees.htm is
            # octrees.md), and a case-insensitive file system would otherwise
            # accept a name that the site renderer cannot resolve.
            alternative = self.docsByLowerName.get(markdown.lower())
            if alternative is not None:
                return '../' + alternative + suffix
            return None

        # Link to a page in the same directory (another sim-2 page).
        markdown = path[:-4] + '.md'
        stem = path[:-4]
        for candidate in (markdown, stem + '_cpp.md'):  # C-function page
            if candidate in self.generatedNames:
                return candidate + suffix
        for candidate in (markdown, stem + '_cpp.md'):
            hit = self.generatedByLower.get(candidate.lower())
            if hit is not None:
                return hit + suffix
        # Some referenced items live in the sim-1 set rather than in sim-2.
        hit = self.sim1ByLowerName.get(markdown.lower())
        if hit is not None:
            return '../sim-1/' + hit + suffix
        hit = self._byItemName(stem)
        if hit is not None:
            return hit + suffix
        return None


# ---------------------------------------------------------------------------
# Markdown page building
# ---------------------------------------------------------------------------

class PageBuilder:
    def __init__(self, docsDir, generatedNames, itemIndex=None):
        self.resolveLink = LinkResolver(docsDir, generatedNames, itemIndex)

    def resolveRef(self, itemKind, refName, refObjName, auxType):
        return self.resolveLink.resolveRef(itemKind, refName, refObjName, auxType)

    # -- small helpers ------------------------------------------------------
    def convert(self, fragment, headingOffset=0):
        return Converter(self.resolveLink, headingOffset).convert(fragment)

    def section(self, title, body):
        body = (body or '').strip()
        if not body:
            return None
        return f'## {title}\n\n{body}'

    def title(self, title, description):
        block = f'# {title}'
        description = (description or '').strip()
        if description:
            block += '\n\n' + description
        return block

    def synopsisSection(self, item, name):
        languages = [language.strip()
                     for language in (item.get('lang') or 'lua').split(',')]
        # The plugin reference lists Lua first; do the same for the code blocks
        # (they are merged into language tabs when the site is rendered).
        languages.sort(key=lambda language: {'lua': 0, 'python': 1}.get(language, 2))

        module = (item.get('module') or '').strip() or None
        callCmd = (item.get('call-cmd') or '').strip() or name

        rawInput = parseParams(item.find('params'))
        rawOutput = parseParams(item.find('returns'))

        blocks = []
        for languageName in languages:
            synopsis = formatSynopsis(
                prepareSynopsis(callCmd, rawInput, rawOutput, languageName, module),
                100,
            )
            fence = {'c': 'cpp'}.get(languageName, languageName)
            blocks.append(f'```{fence}\n{synopsis}\n```')
        return self.section('Synopsis', '\n\n'.join(blocks))

    def paramType(self, param, itemKind, language):
        rawType = param['type']
        if itemKind == 'function':
            return inlineCode(rawType)
        display = escapeAngles(transformTypeForLanguages(rawType, language))
        return typeLink(display, rawType)

    def parameterBullet(self, param, itemKind, language, showDefault=True):
        name = param['name']
        description = self.convert(param['description'])
        typed = self.paramType(param, itemKind, language)
        if showDefault and param.get('default'):
            typed += f", default: {param['default']}"
        return self.bullet(f'- **{name}** ({typed})', description)

    @staticmethod
    def bullet(line, description):
        description = (description or '').strip()
        if not description:
            return line
        lines = description.split('\n')
        if lines[0].startswith(('- ', '#', '```', '>', '|')):
            # Block content (typically a nested list): start it on a new line.
            out = [line + ':']
            out.extend('    ' + item if item.strip() else '' for item in lines)
            return '\n'.join(out)
        out = [line + ': ' + lines[0]]
        out.extend('    ' + item if item.strip() else '' for item in lines[1:])
        return '\n'.join(out)

    @staticmethod
    def descriptionBullet(description):
        """A bullet whose text is the (possibly multi-line) description."""
        description = (description or '').strip()
        if not description:
            return '-'
        lines = description.split('\n')
        out = ['- ' + lines[0]]
        out.extend('  ' + line if line.strip() else '' for line in lines[1:])
        return '\n'.join(out)

    def paramsSection(self, item, itemKind, language, isReturn=False):
        params = parseParams(item.find('returns' if isReturn else 'params'))
        if not params:
            return self.section('Return values' if isReturn else 'Parameters',
                                'No return values.' if isReturn else 'No parameters.')

        bullets = []
        for param in params:
            if itemKind == 'function' and isReturn:
                # C functions: the synopsis carries the return type, and the
                # return value has no meaningful name ("return").
                bullets.append(self.descriptionBullet(self.convert(param['description'])))
            elif itemKind == 'function':
                typed = inlineCode(param['type'])
                bullets.append(self.bullet(f"- **{param['name']}** ({typed})",
                                           self.convert(param['description'])))
            elif isReturn:
                bullets.append(self.parameterBullet(param, itemKind, language, showDefault=False))
            else:
                bullets.append(self.parameterBullet(param, itemKind, language))
        return self.section('Return values' if isReturn else 'Parameters',
                            '\n'.join(bullets))

    def seeAlsoSection(self, item, itemKind, objName):
        links = []
        seeAlso = item.find('see-also')
        if seeAlso is not None:
            for refKind in ('function', 'property'):
                auxType = refKind if (refKind == 'property' or itemKind == 'function') else 'method'
                for ref in seeAlso.findall(refKind + '-ref'):
                    fullName = (ref.get('name') or '').strip()
                    refObjName = objName
                    refName = fullName
                    dotted = fullName.replace(':', '.')
                    dot = dotted.find('.')
                    if dot != -1:
                        refObjName = fullName[:dot]
                        refName = fullName[dot + 1:]
                    target = self.resolveRef(itemKind, refName, refObjName, auxType)
                    if target is None:
                        links.append(f'- {fullName} ({auxType})')
                    else:
                        links.append(f'- [{fullName} ({auxType})]({target})')
            for link in seeAlso.findall('link'):
                label = (link.get('label') or '').strip()
                href = (link.get('href') or '').strip()
                if label:
                    target = self.resolveLink(href)
                    if target is None:
                        links.append(f'- {label}')
                    else:
                        links.append(f'- [{label}]({target})')

        # See-also entries derived from the categories, as in generate.py:
        itemCategories = parseCategories(item.find('categories'))
        if objName:
            itemCategories = [cat for cat in itemCategories if cat != objName]
            itemCategories.insert(0, objName)
        for cat in itemCategories:
            if cat not in categories:
                raise SystemExit(
                    f"Category '{cat}' not found for '{objName}' "
                    f"(page: '{item.get('name')}')")
            if itemKind == 'function':
                anchor = 'functions_' + cat
                label = categories[cat] + ' (functions)'
            else:
                anchor = 'methodsAndProperties_' + cat
                label = categories[cat] + ' (methods & properties)'
            links.append(f'- [{label}](../apiFunctions.md#{anchor})')

        uniqueLinks = []
        for link in links:
            if link not in uniqueLinks:
                uniqueLinks.append(link)
        return self.section('See also', '\n'.join(uniqueLinks))

    def moreSection(self, item):
        more = getTxt(item, 'more')
        if not more:
            return None
        return self.convert(more, headingOffset=-1).strip() or None

    # -- pages --------------------------------------------------------------
    def buildMethod(self, item, objName):
        rawName = (item.get('name') or '').strip()
        displayName = rawName.replace(':', '.')
        dot = displayName.rfind('.')
        if dot != -1:
            displayName = f'{objName}.{displayName[:dot]}:{displayName[dot + 1:]}'
        else:
            displayName = f'{objName}:{displayName}'

        description = getDescription(item, 'short-description')

        language = (item.get('lang') or 'lua').strip()
        itemKind = 'method'

        blocks = [
            self.title(displayName, self.convert(description)),
            self.synopsisSection(item, displayName),
            self.paramsSection(item, itemKind, language),
            self.paramsSection(item, itemKind, language, isReturn=True),
            self.seeAlsoSection(item, itemKind, objName),
            self.moreSection(item),
        ]
        return '\n\n'.join(block for block in blocks if block) + '\n'

    def buildFunction(self, item):
        rawName = (item.get('name') or '').strip()
        description = getDescription(item, 'short-description')

        blocks = [
            self.title(rawName, self.convert(description)),
            self.synopsisSection(item, rawName),
            self.paramsSection(item, 'function', 'c'),
            self.paramsSection(item, 'function', 'c', isReturn=True),
            self.seeAlsoSection(item, 'function', ''),
            self.moreSection(item),
        ]
        return '\n\n'.join(block for block in blocks if block) + '\n'

    def buildProperty(self, item, objName):
        rawName = (item.get('name') or '').strip()
        displayName = objName + '.' + rawName.replace(':', '.')

        description = getDescription(item, 'label')

        rawType = (item.get('type') or '').strip()
        displayType = escapeAngles(transformTypeForLanguage(rawType, 'lua'))
        typeText = typeLink(displayType, rawType)
        enumType = getEnum(item)
        if enumType:
            typeText += (f' (see [sim.{enumType}]'
                         f'(../apiConstants.md#{enumType}))')

        flags = '\n'.join(f'- {flag}' for flag in getPropertyFlags(item))

        blocks = [
            self.title(displayName, self.convert(description)),
            self.section('Type', typeText),
            self.section('Flags', flags),
            self.seeAlsoSection(item, 'property', objName),
        ]
        return '\n\n'.join(block for block in blocks if block) + '\n'


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def parseArgs():
    parser = argparse.ArgumentParser(
        description='Generate the Markdown reference pages of the regular API (sim-2).')
    parser.add_argument('--objects-xml', required=True,
                        help='the objects.xml file (object classes, methods and properties)')
    parser.add_argument('--functions-xml', required=True,
                        help='the functions.xml file (C functions)')
    parser.add_argument('--output-dir', required=True,
                        help='directory where the .md pages are written')
    parser.add_argument('--docs-dir', default=None,
                        help='the Markdown manual directory (used to rewrite links to '
                             'manual pages; optional)')
    parser.add_argument('--verbose', action='store_true', help='print each generated page')
    return parser.parse_args()


def main():
    args = parseArgs()
    objectsXml = Path(args.objects_xml)
    functionsXml = Path(args.functions_xml)
    outputDir = Path(args.output_dir)
    if args.docs_dir:
        docsDir = Path(args.docs_dir)
        if not docsDir.is_dir():
            raise SystemExit(f'Markdown manual directory not found: {docsDir}')
    else:
        # Repository layout: apiDoc/ and docs/ are siblings.
        candidate = Path(__file__).resolve().parent.parent / 'docs'
        docsDir = candidate if candidate.is_dir() else None

    for xmlFile in (objectsXml, functionsXml):
        if not xmlFile.is_file():
            raise SystemExit(f'XML file not found: {xmlFile}')

    try:
        objectClasses = list(ET.parse(objectsXml).getroot())
    except ET.ParseError as error:
        raise SystemExit(f'{objectsXml}: {error}')
    try:
        functions = list(ET.parse(functionsXml).getroot())
    except ET.ParseError as error:
        raise SystemExit(f'{functionsXml}: {error}')

    # Collect the items first: links between pages must resolve regardless of
    # the order in which the pages are generated.
    items = []  # (filename, kind, element, objectName)
    for objectClass in objectClasses:
        if objectClass.tag != 'object-class':
            continue
        objName = (objectClass.get('name') or '').strip()
        for method in objectClass.findall('method'):
            name = (method.get('name') or '').strip()
            items.append((fmpToFilename(name, 'method', objName), 'method', method, objName))
        for prop in objectClass.findall('property'):
            name = (prop.get('name') or '').strip()
            if not getPropertyFlags(prop):
                continue  # deprecated
            if (prop.get('type') or '').strip() == 'group':
                continue
            items.append((fmpToFilename(name, 'property', objName), 'property', prop, objName))
    for function in functions:
        if function.tag != 'function':
            continue
        name = (function.get('name') or '').strip()
        items.append((fmpToFilename(name, 'function', ''), 'function', function, ''))

    # Pages that will exist: links to anything else become plain text.
    generatedNames = {filename[:-4] + '.md' for filename, _, _, _ in items}
    # (kind, item name, class name) -> page, for resolving stale references.
    itemIndex = {}
    for filename, kind, item, objName in items:
        name = (item.get('name') or '').strip().replace('.', '_').replace(':', '_')
        itemIndex[(kind, name, objName)] = filename[:-4] + '.md'

    # Start from a clean directory so that pages of removed XML items do not
    # survive. Only a directory that holds Markdown pages is cleaned.
    if outputDir.exists():
        entries = list(outputDir.iterdir())
        if any(entry.suffix != '.md' for entry in entries):
            raise SystemExit(
                f'{outputDir} contains files other than .md: refusing to clean it')
        for stalePage in entries:
            stalePage.unlink()
    outputDir.mkdir(parents=True, exist_ok=True)

    builder = PageBuilder(docsDir, generatedNames, itemIndex)

    counts = {'method': 0, 'property': 0, 'function': 0}
    for filename, kind, item, objName in items:
        if kind == 'method':
            markdown = builder.buildMethod(item, objName)
        elif kind == 'property':
            markdown = builder.buildProperty(item, objName)
        else:
            markdown = builder.buildFunction(item)

        page = outputDir / (filename[:-4] + '.md')
        page.write_text(markdown, encoding='utf-8')
        counts[kind] += 1
        if args.verbose:
            print(f'  wrote {page}')

    print(f'Generated {counts["method"]} method, {counts["property"]} property and '
          f'{counts["function"]} function Markdown pages in {outputDir}')


if __name__ == '__main__':
    main()
