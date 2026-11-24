# simSetJointTargetPosition

Sets the target linear/angular position of a joint. When in kinematic mode, the joint moves according to a motion profile that respects maximum velocity, acceleration and jerk values. In dynamic and position/custom control mode, the controller is instructed about the desired position

## Synopsis

```cpp
int simSetJointTargetPosition(int objectHandle, double targetPosition)
```

## Parameters

- **objectHandle**: handle of the joint object
- **targetPosition**: target position of the joint

## Return values

- -1 if operation was not successful

## See also

- [simGetJointTargetPosition](simGetJointTargetPosition_cpp.md)
- [simSetJointPosition](simSetJointPosition_cpp.md)
