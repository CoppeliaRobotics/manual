import sys
from pathlib import Path

currentDir = Path(__file__).absolute().parent

records = []
record = {}
field_content = ''
field_name = None
line_num = 0
with (currentDir / 'regularApi.txt').open('r') as f:
    for line in f:
        line_num += 1
        line_trim = line.rstrip('\r\n')
        words = line_trim.split() + [''] * 3
        if line_trim == '*' * 84: # delimiter
            if record: records.append(record)
            record = {}
        elif words[0] == '=' * 20 and words[2] == '=' * 20 + '<': # open tag
            if field_name: raise RuntimeError(f'unexpected open tag at line {line_num}')
            field_name = words[1]
        elif words[0] == '=' * 20 and words[2] == '=' * 20 + '>': # close tag
            if words[1] != field_name: raise RuntimeError(f'mismatched tag at line {line_num}')
            record[field_name] = field_content.rstrip('\r\n')
            field_content, field_name = '', None
        elif field_name:
            field_content += line
        elif line.strip():
            raise RuntimeError(f'unexpected content at line {line_num}: {line!r}')

import xml.etree
import xml.etree.ElementTree as ET
root = ET.Element('functions')
for record in records:
    r = ET.SubElement(root, 'function')
    for k, v in record.items():
        n = ''.join(c.lower() + ('-' if c.islower() and d.isupper() else '') for c, d in zip(k, k[1:] + ' '))
        try:
            vt = ET.fromstring(f'<{n}>{v}</{n}>')
            r.append(vt)
        except xml.etree.ElementTree.ParseError as e:
            print(f'cannot parse XML ({e!s}): {v!r}')
            f = ET.SubElement(r, n)
            f.text = v

if len(sys.argv) != 2:
    print(f'usage: {sys.argv[0]} <path/to/output/regularApi.xml>')
    sys.exit(1)
ET.indent(root, ' ' * 4)
ET.ElementTree(root).write(sys.argv[1], 'utf-8', True)
