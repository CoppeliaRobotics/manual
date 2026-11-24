# sim.rotateAroundAxis

Rotates a pose or transformation matrix around a random axis in space. This function, when used in combination with [sim.getRotationAxis](simGetRotationAxis.md), can be used to build interpolations between poses or transformation matrices

## Synopsis

```lua
float[7]/float[12] poseOut/matrixOut = sim.rotateAroundAxis(float[7]/float[12] poseIn/matrixIn,
                                                            float[3] axis, float[3] axisPos,
                                                            float angle)
```

```python
list poseOut/matrixOut = sim.rotateAroundAxis(list poseIn/matrixIn, list axis, list axisPos,
                                              float angle)
```

## Parameters

- **poseIn/matrixIn**: the pose (array of 7 values [x y z qx qy qz qw]) or transformation matrix (array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2]) to rotate
- **axis**: the axis vector in absolute coordinates to rotate around
- **axisPos**: the position of the rotation axis in absolute coordinates
- **angle**: the amount of rotation to perform

## Return values

- **poseOut/matrixOut**: the transformed (rotated) pose (array of 7 values [x y z qx qy qz qw]) or matrix (array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2])

## See also

- [positions and orientations](../positionOrientationTransformation.md)
