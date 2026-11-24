# sim.getEulerAnglesFromMatrix

Retrieves the [Euler angles](../positionOrientationTransformation.md#euler) from a transformation matrix

## Synopsis

```lua
float[3] eulerAngles = sim.getEulerAnglesFromMatrix(float[12] matrix)
```

```python
list eulerAngles = sim.getEulerAnglesFromMatrix(list matrix)
```

## Parameters

- **matrix**: array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2]

## Return values

- **eulerAngles**: array of 3 values

## See also

- [positions and orientations](../positionOrientationTransformation.md)
