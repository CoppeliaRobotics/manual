# Callback functions

Callbacks or callback functions are script functions that are triggered by a specific event. They represent the only entrance into script code. They can be categorized into user callbacks, and system callbacks:

- User callback functions are directly triggered by user code, or a plugin. This happens for instance when the user calls a script function in a different script via [`script:callFunction`](sim-2/script_callFunction.htm), or when the user clicks a [custom UI](customUserInterfaces.md) button, which triggers a custom event. User callback functions can usually run in [any type of script](scripts.md).
- System callback functions on the other hand are triggered by CoppeliaSim when a certain event happens, for instance when a script is initialized, or before switching to another scene. System callback functions have fixed function names, such as *sysCall_init* or *sysCall_beforeInstanceSwitch*. Not all system callback functions are supported by all types of scripts, e.g. some can only run in an [add-on](addOns.md) (e.g. *sysCall_addOnScriptSuspend*).

While most system callback functions operate in a relatively straight-forward manner and are easy to understand (see further down for a complete list of system callback functions), some require a little bit more explanations:

- [Dynamics callback functions](dynCallbackFunctions.md) are called by the physics engine before and after each dynamics simulation step
- The [contact callback function](contactCallbackFunction.md) is called by the physics engine for each contact pair
- [Joint callback functions](jointCallbackFunctions.md) are called for custom joint control
- [Vision callback functions](visionCallbackFunctions.md) are called whenever a new image is acquired or applied
- [Trigger callback functions](triggerCallbackFunctions.md) are called when a certain trigger event is fired
- [User config callback functions](userConfigCallbackFunctions.md) are called when the user double-clicks a user parameter icon

<a id="systemCallbacks"></a>The following is a list of all supported system callback functions. Most support returning {cmd='cleanup'} or {cmd='restart'} to end or restart the script. Refer to the comments in the code below for details about individual functions:

