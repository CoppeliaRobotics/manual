# simGetJointTargetPosition

Retrieves the target linear/angular position of a joint

## Synopsis

```cpp
int simGetJointTargetPosition(int objectHandle, double* targetPosition)
```

## Parameters

- **objectHandle**: handle of the joint object
- **targetPosition**: (output): target position of the joint

## Return values

- -1 if operation was not successful

## See also

- [simSetJointTargetPosition](simSetJointTargetPosition_cpp.md)
