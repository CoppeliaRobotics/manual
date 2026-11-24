# simSetJointPosition

Sets the linear/angular position of a joint. Cannot be used with spherical joints (use [sim.setObjectChildPose](simSetObjectChildPose.md) instead)

## Synopsis

```cpp
int simSetJointPosition(int objectHandle, double position)
```

## Parameters

- **objectHandle**: handle of the joint object
- **position**: linear/angular position of the joint

## Return values

- -1 if operation was not successful

## See also

- [simGetJointPosition](simGetJointPosition_cpp.md)
- [simSetJointTargetPosition](simSetJointTargetPosition_cpp.md)
