# Add-ons

An add-on is a [script](scripts.md) running in CoppeliaSim, that can act in a similar way as a [plugin](plugins.md): it is automatically loaded at program start-up, and allows CoppeliaSim's functionality to be extended by user-written functionality or functions; it persists across all opened scenes, and is executed constantly, effectively running in the background. Add-ons can run [threaded or non-threaded](threadedAndNonThreadedCode.md), should be segmented into several [system callback functions](callbackFunctions.md#systemCallbacks), and follow a precise [execution order](scriptExecution.md) in relation to other script types. They share many properties with [sandboxes](sandboxScript.md). Add-ons can be accessed via [Menu bar > Modules].

Add-ons should be written in a text file located in the *&lt;CoppeliaSim folder>/addOns/* directory, with the extension indicating the language (*&lt;name.py>* or *&lt;name.lua*>). Other add-ons can still be loaded and run via [command line options](commandLine.md).

By default, add-ons automatically start when CoppeliaSim starts, e.g.:

```python
#python
#using sim-2

def sysCall_init():
    print("Executing the initialization section. Starting together with CoppeliaSim")

def sysCall_addOnScriptSuspend():
    print("Ending... (triggered by the user)")
    sim.self.reset() # end this add-on. The cleanup section will be called

def sysCall_cleanup():
    print("Executing the clean-up section")
```

```lua
--lua
sim = require('sim-2')

function sysCall_init()
    print("Executing the initialization section. Starting together with CoppeliaSim")
end

function sysCall_addOnScriptSuspend()
    print("Ending... (triggered by the user)")
    sim.self:reset() -- end this add-on. The cleanup section will be called
end

function sysCall_cleanup()
    print("Executing the clean-up section")
end
```

An add-on can also be manually started and stopped from the add-on menu, e.g.:

```python
#python
# using sim-2

'''luaExec
-- Here we have a special Lua section:
function sysCall_info()
    return {autoStart = false}
end
'''

def sysCall_init():
    print("Executing the initialization section. Start triggered by the user")

def sysCall_addOnScriptSuspend():
    print("Ending... (triggered by the user)")
    sim.self.reset() # end this add-on. The cleanup section will be called

--lua
sim = require('sim-2')

function sysCall_info()
    return {autoStart = false}
end

function sysCall_init()
    print("Executing the initialization section. Start triggered by the user")
end

function sysCall_addOnScriptSuspend()
    print("Ending... (triggered by the user)")
    sim.self:reset() -- end this add-on. The cleanup section will be called
end
```

```python
An add-on can also be suspended/resumed from the add-on menu, e.g.:

#python
# using sim-2

...

def sysCall_addOnScriptSuspend():
    print("Suspending the add-on... (triggered by the user)")

def sysCall_addOnScriptResume():
    print("Resuming the add-on... (triggered by the user)")

...

--lua
sim = require('sim-2')

...

function sysCall_addOnScriptSuspend()
    print("Suspending the add-on... (triggered by the user)")
end

function sysCall_addOnScriptResume()
    print("Resuming the add-on... (triggered by the user)")
end

...

An add-on can also act as a simple function triggered by the user, e.g.:

#python
# using sim-2

'''luaExec
-- Here we have a special Lua section:
function sysCall_info()
    return {autoStart = false}
end
'''

def sysCall_init():
    print("Executing the initialization section. Start triggered by the user")
    # execute some functions here, e.g. import something
    sim.self.reset() # end this add-on.

--lua
sim = require('sim-2')

function sysCall_info()
    return {autoStart = false}
end

function sysCall_init()
    print("Executing the initialization section. Start triggered by the user")
    -- execute some functions here, e.g. import something
    sim.self:reset() -- end this add-on.
end

An add-on can also display a customized name in the Modules' menu, e.g.:

#python
# using sim-2

'''luaExec
-- Here we have a special Lua section:
function sysCall_info()
    return {menu: 'Exporters\nMy exporter'}
end
'''

def sysCall_init():
    ...

--lua
sim = require('sim-2')

function sysCall_info()
    return {menu = 'Exporters\nMy exporter'}
end

function sysCall_init()
    ...
end
```
