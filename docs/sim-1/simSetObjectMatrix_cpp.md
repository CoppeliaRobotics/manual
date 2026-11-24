# simSetObjectMatrix

Sets the transformation matrix of an object. Dynamically simulated objects, together with their hierarchy tree, are dynamically reset (this however does not apply to static shapes)

## Synopsis

```cpp
int simSetObjectMatrix(int objectHandle, int relativeToObjectHandle, const double* matrix)
```

## Parameters

- **objectHandle**: handle of the object. Can be combined with sim.handleflag_reljointbaseframe
- **relativeToObjectHandle**: indicates relative to which reference frame the matrix is specified. Specify sim.handle_world to set the absolute transformation matrix, sim.handle_inverse to set the inverse of the absolute transformation matrix, sim.handle_parent to set the transformation matrix relative to the object's parent, or an object handle relative to whose reference frame the transformation matrix is specified. If this handle is the handle of a joint, then the matrix is applied relative to the joint's moving frame (unless **objectHandle** is combined with sim.handleflag_reljointbaseframe, in which case the matrix is applied relative to the joint's base frame)
- **matrix**: the matrix (array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2])

## Return values

- -1 if operation was not successful

## See also

- [simGetObjectMatrix](simGetObjectMatrix_cpp.md)
- [positions and orientations](../positionOrientationTransformation.md)
