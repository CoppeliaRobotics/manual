# simBuildPose

Builds a pose based on a position vector and [Euler angles](../positionOrientationTransformation.md#euler) or axes

## Synopsis

```cpp
int simBuildPose(const double* position, const double* eulerAngles, double* pose)
```

## Parameters

- **position**: pointer to 3 values
- **eulerAngles**: pointer to 3 values
- **pose**: pose (array of 7 values [x y z qx qy qz qw])

## Return values

- -1 if operation was not successful

## See also

- [positions and orientations](../positionOrientationTransformation.md)
