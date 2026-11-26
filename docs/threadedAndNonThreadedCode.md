# Threaded and non-threaded script code

Any type of script can run [threaded](#threaded) and/or [non-threaded](#nonThreaded).

## <a id="nonThreaded"></a>Non-threaded code

The entrance to a script is always originating from [callback functions](callbackFunctions.md) which are not running threaded, and should not be blocking. This means that every time they are called, they should perform some task and then return control. If control is not returned, then CoppeliaSim will halt.

Non-threaded code is inherently synchronized with the simulation loop:

```python
import sim

def sysCall_init():
    pass

def sysCall_sensing():
    print('simulation time:', sim.scene.simulation.time)
```

```lua
import 'sim-2'

function sysCall_init()
end

function sysCall_sensing()
    print('simulation time: ', sim.scene.simulation.time)
end
```

## <a id="threaded"></a>Threaded code

Threaded code on the other hand allows running blocking code, without halting CoppeliaSim: the code is in fact preemptively interrupted and later resumed on a regular basis by CoppeliaSim, by default.

Threaded code runs non-blocking (or in non-stepping mode) by default:

```python
import sim

def sysCall_init():
    pass

def sysCall_thread():
    while true:
        print('simulation time:', sim.scene.simulation.time)
```

```lua
import 'sim-2'

function sysCall_init()
end

function sysCall_thread()
    while true do
        print('simulation time: ', sim.scene.simulation.time)
    end
end
```

This behavior can be changed via [`script:setStepping`](sim-2/script_setStepping.md), which then requires explicit yielding via [`script:step`](sim-2/script_step.md):

```python
import sim

def sysCall_init():
    sim.self.setStepping(True)  # enable the stepping mode (no more preemptive yielding from CoppeliaSim)

def sysCall_thread():
    while true:
        print('simulation time:', sim.scene.simulation.time)
        sim.self.step()  # resume in the next simulation step
```

```lua
import 'sim-2'

function sysCall_init()
    sim.self:setStepping(true) -- enable the stepping mode (no more preemtive yielding from CoppeliaSim)
end

function sysCall_thread()
    while true do
        print('simulation time: ', sim.scene.simulation.time)
        sim.self:step() -- resume in next simulation step
    end
end
```

The above while loop now executes exactly once for each main simulation step and does not waste time reading and printing the simulation time over and over for the same simulation step: once the current thread has yielded control back to CoppeliaSim, it resumes in the next simulation step.

Several [blocking functions](apiFunctions.md#methodsAndProperties_blocking) are specifically meant to be running from within threaded code, e.g. [`Motion.MoveToConfig:run`](sim-2/MoveToConfig_run.md) [`or Motion.MoveToPose.run`](sim-2/MoveToPose_run.md): those functions handle thread yielding for you, at the appropriate time.

Refer also to the [stepping mode](simulation.md#stepping), to the [thread-related](apiFunctions.md#methodsAndProperties_thread) and [script-related](apiFunctions.md#methodsAndProperties_script) methods and properties.
