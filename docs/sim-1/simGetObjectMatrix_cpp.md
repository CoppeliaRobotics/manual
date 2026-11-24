# simGetObjectMatrix

Retrieves the transformation matrix of an object

## Synopsis

```cpp
int simGetObjectMatrix(int objectHandle, int relativeToObjectHandle, double* matrix)
```

## Parameters

- **objectHandle**: handle of the object. Can be combined with sim.handleflag_reljointbaseframe (see next argument)
- **relativeToObjectHandle**: indicates relative to which reference frame we want the matrix. Specify sim.handle_world to retrieve the absolute transformation matrix, sim.handle_inverse to retrieve the inverse of the absolute transformation matrix, sim.handle_parent to retrieve the transformation matrix relative to the object's parent, or an object handle relative to whose reference frame we want the transformation matrix. If this handle is the handle of a joint, then the matrix relative to the joint's moving frame will be returned (unless **objectHandle** is combined with sim.handleflag_reljointbaseframe, in which case the matrix relative to the joint's base frame will be returned).
- **matrix**: pointer to 12 double values

## Return values

- -1 if operation was not successful

## See also

- [simSetObjectMatrix](simSetObjectMatrix_cpp.md)
- [positions and orientations](../positionOrientationTransformation.md)
