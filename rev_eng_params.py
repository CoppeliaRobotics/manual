import sys
import xml.etree.ElementTree as ET

from pathlib import Path


curDir = Path(__file__).absolute().parent

zmqRemoteApiToolsDir = curDir.parent / 'programming' / 'zmqRemoteApi' / 'tools'
if zmqRemoteApiToolsDir.is_dir():
    sys.path.append(str(zmqRemoteApiToolsDir))
else:
    sys.stderr.write('zmqRemoteApi/tools directory missing\n')
    sys.exit(1)


import lark
from calltip import FuncDef, Arg, ArgDef


tree = ET.parse(curDir / 'regularApi.xml')
root = tree.getroot()

for func in root:
    name = func.find('api-function-name').text.strip()
    calltip = func.find('api-calltip')
    api_in = func.find('api-input-python-lua')
    api_out = func.find('api-output-python-lua')

    if api_in is None or api_out is None:
        print(f'warning: function "{name}" lacks <api-input-python-lua> or <api-output-python-lua>')
        continue

    li_in, li_out = {}, {}
    for li in api_in.findall('li'):
        s = li.find('strong')
        if s is None:
            print(f'warning: function "{name}" <api-input...> <li> lacks a <strong> element')
        n = s.text.strip()
        li_in[n] = li
    for li in api_out.findall('li'):
        s = li.find('strong')
        if s is None:
            print(f'warning: function "{name}" <api-output...> <li> lacks a <strong> element')
        n = s.text.strip()
        li_out[n] = li

    if calltip is not None:
        calltip = calltip.text.strip()
        for i, c in enumerate(calltip.splitlines()):
            if not c: break
            try:
                fd = FuncDef.from_calltip(c)
                in_node = ET.SubElement(func, 'api-params')
                for arg in fd.in_args:
                    p_node = ET.SubElement(in_node, 'param')
                    p_node.set('name', arg.name)
                    p_node.set('type', arg.type)
                    if isinstance(arg, ArgDef):
                        p_node.set('default', str(arg.default))
                    if arg.name not in li_in:
                        print(f'warning: function "{name}" calltip param "{arg.name}" not present in <api-input...>')
                out_node = ET.SubElement(func, 'api-returns')
                for arg in fd.out_args:
                    p_node = ET.SubElement(out_node, 'param')
                    p_node.set('name', arg.name)
                    p_node.set('type', arg.type)
                    if isinstance(arg, ArgDef):
                        p_node.set('default', str(arg.default))
                    if arg.name not in li_out:
                        print(f'warning: function "{name}" calltip param "{arg.name}" not present in <api-output...>')
                ET.indent(in_node, ' ' * 4, 2)
                ET.indent(out_node, ' ' * 4, 2)
            except lark.exceptions.LarkError as e:
                print(f'error: function "{name}": cannot parse calltip {i} ({c!r}): {e}')
    else:
        print(f'warning: no calltip for function "{name}"')

#ET.dump(tree)

