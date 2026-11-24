# simInterpolatePoses

Computes the interpolated pose between poseIn1 and poseIn2

## Synopsis

```cpp
int simInterpolatePoses(const double* poseIn1, const double* poseIn2, double interpolFactor,
                        double* poseOut)
```

## Parameters

- **poseIn1**: first input pose (array of 7 values [x y z qx qy qz qw])
- **poseIn2**: second input pose (array of 7 values [x y z qx qy qz qw])
- **interpolFactor**: the interpolation factor, a value between 0.0 and 1.0 (0.0--&gt; poseOut = poseIn1, 1.0--&gt; poseOut = poseIn2)
- **poseOut**: output pose (array of 7 values [x y z qx qy qz qw])

## Return values

- -1 if operation was not successful

## See also

- [positions and orientations](../positionOrientationTransformation.md)
