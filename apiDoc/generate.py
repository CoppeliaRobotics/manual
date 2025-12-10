import os
import sys
import re
import shutil
import copy
import xml.etree.ElementTree as ET
import minify_html
from pathlib import Path

currentDir = Path(__file__).absolute().parent

currentVer = 'sim-2'
FUNC_VER_INFO = '<a href="../apisOverview.htm">' + currentVer + '</a>'
apiDir_main = currentDir / '..' / 'en'
apiDir_currentVer = currentDir / '..' / 'en' / currentVer
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
    
def funcname_to_filename(name, isC, objName):
    if isC:
        return name + '_cpp.htm'
    elif name.startswith('sim.'):
        name = name[4:]  # Everything after 'sim.'
        name = 'sim' + name[0].upper() + name[1:]
    elif objName and len(objName) > 0:
        name = objName + '_' + name
    return name + '.htm' 
    
def parse_see_also(see_also_node, isC, objName):
    references = []
    if see_also_node is None:
        return references
    for func_ref in see_also_node.findall('function-ref'):
        fullfuncname = func_ref.get('name', '').strip()
        funcname = fullfuncname
        p = fullfuncname.split(':')
        if len(p) > 1:
            objName = p[0]
            funcname = p[1]
        references.append('<a href="' + funcname_to_filename(funcname, isC, objName) + '">' + fullfuncname + '</a>')
    for link in see_also_node.findall('link'):
        references.append('<a href="' + link.get('href', '') + '">' + link.get('label', '').strip() + '</a>')
    return references
    
def parse_categories(cat_node):
    catList = []
    if cat_node is None:
        return catList
    for cat in cat_node.findall('category'):
        catList.append(cat.get('name', ''))
    return catList
    
