import os
import sys
import re
import argparse
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

categories = [
    # Order matters. Keep first 4 in place!
    {'cat': 'c_main',                   'obj': False,   'txt': 'Main',                                              'page': '',                                                 'oldRefs': []},
    {'cat': 'c_property',               'obj': False,   'txt': 'Properties',                                        'page': 'properties.htm',                                   'oldRefs': []},
    {'cat': 'c_stack',                  'obj': False,   'txt': 'Stack',                                             'page': '',                                                 'oldRefs': []},
    {'cat': 'c_aux',                    'obj': False,   'txt': 'Auxiliary functions',                               'page': '',                                                 'oldRefs': []},
    {'cat': 'object',                   'obj': True,    'txt': 'object',                                            'page': '',                                                 'oldRefs': []},
    {'cat': 'app',                      'obj': True,    'txt': 'app',                                               'page': '',                                                 'oldRefs': []},
    {'cat': 'scene',                    'obj': True,    'txt': 'scene',                                             'page': 'scenes.htm',                                       'oldRefs': []},
    {'cat': 'collection',               'obj': True,    'txt': 'collection',                                        'page': 'collections.htm',                                  'oldRefs': ['collections']},
    {'cat': 'customObject',             'obj': True,    'txt': 'customObject',                                      'page': 'customObjects.htm',                                'oldRefs': []},
    {'cat': 'detachedScript',           'obj': True,    'txt': 'detachedScript',                                    'page': 'scripts.htm',                                      'oldRefs': []},
    {'cat': 'mesh',                     'obj': True,    'txt': 'mesh',                                              'page': 'geometricCalculations.htm',                        'oldRefs': []},
    {'cat': 'sceneObject',              'obj': True,    'txt': 'sceneObject',                                       'page': 'objects.htm',                                      'oldRefs': ['sceneObjectFunctionality']},
    {'cat': 'shape',                    'obj': True,    'txt': 'sceneObject.shape',                                 'page': 'shapes.htm',                                       'oldRefs': ['shapeObject']},
    {'cat': 'joint',                    'obj': True,    'txt': 'sceneObject.joint',                                             'page': 'joints.htm',                                       'oldRefs': ['jointObject']},
    {'cat': 'dummy',                    'obj': True,    'txt': 'sceneObject.dummy',                                             'page': 'dummies.htm',                                      'oldRefs': ['dummyObject']},
    {'cat': 'marker',                   'obj': True,    'txt': 'sceneObject.marker',                                            'page': 'markers.htm',                                      'oldRefs': []},
    {'cat': 'script',                   'obj': True,    'txt': 'sceneObject.script',                                            'page': 'scriptObjects.htm',                                'oldRefs': []},
    {'cat': 'camera',                   'obj': True,    'txt': 'sceneObject.camera',                                            'page': 'cameras.htm',                                      'oldRefs': ['cameraObject']},
    {'cat': 'light',                    'obj': True,    'txt': 'sceneObject.light',                                             'page': 'lights.htm',                                       'oldRefs': ['lightObject']},
    {'cat': 'graph',                    'obj': True,    'txt': 'sceneObject.graph',                                             'page': 'graphs.htm',                                       'oldRefs': ['graphs']},
    {'cat': 'proximitySensor',          'obj': True,    'txt': 'sceneObject.proximitySensor',                                   'page': 'proximitySensors.htm',                             'oldRefs': []},
    {'cat': 'visionSensor',             'obj': True,    'txt': 'sceneObject.visionSensor',                                      'page': 'visionSensors.htm',                                'oldRefs': []},
    {'cat': 'forceSensor',              'obj': True,    'txt': 'sceneObject.forceSensor',                                       'page': 'forceSensors.htm',                                 'oldRefs': []},
    {'cat': 'pointCloud',               'obj': True,    'txt': 'sceneObject.pointCloud',                                        'page': 'pointClouds.htm',                                  'oldRefs': []},
    {'cat': 'ocTree',                   'obj': True,    'txt': 'sceneObject.ocTree',                                            'page': 'octrees.htm',                                      'oldRefs': ['octree']},
    {'cat': 'customSceneObject',        'obj': True,    'txt': 'sceneObject.customSceneObject',                                 'page': 'customSceneObjects.htm',                           'oldRefs': []},
    {'cat': 'Path',                     'obj': False,   'txt': 'Path',                                              'page': 'paths.htm',                                        'oldRefs': ['paths']},
    {'cat': 'file',                     'obj': False,   'txt': 'File operations',                                   'page': '',                                                 'oldRefs': ['fileOperations']},
    {'cat': 'main',                     'obj': False,   'txt': 'General functionality handling',                    'page': '',                                                 'oldRefs': ['mainFunctionalityHandling']},
    {'cat': 'dynamics',                 'obj': False,   'txt': 'Dynamics',                                          'page': 'dynamicsModule.htm',                               'oldRefs': ['dynamicsFunctionality']},
    {'cat': 'property',                 'obj': False,   'txt': 'Properties',                                        'page': 'properties.htm',                                   'oldRefs': ['properties']},
    {'cat': 'collision',                'obj': False,   'txt': 'Collision detection',                               'page': 'collisionDetection.htm',                           'oldRefs': ['collisionDetection']},
    {'cat': 'distance',                 'obj': False,   'txt': 'Distance calculation',                              'page': 'distanceCalculation.htm',                          'oldRefs': ['distanceCalculation']},
    {'cat': 'rendering',                'obj': False,   'txt': 'Rendering',                                         'page': 'dataVisualizationAndOutput.htm',                   'oldRefs': []},
    {'cat': 'customization',            'obj': False,   'txt': 'Customization',                                     'page': '',                                                 'oldRefs': ['customizingLuaFunctions', 'customScriptFunctions']},
    {'cat': 'model',                    'obj': False,   'txt': 'Models',                                            'page': 'models.htm',                                       'oldRefs': ['modelFunctionality']},
    {'cat': 'selection',                'obj': False,   'txt': 'Selection',                                         'page': '',                                                 'oldRefs': ['sceneObjectSelectionFunctionality']},
    {'cat': 'creation',                 'obj': False,   'txt': 'Object creation',                                   'page': '',                                                 'oldRefs': ['sceneObjectCreationFunctionality']},
    {'cat': 'scriptRelated',            'obj': False,   'txt': 'Script related',                                    'page': 'scripts.htm',                                      'oldRefs': []},
    {'cat': 'simulation',               'obj': False,   'txt': 'Simulation',                                        'page': 'simulation.htm',                                   'oldRefs': ['SimulationFunctionality']},
    {'cat': 'thread',                   'obj': False,   'txt': 'Threads',                                           'page': 'threadedAndNonThreadedCode.htm',                   'oldRefs': ['threads', 'threadRelatedFunctionality']},
    {'cat': 'blocking',                 'obj': False,   'txt': 'Blocking methods',                                  'page': '',                                                 'oldRefs': ['blockingFunctions']},
    {'cat': 'transformation',           'obj': False,   'txt': 'Coordinates and transformations',                   'page': 'positionOrientationTransformation.htm',            'oldRefs': ['pose', 'transformations', 'coordinatesAndTransformations']},
    {'cat': 'messaging',                'obj': False,   'txt': 'Messaging',                                         'page': 'meansOfCommunication.htm',                         'oldRefs': []},
    {'cat': 'texture',                  'obj': False,   'txt': 'Textures',                                          'page': '',                                                 'oldRefs': ['textures']},
    {'cat': 'Console',                  'obj': False,   'txt': 'Console',                                           'page': 'dataVisualizationAndOutput.htm#auxConsoles',       'oldRefs': ['auxiliaryConsoles', 'auxiliaryConsoleFunctions']},
    {'cat': 'TextEditor',               'obj': False,   'txt': 'TextEditor',                                        'page': 'dataVisualizationAndOutput.htm#textEditors',       'oldRefs': ['textEditors']},
    {'cat': 'importExport',             'obj': False,   'txt': 'Import/export',                                     'page': 'importExport.htm',                                 'oldRefs': ['importExportFunctions']},
    {'cat': 'Motion',                   'obj': False,   'txt': 'Motion functionality',                              'page': '',                                                 'oldRefs': ['rml', 'ruckig']},
    {'cat': 'MoveToConfig',             'obj': False,   'txt': 'Motion.MoveToConfig',                               'page': '',                                                 'oldRefs': ['rml', 'ruckig']},
    {'cat': 'MoveToPose',               'obj': False,   'txt': 'Motion.MoveToPose',                                 'page': '',                                                 'oldRefs': ['rml', 'ruckig']},
    {'cat': 'TimeOptimalTrajectory',    'obj': False,   'txt': 'Motion.TimeOptimalTrajectory',                      'page': '',                                                 'oldRefs': ['rml', 'ruckig']},
    {'cat': 'RuckigPosition',           'obj': False,   'txt': 'Motion.RuckigPosition',                             'page': '',                                                 'oldRefs': ['rml', 'ruckig']},
    {'cat': 'RuckigVelocity',           'obj': False,   'txt': 'Motion.RuckigVelocity',                             'page': '',                                                 'oldRefs': ['rml', 'ruckig']},
    {'cat': 'packing',                  'obj': False,   'txt': 'Packing/unpacking',                                 'page': '',                                                 'oldRefs': []},
    {'cat': 'stack',                    'obj': False,   'txt': 'Stacks',                                            'page': '',                                                 'oldRefs': ['stacks']},
    {'cat': 'ik',                       'obj': False,   'txt': 'Kinematics',                                        'page': 'kinematics.htm',                                   'oldRefs': []},
    {'cat': 'ikObject',                 'obj': False,   'txt': 'IKObject',                                          'page': 'solvingIkAndFk.htm',                               'oldRefs': []},
    {'cat': 'ikJoint',                  'obj': False,   'txt': 'IKObject.IKjoint',                                  'page': 'solvingIkAndFk.htm',                               'oldRefs': []},
    {'cat': 'ikGroup',                  'obj': False,   'txt': 'IKGroup',                                           'page': 'solvingIkAndFk.htm',                               'oldRefs': []},
    {'cat': 'ikElement',                'obj': False,   'txt': 'IKElement',                                         'page': 'solvingIkAndFk.htm',                               'oldRefs': []},
    {'cat': 'other',                    'obj': False,   'txt': 'Other',                                             'page': '',                                                 'oldRefs': []},
    {'cat': 'drawingObject',            'obj': False,   'txt': 'drawingObject (deprecated, see marker instead)',    'page': '',                                                 'oldRefs': []},
]

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

