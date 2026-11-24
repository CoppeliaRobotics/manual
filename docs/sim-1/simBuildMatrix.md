# sim.buildMatrix

Builds a transformation matrix based on a position vector and [Euler angles](../positionOrientationTransformation.md#euler)

## Synopsis

```lua
float[12] matrix = sim.buildMatrix(float[3] position, float[3] eulerAngles)
```

```python
list matrix = sim.buildMatrix(list position, list eulerAngles)
```

## Parameters

- **position**: array of 3 values
- **eulerAngles**: array of 3 values

## Return values

- **matrix**: array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2]

## See also

- [positions and orientations](../positionOrientationTransformation.md)
