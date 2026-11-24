# simGetEulerAnglesFromMatrix

Retrieves the [Euler angles](../positionOrientationTransformation.md#euler) from a transformation matrix

## Synopsis

```cpp
int simGetEulerAnglesFromMatrix(const double* matrix, double* eulerAngles)
```

## Parameters

- **matrix**: array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2]
- **eulerAngles**: pointer to 3 values

## Return values

- -1 if operation was not successful

## See also

- [positions and orientations](../positionOrientationTransformation.md)
