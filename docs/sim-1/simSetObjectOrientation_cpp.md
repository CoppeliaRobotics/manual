# simSetObjectOrientation

Sets the orientation ([Euler angles](../positionOrientationTransformation.md#euler)) of an object. Dynamically simulated objects, together with their hierarchy tree, are dynamically reset (this however does not apply to static shapes)

## Synopsis

```cpp
int simSetObjectOrientation(int objectHandle, int relativeToObjectHandle, const double* eulerAngles)
```

## Parameters

- **objectHandle**: handle of the object. Can be combined with sim.handleflag_reljointbaseframe
- **relativeToObjectHandle**: indicates relative to which reference frame the orientation is specified. Specify sim.handle_world to set the absolute orientation, sim.handle_inverse to set the inverse of the absolute orientation, sim.handle_parent to set the orientation relative to the object's parent, or an object handle relative to whose reference frame the orientation is specified. If this handle is the handle of a joint, then the orientation is applied relative to the joint's moving frame (unless **objectHandle** is combined with sim.handleflag_reljointbaseframe, in which case the orientation is applied relative to the joint's base frame)
- **eulerAngles**: Euler angles (alpha, beta and gamma)

## Return values

- -1 if operation was not successful

## See also

- [simGetObjectOrientation](simGetObjectOrientation_cpp.md)
- [positions and orientations](../positionOrientationTransformation.md)
