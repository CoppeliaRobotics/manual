# sim.multiplyVector

Multiplies a vector with a quaternion, a pose, or a matrix (e.g. v = m * v)

## Synopsis

```lua
float[3*n] resultVector = sim.multiplyVector(float[4]/float[7]/float[12] quaternion/pose/matrix
                                             float[3*n] vector)
```

```python
list resultVector = sim.multiplyVector(list quaternion/pose/matrix, list vector)
```

## Parameters

- **pose/matrix**: a quaternion (array of 4 values [qx qy qz qw]), a pose (array of 7 values [x y z qx qy qz qw]) or a transformation matrix (array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2])
- **vector**: the original vector: an array of 3 * n values. Each triplet represents one vector to be multiplied

## Return values

- **resultVector**: the result vector: an array of 3 * n values. Each triplet represents one vector

## See also

- [positions and orientations](../positionOrientationTransformation.md)
