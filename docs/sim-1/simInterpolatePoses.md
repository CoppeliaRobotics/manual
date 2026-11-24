# sim.interpolatePoses

Computes the interpolated pose between poseIn1 and poseIn2

## Synopsis

```lua
float[7] resultPose = sim.interpolatePoses(float[7] poseIn1, float[7] poseIn2, float interpolFactor)
```

```python
list resultPose = sim.interpolatePoses(list poseIn1, list poseIn2, float interpolFactor)
```

## Parameters

- **poseIn1**: first input pose (array of 7 values [x y z qx qy qz qw])
- **poseIn2**: second input pose (array of 7 values [x y z qx qy qz qw])
- **interpolFactor**: interpolation factor, a value between 0.0 and 1.0 (0.0--&gt; resultPose = poseIn1, 1.0--&gt; resultPose = poseIn2)

## Return values

- **resultPose**: the result pose (array of 7 values [x y z qx qy qz qw])

## See also

- [positions and orientations](../positionOrientationTransformation.md)
