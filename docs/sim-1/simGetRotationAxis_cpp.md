# simGetRotationAxis

Retrieves an axis and rotation angle that brings one pose or transformation matrix onto another one. The translation part of the poses/matrices is ignored. This function, when used in combination with [sim.rotateAroundAxis](simRotateAroundAxis.md), can be used to build interpolations between transformation matrices

## Synopsis

```cpp
int simGetRotationAxis(const double* matrixStart, const double* matrixGoal, double* axis,
                       double* angle)
```

## Parameters

- **matrixStart**: the *start* transformation matrix (array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2])
- **matrixGoal**: the *goal* transformation matrix (array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2])
- **axis**: the returned rotation axis in absolute coordinates (array of 3 values [Vx Vy Vz])
- **angle**: the returned rotation angle

## Return values

- -1 if operation was not successful

## See also

- [positions and orientations](../positionOrientationTransformation.md)
