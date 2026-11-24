# simInterpolateMatrices

Computes the interpolated transformation matrix between matrixIn1 and matrixIn2. Quaternions are used internally

## Synopsis

```cpp
int simInterpolateMatrices(const double* matrixIn1, const double* matrixIn2, double interpolFactor,
                           double* matrixOut)
```

## Parameters

- **matrixIn1**: the first input matrix (array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2])
- **matrixIn2**: the second input matrix (array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2])
- **interpolFactor**: the interpolation factor, a value between 0.0 and 1.0 (0.0--&gt; matrixOut = matrixIn1, 1.0--&gt; matrixOut = matrixIn2)
- **matrixOut**: the output matrix (array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2])

## Return values

- -1 if operation was not successful

## See also

- [positions and orientations](../positionOrientationTransformation.md)
