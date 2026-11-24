# simMultiplyMatrices

Multiplies two transformation matrices

## Synopsis

```cpp
int simMultiplyMatrices(const double* matrixIn1, const double* matrixIn2, double* matrixOut)
```

## Parameters

- **matrixIn1**: first input matrix (array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2])
- **matrixIn2**: second input matrix (array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2])
- **matrixOut**: output matrix (array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2])

## Return values

- -1 if operation was not successful

## See also

- [positions and orientations](../positionOrientationTransformation.md)
