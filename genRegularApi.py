import os
import sys
import re
import shutil
import xml.etree.ElementTree as ET

from pathlib import Path


currentDir = Path(__file__).absolute().parent

templatesDir = currentDir / 'templates'

if '--calltip' in sys.argv:
    zmqRemoteApiToolsDir = currentDir.parent / 'programming' / 'zmqRemoteApi' / 'tools'
    if zmqRemoteApiToolsDir.is_dir():
        sys.path.append(str(zmqRemoteApiToolsDir))
    else:
        sys.stderr.write('zmqRemoteApi/tools directory missing\n')
        sys.exit(1)

    import lark
    from calltip import FuncDef, Arg, ArgDef


def main():
    regularApiDir = currentDir / 'en' / 'regularApi'
    try:
        shutil.rmtree(regularApiDir)
    except Exception as e:
        pass
    os.makedirs(regularApiDir)

    with (templatesDir / 'regularApi_cpp.htm').open('r') as file_r:
        template_cpp = file_r.read()

    with (templatesDir / 'regularApi_pythonLua.htm').open('r') as file_r:
        template = file_r.read()

    tree = ET.parse(currentDir / 'regularApi.xml')
    funcs = tree.getroot()

    allCpp = {}
    allPythonLua = {}

    def getTxt(n):
        node = func.find(n)
        if node is not None:
            # preserve HTML tags (returning node.text woudln't work):
            txt = ET.tostring(node, 'unicode')
            txt = txt.strip()
            txt = re.sub(f'^<{n}>(.*)</{n}>$', r'\1', txt, flags=re.DOTALL)
            return txt

    for func in funcs:
        if apiFunc := getTxt('api-function-name'):
            if getTxt('api-synopsis-cpp'):
                allCpp[getCppName(apiFunc)] = True
            if getTxt('api-synopsis-python') or getTxt('api-synopsis-lua'):
                allPythonLua[getPythonLuaName(apiFunc)] = True

    cnt = 0
    for func in funcs:
        apiFunc = getTxt('api-function-name').strip()
        assert apiFunc, f'missing <api-function-name>: {ET.tostring(func, "unicode")}'

        cnt += 1
        apiDescription = getTxt('api-description')
        if apiSeeAlso := getTxt('api-see-also'):
            apiSeeAlsoCpp = prepSeeAlso(apiSeeAlso, allCpp, allPythonLua, 'cpp')
            apiSeeAlsoPythonLua = prepSeeAlso(apiSeeAlso, allCpp, allPythonLua, 'pythonLua')
        else:
            apiSeeAlsoCpp = ''
            apiSeeAlsoPythonLua = ''
        apiSynopsisCpp = getTxt('api-synopsis-cpp')
        apiInputCpp = getTxt('api-input-cpp')
        apiOutputCpp = getTxt('api-output-cpp')
        apiMoreCpp = getTxt('api-more-cpp') or ''
        apiSynopsisPython = getTxt('api-synopsis-python')
        apiSynopsisLua = getTxt('api-synopsis-lua')
        apiInputPythonLua = getTxt('api-input-python-lua')
        apiOutputPythonLua = getTxt('api-output-python-lua')
        apiMorePythonLua = getTxt('api-more-python-lua') or ''
        apiCalltip = getTxt('api-calltip')

        if apiSynopsisPython or apiSynopsisLua:
            nm = currentDir / 'en' / 'regularApi' / (getCppName(apiFunc) + '.htm')
            with nm.open('w') as file_w:
                a = template
                a = a.replace('__funcName__', apiFunc)
                a = a.replace('__funcDescription__', apiDescription)
                a = a.replace('__seeAlso__', apiSeeAlsoPythonLua)
                a = a.replace('__pythonSynopsis__', addCodeSection(formatSynopsis(apiSynopsisPython, 100), 'python'))
                a = a.replace('__luaSynopsis__', addCodeSection(formatSynopsis(apiSynopsisLua, 100), 'lua') +
                    # XXX: TEST
                    (formatCalltips(apiCalltip) if '--calltip' in sys.argv and apiCalltip else '')
                )
                if apiInputPythonLua:
                    a = a.replace('__input__', apiInputPythonLua)
                    a = a.replace('__inputVisibility__', '')
                else:
                    a = a.replace('__input__', '')
                    a = a.replace('__inputVisibility__', 'style="display: none;"')
                if apiOutputPythonLua:
                    a = a.replace('__output__', apiOutputPythonLua)
                    a = a.replace('__outputVisibility__', '')
                else:
                    a = a.replace('__output__', '')
                    a = a.replace('__outputVisibility__', 'style="display: none;"')
                a = a.replace('__more__', apiMorePythonLua)
                file_w.write(a)
        if apiSynopsisCpp:
            nm = currentDir / 'en' / 'regularApi' / (getCppName(apiFunc) + '_cpp' + '.htm')
            with nm.open('w') as file_w:
                a = template_cpp
                a = a.replace('__funcName__', getCppName(apiFunc))
                a = a.replace('__funcDescription__', apiDescription)
                a = a.replace('__seeAlso__', apiSeeAlsoCpp)
                a = a.replace('__cppSynopsis__', formatSynopsis(apiSynopsisCpp, 100))
                if apiInputCpp:
                    a = a.replace('__input__', apiInputCpp)
                    a = a.replace('__inputVisibility__', '')
                else:
                    a = a.replace('__input__', '')
                    a = a.replace('__inputVisibility__', 'style="display: none;"')
                if apiOutputCpp:
                    a = a.replace('__output__', apiOutputCpp)
                    a = a.replace('__outputVisibility__', '')
                else:
                    a = a.replace('__output__', '')
                    a = a.replace('__outputVisibility__', 'style="display: none;"')
                a = a.replace('__more__', apiMoreCpp)
                file_w.write(a)

    print(f'\nTotal generated: {cnt}')

