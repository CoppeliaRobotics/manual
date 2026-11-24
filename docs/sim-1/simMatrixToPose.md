# sim.matrixToPose

Converts a transformation matrix to a pose

## Synopsis

```lua
float[7] pose = sim.matrixToPose(float[12] matrix)
```

```python
list pose = sim.matrixToPose(list matrix)
```

## Parameters

- **matrix**: input matrix (array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2])

## Return values

- **pose**: the output pose (array of 7 values [x y z qx qy qz qw])

## See also

- [positions and orientations](../positionOrientationTransformation.md)
