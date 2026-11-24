# sim.resetDynamicObject

Dynamically resets an object that is dynamically simulated. This means that the object representation in the dynamics engine is removed, and added again. This can be useful when the set-up of a dynamically simulated chain needs to be modified during simulation (e.g. joint or shape attachement position/orientation changed)

## Synopsis

```lua
sim.resetDynamicObject(int objectHandle)
```

```python
sim.resetDynamicObject(int objectHandle)
```

## Parameters

- **objectHandle**: handle of the object. Can be combined with [sim.handleflag_model](../apiConstants-1.md#specialHandleFlags), if you wish to reset all objects in a [model](../models.md) (where objectHandle would be the model base).

## Return values

No return values.
