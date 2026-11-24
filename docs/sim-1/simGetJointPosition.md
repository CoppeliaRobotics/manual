# sim.getJointPosition

Retrieves the linear/angular position of a joint. This function cannot be used with spherical joints (use [sim.getObjectChildPose](simGetObjectChildPose.md) instead)

## Synopsis

```lua
float position = sim.getJointPosition(int objectHandle)
```

```python
float position = sim.getJointPosition(int objectHandle)
```

## Parameters

- **objectHandle**: handle of the joint

## Return values

- **position**: linear/angular position of the joint

## See also

- [sim.setJointPosition](simSetJointPosition.md)
