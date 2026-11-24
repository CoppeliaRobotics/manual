# sim.setJointPosition

Sets the linear/angular position of a joint. Cannot be used with spherical joints (use [sim.setObjectChildPose](simSetObjectChildPose.md) instead)

## Synopsis

```lua
sim.setJointPosition(int objectHandle, float position)
```

```python
sim.setJointPosition(int objectHandle, float position)
```

## Parameters

- **objectHandle**: handle of the joint object
- **position**: linear/angular position of the joint

## Return values

No return values.

## See also

- [sim.getJointPosition](simGetJointPosition.md)
- [sim.setJointTargetPosition](simSetJointTargetPosition.md)
