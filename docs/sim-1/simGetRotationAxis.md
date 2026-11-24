# sim.getRotationAxis

Retrieves an axis and rotation angle that brings one pose or transformation matrix onto another one. The translation part of the poses/matrices is ignored. This function, when used in combination with [sim.rotateAroundAxis](simRotateAroundAxis.md), can be used to build interpolations between transformation matrices

## Synopsis

```lua
float[3] axis, float angle = sim.getRotationAxis(float[7]/float[12] poseStart/matrixStart,
                                                 float[7]/float[12] poseGoal/matrixGoal)
```

```python
list axis, float angle = sim.getRotationAxis(list poseStart/matrixStart, list poseGoal/matrixGoal)
```

## Parameters

- **poseStart/matrixStart**: the *start* pose (array of 7 values [x y z qx qy qz qw]) or transformation matrix (array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2])
- **poseGoal/matrixGoal**: the *goal* pose (array of 7 values [x y z qx qy qz qw]) or transformation matrix (array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2])

## Return values

- **axis**: the rotation axis in absolute coordinates [Vx Vy Vz]
- **angle**: the rotation angle

## See also

- [positions and orientations](../positionOrientationTransformation.md)
