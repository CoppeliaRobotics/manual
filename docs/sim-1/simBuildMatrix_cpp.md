# simBuildMatrix

Builds a transformation matrix based on a position vector and [Euler angles](../positionOrientationTransformation.md#euler)

## Synopsis

```cpp
int simBuildMatrix(const double* position, const double* eulerAngles, double* matrix)
```

## Parameters

- **position**: pointer to 3 values
- **eulerAngles**: pointer to 3 values
- **matrix**: matrix (array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2])

## Return values

- -1 if operation was not successful

## See also

- [positions and orientations](../positionOrientationTransformation.md)
