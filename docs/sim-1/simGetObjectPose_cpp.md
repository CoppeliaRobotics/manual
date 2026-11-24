# simGetObjectPose

Retrieves the pose of an object

## Synopsis

```cpp
int simGetObjectPose(int objectHandle, int relativeToObjectHandle, double* pose)
```

## Parameters

- **objectHandle**: handle of the object. Combine with sim.handleflag_wxyzquat to retrieve the quaternion as [qw qx qy qz] order instead of [qx qy qz qw] order. Can also be combined with sim.handleflag_reljointbaseframe (see next argument)
- **relativeToObjectHandle**: indicates relative to which reference frame we want the pose. Specify sim.handle_world to retrieve the absolute pose, sim.handle_inverse to retrieve the inverse of the absolute pose, sim.handle_parent to retrieve the pose relative to the object's parent, or an object handle relative to whose reference frame we want the pose. If this handle is the handle of a joint, then the pose relative to the joint's moving frame will be returned (unless **objectHandle** is combined with sim.handleflag_reljointbaseframe, in which case the pose relative to the joint's base frame will be returned).
- **pose**: pointer to 7 values: [x y z qx qy qz qw]

## Return values

- -1 if operation was not successful

## See also

- [simSetObjectPose](simSetObjectPose_cpp.md)
- [positions and orientations](../positionOrientationTransformation.md)