def parse_commandline_args():
    parser = argparse.ArgumentParser(description="Process XML input files.")

    parser.add_argument(
        "--enums-xml",
        required=True,
        help="Path to enums XML file"
    )

    parser.add_argument(
        "--functions-xml",
        required=True,
        help="Path to functions XML file"
    )

    parser.add_argument(
        "--objects-xml",
        required=True,
        help="Path to objects XML file"
    )

    parser.add_argument(
        "--output-dir",
        help="Directory where all generated files will be written"
    )

    parser.add_argument(
        "--debug",
        help="Enable debug output"
    )
    return parser.parse_args()

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

def getPropertyFlags(node):
    retVal = []
    s = node.find('flags')
    if s != None:
        fl = ['deprecated', 'readable', 'writable', 'removable', 'silent', 'constant']
        for f in fl:
            v = s.get(f)
            if v != None:
                retVal.append(f)
    if retVal[0] == 'deprecated':
        return []
    return retVal

def fmpToFilename(name, docItemType, objName, auxType = None):
    name = name.replace('.', '_').replace(':', '_')
    if auxType == None:
        auxType = docItemType
    if auxType == 'function':
        name = name + '_cpp'
    if auxType == 'method':
        if objName and len(objName) > 0:
            name = objName + '_' + name
    if auxType == 'property':
        if objName and len(objName) > 0:
            name = objName + '_' + name
        name = 'property_' + name
    return name + '.htm'

