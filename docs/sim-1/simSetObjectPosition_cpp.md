# simSetObjectPosition

Sets the position (x, y and z-coordinates) of an object. Dynamically simulated objects, together with their hierarchy tree, are dynamically reset (this however does not apply to static shapes)

## Synopsis

```cpp
int simSetObjectPosition(int objectHandle, int relativeToObjectHandle, const double* position)
```

## Parameters

- **objectHandle**: handle of the object. Can be combined with sim.handleflag_reljointbaseframe
- **relativeToObjectHandle**: indicates relative to which reference frame the position is specified. Specify sim.handle_world to set the absolute position, sim.handle_parent to set the position relative to the object's parent, or an object handle relative to whose reference frame the position is specified. If this handle is the handle of a joint, then the position is applied relative to the joint's moving frame (unless **objectHandle** is combined with sim.handleflag_reljointbaseframe, in which case the position is applied relative to the joint's base frame)
- **position**: coordinates of the object

## Return values

- -1 if operation was not successful

## See also

- [simGetObjectPosition](simGetObjectPosition_cpp.md)
- [positions and orientations](../positionOrientationTransformation.md)
