# sim.isDynamicallyEnabled

Checks whether a scene object is dynamically enabled, i.e. is being handled and simulated by the physics engine. Note that until the physics engine has parsed the scene in the first simulation step (i.e. the first time [sim.handleDynamics](simHandleDynamics.md) is called), no object will be dynamically enabled

## Synopsis

```lua
bool dynamicallyEnabled = sim.isDynamicallyEnabled(int objectHandle)
```

```python
bool dynamicallyEnabled = sim.isDynamicallyEnabled(int objectHandle)
```

## Parameters

- **ojectHandle**: handle of the scene object

## Return values

- **dynamicallyEnabled**: whether the object is dynamically enabled
