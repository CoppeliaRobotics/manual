# sim.setObjectChildPose

Can be used to set a spherical joint's rotational transformation (the translational part is ignored)

## Synopsis

```lua
sim.setObjectChildPose(int objectHandle, float[7] pose)
```

```python
sim.setObjectChildPose(int objectHandle, list pose)
```

## Parameters

- **objectHandle**: handle of the object
- **pose**: the pose (array of 7 values [x y z qx qy qz qw])

## Return values

No return values.

## See also

- [sim.getObjectChildPose](simGetObjectChildPose.md)
- [positions and orientations](../positionOrientationTransformation.md)