'''def parse_restrict_obj_type(restr_node):
    tList = []
    if restr_node is None:
        return tList
    for cat in restr_node.findall('object-type'):
        tList.append(cat.get('name', ''))
    return tList
'''
    
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
    methodCategories = [
        {'cat': 'object',           'obj': True,    'txt': 'Object',                                        'page': '',                                                 'oldRefs': []},
        {'cat': 'app',              'obj': True,    'txt': 'App',                                           'page': '',                                                 'oldRefs': []},
        {'cat': 'scene',            'obj': True,    'txt': 'Scene',                                         'page': 'scenes.htm',                                       'oldRefs': []},
        {'cat': 'collection',       'obj': True,    'txt': 'Collection',                                    'page': 'collections.htm',                                  'oldRefs': ['collections']},
        {'cat': 'drawingObject',    'obj': True,    'txt': 'Drawing object',                                'page': 'dataVisualizationAndOutput.htm#augmentingScene',   'oldRefs': []},
        {'cat': 'detachedScript',   'obj': True,    'txt': 'Detached script',                               'page': 'scripts.htm',                                      'oldRefs': []},
        {'cat': 'mesh',             'obj': True,    'txt': 'Mesh',                                          'page': 'geometricCalculations.htm',                        'oldRefs': []},
        {'cat': 'sceneObject',      'obj': True,    'txt': 'Scene object',                                  'page': 'objects.htm',                                      'oldRefs': ['sceneObjectFunctionality']},
        {'cat': 'shape',            'obj': True,    'txt': 'Shape',                                         'page': 'shapes.htm',                                       'oldRefs': ['shapeObject']},
        {'cat': 'joint',            'obj': True,    'txt': 'Joint',                                         'page': 'joints.htm',                                       'oldRefs': ['jointObject']},
        {'cat': 'dummy',            'obj': True,    'txt': 'Dummy',                                         'page': 'dummies.htm',                                      'oldRefs': ['dummyObject']},
        {'cat': 'script',           'obj': True,    'txt': 'Script',                                        'page': 'scriptObjects.htm',                                'oldRefs': []},
        {'cat': 'camera',           'obj': True,    'txt': 'Camera',                                        'page': 'cameras.htm',                                      'oldRefs': ['cameraObject']},
        {'cat': 'light',            'obj': True,    'txt': 'Light',                                         'page': 'lights.htm',                                       'oldRefs': ['lightObject']},
        {'cat': 'graph',            'obj': True,    'txt': 'Graph',                                         'page': 'graphs.htm',                                       'oldRefs': ['graphs']},
        {'cat': 'proximitySensor',  'obj': True,    'txt': 'Proximity sensor',                              'page': 'proximitySensors.htm',                             'oldRefs': []},
        {'cat': 'visionSensor',     'obj': True,    'txt': 'Vision sensor',                                 'page': 'visionSensors.htm',                                'oldRefs': []},
        {'cat': 'forceSensor',      'obj': True,    'txt': 'Force sensor',                                  'page': 'forceSensors.htm',                                 'oldRefs': []},
        {'cat': 'pointCloud',       'obj': True,    'txt': 'Point cloud',                                   'page': 'pointClouds.htm',                                  'oldRefs': []},
        {'cat': 'ocTree',           'obj': True,    'txt': 'OC-tree',                                       'page': 'octrees.htm',                                      'oldRefs': ['octree']},
        {'cat': 'path',             'obj': False,   'txt': 'Paths',                                         'page': 'paths.htm',                                        'oldRefs': ['paths']},
        {'cat': 'file',             'obj': False,   'txt': 'File operations',                               'page': '',                                                 'oldRefs': ['fileOperations']},
        {'cat': 'main',             'obj': False,   'txt': 'General functionality handling',                'page': '',                                                 'oldRefs': ['mainFunctionalityHandling']},
        {'cat': 'dynamics',         'obj': False,   'txt': 'Dynamics',                                      'page': 'dynamicsModule.htm',                               'oldRefs': ['dynamicsFunctionality']},
        {'cat': 'property',         'obj': False,   'txt': 'Properties',                                    'page': 'properties.htm',                                   'oldRefs': ['properties']},
        {'cat': 'collision',        'obj': False,   'txt': 'Collision detection',                           'page': 'collisionDetection.htm',                           'oldRefs': ['collisionDetection']},
        {'cat': 'distance',         'obj': False,   'txt': 'Distance calculation',                          'page': 'distanceCalculation.htm',                          'oldRefs': ['distanceCalculation']},
        {'cat': 'rendering',        'obj': False,   'txt': 'Rendering',                                     'page': 'dataVisualizationAndOutput.htm',                   'oldRefs': []},
        {'cat': 'customization',    'obj': False,   'txt': 'Customization',                                 'page': '',                                                 'oldRefs': ['customizingLuaFunctions', 'customScriptFunctions']},
        {'cat': 'model',            'obj': False,   'txt': 'Models',                                        'page': 'models.htm',                                       'oldRefs': ['modelFunctionality']},
        {'cat': 'selection',        'obj': False,   'txt': 'Selection',                                     'page': '',                                                 'oldRefs': ['sceneObjectSelectionFunctionality']},
        {'cat': 'creation',         'obj': False,   'txt': 'Object creation',                               'page': '',                                                 'oldRefs': ['sceneObjectCreationFunctionality']},
        {'cat': 'scriptRelated',    'obj': False,   'txt': 'Script related',                                'page': 'scripts.htm',                                      'oldRefs': []},
        {'cat': 'simulation',       'obj': False,   'txt': 'Simulation',                                    'page': 'simulation.htm',                                   'oldRefs': ['SimulationFunctionality']},
        {'cat': 'thread',           'obj': False,   'txt': 'Threads',                                       'page': 'threadedAndNonThreadedCode.htm',                   'oldRefs': ['threads', 'threadRelatedFunctionality']},
        {'cat': 'blocking',         'obj': False,   'txt': 'Blocking functions',                            'page': '',                                                 'oldRefs': ['blockingFunctions']},
        {'cat': 'transformation',   'obj': False,   'txt': 'Coordinates and transformations',               'page': 'positionOrientationTransformation.htm',            'oldRefs': ['pose', 'transformations', 'coordinatesAndTransformations']},
        {'cat': 'messaging',        'obj': False,   'txt': 'Messaging',                                     'page': 'meansOfCommunication.htm',                         'oldRefs': []},
        {'cat': 'texture',          'obj': False,   'txt': 'Textures',                                      'page': '',                                                 'oldRefs': ['textures']},
        {'cat': 'auxConsole',       'obj': False,   'txt': 'Auxiliary consoles',                            'page': 'dataVisualizationAndOutput.htm#auxConsoles',       'oldRefs': ['auxiliaryConsoles', 'auxiliaryConsoleFunctions']},
        {'cat': 'textEditor',       'obj': False,   'txt': 'Text/code editor',                              'page': 'dataVisualizationAndOutput.htm#textEditors',       'oldRefs': ['textEditors']},
        {'cat': 'importExport',     'obj': False,   'txt': 'Import/export',                                 'page': 'importExport.htm',                                 'oldRefs': ['importExportFunctions']},
        {'cat': 'motion',           'obj': False,   'txt': 'Motion functionality',                          'page': '',                                                 'oldRefs': ['rml', 'ruckig']},
        {'cat': 'packing',          'obj': False,   'txt': 'Packing/unpacking',                             'page': '',                                                 'oldRefs': []},
        {'cat': 'stack',            'obj': False,   'txt': 'Stacks',                                        'page': '',                                                 'oldRefs': ['stacks']},
        {'cat': 'other',            'obj': False,   'txt': 'Other',                                         'page': '',                                                 'oldRefs': []}
    ]

    functionCategories = copy.deepcopy(methodCategories)

    allMethodCategories = {}
    for item in methodCategories:
        allMethodCategories[item['cat']] = {'txt': item['txt'], 'api': []}

    allFunctionCategories = {}
    for item in functionCategories:
        allFunctionCategories[item['cat']] = {'txt': item['txt'], 'api': []}
    
    def handle_func_or_method(file, func, obj_name, template, template_cpp):
        funcnameRaw = func.get('name').strip()
        #print('className:', obj_name, 'funcName:', funcnameRaw)
        lang = func.get('lang').strip()
        deprecated = (func.get('deprecated') == 'true')
        isC = (lang == 'c')
        funcdescription = getTxt(func, 'description').strip().rstrip('. ')
        more = (getTxt(func, 'more') or '').strip().rstrip('. ')
        input = parse_params(func.find('params'))
        output = parse_params(func.find('returns'))
        
        see_also = parse_see_also(func.find('see-also'), isC, obj_name)
        if len(obj_name) > 0:
            if not see_also:
                see_also = []
            see_also.insert(0, '<a href="../apiFunctions.htm#' + obj_name + '">' + "all methods in '" + obj_name + "'</a>") 
        if see_also and (len(see_also) > 0):
            html = '<ul>\n'
            for item in see_also:
                html += f'    <li>{item}</li>\n'
            see_also = html + '</ul>'
        else:
            see_also = ''
        filename = funcname_to_filename(funcnameRaw, isC, obj_name)
        funcname = funcnameRaw
        if obj_name and len(obj_name) > 0:
            funcname = obj_name + ':' + funcname
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

        categories = parse_categories(func.find('categories'))
        if obj_name and len(obj_name) > 0:
            categories = [x for x in categories if x != obj_name] # remove possible obj_name listed there
            categories.insert(0, obj_name) # add to front
        for cat in categories:
            if cat in file['categoriesMap']:
                file['categoriesMap'][cat]['api'].append({'fullName': funcname, 'name': funcnameRaw, 'file': currentVer + '/' + filename, 'c': isC})
            else:
                raise Exception("Category '" + cat + "' not found!")
                
        #restrictToObjectTypes = parse_restrict_obj_type(func.find('restrict-object-types'))
        #if len(restrictToObjectTypes) > 0:
        #    print(restrictToObjectTypes)
        
        nm = apiDir_currentVer / filename
        with nm.open('w') as file_w:
            if not isC:
                a = template
            else:
                a = template_cpp
            funcnamePlus = funcname
            if deprecated:
                funcnamePlus += ' (deprecated)'
            a = a.replace('__funcName__', funcnamePlus)
            a = a.replace('__funcDescription__', funcdescription)
            a = a.replace('__funcVer__', FUNC_VER_INFO)
            
            a = a.replace('__seeAlso__', see_also)
            if len(see_also) > 0:
                a = a.replace('__seealsoVisibility__', '')
            else:
                a = a.replace('__seealsoVisibility__', 'style="display: none;"')
            
            
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

    files = [
        {
            'inputFile': currentDir / 'functions.xml',
            'cTemplate': templatesDir / 'cFunc.htm',
            'pythonLuaTemplate': templatesDir / 'pythonLuaFunc.htm',
            'categories': functionCategories,
            'categoriesMap': allFunctionCategories,
            'type': 'functions'
        },
        {
            'inputFile': currentDir / 'objects.xml',
            'pythonLuaTemplate': templatesDir / 'pythonLuaMethod.htm',
            'categories': methodCategories,
            'categoriesMap': allMethodCategories,
            'type': 'objects'
        }
    ]

    for file in files:

        handleFunctions = (file['type'] == 'functions')
        
        if handleFunctions:
            with (file['cTemplate']).open('r') as file_r:
                template_cpp = file_r.read()

        with (file['pythonLuaTemplate']).open('r') as file_r:
            template = file_r.read()

            
        tree = ET.parse(file['inputFile'])
        cnt = 0
        
        if handleFunctions:
            funcs = tree.getroot()
            for func in funcs:
                handle_func_or_method(file, func, '', template, template_cpp)
                cnt += 1
        else:
            objs = tree.getroot()
            for obj in objs:
                obj_name = obj.get('name').strip()
                for method in obj.findall('method'):
                    handle_func_or_method(file, method, obj_name, template, template_cpp)
                    cnt += 1
        file['cnt'] = cnt

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
    cnt1 = files[0]['cnt']     
    cnt2 = files[1]['cnt']     
    print(f'\nTotal generated: {cnt1} + {cnt2}')

    # Now generate apiFunctions.htm:
    with (templatesDir / 'funcList.htm').open('r') as file_r:
        listTemplate = file_r.read()

    methodCatLinks = ''
    methodSection = ''
    for item in methodCategories:
        cat = item['cat']
        oldRefs = item['oldRefs']
        page = item['page']
        obj = item['obj']
        if len(allMethodCategories[cat]['api']):
            methodLinks = ''
            title = allMethodCategories[cat]['txt']
            catApis = allMethodCategories[cat]['api']
            if obj:
                catApis = [f for f in catApis if f['fullName'].startswith(cat + ':')] # remove functions that do not belong to cat (but only for objects)
            funcs = sorted(catApis, key=lambda x: x['fullName'])
            for e in funcs:
                name = e['fullName']
                file = e['file']
                if len(methodLinks) != 0:
                    methodLinks += '\n'
                methodLinks += '<a href="' + file + '">' + name + '</a>'
            methodCatLinks += '<li><a href="#' + cat + '">' + title + '</a></li>'
            methodSection += '<h2><a name="' + cat + '"></a>' 
            for r in oldRefs:
                methodSection += '<h2><a name="' + r + '"></a>' 
            if len(page) > 0:
                title = '<a href="' + page + '">' + title + '</a>'
            methodSection += title + ' (methods)</h2>\n'
            methodSection += '<code class="language-python-lua coppelia-coppeliasim-script api-list">'
            methodSection += methodLinks
            methodSection += '</code><br>'

    functionCatLinks = ''
    functionSection = ''
    cfunctionCatLinks = ''
    cfunctionSection = ''
    for item in functionCategories:
        cat = item['cat']
        oldRefs = item['oldRefs']
        page = item['page']
        if len(allFunctionCategories[cat]['api']):
            functionLinks = ''
            cfunctionLinks = ''
            title = allFunctionCategories[cat]['txt']
            funcs = sorted(allFunctionCategories[cat]['api'], key=lambda x: x['fullName'])
            for e in funcs:
                name = e['fullName']
                file = e['file']
                isC = e['c']
                if isC:
                    if len(cfunctionLinks) != 0:
                        cfunctionLinks += '\n'
                    cfunctionLinks += '<a href="' + file + '">' + name + '</a>'
                else:
                    if len(functionLinks) != 0:
                        functionLinks += '\n'
                    functionLinks += '<a href="' + file + '">' + name + '</a>'
            if len(functionLinks) != 0:
                functionCatLinks += '<li><a href="#_' + cat + '">' + title + '</a></li>'
                functionSection += '<h2><a name="_' + cat + '"></a>'
                for r in oldRefs:
                    functionSection += '<h2><a name="' + r + '"></a>' 
                if len(page) > 0:
                    title = '<a href="' + page + '">' + title + '</a>'
                functionSection += title + ' (Python/Lua functions)</h2>\n'
                functionSection += '<code class="language-python-lua coppelia-coppeliasim-script api-list">'
                functionSection += functionLinks
                functionSection += '</code><br>'
            if len(cfunctionLinks) != 0:
                cfunctionCatLinks += '<li><a href="#c_' + cat + '">' + title + '</a></li>'
                cfunctionSection += '<h2><a name="c_' + cat + '"></a>'
                for r in oldRefs:
                    cfunctionSection += '<h2><a name="' + r + '"></a>' 
                if len(page) > 0:
                    title = '<a href="' + page + '">' + title + '</a>'
                cfunctionSection += title + ' (C-functions)</h2>\n'
                cfunctionSection += '<code class="language-c++ coppelia-coppeliasim-plugin api-list">'
                cfunctionSection += cfunctionLinks
                cfunctionSection += '</code><br>'

    listTemplate = listTemplate.replace('__methodLinks__', methodCatLinks)
    listTemplate = listTemplate.replace('__methodSection__', methodSection)
    listTemplate = listTemplate.replace('__functionLinks__', functionCatLinks)
    listTemplate = listTemplate.replace('__functionSection__', functionSection)
    listTemplate = listTemplate.replace('__cfunctionLinks__', cfunctionCatLinks)
    listTemplate = listTemplate.replace('__cfunctionSection__', cfunctionSection)
            
    nm = apiDir_main / 'apiFunctions.htm'
    with nm.open('w') as file_w:
        file_w.write(minify_html.minify(listTemplate))


if __name__ == "__main__":
    main()
