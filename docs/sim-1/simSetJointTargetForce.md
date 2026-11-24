# sim.setJointTargetForce

Sets the force or torque that a joint can exert

## Synopsis

```lua
sim.setJointTargetForce(int objectHandle, float forceOrTorque, bool signedValue = true)
```

```python
sim.setJointTargetForce(int objectHandle, float forceOrTorque)
```

## Parameters

- **objectHandle**: handle of the joint object
- **forceOrTorque**: maximum force or torque the joint can exert
- **signedValue**: if true, the sign of the force/torque indicates the desired movement direction

## Return values

No return values.

## See also

- [sim.getJointTargetForce](simGetJointTargetForce.md)
- [sim.getJointForce](simGetJointForce.md)
- [sim.setJointTargetVelocity](simSetJointTargetVelocity.md)
