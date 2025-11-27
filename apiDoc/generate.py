import os
import sys
import re
import shutil
import xml.etree.ElementTree as ET
import minify_html
from pathlib import Path

currentDir = Path(__file__).absolute().parent

FUNC_VER_INFO = '<a href="../apisOverview.htm">sim-2</a>'
apiDir_currentVer = currentDir / '..' / 'en' / 'sim-2'
apiDirs_oldVer = [currentDir / '..' / 'en' / 'sim-1'] # older API versions
apiDir_deprecated_currentVer = currentDir / '..' / 'en' / 'deprecated' # deprecated but in the same API version
apiDir_all = currentDir / '..' / 'en' / 'sim'
templatesDir = currentDir / 'templates'

def getTxt(node, n):
    node = node.find(n)
    if node is not None:
        # preserve HTML tags (returning node.text woudln't work):
        txt = ET.tostring(node, 'unicode')
        txt = txt.strip()
        txt = re.sub(f'^<{n}>(.*)</{n}>$', r'\1', txt, flags=re.DOTALL)
        #txt = txt.replace('\r\n', ' ').replace('\r', ' ').replace('\n', ' ') # remove carriage returns
        #txt = ' '.join(txt.split()) # remove multiple successive spaces
        return txt
        
def parse_params(params_node):
    arguments = []
    if params_node is None:
        return arguments
    for param in params_node.findall('param'):
        arg = {
            'name': param.get('name', ''),
            'type': param.get('type', ''),
            'default': param.get('default', ''),
            'description': getTxt(param, 'description').strip().rstrip('. ')
        }
        arguments.append(arg)
    return arguments
    
def funcname_to_filename(name, isC):
    if isC:
        return name + '_cpp.htm'
    if name.startswith('sim.'):
        name = name[4:]  # Everything after 'sim.'
        name = 'sim' + name[0].upper() + name[1:]
    return name + '.htm' 
    
def parse_see_also(see_also_node, isC):
    references = []
    if see_also_node is None:
        return references
    for func_ref in see_also_node.findall('function-ref'):
        funcname = func_ref.get('name', '').strip()
        references.append('<a href="' + funcname_to_filename(funcname, isC) + '">' + funcname + '</a>')
    for link in see_also_node.findall('link'):
        references.append('<a href="' + link.get('href', '') + '">' + link.get('label', '').strip() + '</a>')
    return references
    
def prepare_synopsis(func_name, input_params, output_params, lang):
    def transform_params_for_language(params, language):
        def transform_default_for_language(default_value, param_type, language):
            def transform_map_default(lua_map):
                if not lua_map.startswith('{') or not lua_map.endswith('}'):
                    return lua_map
                content = lua_map[1:-1].strip()
                if not content:
                    return '{}'
                pairs = content.split(',')
                python_pairs = []
                for pair in pairs:
                    if '=' in pair:
                        key, value = pair.split('=', 1)
                        key = key.strip()
                        value = value.strip()
                        value = value.replace('true', 'True').replace('false', 'False').replace('nil', 'None')
                        python_pairs.append(f"'{key}': {value}")
                    else:
                        python_pairs.append(pair.strip())
                return '{' + ', '.join(python_pairs) + '}'

            if language == 'python':
                # Check if it's an array type (any type followed by '[')
                if '[' in param_type:
                    # Transform array syntax: {1,2,3} -> [1,2,3]
                    default_value = default_value.replace('{', '[').replace('}', ']')
                # Transform map/table syntax
                elif param_type.startswith('map') or param_type.startswith('table'):
                    default_value = transform_map_default(default_value)
                elif param_type.startswith('bool'):
                    default_value = default_value.replace('true', 'True').replace('false', 'False')
                if default_value == 'nil':
                    default_value = 'None'
            return default_value
            
        def transform_type_for_language(param_type, language):
            if language == 'python':
                type_map = {
                    'int[': 'list',
                    'float[': 'list',
                    'string[': 'list',
                    'handle[': 'list',
                    'map[': 'list',
                    'vector3': 'vector3',
                    'quaternion': 'quaternion',
                    'pose': 'pose',
                    'matrix': 'matrix',
                    'color': 'color',
                    'func': 'func',
                    'map': 'dict',
                    'table': 'dict',
                    'bool': 'bool',
                    'int': 'int',
                    'float': 'float',
                    'string': 'str',
                    'any': 'any',
                    'handle': 'int',
                    'buffer': 'bytes',
                }
                for lua_type, python_type in type_map.items():
                    if param_type.startswith(lua_type):
                        return python_type
                raise ValueError(f"Unsupported type '{param_type}' for language '{language}'")
            raise ValueError(f"Unsupported language: '{language}'")
            
        transformed = []
        for param in params:
            new_param = param.copy()
            new_param['type'] = transform_type_for_language(param['type'], language)
            if 'default' in param and param['default']:
                new_param['default'] = transform_default_for_language(
                    param['default'], 
                    param['type'], 
                    language
                )
            transformed.append(new_param)
        return transformed
        
    if (lang != 'c') and (lang != 'lua'):
        input_params = transform_params_for_language(input_params, lang)
        output_params = transform_params_for_language(output_params, lang)
    output_part = ""
    if output_params:
        output_types = [param['type'] for param in output_params]
        output_names = [param['name'] for param in output_params]
        if lang == 'c':
            if len(output_types) >= 1:
                output_part = output_types[0] + ' '
        else:
            # Combine type and name for each output
            outputs = [f"{t} {n}" for t, n in zip(output_types, output_names)]
            output_part = ", ".join(outputs) + " = "
    
    input_args = []
    for param in input_params:
        arg = f"{param['type']} {param['name']}"
        if 'default' in param and param['default']:
            arg += f" = {param['default']}"
        input_args.append(arg)
    
    input_part = ", ".join(input_args)
    
    # Combine everything
    synopsis = f"{output_part}{func_name}({input_part})"
    
    return synopsis
    
