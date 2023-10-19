import sys
import xml.etree.ElementTree as ET

from pathlib import Path

from coppeliasim_zmqremoteapi_client import RemoteAPIClient


client = RemoteAPIClient()
sim = client.require('sim')

curDir = Path(__file__).absolute().parent

tree = ET.parse(curDir / 'regularApi.xml')
root = tree.getroot()

for func in root:
    name = func.find('api-function-name').text.strip()
    calltip = sim.getApiInfo(-1, name)
    if calltip:
        ET.SubElement(func, 'api-calltip').text = calltip

ET.dump(tree)
