# sim.interpolateMatrices

Computes the interpolated transformation matrix between matrixIn1 and matrixIn2. Quaternions are used internally

## Synopsis

```lua
float[12] resultMatrix = sim.interpolateMatrices(float[12] matrixIn1, float[12] matrixIn2,
                                                 float interpolFactor)
```

```python
list resultMatrix = sim.interpolateMatrices(list matrixIn1, list matrixIn2, float interpolFactor)
```

## Parameters

- **matrixIn1**: first input matrix (array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2])
- **matrixIn2**: second input matrix (array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2])
- **interpolFactor**: interpolation factor, a value between 0.0 and 1.0 (0.0--&gt; resultMatrix = matrixIn1, 1.0--&gt; resultMatrix = matrixIn2)

## Return values

- **resultMatrix**: the result matrix (array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2])

## See also

- [positions and orientations](../positionOrientationTransformation.md)