def parse_see_also(see_also_node, docItemType, objName):
    references = []
    if see_also_node is None:
        return references
    for funcProp in ['function', 'property']:
        if funcProp == 'property':
            auxType = funcProp
        if funcProp == 'function':
            if docItemType == 'function':
                auxType = docItemType
            else:
                auxType = 'method'
        for funcProp_ref in see_also_node.findall(funcProp + '-ref'):
            fullfuncPropName = funcProp_ref.get('name', '').strip()
            funcPropName = fullfuncPropName
            tmp = fullfuncPropName.replace(':', '.')
            p = tmp.find('.')
            if p != -1:
                objName = fullfuncPropName[:p]
                funcPropName = fullfuncPropName[p + 1:]
            '''
            p = re.split(r'[:.]+', fullfuncPropName)
            print(fullfuncPropName, '     ', p)
            if len(p) > 1:
                objName = p[0]
                funcPropName = ''.join(p[1:])
            '''
            references.append('<a href="' + fmpToFilename(funcPropName, docItemType, objName, auxType) + '">' + fullfuncPropName + ' (' + auxType + ')</a>')
    for link in see_also_node.findall('link'):
        references.append('<a href="' + link.get('href', '') + '">' + link.get('label', '').strip() + '</a>')
    return references

def parse_categories(cat_node):
    catList = []
    if cat_node is None:
        return catList
    for cat in cat_node.findall('category'):
        nm = cat.get('name', '')
        catList.append(nm.lower())
    return catList

