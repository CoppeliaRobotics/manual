# simAddForce

Adds a non-central force to a shape object that is dynamically enabled. Added forces are cumulative, applied relative to the center of mass, and are reset to zero after [sim.handleDynamics](simHandleDynamics.md) was called (or by using the following flag: sim.handleflag_resetforcetorque)

## Synopsis

```cpp
int simAddForce (int shapeHandle, const double* position, const double* force)
```

## Parameters

- **shapeHandle**: handle of a dynamically enabled shape. Can be combined with sim.handleflag_resetforcetorque in order to clear the accumulated force and torque.
- **position**: pointer to 3 values that represent the relative position where the force should be applied.
- **force**: pointer to 3 values that represent the force (in relative coordinates) to add.

## Return values

- -1 if operation was not successful

## See also

- [simAddForceAndTorque](simAddForceAndTorque_cpp.md)
