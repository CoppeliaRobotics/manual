# simGetJointTargetVelocity

Retrieves the target linear/angular velocity of a non-spherical joint

## Synopsis

```cpp
int simGetJointTargetVelocity(int objectHandle, double* targetVelocity)
```

## Parameters

- **objectHandle**: handle of the joint object
- **targetVelocity**: (output): target linear/angular velocity of the joint

## Return values

- -1 if operation was not successful

## See also

- [simSetJointTargetVelocity](simSetJointTargetVelocity_cpp.md)
