# simGetObjectVelocity

Retrieves the linear and/or angular velocity of an object, in absolute coordinates. The velocity is a measured velocity (i.e. from one simulation step to the next), and is available for all objects in the scene

## Synopsis

```cpp
int simGetObjectVelocity(int objectHandle, double* linearVelocity, double* angularVelocity)
```

## Parameters

- **objectHandle**: handle of a [scene object](../objects.md). It is highly recommended to add  *[sim.handleflag_axis](../apiConstants-1.md#specialHandleFlags)*  to the object handle, in order to obtain the *regular* angular velocity for the object, i.e. the rotation axis and the rotation velocity that is represented by the axis' length. If *sim.handleflag_axis* is omitted, then a derivative of Euler angles expressed relative to previous' simulation frame will be returned for the angular velocity
- **linearVelocity**: pointer to 3 values that will receive the linear velocity. Can be nullptr
- **angularVelocity**: pointer to 3 values that will receive the angular velocity. Can be nullptr

## Return values

- -1 if operation was not successful

## See also

- [simGetVelocity](simGetVelocity_cpp.md)
