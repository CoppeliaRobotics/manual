# Remote API

The remote API is one of [several ways an application can connect with CoppeliaSim](meansOfCommunication.md). It allows communication between CoppeliaSim and an external application (i.e. an application running in a different process, or on a different machine), is cross-platform, and supports the exact same API function calls as from within a CoppeliaSim script. It comes in three distinct versions/frameworks:

- [The ZeroMQ remote API](zmqRemoteApiOverview.md): based on [sim-1](apiFunctions-1.md), it is a function-based API that supports Python, C++, Matlab, Octave, Java, Lua and Rust clients.
- [The ZeroMQ remote API-2](zmqRemoteApi2Overview.md): based on [sim-2](apiFunctions.md), it is an OOP API that supports Python clients.
- [The WebSocket remote API](wsRemoteApiOverview.md): based on [sim-1](apiFunctions-1.md), it supports JavaScript clients.

As an example, a Python ZeroMQ remote API-2 client receiving and applying back a [vision sensor](visionSensors.md) image could look like:

```python
import sim
from sim.zmqremoteapi import ZMQRemoteAPI

port = ZMQRemoteAPI().call(None, 'spawnWorker')
rapi = ZMQRemoteAPI(port = port)
sim.Object._callMethod = rapi.call

sensor1 = sim.self.getObject('/VisionSensor')
sensor2 = sim.self.getObject('/PassiveVisionSensor')

sim.scene.simulation.start()
while sim.scene.simulation.time < 10:
    sensor2.image = sensor1.image
sim.scene.simulation.stop()
```
