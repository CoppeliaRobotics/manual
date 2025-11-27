#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import re
import sys

def extract_function_name_cpp(synopsis):
    """Extract function name from C++ API synopsis like 'int simAddDrawingObject(args...)'"""
    # Match pattern: optional return type, then function name followed by (
    match = re.search(r'\b(sim[A-Za-z0-9_]*)\s*\(', synopsis)
    if match:
        return match.group(1)
    return None

def extract_function_name_lua(synopsis):
    """Extract function name from Lua API synopsis like 'int retArg1 = sim.addDrawingObject(args...)'"""
    # Match pattern: sim.functionName(
    match = re.search(r'\bsim\.([A-Za-z0-9_]+)\s*\(', synopsis)
    if match:
        return 'sim.' + match.group(1)
    return None

def get_function_names_from_a(xml_file):
    """Extract all function names from a.xml's api-synopsis-cpp and api-synopsis-lua elements"""
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    function_names = set()
    
    # Find all api-synopsis-cpp elements
    for elem in root.iter('api-synopsis-cpp'):
        if elem.text:
            func_name = extract_function_name_cpp(elem.text.strip())
            if func_name:
                function_names.add(func_name)
    
    # Find all api-synopsis-lua elements
    for elem in root.iter('api-synopsis-lua'):
        if elem.text:
            func_name = extract_function_name_lua(elem.text.strip())
            if func_name:
                function_names.add(func_name)
    
    return function_names

def get_function_names_from_b(xml_file):
    """Extract all function names from 'name' attributes of 'function' elements in b.xml"""
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    function_names = set()
    
    # Find all function elements with name attribute
    for elem in root.iter('function'):
        name = elem.get('name')
        if name:
            function_names.add(name)
    
    return function_names

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py a.xml b.xml")
        sys.exit(1)
    
    file_a = sys.argv[1]
    file_b = sys.argv[2]
    
    try:
        # Get function names from both files
        functions_in_a = get_function_names_from_a(file_a)
        functions_in_b = get_function_names_from_b(file_b)
        
        # Find functions in a.xml that are not in b.xml
        missing_functions = functions_in_a - functions_in_b
        
        if missing_functions:
            print("Functions found in {} but not in {}:".format(file_a, file_b))
            print("-" * 50)
            for func in sorted(missing_functions):
                print(func)
            print("-" * 50)
            print("Total missing functions: {}".format(len(missing_functions)))
        else:
            print("All functions from {} are present in {}".format(file_a, file_b))
    
    except FileNotFoundError as e:
        print("Error: File not found - {}".format(e))
        sys.exit(1)
    except ET.ParseError as e:
        print("Error: Failed to parse XML - {}".format(e))
        sys.exit(1)
    except Exception as e:
        print("Error: {}".format(e))
        sys.exit(1)

if __name__ == "__main__":
    main()
