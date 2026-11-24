# sim.buildPose

Builds a pose based on a position vector and [Euler angles](../positionOrientationTransformation.md#euler) or axes

## Synopsis

```lua
float[7] pose = sim.buildPose(float[3] position, float[3] eulerAnglesOrAxis1, int mode = 0,
                              float[3] axis2 = nil)
```

```python
list pose = sim.buildPose(list position, list eulerAnglesOrAxis, int mode = 0, list axis2 = None)
```

## Parameters

- **position**: pointer to 3 values representing the position component
- **eulerAnglesOrAxis1**: pointer to 3 values representing Euler angles or a reference frame axis (see mode below)
- **mode**: describes how the orientation is specified:

    - 0: eulerAnglesOrAxis1 represents Euler angles and axis2 is ignored
    - 1: eulerAnglesOrAxis1 represents the x-axis of the new pose's reference frame, axis2 is ignored
    - 2: eulerAnglesOrAxis1 represents the y-axis of the new pose's reference frame, axis2 is ignored
    - 3: eulerAnglesOrAxis1 represents the z-axis of the new pose's reference frame, axis2 is ignored
    - 4: eulerAnglesOrAxis1 represents the x-axis and axis2 represents the y-axis of the new pose's reference frame
    - 5: eulerAnglesOrAxis1 represents the y-axis and axis2 represents the z-axis of the new pose's reference frame
    - 6: eulerAnglesOrAxis1 represents the z-axis and axis2 represents the x-axis of the new pose's reference frame
    - 7: eulerAnglesOrAxis1 represents the x-axis and axis2 represents the z-axis of the new pose's reference frame
    - 8: eulerAnglesOrAxis1 represents the y-axis and axis2 represents the x-axis of the new pose's reference frame
    - 9: eulerAnglesOrAxis1 represents the z-axis and axis2 represents the y-axis of the new pose's reference frame
- **axis2**: pointer to 3 values representing a reference frame axis (see mode above)

## Return values

- **pose**: the pose (array of 7 values [x y z qx qy qz qw])

## See also

- [positions and orientations](../positionOrientationTransformation.md)
