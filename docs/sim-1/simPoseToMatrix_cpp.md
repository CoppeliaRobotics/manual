# simPoseToMatrix

Converts a pose to a transformation matrix

## Synopsis

```cpp
int simPoseToMatrix(const double* poseIn, double* matrixOut)
```

## Parameters

- **poseIn**: the input pose (array of 7 values [x y z qx qy qz qw])
- **matrixOut**: the output matrix (array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2])

## Return values

- -1 if operation was not successful

## See also

- [positions and orientations](../positionOrientationTransformation.md)
