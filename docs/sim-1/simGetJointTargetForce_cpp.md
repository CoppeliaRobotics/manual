# simGetJointTargetForce

Retrieves the force or torque that a joint can exert

## Synopsis

```cpp
int simGetJointTargetForce(int jointHandle, double* forceOrTorque)
```

## Parameters

- **jointHandle**: handle of the joint.
- **forceOrTorque**: the maximum force or torque the joint can apply. The sign indicates the desired movement direction.

## Return values

- -1 if operation was not successful. .

## See also

- [simSetJointTargetForce](simSetJointTargetForce_cpp.md)
- [simGetJointTargetVelocity](simGetJointTargetVelocity_cpp.md)
