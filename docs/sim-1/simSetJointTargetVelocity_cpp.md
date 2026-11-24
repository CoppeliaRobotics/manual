# simSetJointTargetVelocity

Sets the target linear/angular velocity of a non-spherical joint. When in kinematic mode, the joint moves according to a motion profile that respects maximum acceleration and jerk values. In dynamic and velocity control mode, the controller is instructed about the desired velocity

## Synopsis

```cpp
int simSetJointTargetVelocity(int objectHandle, double targetVelocity)
```

## Parameters

- **objectHandle**: handle of the joint object
- **targetVelocity**: target velocity of the joint

## Return values

- -1 if operation was not successful

## See also

- [simGetJointTargetVelocity](simGetJointTargetVelocity_cpp.md)
