# simMultiplyPoses

Multiplies two poses

## Synopsis

```cpp
int simMultiplyPoses(const double* poseIn1, const double* poseIn2, double* poseOut)
```

## Parameters

- **poseIn1**: first input pose (array of 7 values [x y z qx qy qz qw])
- **poseIn2**: second input pose (array of 7 values [x y z qx qy qz qw])
- **poseOut**: output pose (array of 7 values [x y z qx qy qz qw])

## Return values

- -1 if operation was not successful

## See also

- [positions and orientations](../positionOrientationTransformation.md)
