# simGetObjectOrientation

Retrieves the orientation ([Euler angles](../positionOrientationTransformation.md#euler)) of an object

## Synopsis

```cpp
int simGetObjectOrientation(int objectHandle, int relativeToObjectHandle, double* eulerAngles)
```

## Parameters

- **objectHandle**: handle of the object. Can be combined with sim.handleflag_reljointbaseframe (see next argument)
- **relativeToObjectHandle**: indicates relative to which reference frame we want the orientation. Specify sim.handle_world to retrieve the absolute orientation, sim.handle_inverse to retrieve the inverse of the absolute orientation, sim.handle_parent to retrieve the orientation relative to the object's parent, or an object handle relative to whose reference frame you want the orientation. If this handle is the handle of a joint, then the orientation relative to the joint's moving frame will be returned (unless **objectHandle** is combined with sim.handleflag_reljointbaseframe, in which case the orientation relative to the joint's base frame will be returned).
- **eulerAngles**: Euler angles (alpha, beta and gamma)

## Return values

- -1 if operation was not successful

## See also

- [simSetObjectOrientation](simSetObjectOrientation_cpp.md)
- [positions and orientations](../positionOrientationTransformation.md)
