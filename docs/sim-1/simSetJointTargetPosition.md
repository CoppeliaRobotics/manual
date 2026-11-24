# sim.setJointTargetPosition

Sets the target linear/angular position of a joint. When in kinematic mode, the joint moves according to a motion profile that respects maximum velocity, acceleration and jerk values. In dynamic and position/custom control mode, the controller is instructed about the desired position

## Synopsis

```lua
sim.setJointTargetPosition(int objectHandle, float targetPosition, float[] motionParams = {})
```

```python
sim.setJointTargetPosition(int objectHandle, float targetPosition, float[] motionParams = [])
```

## Parameters

- **objectHandle**: handle of the joint object
- **targetPosition**: target position of the joint
- **motionParams**: when in kinematic mode: the maximum allowed velocity, acceleration and jerk. When in dynamics mode with position control and motion profile enabled, the maximum allowed velocity, acceleration and jerk. Can be None/nil for default values. See also [joint.maxVelAccelJerk](../sim-2/property_joint_maxVelAccelJerk.md)

## Return values

No return values.

## See also

- [sim.getJointTargetPosition](simGetJointTargetPosition.md)
- [sim.setJointPosition](simSetJointPosition.md)