```python
#python
# using sim-2

def sysCall_init():
    # Do some initialization here.
    pass

def sysCall_thread():
    # Entry point for threaded scripts.
    pass

def sysCall_cleanup():
    # Do some clean-up here.
    pass

def sysCall_nonSimulation():
    # Is executed when simulation is not running.
    # Not for simulation scripts or the main script.
    pass

def sysCall_beforeSimulation():
    # Simulation is about to start.
    # Not for simulation scripts or the main script.
    pass

def sysCall_afterSimulation():
    # Simulation has just ended.
    # Not for simulation scripts or the main script.
    pass

def sysCall_actuation():
    # Put some actuation code here.
    pass

def sysCall_sensing():
    # Put some sensing code here.
    pass

def sysCall_suspend():
    # Simulation is about to be suspended.
    pass

def sysCall_suspended():
    # Simulation is suspended.
    pass

def sysCall_resume():
    # Simulation is about to resume.
    pass

def sysCall_realTimeIdle():
    # Is executed when idle in real-time mode
    pass

def sysCall_beforeInstanceSwitch():
    # About to switch to another scene.
    # Not for simulation scripts or the main script.
    pass

def sysCall_afterInstanceSwitch():
    # Switched to another scene.
    # Not for simulation scripts or the main script.
    pass

def sysCall_beforeSave(inData):
    # About to save the scene, or about to set an undo/redo point
    print(str(inData['regularSave']), inData['file'])

def sysCall_afterSave(inData):
    # After the scene was saved, or after an undo/redo point was set
    print(str(inData['regularSave']), inData['file'])

def sysCall_afterLoad():
    # After the scene was loaded
    pass

def sysCall_selChange(inData):
    # After selection was changed
    for object in inData['selection']:
        print(f"Object with handle {object.handle} is selected")

def sysCall_beforeCopy(inData):
    # Before one or several objects will be copied. Can be reentrant
    for object in inData['objectList']:
        print(f"Object with handle {object.handle} will be copied")

def sysCall_afterCopy(inData):
    # After one or several objects were copied. Can be reentrant
    for object in inData['objectList']:
        print(f"Object with handle {object.handle} was copied")

def sysCall_afterCreate(inData):
    # After one or several objects were created. Can be reentrant
    for object in inData['objectList']:
        print(f"Object with handle {object.handle} was created")

def sysCall_beforeDelete(inData):
    # Before one or several objects will be deleted. Can be reentrant
    for object in inData['objectList']:
        print(f"Object with handle {object.handle} will be deleted")

def sysCall_afterDelete(inData):
    # After one or several objects were deleted. Can be reentrant
    for object in inData['objectList']:
        print(f"Object with handle {object.handle} was deleted")

def sysCall_beforeMainScript():
    # Can be used to step a simulation in a custom manner.
    outData = {"doNotRunMainScript": False}  # when true, then the main script won't be executed
    return outData

def sysCall_addOnScriptSuspend():
    # Add-on execution is about to be suspended.
    # Only for add-ons.
    pass

def sysCall_addOnScriptResume():
    # Add-on execution is about to be resumed.
    # Only for add-ons.
    pass

def sysCall_dyn(inData):
    # See the dynamics callback function section for details
    return {...}

def sysCall_joint(inData):
    # See the joint callback function section for details
    return {...}

def sysCall_contact(inData):
    # See the contact callback function section for details
    return {...}

def sysCall_vision(inData):
    # See the vision callback function section for details
    # Only for customization scripts and simulation scripts.
    return {...}

def sysCall_trigger(inData):
    # See the trigger callback function section for details
    # Only for customization scripts and simulation scripts.
    return {...}

def sysCall_userConfig():
    # See the user config callback function section for details.
    # Only for customization scripts.
    pass

def sysCall_moduleEntry(inData):
    # Called when a user module menu entry is selected, e.g.
    print(f"Following module menu entry was selected: {inData['handle']}")
    # See sim.moduleEntry for details.

def sysCall_msg(msg, origin):
    # Synchronously called when script.broadcastMsg is called, or when sysCall_init, sysCall_cleanup,
    # sysCall_addOnScriptSuspend, sysCall_addOnScriptResume or sysCall_userConfig is called. Can be reentrant
    pass

def sysCall_data(inData):
    # Asynchronously called when custom data properties attached to this script, or this script's parent are modified
    # Only for simulation- and customization scripts
    pass

def sysCall_event(cborBuffer):
    # Asynchronously called when an internal variable or state changes. Can be reentrant
    # Mainly used to synchronize an external GUI/viewer/renderer with CoppeliaSim.
    # See also sim.getGenesisEvents and sim.setEventFilters
    pass
```

