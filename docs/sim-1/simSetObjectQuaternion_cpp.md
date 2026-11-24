# simSetObjectQuaternion

Sets the quaternion of an object. Dynamically simulated objects, together with their hierarchy tree, are dynamically reset (this however does not apply to static shapes)

## Synopsis

```cpp
int simSetObjectQuaternion(int objectHandle, int relativeToObjectHandle, const double* quaternion)
```

## Parameters

- **objectHandle**: handle of the object. Combine with sim.handleflag_wxyzquat to provide the quaternion as [qw qx qy qz] order instead of [qx qy qz qw] order. Can also be combined with sim.handleflag_reljointbaseframe
- **relativeToObjectHandle**: indicates relative to which reference frame the orientation is specified. Specify sim.handle_world to set the absolute orientation, sim.handle_inverse to set the inverse of the absolute orientation, sim.handle_parent to set the orientation relative to the object's parent, or an object handle relative to whose reference frame the orientation is specified. If this handle is the handle of a joint, then the quaternion is applied relative to the joint's moving frame (unless **objectHandle** is combined with sim.handleflag_reljointbaseframe, in which case the quaternion is applied relative to the joint's base frame)
- **quaternion**: the quaternion (array of 4 values [qx qy qz qw])

## Return values

- -1 if operation was not successful

## See also

- [simGetObjectQuaternion](simGetObjectQuaternion_cpp.md)
- [positions and orientations](../positionOrientationTransformation.md)
