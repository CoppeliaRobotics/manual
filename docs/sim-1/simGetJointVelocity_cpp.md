# simGetJointVelocity

Retrieves the linear or angular velocity of a joint. The velocity is a measured velocity (i.e. from one simulation step to the next), and is available for all joints in the scene

## Synopsis

```cpp
int simGetJointVelocity(int jointHandle, double* velocity)
```

## Parameters

- **jointHandle**: handle of a joint.
- **velocity**: a pointer that will receive the velocity.

## Return values

- -1 if operation was not successful