```lua
--lua
sim = require('sim-2')

function sysCall_info()
    -- Lua only. Can be used to specify initial configuration data. E.g. in case of an add-on:
    return {autoStart = false, menu = 'menu1\nmenu2\nadd-on name', menuEnabled = true}
end

function sysCall_init()
    -- Do some initialization here.
end

function sysCall_thread()
    -- Entry point for threaded scripts.
end

function sysCall_cleanup()
    -- Do some clean-up here.
end

function sysCall_nonSimulation()
    -- Is executed when simulation is not running.
    -- Not for simulation scripts or the main script.
end

function sysCall_beforeSimulation()
    -- Simulation is about to start.
    -- Not for simulation scripts or the main script.
end

function sysCall_afterSimulation()
    -- Simulation has just ended.
    -- Not for simulation scripts or the main script.
end

function sysCall_actuation()
    -- Put some actuation code here.
end

function sysCall_sensing()
    -- Put some sensing code here.
end

function sysCall_suspend()
    -- Simulation is about to be suspended.
end

function sysCall_suspended()
    -- Simulation is suspended.
end

function sysCall_resume()
    -- Simulation is about to resume.
end

function sysCall_realTimeIdle()
    -- Is executed when idle in real-time mode
end

function sysCall_beforeInstanceSwitch()
    -- About to switch to another scene.
    -- Not for simulation scripts or the main script.
end

function sysCall_afterInstanceSwitch()
    -- Switched to another scene.
    -- Not for simulation scripts or the main script.
end

function sysCall_beforeSave(inData)
    -- About to save the scene, or about to set an undo/redo point
    print(inData.regularSave, inData.file)
end

function sysCall_afterSave(inData)
    -- After the scene was saved , or after an undo/redo point was set
    print(inData.regularSave, inData.file)
end

function sysCall_afterLoad()
    -- After the scene was loaded
end

function sysCall_selChange(inData)
    -- After selection was changed
    for i = 1, #inData.selection do
        print("Object with handle " .. inData.selection[i].handle .. " is selected")
    end
end

function sysCall_beforeCopy(inData)
    -- Before one or several objects will be copied. Can be reentrant
    for i = 1, #inData.objectList do
        print("Object with handle " .. inData.objectList[i].handle .. " will be copied")
    end
end

function sysCall_afterCopy(inData)
    -- After one or several objects were copied. Can be reentrant
    for i = 1, #inData.objectList do
        print("Object with handle " .. inData.objectList[i].handle .. " was copied")
    end
end

function sysCall_afterCreate(inData)
    -- After one or several objects were created. Can be reentrant
    for i = 1, #inData.objectList do
        print("Object with handle " .. inData.objectList[i].handle .. " was created")
    end
end

function sysCall_beforeDelete(inData)
    -- Before one or several objects will be deleted. Can be reentrant
    for i = 1, #inData.objectList do
        print("Object with handle " .. inData.objectList[i].handle .. " will be deleted")
    end
end

function sysCall_afterDelete(inData)
    -- After one or several objects were deleted. Can be reentrant
    for i = 1, #inData.objectHandleList do
        print("Object with handle " .. inData.objectHandleList[i] .. " was deleted")
    end
end

function sysCall_beforeMainScript()
    -- Can be used to step a simulation in a custom manner.
    local outData = {doNotRunMainScript = false} -- when true, then the main script won't be executed
    return outData
end

function sysCall_addOnScriptSuspend()
    -- Add-on execution is about to be suspended.
    -- Only for add-ons.
end

function sysCall_addOnScriptResume()
    -- Add-on execution is about to be resumed.
    -- Only for add-ons.
end

function sysCall_dyn(inData)
    -- See the dynamics callback function section for details
    return outData
end

function sysCall_joint(inData)
    -- See the joint callback function section for details
    return outData
end

function sysCall_contact(inData)
    -- See the contact callback function section for details
    return outData
end

function sysCall_vision(inData)
    -- See the vision callback function section for details
    -- Only for customization scripts and simulation scripts.
    return outData
end

function sysCall_trigger(inData)
    -- See the trigger callback function section for details
    -- Only for customization scripts and simulation scripts.
    return outData
end

function sysCall_userConfig()
    -- See the user config callback function section for details.
    -- Only for customization scripts.
end

function sysCall_moduleEntry(inData)
    -- Called when a user module menu entry is selected, e.g.
    print('Following module menu entry was selected: ' .. inData.handle)
    -- See sim.moduleEntry for details.
end

function sysCall_msg(msg, origin)
    -- Synchronously called when script:broadcastMsg is called, or when sysCall_init, sysCall_cleanup,
    -- sysCall_addOnScriptSuspend, sysCall_addOnScriptResume or sysCall_userConfig is called. Can be reentrant
end

function sysCall_data(inData)
    -- Asynchronously called when custom data properties attached to this script's parent object are modified
    -- Only for simulation- and customization scripts
end

function sysCall_event(cborBuffer)
    -- Asynchronously called when an internal variable or state changes. Can be reentrant
    -- Mainly used to synchronize an external GUI/viewer/renderer with CoppeliaSim.
    -- See also sim.getGenesisEvents and sim.setEventFilters
end

function sysCall_ext(funcName, inData)
    -- When this function is present, then all external calls to a script function, i.e. user callbacks,
    -- will be intercepted (the original function will be shadowed). If only monitoring is desired,
    -- then one should use script:registerFunctionHook on this function.
end
```
