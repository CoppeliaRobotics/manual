# simMatrixToPose

Converts a transformation matrix to a pose

## Synopsis

```cpp
int simMatrixToPose(const double* matrixIn, double* poseOut)
```

## Parameters

- **matrixIn**: input matrix (array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2])
- **poseOut**: output pose (array of 7 values [x y z qx qy qz qw])

## Return values

- -1 if operation was not successful

## See also

- [positions and orientations](../positionOrientationTransformation.md)
