# simTransformVector

Multiplies a vector with a transformation matrix (v = m * v)

## Synopsis

```cpp
int simTransformVector(const double* matrix, double* vect)
```

## Parameters

- **matrix**: the transformation matrix: [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2]
- **vect**: the vector to be transformed (a pointer to 3 values)

## Return values

- -1 if operation was not successful

## See also

- [matrix/transformation functions](../apiFunctions-1.md#coordinatesAndTransformations)
