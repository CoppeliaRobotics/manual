# sim.addForceAndTorque

Adds a force and/or torque to a shape object that is dynamically enabled. Forces are applied at the center of mass. Added forces and torques are cumulative, and are reset to zero after [sim.handleDynamics](simHandleDynamics.md) was called (or by using the following flags: sim.handleflag_resetforce and/or sim.handleflag_resettorque)

## Synopsis

```lua
sim.addForceAndTorque(int shapeHandle, float[3] force, float[3] torque)
```

```python
sim.addForceAndTorque(int shapeHandle, list force, list torque)
```

## Parameters

- **shapeHandle**: handle of a dynamically enabled shape. Can be combined with sim.handleflag_resetforce and/or sim.handleflag_resettorque in order to clear the accumulated force or torque.
- **force**: array of 3 values that represent the force (in absolute coordinates) to add. Can be None/nil
- **torque**: array of 3 values that represent the torque (in absolute coordinates) to add. Can be None/nil

## Return values

No return values.

## See also

- [sim.addForce](simAddForce.md)
