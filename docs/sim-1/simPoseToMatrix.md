# sim.poseToMatrix

Converts a pose to a transformation matrix

## Synopsis

```lua
float[12] matrix = sim.poseToMatrix(float[7] pose)
```

```python
list matrix = sim.poseToMatrix(list pose)
```

## Parameters

- **pose**: input pose (array of 7 values [x y z qx qy qz qw])

## Return values

- **matrix**: the output matrix (array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2])

## See also

- [positions and orientations](../positionOrientationTransformation.md)
