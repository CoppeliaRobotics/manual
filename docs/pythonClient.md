# <a id="lib"></a>CoppeliaSim's library

CoppeliaSim offers a wide range of functionalities via its graphical user interface. For more customized scenarios where fine-grained control of the simulation loop(s) is required (e.g. reinforcement learning), it also offers the flexibility to be used as a library within custom programs.

Using CoppeliaSim as a library consists of the following steps:

1. Loading CoppeliaSim's library:
   - Windows: `LoadLibrary("coppeliaSim.dll")`
   - Linux: `dlopen("libcoppeliaSim.so")`
   - macOS: `dlopen("libcoppeliaSim.dylib")`
2. Creating a secondary (SIM) thread (this step is mandatory) and in the secondary thread:
   1. Call `simInitialize` to initialize.
   2. Any other coppeliaSim API functions, and/or call `simLoop` until `simGetExitRequest` returns false
   3. Call `simDeinitialize` before termination.
3. On the main (UI) thread: call the `simRunGui` function (this step is mandatory, also when running headless, i.e. without GUI). Argument to `simRunGui` can be used to toggle on/off individual part of the interface (use `sim_gui_all` to enable all), or to run in headless mode (`sim_gui_headless`).

<a id="pythonClient"></a>

# Python client

A complete working example of loading the CoppeliaSim library in Python is given in [coppeliaSimClientPython](https://github.com/CoppeliaRobotics/coppeliaSimClientPython).

In this section, relevant parts are explained.

## Initialization

Module `coppeliaSim.lib` handles the load and setup of core functions (`simInitialize`, `simDeinitialize`, etc...) via `ctypes`.

```python
import builtins
import os
import threading

from ctypes import *

# set the path to the coppeliaSim's library:
builtins.coppeliaSim_library = "/path/to/libcoppeliaSim.so"

# import the coppeliaSim's library functions:
from coppeliaSim.lib import *

appDir = os.path.dirname(builtins.coppeliaSim_library)

# start the sim thread (see in the next section)
t = threading.Thread(target=simThreadFunc, args=(appDir,))
t.start()
simRunGui(sim_gui_all) # use sim_gui_headless for headless mode
t.join()
```

## SIM thread loop

The basic implementation of simThreadFunc simply executes the application until quit is requested:

```python
def simThreadFunc(appDir):
    simInitialize(c_char_p(appDir.encode('utf-8')), 0)
    while not simGetExitRequest():
        simLoop(None, 0)
    simDeinitialize()
```

Another possible scenario would be to manually control the operations used to setup a simulation environment (e.g. `sim.loadScene`) and to execute a simulation, e.g. by manually stepping for a predetermined amount of steps:

```python
def simThreadFunc(appDir):
    simInitialize(c_char_p(appDir.encode('utf-8')), 0)

    # script bridge, see next section
    import coppeliaSim.bridge
    coppeliaSim.bridge.load()

    global sim
    sim = coppeliaSim.bridge.require('sim')

    sim.loadScene('path/to/scene.ttt')
    simStart()
    for i in range(1000):
        t = sim.getSimulationTime()
        print(f'Simulation time: {t:.2f} [s] (running in stepped mode)')
        simStep()
    simStop()

    simDeinitialize()

def simStart():
    if sim.getSimulationState() == sim.simulation_stopped:
        sim.startSimulation()

def simStep():
    if sim.getSimulationState() != sim.simulation_stopped:
        t = sim.getSimulationTime()
        while t == sim.getSimulationTime():
            simLoop(None, 0)

def simStop():
    while sim.getSimulationState() != sim.simulation_stopped:
        sim.stopSimulation()
        simLoop(None, 0)
```

## coppeliaSim.bridge

The `coppeliaSim.bridge` module provides seamless access to the regular API used by scripts, e.g.:

```python
import coppeliaSim.bridge

# load the bridge component:
coppeliaSim.bridge.load()

# fetch API objects:
sim = coppeliaSim.bridge.require('sim')

# e.g.: use some API function:
program_version = sim.getIntProperty(sim.handle_app, 'productVersionNb')
```

Please refer to [coppeliaSimClientPython/main_with_ui.py](https://github.com/CoppeliaRobotics/coppeliaSimClientPython/blob/main/main_with_ui.py) for the complete code.
