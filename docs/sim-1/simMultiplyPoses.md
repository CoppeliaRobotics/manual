# sim.multiplyPoses

Multiplies two poses

## Synopsis

```lua
float[7] resultPose = sim.multiplyPoses(float[7] poseIn1, float[7] poseIn2)
```

```python
list resultPose = sim.multiplyPoses(list poseIn1, list poseIn2)
```

## Parameters

- **poseIn1**: first input pose (array of 7 values [x y z qx qy qz qw])
- **poseIn2**: second input pose (array of 7 values [x y z qx qy qz qw])

## Return values

- **resultPose**: the result pose (array of 7 values [x y z qx qy qz qw])

## See also

- [positions and orientations](../positionOrientationTransformation.md)
