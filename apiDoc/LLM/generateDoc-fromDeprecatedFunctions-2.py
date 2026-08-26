#!/usr/bin/env python3
"""
Parse CoppeliaSim API 'sim*.htm' files (excluding '*_cpp.htm') in a directory
and generate corresponding '.deprecated' text files.

Requires: beautifulsoup4  (pip install beautifulsoup4)
"""

import os
import re
import sys
from bs4 import BeautifulSoup, NavigableString, Tag

DIRECTORY = sys.argv[1] if len(sys.argv) > 1 else '.'

def clean_text(text):
    """Collapse whitespace/linefeeds into single spaces and strip."""
    return re.sub(r'\s+', ' ', text).strip()

def get_cell(soup, cls):
    """Return the first td with the given class, or None."""
    return soup.find('td', class_=cls)

def extract_function_name(soup):
    bar = soup.find(class_='subsectionBar')
    if bar is None:
        return None
    text = clean_text(bar.get_text())
    # remove trailing "(in ...)" part
    text = re.sub(r'\(in .*?\)', '', text).strip()
    # several names may be separated by '/'
    candidates = [c.strip() for c in text.split('/')]
    for c in candidates:
        if c.startswith('sim.'):
            return c
    # fallback: first candidate
    return candidates[0] if candidates else None

def extract_items(cell):
    """
    Extract parameter items from a td cell.
    Each top-level <div> is a parameter. Nested <ul>/<li> (or nested divs)
    become sub-items, indented one level per depth.
    Returns list of (depth, text) tuples.
    """
    items = []

    def li_walk(li, depth):
        # own text without nested lists
        own = ''
        for child in li.children:
            if isinstance(child, Tag) and child.name in ('ul', 'ol'):
                continue
            own += child.get_text() if isinstance(child, Tag) else str(child)
        own = clean_text(own)
        if own:
            items.append((depth, own))
        for sub in li.find_all(['ul', 'ol'], recursive=False):
            for subli in sub.find_all('li', recursive=False):
                li_walk(subli, depth + 1)

    def div_walk(div, depth):
        own = ''
        for child in div.children:
            if isinstance(child, Tag) and child.name in ('ul', 'ol', 'div'):
                continue
            own += child.get_text() if isinstance(child, Tag) else str(child)
        own = clean_text(own)
        if own:
            items.append((depth, own))
        for child in div.children:
            if isinstance(child, Tag):
                if child.name in ('ul', 'ol'):
                    for li in child.find_all('li', recursive=False):
                        li_walk(li, depth + 1)
                elif child.name == 'div':
                    div_walk(child, depth + 1)

    for child in cell.children:
        if isinstance(child, Tag):
            if child.name == 'div':
                div_walk(child, 0)
            elif child.name in ('ul', 'ol'):
                for li in child.find_all('li', recursive=False):
                    li_walk(li, 0)
    return items

def refers_to_c(cell):
    txt = cell.get_text() if cell else ''
    return ('Similar to' in txt) or ('C-function' in txt)

def get_c_params(soup, want_output):
    """Get items from apiTableRightCParam, filtered by '(output)' marker."""
    cell = get_cell(soup, 'apiTableRightCParam')
    if cell is None:
        return []
    result = []
    include_subtree = False
    for depth, text in extract_items(cell):
        is_output = '(output)' in text
        if depth == 0:
            include_subtree = (is_output == want_output)
        if include_subtree:
            result.append((depth, text.replace('(output)', '').replace('(input)', '').strip()))
    return result

def get_params(soup, own_cls, want_output):
    cell = get_cell(soup, own_cls)
    if cell is None:
        return None
    if refers_to_c(cell):
        if want_output:
            first = []
            cret = get_cell(soup, 'apiTableRightCRet')
            if cret is not None:
                first = extract_items(cret)
            return first + get_c_params(soup, True)
        return get_c_params(soup, False)
    return extract_items(cell)

def format_items(items):
    lines = []
    counter = 0
    for depth, text in items:
        if depth == 0:
            counter += 1
            lines.append(f'{counter}. {text}')
        else:
            lines.append('    ' * depth + f'- {text}')
    return lines

def process_file(path):
    with open(path, encoding='utf-8', errors='replace') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    name = extract_function_name(soup)
    descr_cell = get_cell(soup, 'apiTableRightDescr')
    description = clean_text(descr_cell.get_text()) if descr_cell else None

    lsyn_cell = get_cell(soup, 'apiTableRightLSyn')
    lua_syn = None
    if lsyn_cell:
        # keep first version only (first line / first div)
        first = lsyn_cell.find('div')
        lua_syn = clean_text((first or lsyn_cell).get_text().split('\n')[0]) or None
        if lua_syn is None or lua_syn == '':
            lua_syn = None

    psyn_cell = get_cell(soup, 'apiTableRightPSyn')
    py_syn = None
    if psyn_cell:
        first = psyn_cell.find('div')
        py_syn = clean_text((first or psyn_cell).get_text().split('\n')[0]) or None

    if not name or not description:
        print(f'Skipping "{path}": missing '
              f'{"function name" if not name else "description"}')
        return
    description = description.replace('sim.', 'simXXX')
    if description.lower().startswith('deprecated. use'):
        p = description.find('.')
        p = description.find('.', p + 1)
        if p == -1:
            description = ''
        else:
            description = description[p + 1:]
    if description.lower().startswith('deprecated. see'):
        p = description.find('.')
        p = description.find('.', p + 1)
        if p == -1:
            description = ''
        else:
            description = description[p + 1:]
    if description.lower().startswith('deprecated.'):
        p = description.find('.')
        description = description[p + 1:]
    description = description.replace('simXXX', 'sim.')
    # prefer Lua parameters, fall back to Python
    inputs = get_params(soup, 'apiTableRightLParam', False)
    if inputs is None:
        inputs = get_params(soup, 'apiTableRightPParam', False)
    outputs = get_params(soup, 'apiTableRightLRet', True)
    if outputs is None:
        outputs = get_params(soup, 'apiTableRightPRet', True)

    if inputs is None or outputs is None:
        print(f'Skipping "{path}": missing '
              f'{"input" if inputs is None else "output"} parameters')
        return

    lines = [f'name: {name}', f'description: {description}']
    if lua_syn:
        lines.append(f'luaSynopsis: {lua_syn}')
    if py_syn:
        lines.append(f'pythonSynopsis: {py_syn}')
    lines.append('inputs (possibly taken/adapted from C-function counterpart. Adjust accordingly):')
    lines.extend(format_items(inputs))
    lines.append('outputs (possibly taken/adapted from C-function counterpart. Adjust accordingly):')
    lines.extend(format_items(outputs))

    out_path = os.path.splitext(path)[0] + '.deprecated'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    print(f'Generated: {out_path}')

def main():
    for fname in sorted(os.listdir(DIRECTORY)):
        base, ext = os.path.splitext(fname)
        if ext.lower() == '.htm' and base.startswith('sim') and not base.endswith('_cpp'):
            process_file(os.path.join(DIRECTORY, fname))

if __name__ == '__main__':
    main()
