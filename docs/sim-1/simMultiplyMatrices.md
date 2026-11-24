# sim.multiplyMatrices

Multiplies two transformation matrices

## Synopsis

```lua
float[12] resultMatrix = sim.multiplyMatrices(float[12] matrixIn1, float[12] matrixIn2)
```

```python
list resultMatrix = sim.multiplyMatrices(list matrixIn1, list matrixIn2)
```

## Parameters

- **matrixIn1**: first input matrix (array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2])
- **matrixIn2**: second input matrix (array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2])

## Return values

- **resultMatrix**: the result matrix (array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2])

## See also

- [positions and orientations](../positionOrientationTransformation.md)
