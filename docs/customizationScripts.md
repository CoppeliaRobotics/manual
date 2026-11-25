# Customization scripts

A customization script is an instance of the [scriptObject type](mainObjectTypes.md#scriptObject), which in turn derives from the [sceneObject type](mainObjectTypes.md#sceneObject). It wraps an instance of the [script type](mainObjectTypes.md#script), itself of type *customization*. It is used to customize a [scene](scenes.md) or [model](models.md) to a great extent: imagine a model that was dropped into a scene and that is able to configure or adapt itself, even when simulation is not running. This could be a robot where the user can adjust the various link lengths with a single slider repositioning.

Customization scripts are executed all the time (within a same scene): when simulation is running, as well as when simulation is not running. They follow a [precise calling or execution order](scriptExecution.md) and can [run threaded or non-threaded](threadedAndNonThreadedCode.md). Double-clicking their icon in the scene hierarchy opens the [script editor](scriptEditor.md).

A customization script is typically segmented into [system callback functions](callbackFunctions.md#systemCallbacks), the most important of which are:

- **sysCall_init** is called just one time, the first time the script is called. Usually you would put some initialization code in this part.
- **sysCall_thread** is the entrance to the script's threaded execution code. Threaded code is interrupted (and later resumed) on a regular basis by CoppeliaSim, by default. This behavior can however be adjusted via [`script:setStepping`](sim-2/script_setStepping.md). See also [the other thread-related API functions](apiFunctions.md#threads) for more details.
- **sysCall_nonSimulation** is called on a regular basis, when simulation is not running.
- **sysCall_beforeSimulation** is called once just before simulation starts.
- **sysCall_afterSimulation** is called once just after simulation ended.
- **sysCall_cleanup** is called one time just before the script state is destroyed (e.g. when the script object is removed)
