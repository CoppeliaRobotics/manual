# sim.getJointType

Retrieves the type of a joint

## Synopsis

```lua
int jointType = sim.getJointType(int objectHandle)
```

```python
int jointType = sim.getJointType(int objectHandle)
```

## Parameters

- **objectHandle**: handle of the joint

## Return values

- **jointType**: type of the joint:

    - sim.joint_revolute
    - sim.joint_prismatic
    - sim.joint_spherical