def transform_type_for_languages(param_type, languages):
    retVal = ''
    cnt = 0
    if 'lua' in languages:
        cnt += 1
        retVal += transform_type_for_language(param_type, 'lua')
    if 'python' in languages:
        cnt += 1
        pt = transform_type_for_language(param_type, 'python')
        if pt != retVal:
            if cnt == 2:
                retVal += '/'
            retVal += pt
    if len(retVal) == 0:
        retVal = param_type
    return retVal

def transform_type_for_language(param_type, language):
    retVal = ''
    param_python = ''
    type_map = {
        'vector': 'vector',
        'vector3': 'vector3',
        'quaternion': 'quaternion',
        'pose': 'pose',
        'matrix': 'matrix',
        'color': 'color',
        'func': 'func',
        'map': 'dict',
        'bool': 'bool',
        'int': 'int',
        'float': 'float',
        'string': 'str',
        'any': 'any',
        'handle': 'int',
        'buffer': 'bytes',
        'enum': 'int',
        'object': 'object',
    }
    for lua_type, python_type in type_map.items():
        if param_type == lua_type:
            param_python = python_type
            break
        else:
            if ('[' in param_type) and param_type.startswith(lua_type):
                param_python = 'list'
                break
    if len(param_python) == 0:
        raise ValueError(f"Unsupported type '{param_type}' for language '{language}'")

    if language == 'lua':
        retVal = param_type
    if language == 'python':
        retVal = param_python

    if len(retVal) == 0:
        raise ValueError(f"Unsupported language: '{language}'")

    return retVal

def transformTypeValueForHyperlink(name, param_type):
    retVal = name
    a=retVal
    descrpt_map = {
        'vector': "vector",
        'vector3': "vector3",
        'quaternion': "quaternion",
        'pose': "pose",
        'matrix': "matrix",
        'color': "color",
        'func': "function",
        'map': "map",
        'bool': "bool",
        'int': "int",
        'float': "float",
        'string': "string",
        'any': "any",
        'handle': "handle",
        'buffer': "buffer",
        'enum': "enum",
        'object': "object",
    }
    for lua_type, lua_descr in descrpt_map.items():
        if param_type == lua_type:
            retVal = '<a href="../commonTypes.htm#' + lua_descr + '">' + retVal + "</a>"
            break
        else:
            if ('[' in param_type) and param_type.startswith(lua_type):
                retVal = '<a href="../commonTypes.htm#' + lua_descr + 'Array">' + retVal + "</a>"
                break
    b=retVal
    if a == b:
        print("b",retVal, param_type)
    return retVal

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

    if (lang != 'c'):
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

def getRefCategories(docItem, fmpItem, obj_name): # "fmp" for "function, method or property"
    # Returns a list (with duplicates allowed) of categories that are referenced:
    itemCategories = parse_categories(fmpItem.find('categories'))
    if obj_name and len(obj_name) > 0:
        nm = obj_name.lower()
        itemCategories = [x for x in itemCategories if x != nm] # remove possible obj_name listed there
        itemCategories.append(nm)
    return itemCategories

