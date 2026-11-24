# simGetJointDependency

Retrieves joint dependency information, when the joint is in dependent mode

## Synopsis

```cpp
int simGetJointDependency(int jointHandle, int* masterJointHandle, double* offset, double* multCoeff)
```

## Parameters

- **jointHandle**: handle of the slave joint
- **masterJointHandle**: handle of the master joint, or -1 if the joint is not dependent
- **offset**: offset in equation slave = offset + master * multCoeff
- **multCoeff**: coeff in equation slave = offset + master * multCoeff

## Return values

- -1 if operation was not successful

## See also

- [simSetJointDependency](simSetJointDependency_cpp.md)
- [simGetJointMode](simGetJointMode_cpp.md)
