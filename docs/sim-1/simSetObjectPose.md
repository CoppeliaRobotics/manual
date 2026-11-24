# sim.setObjectPose

Sets the pose of an object. Dynamically simulated objects, together with their hierarchy tree, are dynamically reset (this however does not apply to static shapes)

## Synopsis

```lua
sim.setObjectPose(int objectHandle, float[7] pose, int relativeToObjectHandle = sim.handle_world)
```

```python
sim.setObjectPose(int objectHandle, list pose, int relativeToObjectHandle = sim.handle_world)
```

## Parameters

- **objectHandle**: handle of the object. Combine with sim.handleflag_wxyzquat to provide the quaternion as [qw qx qy qz] order instead of [qx qy qz qw] order. Can also be combined with sim.handleflag_reljointbaseframe
- **pose**: the pose (array of 7 values [x y z qx qy qz qw])
- **relativeToObjectHandle**: indicates relative to which reference frame the pose is specified. Specify sim.handle_world to set the absolute pose, sim.handle_inverse to set the inverse of the absolute pose, sim.handle_parent to set the pose relative to the object's parent, or an object handle relative to whose reference frame the pose is specified. If this handle is the handle of a joint, then the pose is applied relative to the joint's moving frame (unless **objectHandle** is combined with sim.handleflag_reljointbaseframe, in which case the pose is applied relative to the joint's base frame)

## Return values

No return values.

## See also

- [sim.getObjectPose](simGetObjectPose.md)
- [positions and orientations](../positionOrientationTransformation.md)
