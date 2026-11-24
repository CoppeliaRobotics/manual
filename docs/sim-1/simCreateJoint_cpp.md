# simCreateJoint

Creates a [joint](../joints.md)

## Synopsis

```cpp
int simCreateJoint(int jointType, int jointMode, int options, const double* sizes,
                   const double* reservedA, const double* reservedB)
```

## Parameters

- **jointType**:
    - sim.joint_revolute
    - sim.joint_prismatic
    - sim.joint_spherical
- **jointMode**: a [joint mode](../apiConstants-1.md#jointModes)
- **options**: reserved. Set to 0
- **sizes**: pointer to 2 values indicating the joint length and diameter. Can be nullptr for default values
- **reservedA**: + **reservedB**: set to nullptr

## Return values

- -1 if operation was not successful, otherwise the handle of the joint

## See also

- [simSetJointInterval](simSetJointInterval_cpp.md)
