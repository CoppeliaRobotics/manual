# simSetObjectChildPose

Can be used to set a spherical joint's rotational transformation (the translational part is ignored)

## Synopsis

```cpp
int simSetObjectChildPose(int objectHandle, const double* pose)
```

## Parameters

- **objectHandle**: handle of the object
- **pose**: pointer to the pose (array of 7 values [x y z qx qy qz qw])

## Return values

- -1 if operation was not successful

## See also

- [simGetObjectChildPose](simGetObjectChildPose_cpp.md)
- [positions and orientations](../positionOrientationTransformation.md)
