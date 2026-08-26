#!/usr/bin/env python3
import os
import re
import sys
from html.parser import HTMLParser

def strip_html(text):
    """Remove all html tags and unescape entities, collapse whitespace."""
    import html as html_mod
    text = re.sub(r'<[^>]+>', '', text)
    text = html_mod.unescape(text)
    text = text.replace('\n', ' ').replace('\r', ' ')
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def extract_between(content, start_marker, end_marker, from_pos=0):
    """Return (text, end_index) between markers, or (None, -1)."""
    i = content.find(start_marker, from_pos)
    if i == -1:
        return None, -1
    i += len(start_marker)
    j = content.find(end_marker, i)
    if j == -1:
        return None, -1
    return content[i:j], j + len(end_marker)

def parse_list_items(section_html):
    """Parse nested <ul>/<li> structure, return list of lines with indentation.

    Returns a list of (depth, text) tuples for the items.
    """
    items = []  # (depth, text)

    class LiParser(HTMLParser):
        def __init__(self):
            super().__init__()
            self.depth = 0          # ul nesting depth
            self.li_stack = []      # stack of [depth, text_parts]
        def handle_starttag(self, tag, attrs):
            if tag == 'ul' or tag == 'ol':
                self.depth += 1
            elif tag == 'li':
                self.li_stack.append([self.depth, []])
        def handle_endtag(self, tag):
            if tag == 'ul' or tag == 'ol':
                self.depth -= 1
            elif tag == 'li':
                if self.li_stack:
                    depth, parts = self.li_stack.pop()
                    text = re.sub(r'\s+', ' ', ''.join(parts)).strip()
                    if text:
                        items.append((depth, text))
        def handle_data(self, data):
            if self.li_stack:
                # only append to the innermost li
                self.li_stack[-1][1].append(data)

    # Sort back into document order: HTMLParser closes nested li's first,
    # so instead collect with position. Simpler approach: track order manually.
    ordered = []

    class LiParser2(HTMLParser):
        def __init__(self):
            super().__init__()
            self.depth = 0
            self.li_stack = []  # each: dict(depth, parts, index)
            self.counter = 0
        def handle_starttag(self, tag, attrs):
            if tag in ('ul', 'ol'):
                self.depth += 1
            elif tag == 'li':
                self.li_stack.append({'depth': self.depth, 'parts': [], 'idx': self.counter})
                self.counter += 1
        def handle_endtag(self, tag):
            if tag in ('ul', 'ol'):
                self.depth -= 1
            elif tag == 'li':
                if self.li_stack:
                    li = self.li_stack.pop()
                    text = re.sub(r'\s+', ' ', ''.join(li['parts'])).strip()
                    ordered.append((li['idx'], li['depth'], text))
        def handle_data(self, data):
            if self.li_stack:
                self.li_stack[-1]['parts'].append(data)

    p = LiParser2()
    p.feed(section_html)
    ordered.sort(key=lambda t: t[0])
    return [(depth, text) for _, depth, text in ordered if text]

def extract_params(content, header):
    """Extract list items following a header like <h3>Arguments</h3>."""
    i = content.find(header)
    if i == -1:
        return None
    i += len(header)
    # take until the end of the enclosing section div
    j = content.find('</div>', i)
    section = content[i:j] if j != -1 else content[i:]
    return parse_list_items(section)

def format_params(items):
    """Format items: top-level numbered, sub-items indented with dashes."""
    lines = []
    counter = 0
    base_depth = None
    for depth, text in items:
        if base_depth is None:
            base_depth = depth
        if depth <= base_depth:
            counter += 1
            lines.append(f"{counter}. {text}")
        else:
            indent = '    ' * (depth - base_depth)
            lines.append(f"{indent}- {text}")
    return lines

def process_file(path):
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    filename = os.path.basename(path)

    # function name
    name_raw, _ = extract_between(
        content,
        '<h2><div style="display: flex; justify-content: space-between;">',
        '</div></h2>')
    if name_raw is None:
        print(f"Skipping '{filename}': function name not found")
        return
    # take first span content
    func_name = strip_html(name_raw.split('</span>')[0])

    # description
    desc_raw, _ = extract_between(
        content,
        '<a href="../apisOverview.htm">sim-1</a></span></div></h2>',
        '</div>')
    if desc_raw is None:
        print(f"Skipping '{filename}': description not found")
        return
    description = strip_html(desc_raw)

    # synopses (optional)
    lua_raw, _ = extract_between(
        content, '<code class="hljs language-python coppelia-coppeliasim-script">', '</code>')
    py_raw, _ = extract_between(
        content, '<code class="hljs language-lua coppelia-coppeliasim-script">', '</code>')
    lua_syn = strip_html(lua_raw) if lua_raw is not None else None
    py_syn = strip_html(py_raw) if py_raw is not None else None

    # parameters
    in_items = extract_params(content, '<h3>Arguments</h3>')
    out_items = extract_params(content, '<h3>Return values</h3>')
    if in_items is None:
        print(f"Skipping '{filename}': Arguments section not found")
        return
    if out_items is None:
        print(f"Skipping '{filename}': Return values section not found")
        return

    lines = []
    lines.append(f"name: {func_name}")
    lines.append(f"description: {description}")
    if lua_syn:
        lines.append(f"luaSynopsis: {lua_syn}")
    if py_syn:
        lines.append(f"pythonSynopsis: {py_syn}")
    lines.append("inputs:")
    lines.extend(format_params(in_items))
    lines.append("outputs:")
    lines.extend(format_params(out_items))

    out_path = os.path.splitext(path)[0] + '.deprecated'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    #os.remove(filename)
    print(f"Generated '{os.path.basename(out_path)}'")

def main():
    directory = sys.argv[1] if len(sys.argv) > 1 else '.'
    for fn in sorted(os.listdir(directory)):
        base, ext = os.path.splitext(fn)
        #if ext.lower() == '.htm' and base.endswith('_cpp'):
        #    os.remove(os.path.join(directory, fn))
        if ext.lower() == '.htm' and fn.startswith('sim') and not base.endswith('_cpp'):
            process_file(os.path.join(directory, fn))

if __name__ == '__main__':
    main()
