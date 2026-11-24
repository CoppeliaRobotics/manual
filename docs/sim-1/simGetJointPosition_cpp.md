# simGetJointPosition

Retrieves the linear/angular position of a joint. This function cannot be used with spherical joints (use [sim.getObjectChildPose](simGetObjectChildPose.md) instead)

## Synopsis

```cpp
int simGetJointPosition(int objectHandle, double* position)
```

## Parameters

- **objectHandle**: handle of the joint
- **position**: linear/angular position of the joint

## Return values

- -1 if operation was not successful

## See also

- [simSetJointPosition](simSetJointPosition_cpp.md)
