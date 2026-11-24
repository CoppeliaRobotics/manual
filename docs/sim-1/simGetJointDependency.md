# sim.getJointDependency

Retrieves joint dependency information, when the joint is in dependent mode

## Synopsis

```lua
int masterJointHandle, float offset, float multCoeff = sim.getJointDependency(int jointHandle)
```

```python
int masterJointHandle, float offset, float multCoeff = sim.getJointDependency(int jointHandle)
```

## Parameters

- **jointHandle**: handle of the slave joint

## Return values

- **masterJointHandle**: handle of the master joint, or -1 if the joint is not dependent
- **offset**: offset in equation slave = offset + master * multCoeff
- **multCoeff**: coeff in equation slave = offset + master * multCoeff

## See also

- [sim.setJointDependency](simSetJointDependency.md)
- [sim.getJointMode](simGetJointMode.md)
