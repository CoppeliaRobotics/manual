# Lua vs Python scripts

The way embedded Lua and Python scripts are handled in CoppeliaSim (next to differences related to the language itself) displays small differences, which are discussed here:

- Global variables are inconvenient and not recommended in Python:

```python
import sim
from types import SimpleNamespace
state = SimpleNamespace()

def sysCall_init():
    state.myVariable = 21

def sysCall_sensing():
    print(state.myVariable)
```

- CoppeliaSim selects the default Python interpreter present on your system. If this does not work, or if another interpreter is desired, then you can edit the [*usrset.txt*](commandLine.md#settingsFile) file entry named *defaultInterpreters.python*. In addition to that, each script can specify a custom Python executable if required, via the [*luaExec*](#luaExec) directive.
- Python scripts are handled via Lua wrapper code, which handles the launch and communication of each Python script. The default wrapper can be specified in the [*usrset.txt*](commandLine.md#settingsFile) file entry named *languages.python*. In addition to that, each script can specify a custom wrapper if required, via the [*luaExec*](#luaExec) directive.
- Lua code always executes in the same thread as CoppeliaSim and is thus quite fast. Python code on the other hand is launched in a new process, which connects to CoppeliaSim via socket communication. This implies that Python code will usually start and run slower than Lua code
- <a id="luaExec"></a>Auxiliary settings or any other Lua code can be passed via the *luaExec* directive, within a Python comment section. That code must come immediately at the beginning of the script:

```python
# custom wrapper: looks for pythonWrapper-3.lua in Lua search path:
#luaExec wrapper = 'pythonWrapper-3' -- looks for pythonWrapper-3.lua

# start-up timeout in seconds:
#luaExec initTimeout = 60 

# run a specific Python executable:
#luaExec pythonExecutable = 'c:/python38/python.exe'

# add more Python module search paths:
#luaExec additionalPaths = {'c:/path1', 'c:/path2'}

# add more paths to search for the include file:
#luaExec additionalIncludePaths = {'c:/Python38', 'c:/path2'}

# add a Lua function:
'''luaExec
function myLuaFunction(...)
    print('hello John!', ...)
    sim.self:callFunction('myPythonFunction', ...)
end
'''

import sim
from types import SimpleNamespace
state = SimpleNamespace()

def myPythonFunction(arg1, arg2, arg3):
    print('hello Jane!', str((arg1, arg2, arg3)))
    
def sysCall_init():
    sim.self.callFunction('myLuaFunction', 1, 2, 3)
    print("hello Ben!")
```

- The import directive does not work when importing the primary Python file, and the following should be used instead:

```python
include myExternalFile

# myExternalFile is the pythonScript name or path (absolute or relative),
# without quotes nor the ending '.py'
# searched paths include:
# <CoppeliaSim executable path>/ 
# <CoppeliaSim executable path>/python 
# <current scene path>/ 
# <additional path>/
# <additional include path>/
```

- Lua modules are imported in Python in a similar manner as Python modules:

```python
import sim
import simUI
import simIK_2 # effectively imports simIK-2

def sysCall_thread():
    xml = '<ui title="Custom UI"> <button text="Click me!" on-click="click_callback"/> </ui>'
    ui = simUI.create(xml)
```

- Python threaded scripts need to handle the message pump (via [`app.handleMessagePump`](sim-2/app_handleMessagePump.md)) to have user callback functions serviced, depending on the situation:

```python
import sim
import simUI

def sysCall_thread():
    xml = '<ui title="Custom UI"> <button text="Click me!" on-click="click_callback"/> </ui>'
    ui = simUI.create(xml)
    while True:
        sim.app.handleMessagePump()
    simUI.destroy(ui)

def click_callback(ui, button):
    print("button was clicked!")
```

- Some rare API methods will only be available in Lua, while others only in Python.
- The word *table* in the documentation refers to array-like or map-like items in Lua, while in Python, it refers to either *lists* or *dicts*.
- Finally remember that Python lists have a zero-based numbering, while Lua array-like tables have a 1-based numbering.