def main():
    def handleFunctionsMethodsOrProperties(docItem, fmpItem, obj_name, superclass, namespace, template): # "fmp" for "function, method or property"
        # Processes each function, method or property, by generating the API file and additional info:
        def addEnums(str, enumsAlreadyFound):
            patterns = re.findall(r'<a\s+[^>]*href=["\']#([^"\']+)["\']', str)
            for p in patterns:
                if p not in enumsAlreadyFound:
                    enumsAlreadyFound.append(p)
            return enumsAlreadyFound
        enums = []
        fmpNameRaw = fmpItem.get('name').strip()
        if debug:
            print('class:', obj_name, ', func/method/property:', fmpNameRaw)
        docItemType = docItem['type']
        if docItemType == 'property':
            propType = fmpItem.get('type').strip()
            if propType == 'group':
                return
            propType = transformTypeValueForHyperlink(transform_type_for_language(propType, 'lua'), propType)
        else:
            lang = fmpItem.get('lang').strip()
        if docItemType == 'property':
            propFlags = getPropertyFlags(fmpItem)
            if propFlags == []:
                return # means deprecated
            html = '<ul>\n'
            for item in propFlags:
                html += f'    <li>{item}</li>\n'
            html = html + '</ul>'
            propFlags = html


        if docItemType == 'property':
            fmpDescription = getTxt(fmpItem, 'description')
            if fmpDescription == None:
                fmpDescription = getTxt(fmpItem, 'label')
            shortDescription = getTxt(fmpItem, 'label')
            if shortDescription == None:
                shortDescription = getTxt(fmpItem, 'label')
        else:
            fmpDescription = getTxt(fmpItem, 'description')
            shortDescription = getTxt(fmpItem, 'short-description')
            if fmpDescription == None:
                fmpDescription = shortDescription
            if shortDescription == None:
                shortDescription = fmpDescription
        if fmpDescription == None:
            fmpDescription = 'no description'
        if shortDescription == None:
            shortDescription = ''
        else:
            shortDescription = '     ' + shortDescription
        fmpDescription = fmpDescription.strip().rstrip('. ')
        enums = addEnums(fmpDescription, enums)
        more = (getTxt(fmpItem, 'more') or '').strip().rstrip('. ')
        input = parse_params(fmpItem.find('params'))
        output = parse_params(fmpItem.find('returns'))

        filename = fmpToFilename(fmpNameRaw, docItemType, obj_name)
        fmpName = fmpNameRaw
        if obj_name and len(obj_name) > 0:
            fmpName = fmpName.replace(':', '.')
            if docItemType == 'property':
                fmpName = obj_name + '.' + fmpName
            else:
                p = fmpName.rfind('.')
                if p != -1:
                    fmpName = obj_name + '.' + fmpName[:p] + ':' + fmpName[p + 1:]
                else:
                    fmpName = obj_name + ':' + fmpName
        fmpName = namespace + fmpName
        superclassFmpName = fmpName
        #if superclass and (len(superclass) > 0) and (superclass != 'object'):
        #    superclassFmpName = superclass + '.' + fmpName

        # Get the see-also items listed:
        see_also = parse_see_also(fmpItem.find('see-also'), docItemType, obj_name)
        if not see_also:
            see_also = []
        see_also_cat1 = []
        see_also_cat2 = []

        # Get the categories that function, property or method relates to:
        itemCategories = parse_categories(fmpItem.find('categories'))
        if obj_name and len(obj_name) > 0:
            nm = obj_name.lower()
            itemCategories = [x for x in itemCategories if x != nm] # remove possible obj_name listed there
            itemCategories.insert(0, nm) # add to front

        for cat in itemCategories:
            cat = cat.lower()
            if cat in docItem['categoriesMap']:
                docItem['categoriesMap'][cat]['api'].append({'fullName': fmpName, 'name': fmpNameRaw, 'file': currentVer + '/' + filename, 'c': docItemType == 'function', 'short': shortDescription})
                # Add see-also items related to the listed categories (but only within the same category type, i.e. method/prop cat for methods, function cat for functions, and method/property cat for properties):
                methFunc = 'methodsAndProperties'
                methFuncNm = 'methods &amp; properties'
                if docItemType == 'function':
                    methFunc = 'functions'
                    methFuncNm = 'functions'
                pref = methFunc + '_'
                see_also_cat1.append('<a href="../apiFunctions.htm#' + pref + cat + '">' + docItem['categoriesMap'][cat]['txt'] + ' (' + methFuncNm + ")</a>")
            else:
                raise Exception("Category '" + cat + "' not found for '" + fmpNameRaw + "'")

        # Add see-also items related to the listed categories, across a different category type (method/property cat for functions):

        if docItemType == 'function':
            for cat in itemCategories:
                cat = cat.lower()
                if (cat in methodDocItem['categoriesMap']) or (cat in propertyDocItem['categoriesMap']):
                    see_also_cat2.append('<a href="../apiFunctions.htm#' + 'methodsAndProperties_' + cat + '">' + categoriesMap[cat]['txt'] + " (methods &amp; properties)</a>")

        # Assemble see-also html string:
        if len(see_also) > 0 or len(see_also_cat1) or len(see_also_cat2) > 0:
            html = '<ul>\n'
            for item in see_also:
                html += f'    <li>{item}</li>\n'
            if len(see_also_cat1) > 0:
                html = html + '</ul><ul>\n'
                for item in see_also_cat1:
                    html += f'    <li>{item}</li>\n'
            if len(see_also_cat2) > 0:
                html = html + '</ul><ul>\n'
                for item in see_also_cat2:
                    html += f'    <li>{item}</li>\n'
            see_also = html + '</ul>'
        else:
            see_also = ''

        synopsis = ''
        if docItemType != 'property':
            for l in lang.split(','):
                if synopsis != '':
                    synopsis += '\n\n'
                syn = format_synopsis(prepare_synopsis(fmpName, input, output, l), 100)
                if l != 'c':
                    syn = addCodeSection(syn, l)
                synopsis = synopsis + syn

        if input and (len(input) > 0):
            html = "<ul>\n"
            for param in input:
                name = param.get('name', '')
                tp = param.get('type', '')
                if docItemType != 'function':
                    name = '<strong>' + name + '</strong>' + ' (' + transformTypeValueForHyperlink(transform_type_for_languages(tp, lang), tp) + ')'
                description = param.get('description', '')
                enums = addEnums(description, enums)
                html += f"    <li>{name}: {description}</li>\n"
            input = html + "</ul>"
        else:
            input = ''

        if output and (len(output) > 0):
            html = "<ul>\n"
            for param in output:
                name = param.get('name', '')
                tp = param.get('type', '')
                if docItemType != 'function':
                    name = '<strong>' + name + '</strong>' + ' (' + transformTypeValueForHyperlink(transform_type_for_languages(tp, lang), tp) + ')'
                description = param.get('description', '')
                enums = addEnums(description, enums)
                if docItemType == 'function':
                    html += f"    <li>{description}</li>\n"
                else:
                    html += f"    <li>{name}: {description}</li>\n"
            output = html + "</ul>"
        else:
            output = ''

        enums = addEnums(more, enums)

        enumSection = ''
        enumCnt = 0
        if 'enums' in docItem:
            enumSection = '<ul>'
            for enumT in enums:
                if enumT in docItem['enums']:
                    if enumCnt > 0:
                        enumSection += "<br>"
                    enumCnt += 1
                    item = docItem['enums'][enumT]
                    enumSection += '<li id="' + enumT + '"><b>' + item['label'] + '</b>:<ul>'
                    for iitem in item['enums']:
                        enumSection += "<li>" + iitem['name']
                        if iitem['val']:
                            enumSection += " (" + iitem['val'] + ")"
                        if iitem['descr']:
                            enumSection += ": " + iitem['descr']
                        enumSection += "</li>"
                    enumSection += "</ul></li>"
            enumSection += "</ul>"
        if enumCnt == 0:
            enumSection = ''

        nm = apiDir_currentVer / filename
        with nm.open('w', encoding='utf-8') as file_w:
            a = template
            funcnamePlus = superclassFmpName
            if docItemType == 'property':
                a = a.replace('__propName__', funcnamePlus)
                a = a.replace('__propDescription__', fmpDescription)
                a = a.replace('__propFlags__', propFlags)
            else:
                a = a.replace('__funcName__', funcnamePlus)
                a = a.replace('__funcDescription__', fmpDescription)
            a = a.replace('__funcVer__', FUNC_VER_INFO)

            a = a.replace('__seeAlso__', see_also)
            if len(see_also) > 0:
                a = a.replace('__seealsoVisibility__', '')
            else:
                a = a.replace('__seealsoVisibility__', 'style="display: none;"')

            if docItemType == 'property':
                a = a.replace('__type__', propType)
            else:
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

            a = a.replace('__enums__', enumSection)
            if len(enumSection) > 0:
                a = a.replace('__enumVisibility__', '')
            else:
                a = a.replace('__enumVisibility__', 'style="display: none;"')

            #file_w.write(a)
            file_w.write(minify_html.minify(a))

    categoriesMap = {}
    for item in categories:
        item['cat'] = item['cat'].lower()
        categoriesMap[item['cat']] = {'txt': item['txt'], 'api': []}

    args = parse_commandline_args()
    debug = (args.debug == 'true') or (args.debug == 'True')

    # If an output directory was provided, redirect all generated files there
    if args.output_dir:
        output_base = Path(args.output_dir).resolve()
        apiDir_main = output_base / 'en'
        apiDir_currentVer = output_base / 'en' / currentVer
        apiDir_all = output_base / 'en' / 'sim'
        # Note: apiDirs_oldVer and apiDir_deprecated_currentVer remain input directories (unchanged)

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

    methodDocItem = {
        'inputFile': args.objects_xml,
        #'enumFile': args.enums_xml,
        'apiFileTemplate': templatesDir / 'method.htm',
        'categoriesMap': copy.deepcopy(categoriesMap),
        'type': 'method',
    }

    functionDocItem = {
        'inputFile': args.functions_xml,
        'apiFileTemplate': templatesDir / 'function.htm',
        #'enumFile': args.enums_xml,
        #'methodTemplate': templatesDir / 'pythonLuaFunc.htm',
        'categoriesMap': copy.deepcopy(categoriesMap),
        'type': 'function',
    }

    propertyDocItem = {
        'inputFile': args.objects_xml,
        #'enumFile': args.enums_xml,
        'apiFileTemplate': templatesDir / 'property.htm',
        'categoriesMap': copy.deepcopy(categoriesMap),
        'type': 'property',
    }

    docItems = [methodDocItem, functionDocItem, propertyDocItem]

    # First remove unreferenced categories in methodDocItem, functionDocItem and propertyDocItem:
    for docItem in docItems:
        docItemType = docItem['type']
        try:
            tree = ET.parse(docItem['inputFile'])
        except ET.ParseError as e:
            raise ET.ParseError(f'{docItem["inputFile"]}: {e!s}')

        items = tree.getroot()

        usedCategories = {} # can contain duplicates
        for item in items:
            if docItemType == 'function':
                l = getRefCategories(docItem, item, '')
                for it in l:
                    usedCategories[it] = True
            else:
                obj_name = item.get('name').strip()
                for subItem in item.findall(docItemType):
                    l = getRefCategories(docItem, subItem, obj_name)
                    for it in l:
                        usedCategories[it] = True
        toRemove = []
        for key, val in docItem['categoriesMap'].items():
            if key not in usedCategories:
                toRemove.append(key)
        for item in toRemove:
            del docItem['categoriesMap'][item]

    # Now process methodDocItem, functionDocItem and propertyDocItem:
    for docItem in docItems:
        docItemType = docItem['type']

        with (docItem['apiFileTemplate']).open('r') as file_r:
            templateFile = file_r.read()
        '''
        if 'enumFile' in docItem:
            enumTree = ET.parse(docItem['enumFile'])
            enums_node = enumTree.getroot()
            enums = {}
            for enum_node in enums_node:
                enum_name = enum_node.get('name').strip()
                txt = enum_node.get('label').strip()
                enum = []
                for item_node in enum_node.findall('item'):
                    n = item_node.get('name').strip()
                    v = item_node.get('value')
                    if v:
                        v.strip()
                    d = getTxt(item_node, 'description')
                    if d:
                        d = d.strip().rstrip('. ')
                    enum.append({'name': n, 'val': v, 'descr': d})
                enums[enum_name] = {'label': txt, 'enums': enum}
            docItem['enums'] = enums
        '''

        try:
            tree = ET.parse(docItem['inputFile'])
        except ET.ParseError as e:
            raise ET.ParseError(f'{docItem["inputFile"]}: {e!s}')

        items = tree.getroot()

        cnt = 0
        # Process each method, function and property:
        for item in items:
            if docItemType == 'function':
                handleFunctionsMethodsOrProperties(docItem, item, '', '', '', templateFile)
                cnt += 1
            else:
                obj_name = item.get('name').strip()
                namespace = item.get('singleton')
                if namespace != None and len(namespace) > 0:
                    namespace = namespace.strip().split('.')[0] + '.'
                else:
                    namespace = ''
                superclass = item.get('superclass').strip()
                for subItem in item.findall(docItemType):
                    handleFunctionsMethodsOrProperties(docItem, subItem, obj_name, superclass, namespace, templateFile)
                    cnt += 1
        docItem['cnt'] = cnt

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

    cnt = [0, 0, 0]
    for index, docItem in enumerate(docItems):
        cnt[index] = cnt[index] + docItem['cnt']
    print(f'\nTotal generated: {cnt}')

    # Now generate apiFunctions.htm:
    with (templatesDir / 'apiList.htm').open('r') as file_r:
        listTemplate = file_r.read()

    # First fill items related to methods and properties:
    methodPropCatLinks = ''
    methodPropSection = ''
    for item in categories:
        cat = item['cat']
        oldRefs = item['oldRefs']
        page = item['page']
        obj = item['obj']
        if ( (cat in methodDocItem['categoriesMap']) and (len(methodDocItem['categoriesMap'][cat]['api']) > 0) ) or ( (cat in propertyDocItem['categoriesMap']) and (len(propertyDocItem['categoriesMap'][cat]['api']) > 0) ):
            title = categoriesMap[cat]['txt']

            methodLinks = ''
            if (cat in methodDocItem['categoriesMap']) and (len(methodDocItem['categoriesMap'][cat]['api']) > 0):
                catApis = methodDocItem['categoriesMap'][cat]['api']
                tfuncs = sorted(catApis, key=lambda x: x['fullName'])
                funcs = []
                funcsEnd = []
                for c in tfuncs:
                    if obj and c['fullName'].lower().startswith(cat + ':'):
                        funcs.append(c)
                    else:
                        funcsEnd.append(c)
                funcs = funcs + funcsEnd
                for e in funcs:
                    name = e['fullName']
                    file = e['file']
                    if len(methodLinks) != 0:
                        methodLinks += '\n'
                    methodLinks += '<a href="' + file + '">' + name + '</a>' + e['short']

            propertyLinks = ''
            if (cat in propertyDocItem['categoriesMap']) and (len(propertyDocItem['categoriesMap'][cat]['api']) > 0):
                if len(methodLinks) > 0:
                    methodLinks += '\n'
                title = propertyDocItem['categoriesMap'][cat]['txt']
                catApis = propertyDocItem['categoriesMap'][cat]['api']
                tfuncs = sorted(catApis, key=lambda x: x['fullName'])
                funcs = []
                funcsEnd = []
                for c in tfuncs:
                    if obj and c['fullName'].lower().startswith(cat + ':'):
                        funcs.append(c)
                    else:
                        funcsEnd.append(c)
                funcs = funcs + funcsEnd
                for e in funcs:
                    name = e['fullName']
                    file = e['file']
                    if len(propertyLinks) != 0:
                        propertyLinks += '\n'
                    propertyLinks += '<a href="' + file + '">' + name + '</a>' + e['short']

            methodPropCatLinks += '<li><a href="#methodsAndProperties_' + cat + '">' + title + '</a></li>'
            methodPropSection += '<h2><a name="methodsAndProperties_' + cat + '"></a>'
            for r in oldRefs:
                methodPropSection += '<a name="methodsAndProperties_' + r + '"></a>'
            if len(page) > 0:
                title = '<a href="' + page + '">' + title + '</a>'
            methodPropSection += '<div style="display: flex; justify-content: space-between;"><span>' + title + '</span><span>(methods &amp; properties)</span></div></h2>'
            #methodPropSection += title + ' (methods and categories)</h2>\n'
            methodPropSection += '<code class="language-python-lua coppelia-coppeliasim-script api-list">'
            methodPropSection += methodLinks + propertyLinks
            methodPropSection += '</code><br>'

    # Fill items related to functions:
    functionCatLinks = ''
    functionSection = ''
    for item in categories:
        cat = item['cat']
        c_Prefix = ('c_' in cat)
        oldRefs = item['oldRefs']
        page = item['page']
        if (cat in functionDocItem['categoriesMap']) and (len(functionDocItem['categoriesMap'][cat]['api']) > 0):
            functionLinks = ''
            title = functionDocItem['categoriesMap'][cat]['txt']
            funcs = sorted(functionDocItem['categoriesMap'][cat]['api'], key=lambda x: x['fullName'])
            for e in funcs:
                name = e['fullName']
                file = e['file']
                if len(functionLinks) != 0:
                    functionLinks += '\n'
                functionLinks += '<a href="' + file + '">' + name + '</a>'
            if len(functionLinks) != 0:
                if c_Prefix:
                    functionCatLinks += '<li><a href="#functions_' + cat + '">' + title + '</a></li>'
                functionSection += '<h2><a name="functions_' + cat + '"></a>'
                for r in oldRefs:
                    functionSection += '<a name="' + r + '"></a>'
                if len(page) > 0:
                    title = '<a href="' + page + '">' + title + '</a>'
                functionSection += '<div style="display: flex; justify-content: space-between;"><span>' + title + '</span><span>(C-functions)</span></div></h2>'
                #functionSection += title + ' (C-functions)</h2>\n'
                functionSection += '<code class="language-c++ coppelia-coppeliasim-plugin api-list">'
                functionSection += functionLinks
                functionSection += '</code><br>'

    listTemplate = listTemplate.replace('__methodPropLinks__', methodPropCatLinks)
    listTemplate = listTemplate.replace('__methodPropSection__', methodPropSection)
    listTemplate = listTemplate.replace('__functionLinks__', functionCatLinks)
    listTemplate = listTemplate.replace('__functionSection__', functionSection)

    nm = apiDir_main / 'apiFunctions.htm'
    with nm.open('w') as file_w:
        file_w.write(minify_html.minify(listTemplate))

if __name__ == "__main__":
    main()