def addCodeSection(string, lang):
    s = ''
    if string != None and len(string) > 0:
        s = '<code class="hljs language-' + lang + ' coppelia-coppeliasim-script">' + string + '</code>'
    return s

def getCppName(s):
    def repl(match):
        return match.group(1).upper()
    return re.sub(r'\.([a-zA-Z])', repl, s)

def getPythonLuaName(s):
    if s.find('.') !=-1 :
        return s
    if not s.startswith('sim') or len(s) < 5:
        return s
    s = s[:3] + '.' + s[3:]
    s = s[:4] + s[4].lower() + s[5:]
    return s

def prepSeeAlso(items, allCpp, allPythonLua, lang):
    ret = ''
    lines = items.splitlines()
    bullets = []
    for line in lines:
        line = line.strip()
        if len(line) > 0:
            if line.startswith('<'):
               bullets.append(line)
            else:
                if lang == 'cpp':
                    if getCppName(line) in allCpp:
                        bullets.append('<a href="' + getCppName(line) + '_cpp.htm">' + getCppName(line) + '</a>')
                    else:
                        if getPythonLuaName(line) in allPythonLua:
                            bullets.append('<a href="' + getCppName(line) + '.htm">' + getPythonLuaName(line) + '</a>')
                        else:
                            print("Error with cpp 'see also' item " + line)
                else:
                    if getPythonLuaName(line) in allPythonLua:
                        bullets.append('<a href="' + getCppName(line) + '.htm">' + getPythonLuaName(line) + '</a>')
                    #else:
                    #    print("Error with python/lua 'see also' item " + line)
    if len(bullets) > 0:
        ret = '<br>See also:\n<ul>\n'
        for l in bullets:
            ret += '<li>' + l + '</li>\n'
        ret += '</ul>\n'
    return ret

def formatSynopsis(s, maxLength):
    if s == None:
        return s

    s = s.replace(' = ','##_##')
    s = s.replace('= ','_##')
    s = s.replace(' =','##_')
    s = s.replace('=',' = ')
    s = s.replace('##_##',' = ')
    s = s.replace('##_',' =')
    s = s.replace('_##','= ')

    s = s.replace(' , ','_##')
    s = s.replace(', ','_##')
    s = s.replace(' ,','_##')
    s = s.replace(',',', ')
    s = s.replace('_##',', ')

    if s.find('<div>') != -1:
        return s

    if s.find('\n') != -1:
        return s

    if len(s) <= maxLength:
        return s

    # Function to format the content inside parentheses
    def replacer(match):
        contents = match.group(1).split(',')

        # Determine the amount of padding needed
        indent = match.start() + 1
        indent_str = ' ' * indent

        # Split and join the content based on the maxLength
        line = ''
        formatted_contents = []
        for content in contents:
            if line and len(line + ', ' + content.strip()) + indent > maxLength:
                formatted_contents.append(line)
                line = content.strip()
            elif not line:
                line = content.strip()
            else:
                line += ', ' + content.strip()
        if line:
            formatted_contents.append(line)

        return '(' + ('\n' + indent_str).join(formatted_contents) + ')'

    # Regular expression to match content inside parentheses
    pattern = r'\(([^)]+)\)'

    # Format the content inside parentheses
    formatted_string = re.sub(pattern, replacer, s)

    return formatted_string

def formatCalltip(s):
    d = FuncDef.from_calltip(s)
    render_arg = lambda arg: f'<span class="hljs-built_in">{arg.type}</span> {arg.name}' + (f'={arg.default}' if isinstance(arg, ArgDef) else '')
    render_funcname = lambda n: f'<span class="hljs-title function_">{n}</span>'
    render_args = lambda args: ', '.join(map(render_arg, args))
    return f'{render_args(d.out_args)} = {render_funcname(d.func_name)}({render_args(d.in_args)})'

def formatCalltips(s):
    r = []
    for c in s.splitlines():
        if c == '': break # an empty line marks the begin of comments
        try:
            r.append(formatCalltip(c))
        except lark.exceptions.LarkError as e:
            print(f'Cannot parse calltip: {c!r}')
    if r:
        return addCodeSection('<br/>'.join(r), 'calltip')
    else:
        return ''

if __name__ == "__main__":
    main()
