# simAddForceAndTorque

Adds a force and/or torque to a shape object that is dynamically enabled. Forces are applied at the center of mass. Added forces and torques are cumulative, and are reset to zero after [sim.handleDynamics](simHandleDynamics.md) was called (or by using the following flags: sim.handleflag_resetforce and/or sim.handleflag_resettorque)

## Synopsis

```cpp
int simAddForceAndTorque(int shapeHandle, const double* force, const double* torque)
```

## Parameters

- **shapeHandle**: handle of a dynamically enabled shape. Can be combined with sim.handleflag_resetforce and/or sim.handleflag_resettorque in order to clear the accumulated force or torque.
- **force**: pointer to 3 values that represent the force (in absolute coordinates) to add. Can be nullptr.
- **torque**: pointer to 3 values that represent the torque (in absolute coordinates) to add. Can be nullptr

## Return values

- -1 if operation was not successful

## See also

- [simAddForce](simAddForce_cpp.md)
