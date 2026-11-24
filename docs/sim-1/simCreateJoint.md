# sim.createJoint

Creates a [joint](../joints.md)

## Synopsis

```lua
int jointHandle = sim.createJoint(int jointType, int jointMode, int options, float[2] sizes = nil)
```

```python
int jointHandle = sim.createJoint(int jointType, int jointMode, int options, list sizes = None)
```

## Parameters

- **jointType**:
    - sim.joint_revolute
    - sim.joint_prismatic
    - sim.joint_spherical
- **jointMode**: a [joint mode](../apiConstants-1.md#jointModes)
- **options**: reserved. Set to 0
- **sizes**: array of 2 values indicating the joint length and diameter. Can be None/nil for default values

## Return values

- **jointHandle**: handle of the joint

## See also

- [sim.setJointInterval](simSetJointInterval.md)
