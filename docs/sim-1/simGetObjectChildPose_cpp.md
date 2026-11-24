# simGetObjectChildPose

Retrieves the intrinsic or internal transformation of an object. For a joint, this is the transformation caused by the joint movement, mainly. For joints and force sensors, this will also include a possible error transformation caused by the physics engine (a physics engine can cause joints and force sensors to come apart, when constraints can't be perfectly resolved)

## Synopsis

```cpp
int simGetObjectChildPose(int objectHandle, double* pose)
```

## Parameters

- **objectHandle**: handle of the object
- **pose**: pointer to the pose

## Return values

- -1 if operation was not successful

## See also

- [simSetObjectChildPose](simSetObjectChildPose_cpp.md)
- [positions and orientations](../positionOrientationTransformation.md)
