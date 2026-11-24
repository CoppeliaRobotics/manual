# sim.getObjectChildPose

Retrieves the intrinsic or internal transformation of an object. For a joint, this is the transformation caused by the joint movement, mainly. For joints and force sensors, this will also include a possible error transformation caused by the physics engine (a physics engine can cause joints and force sensors to come apart, when constraints can't be perfectly resolved)

## Synopsis

```lua
float[7] pose = sim.getObjectChildPose(int objectHandle)
```

```python
list pose = sim.getObjectChildPose(int objectHandle)
```

## Parameters

- **objectHandle**: handle of the joint

## Return values

- **pose**: the pose

## See also

- [sim.setObjectChildPose](simSetObjectChildPose.md)
- [positions and orientations](../positionOrientationTransformation.md)