def addCodeSection(string, lang):
    s = ''
    if string != None and len(string) > 0:
        s = '<code class="hljs language-' + lang + ' coppelia-coppeliasim-script">' + string + '</code>'
    return s

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
    
def format_synopsis(S, L):
    """
    Formats a programming language synopsis with line breaks to respect max length.
    Only breaks after commas that are function argument separators (not inside brackets/braces).
    
    Args:
        S: Input string (function synopsis)
        L: Maximum line length
    
    Returns:
        Formatted string with carriage returns and proper indentation
    """
    # Find the position of the first '(' to determine indentation
    first_paren = S.find('(')
    if first_paren == -1:
        return S  # No parenthesis found, return as is
    
    indent = first_paren + 1
    indent_str = ' ' * indent
    
    # Track nesting level to identify argument-separator commas
    def is_argument_separator_comma(s, pos):
        """Check if comma at position pos is a function argument separator"""
        paren_depth = 0
        bracket_depth = 0
        brace_depth = 0
        
        for i in range(pos + 1):  # Check up to and including the comma
            if s[i] == '(':
                paren_depth += 1
            elif s[i] == ')':
                paren_depth -= 1
            elif s[i] == '[':
                bracket_depth += 1
            elif s[i] == ']':
                bracket_depth -= 1
            elif s[i] == '{':
                brace_depth += 1
            elif s[i] == '}':
                brace_depth -= 1
        
        # It's an argument separator if we're inside parentheses but not inside brackets/braces
        return paren_depth == 1 and bracket_depth == 0 and brace_depth == 0
    
    result = []
    current_line = ""
    i = 0
    
    while i < len(S):
        char = S[i]
        current_line += char
        
        # Check if we should consider a break after ','
        if char == ',' and is_argument_separator_comma(S, i):
            # Skip any immediate whitespace after comma
            j = i + 1
            while j < len(S) and S[j] == ' ':
                j += 1
            
            # Find the next break point (next comma or closing paren)
            next_break = j
            paren_depth = 0
            bracket_depth = 0
            brace_depth = 0
            
            for k in range(i + 1, len(S)):
                if S[k] == '(':
                    paren_depth += 1
                elif S[k] == ')':
                    if paren_depth == 0:
                        next_break = k
                        break
                    paren_depth -= 1
                elif S[k] == '[':
                    bracket_depth += 1
                elif S[k] == ']':
                    bracket_depth -= 1
                elif S[k] == '{':
                    brace_depth += 1
                elif S[k] == '}':
                    brace_depth -= 1
                elif S[k] == ',' and paren_depth == 0 and bracket_depth == 0 and brace_depth == 0:
                    next_break = k
                    break
            
            next_segment = S[j:next_break].strip()
            
            # Check if adding the next segment would exceed length
            if len(result) == 0:
                # First line
                potential_length = len(current_line) + 1 + len(next_segment)
            else:
                # Already indented line
                potential_length = len(current_line) + 1 + len(next_segment)
            
            if potential_length > L:
                # Need to break
                result.append(current_line.rstrip())
                current_line = indent_str
                # Skip whitespace after comma
                while i + 1 < len(S) and S[i + 1] == ' ':
                    i += 1
        
        i += 1
    
    # Add any remaining content
    if current_line.strip():
        result.append(current_line.rstrip())
    
    return '\n'.join(result)
    
