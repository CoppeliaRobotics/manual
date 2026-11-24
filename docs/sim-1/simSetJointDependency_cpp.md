# simSetJointDependency

Sets a joint dependent of another joint. The dependent joint should first be set into dependent mode via [sim.setJointMode](simSetJointMode.md)

## Synopsis

```cpp
int simSetJointDependency(int jointHandle, int masterJointHandle, double offset, double multCoeff)
```

## Parameters

- **jointHandle**: handle of the joint to become slave
- **masterJointHandle**: handle of the joint to become master, or -1 to free the slave joint from dependency
- **offset**: offset in equation slave = offset + master * multCoeff
- **multCoeff**: coeff in equation slave = offset + master * multCoeff

## Return values

- -1 if operation was not successful

## See also

- [simGetJointDependency](simGetJointDependency_cpp.md)
