# sim.setJointDependency

Sets a joint dependent of another joint. The dependent joint should first be set into dependent mode via [sim.setJointMode](simSetJointMode.md)

## Synopsis

```lua
sim.setJointDependency(int jointHandle, int masterJointHandle, float offset, float multCoeff)
```

```python
sim.setJointDependency(int jointHandle, int masterJointHandle, float offset, float multCoeff)
```

## Parameters

- **jointHandle**: handle of the joint to become slave
- **masterJointHandle**: handle of the joint to become master, or -1 to free the slave joint from dependency
- **offset**: offset in equation slave = offset + master * multCoeff
- **multCoeff**: coeff in equation slave = offset + master * multCoeff

## Return values

No return values.

## See also

- [sim.getJointDependency](simGetJointDependency.md)
