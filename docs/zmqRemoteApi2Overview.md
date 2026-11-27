# ZeroMQ remote API, version 2

The ZeroMQ remote API version 2 is one of [several ways an application can connect with CoppeliaSim](meansOfCommunication.md). It allows you to control a simulation (or the simulator itself) from an external application or a remote hardware (e.g. real robot, remote computer), and offers all API properties and methods also available via a CoppeliaSim script in [sim-2](apiFunctions.md).

The remote API is interacting with CoppeliaSim via [ZeroMQ](http://api.zeromq.org/) and its [interface plugin](simZMQ/simZMQ.md) to CoppeliaSim, and the ZMQ remote API-2 [add-on](addOns.md). All this happens in a hidden fashion to the user. The remote API can let one or several external applications interact with CoppeliaSim in a [stepping](simulation.md#stepped) (i.e. *synchronized* with each simulation step) or non-stepping way (i.e. the normal operation mode), and even remote control of the simulator is supported (e.g. remotely loading a scene, starting, pausing or stopping a simulation for instance).

See programming/zmqRemoteApi-2 folder or [its related repository](https://github.com/CoppeliaRobotics/zmqRemoteApi-2) for examples.

## <a id="python"></a>Python client

Install client package:

```
$ python3 -m pip install coppeliasim-python
```

Requirements: Python 3.10 or newer, plus `numpy`, `pyzmq` and `cbor2` (installed automatically).

The following is a very simple example ZeroMQ remote API-2 client code, which starts then runs a [stepping](simulation.md#stepped) simulation for 3 seconds:

```python
import sim
from sim.zmqremoteapi import ZMQRemoteAPI

rapi = ZMQRemoteAPI()
sim.Object._callMethod = rapi.call

sim.self.setStepping(True)

sim.scene.simulation.start()
while (t := sim.scene.simulation.time) < 3:
    print(f'Simulation time: {t:.2f} [s]')
    sim.self.step()
sim.scene.simulation.stop()
```
