# simSetJointTargetForce

Sets the force or torque that a joint can exert

## Synopsis

```cpp
int simSetJointTargetForce(int objectHandle, double forceOrTorque, bool signedValue)
```

## Parameters

- **objectHandle**: handle of the joint object
- **forceOrTorque**: maximum force or torque the joint can exert
- **signedValue**: if true, the sign of the force/torque indicates the desired movement direction

## Return values

- -1 if operation was not successful

## See also

- [simGetJointTargetForce](simGetJointTargetForce_cpp.md)
- [simGetJointForce](simGetJointForce_cpp.md)
- [simSetJointTargetVelocity](simSetJointTargetVelocity_cpp.md)
