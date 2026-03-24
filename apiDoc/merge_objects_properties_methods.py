import sys
import xml.etree.ElementTree as ET
from copy import deepcopy


def merge_xml(properties_file, methods_file, output_file):
    props_tree = ET.parse(properties_file)
    methods_tree = ET.parse(methods_file)

    props_root = props_tree.getroot()
    methods_root = methods_tree.getroot()

    if props_root.tag != "object-classes" or methods_root.tag != "object-classes":
        raise ValueError("Both XML files must have <object-classes> as root")

    # Build lookup for methods.xml object-classes
    methods_classes = {}
    for cls in methods_root.findall("object-class"):
        name = cls.get("name")
        if name:
            methods_classes[name] = cls

    # Process all classes from properties.xml
    for props_cls in props_root.findall("object-class"):
        name = props_cls.get("name")
        if not name:
            continue

        if name in methods_classes:
            methods_cls = methods_classes[name]

            # ---- Merge attributes (properties.xml has priority) ----
            merged_attrib = dict(methods_cls.attrib)  # start from methods.xml
            merged_attrib.update(props_cls.attrib)    # overwrite with properties.xml
            methods_cls.attrib.clear()
            methods_cls.attrib.update(merged_attrib)

            # ---- Replace property nodes ----
            for prop in methods_cls.findall("property"):
                methods_cls.remove(prop)

            for prop in props_cls.findall("property"):
                methods_cls.append(deepcopy(prop))

        else:
            # Create new object-class with properties.xml attributes
            new_cls = ET.Element("object-class", dict(props_cls.attrib))

            for prop in props_cls.findall("property"):
                new_cls.append(deepcopy(prop))

            methods_root.append(new_cls)

    methods_tree.write(output_file, encoding="utf-8", xml_declaration=True)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python merge_xml.py properties.xml methods.xml merged.xml")
        sys.exit(1)

    merge_xml(sys.argv[1], sys.argv[2], sys.argv[3])