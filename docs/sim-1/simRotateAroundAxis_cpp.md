# simRotateAroundAxis

Rotates a pose or transformation matrix around a random axis in space. This function, when used in combination with [sim.getRotationAxis](simGetRotationAxis.md), can be used to build interpolations between poses or transformation matrices

## Synopsis

```cpp
int simRotateAroundAxis(const double* matrixIn, const double* axis, const double* axisPos,
                        double angle, double* matrixOut)
```

## Parameters

- **matrixIn**: transformation matrix to rotate (array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2])
- **axis**: axis vector in absolute coordinates to rotate around
- **axisPos**: position of the rotation axis in absolute coordinates
- **angle**: amount of rotation to perform
- **matrixOut**: returned transformed (rotated) matrix (array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2])

## Return values

- -1 if operation was not successful

## See also

- [positions and orientations](../positionOrientationTransformation.md)
