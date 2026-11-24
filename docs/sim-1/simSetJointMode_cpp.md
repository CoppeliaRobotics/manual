# simSetJointMode

Sets the operation mode of a joint

## Synopsis

```cpp
int simSetJointMode(int jointHandle, int jointMode, int options)
```

## Parameters

- **jointHandle**: handle of the joint object
- **jointMode**: [joint mode](../apiConstants-1.md#jointModes) value
- **options**: not used. Set to 0.

## Return values

- -1 if operation was not successful

## See also

- [simGetJointMode](simGetJointMode_cpp.md)
- [simSetJointDependency](simSetJointDependency_cpp.md)