def main():
    try:
        shutil.rmtree(apiDir_currentVer)
    except Exception as e:
        pass
    os.makedirs(apiDir_currentVer)

    # first insert deprecated functions (for the same API version):
    for filename in os.listdir(apiDir_deprecated_currentVer):
        if filename.endswith('.htm'):
            src_path = os.path.join(apiDir_deprecated_currentVer, filename)
            dst_path = os.path.join(apiDir_currentVer, filename)
            shutil.copy2(src_path, dst_path)    

    with (templatesDir / 'cFunc.htm').open('r') as file_r:
        template_cpp = file_r.read()

    with (templatesDir / 'pythonLuaFunc.htm').open('r') as file_r:
        template = file_r.read()

    tree = ET.parse(currentDir / 'functions.xml')
    funcs = tree.getroot()

    allCpp = {}
    allPythonLua = {}

    cnt = 0
    for func in funcs:
        cnt += 1
        funcname = func.get('name').strip()
        lang = func.get('lang').strip()
        isC = (lang == 'c')
        funcdescription = getTxt(func, 'description').strip().rstrip('. ')
        more = (getTxt(func, 'more') or '').strip().rstrip('. ')
        input = parse_params(func.find('params'))
        output = parse_params(func.find('returns'))
        categories_node = func.find('categories')
        see_also = parse_see_also(func.find('see-also'), isC)
        if see_also and (len(see_also) > 0):
            html = '<ul>\n'
            for item in see_also:
                html += f'    <li>{item}</li>\n'
            see_also = html + '</ul>'
        else:
            see_also = ''
        filename = funcname_to_filename(funcname, isC)
        synopsis = ''
        for l in lang.split(','):
            if synopsis != '':
                synopsis += '\n\n'
            syn = format_synopsis(prepare_synopsis(funcname, input, output, l), 100)
            if l != 'c':
                syn = addCodeSection(syn, l)
            synopsis = synopsis + syn

        if input and (len(input) > 0):
            html = "<ul>\n"
            for param in input:
                name = param.get('name', '')
                description = param.get('description', '')
                html += f"    <li><strong>{name}</strong>: {description}</li>\n"
            input = html + "</ul>"
        else:
            input = ''
            
        if output and (len(output) > 0):
            html = "<ul>\n"
            for param in output:
                name = param.get('name', '')
                description = param.get('description', '')
                if isC:
                    html += f"    <li>{description}</li>\n"
                else:
                    html += f"    <li><strong>{name}</strong>: {description}</li>\n"
            output = html + "</ul>"
        else:
            output = ''

        nm = apiDir_currentVer / filename
        with nm.open('w') as file_w:
            if not isC:
                a = template
            else:
                a = template_cpp
            a = a.replace('__funcName__', funcname)
            a = a.replace('__funcDescription__', funcdescription)
            a = a.replace('__funcVer__', FUNC_VER_INFO)
            a = a.replace('__seeAlso__', see_also)
            if len(see_also) > 0:
                a = a.replace('__seealsoVisibility__', '')
            else:
                a = a.replace('__seealsoVisibility__', 'style="display: none;"')
            a = a.replace('__synopsis__', synopsis)
            a = a.replace('__input__', input)
            if len(input) > 0:
                a = a.replace('__inputVisibility__', '')
            else:
                a = a.replace('__inputVisibility__', 'style="display: none;"')
            a = a.replace('__output__', output)
            if len(output) > 0:
                a = a.replace('__outputVisibility__', '')
            else:
                a = a.replace('__outputVisibility__', 'style="display: none;"')
            a = a.replace('__more__', more)
            if len(more) > 0:
                a = a.replace('__moreVisibility__', '')
            else:
                a = a.replace('__moreVisibility__', 'style="display: none;"')
            file_w.write(minify_html.minify(a))

    # Now copy ALL functions into apiDir_all:
    try:
        shutil.rmtree(apiDir_all)
    except Exception as e:
        pass
    os.makedirs(apiDir_all)
    # First, copy previous API functions:
    for item in apiDirs_oldVer:
        for filename in os.listdir(item):
            if filename.endswith('.htm'):
                src_path = os.path.join(item, filename)
                dst_path = os.path.join(apiDir_all, filename)
                shutil.copy2(src_path, dst_path)    
    # Now, copy current API functions:
    for filename in os.listdir(apiDir_currentVer):
        if filename.endswith('.htm'):
            src_path = os.path.join(apiDir_currentVer, filename)
            dst_path = os.path.join(apiDir_all, filename)
            shutil.copy2(src_path, dst_path)    
            
    print(f'\nTotal generated: {cnt}')

if __name__ == "__main__":
    main()
