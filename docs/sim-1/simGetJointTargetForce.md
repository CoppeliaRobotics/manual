# sim.getJointTargetForce

Retrieves the force or torque that a joint can exert

## Synopsis

```lua
float forceOrTorque = sim.getJointTargetForce(int jointHandle)
```

```python
float forceOrTorque = sim.getJointTargetForce(int jointHandle)
```

## Parameters

- **jointHandle**: handle of the joint

## Return values

- **forceOrTorque**: the maximum force or torque the joint can apply. The sign indicates the desired movement direction

## See also

- [sim.setJointTargetForce](simSetJointTargetForce.md)
- [sim.getJointTargetVelocity](simGetJointTargetVelocity.md)
