#!/usr/bin/env python3
import re
import sys
from typing import Dict, List, Optional, Tuple
import xml.etree.ElementTree as ET
from xml.dom import minidom

'''
python script to parse enums in a C header file annotated with special comments:

// @enum name="sceneObjectType" label="scene object types" type="int" prefix="sim_sceneobject_" description=""
enum { // values are serialized
        sim_sceneobject_shape =0,
        sim_sceneobject_joint,
        sim_sceneobject_forcesensor = 12, // @item label="force sensor"
};

and write the XML:

<enum name="sceneObjectType" label="scene object types" type="int" prefix="sim_sceneobject_" description="">
    <item name="shape" value="0" />
    <item name="joint" value="1" />
    <item name="forcesensor" value="12" label="force sensor" />
</enum>

enum special comment starts with @enum, contains variables: name, label, type, prefix, description

prefix is used to strip the prefix from C enum items

item special comment starts with @item, but you should collect also enum items without this special comment

to determine the value of the enum, use normal C/C++ rules, e.g. first item has default value 0, and any other item has default value of previous item + 1, but of course value can be overridden by assigning it explicitly, as per C/C++ standard.
'''

class EnumItem:
    def __init__(self, name: str, value: Optional[int] = None, label: str = ""):
        self.name = name
        self.value = value
        self.label = label

class EnumDefinition:
    def __init__(self, name: str, label: str, type_: str, prefix: str, description: str):
        self.name = name
        self.label = label
        self.type = type_
        self.prefix = prefix
        self.description = description
        self.items: List[EnumItem] = []

def parse_enum_comment(line: str) -> Optional[Dict[str, str]]:
    """Parse @enum comment and extract parameters."""
    match = re.search(r'@enum\s+(.*?)(?:\*/|$)', line)
    if not match:
        return None

    params_str = match.group(1)
    params = {}

    # Parse name="value" pairs
    pattern = r'(\w+)="([^"]*)"'
    for key, value in re.findall(pattern, params_str):
        params[key] = value

    return params

def parse_item_comment(line: str) -> Optional[Dict[str, str]]:
    """Parse @item comment and extract parameters."""
    match = re.search(r'@item\s+(.*?)(?:\*/|$)', line)
    if not match:
        return None

    params_str = match.group(1)
    params = {}

    # Parse name="value" pairs
    pattern = r'(\w+)="([^"]*)"'
    for key, value in re.findall(pattern, params_str):
        params[key] = value

    return params

def parse_c_value(value_str: str) -> int:
    """Parse a C integer constant (handles decimal and hex)."""
    value_str = value_str.strip()
    if value_str.startswith('0x') or value_str.startswith('0X'):
        return int(value_str, 16)
    return int(value_str)

def strip_prefix(name: str, prefix: str) -> str:
    """Strip the prefix from an enum item name."""
    if prefix and name.startswith(prefix):
        return name[len(prefix):]
    return name

def parse_enum_block(lines: List[str], start_idx: int) -> Tuple[Optional[EnumDefinition], int]:
    """Parse an enum block starting at start_idx."""

    # Look for @enum comment before the enum keyword
    enum_params = None
    for i in range(start_idx, max(-1, start_idx - 5), -1):
        if i >= 0 and '//' in lines[i]:
            enum_params = parse_enum_comment(lines[i])
            if enum_params:
                break

    if not enum_params:
        # Check if @enum is on the same line as enum
        current_line = lines[start_idx]
        if '//' in current_line:
            parts = current_line.split('//')
            if len(parts) > 1:
                enum_params = parse_enum_comment('//' + parts[1])

    if not enum_params:
        return None, start_idx

    # Find the start of enum block
    line_idx = start_idx
    while line_idx < len(lines) and '{' not in lines[line_idx]:
        line_idx += 1

    if line_idx >= len(lines):
        return None, start_idx

    # Create enum definition
    enum_def = EnumDefinition(
        name=enum_params.get('name', ''),
        label=enum_params.get('label', ''),
        type_=enum_params.get('type', 'int'),
        prefix=enum_params.get('prefix', ''),
        description=enum_params.get('description', '')
    )

    # Parse enum items
    line_idx += 1  # Skip past '{'
    current_value = 0
    items = []

    while line_idx < len(lines):
        line = lines[line_idx].strip()

        # Check for end of enum
        if line.startswith('}'):
            line_idx += 1
            break

        # Skip empty lines and comments (except @item comments)
        if not line or (line.startswith('//') and '@item' not in line):
            line_idx += 1
            continue

        # Check for item comment
        item_params = None
        if '//' in line:
            parts = line.split('//')
            if len(parts) > 1:
                item_params = parse_item_comment('//' + parts[1])

        # Parse enum item
        if line.endswith(','):
            line = line[:-1]

        # Handle assignment
        if '=' in line:
            parts = line.split('=', 1)
            name = parts[0].strip()
            value_expr = parts[1].split(',')[0].strip()  # In case there's a comment after value
            # Remove any trailing comment from value expression
            if '//' in value_expr:
                value_expr = value_expr.split('//')[0].strip()
            try:
                current_value = parse_c_value(value_expr)
            except ValueError:
                # If we can't parse the value, use the default
                pass
        else:
            # No assignment, use default value
            name = line.split(',')[0].strip()

        # Clean up name (remove any trailing comma or comment)
        name = name.split(',')[0].strip()

        if name:  # Only add if we have a name
            item_label = item_params.get('label', '') if item_params else ''
            items.append(EnumItem(name, current_value, item_label))

        current_value += 1
        line_idx += 1

    # Process items: strip prefix and assign to enum definition
    for item in items:
        stripped_name = strip_prefix(item.name, enum_def.prefix)
        enum_def.items.append(EnumItem(stripped_name, item.value, item.label))

    return enum_def, line_idx

def parse_c_header(filename: str) -> List[EnumDefinition]:
    """Parse a C header file and extract all annotated enums."""
    with open(filename, 'r') as f:
        content = f.read()

    # Split into lines and clean up
    lines = [line.rstrip() for line in content.split('\n')]

    enums = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Look for enum keyword
        if 'enum' in line:
            enum_def, new_idx = parse_enum_block(lines, i)
            if enum_def:
                enums.append(enum_def)
                i = new_idx
                continue

        i += 1

    return enums

def enum_to_xml(enum_def: EnumDefinition) -> ET.Element:
    """Convert an EnumDefinition to XML element."""
    enum_elem = ET.Element('enum', {
        'name': enum_def.name,
        'label': enum_def.label,
        'type': enum_def.type,
        'prefix': enum_def.prefix,
        'description': enum_def.description
    })

    for item in enum_def.items:
        attrs = {'name': item.name, 'value': str(item.value)}
        if item.label:
            attrs['label'] = item.label
        ET.SubElement(enum_elem, 'item', attrs)

    return enum_elem

def prettify_xml(elem: ET.Element) -> str:
    """Return a pretty-printed XML string for the Element."""
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="    ")

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <header_file.h>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        enums = parse_c_header(input_file)

        # Create root element
        root = ET.Element('enums')

        # Add all enums
        for enum_def in enums:
            root.append(enum_to_xml(enum_def))

        # Output XML
        xml_str = prettify_xml(root)

        # Remove XML declaration if you want just the enums
        lines = xml_str.split('\n')
        if lines[0].startswith('<?xml'):
            lines = lines[1:]

        # Print result
        print('\n'.join(lines).strip())

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
