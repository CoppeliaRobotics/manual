# sim.addForce

Adds a non-central force to a shape object that is dynamically enabled. Added forces are cumulative, applied relative to the center of mass, and are reset to zero after [sim.handleDynamics](simHandleDynamics.md) was called (or by using the following flag: sim.handleflag_resetforcetorque)

## Synopsis

```lua
sim.addForce(int shapeHandle, float[3] position, float[3] force)
```

```python
sim.addForce(int shapeHandle, list position, list force)
```

## Parameters

- **shapeHandle**: handle of a dynamically enabled shape. Can be combined with sim.handleflag_resetforcetorque in order to clear the accumulated force and torque.
- **position**: array of 3 values that represent the relative position where the force should be applied.
- **force**: array of 3 values that represent the force (in relative coordinates) to add.

## Return values

No return values.

## See also

- [sim.addForceAndTorque](simAddForceAndTorque.md)
