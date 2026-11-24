# sim.setJointTargetVelocity

Sets the target linear/angular velocity of a non-spherical joint. When in kinematic mode, the joint moves according to a motion profile that respects maximum acceleration and jerk values. In dynamic and velocity control mode, the controller is instructed about the desired velocity

## Synopsis

```lua
sim.setJointTargetVelocity(int objectHandle, float targetVelocity, float[] motionParams = {})
```

```python
sim.setJointTargetVelocity(int objectHandle, float targetVelocity, float[] motionParams = [])
```

## Parameters

- **objectHandle**: handle of the joint object
- **targetVelocity**: target velocity of the joint
- **motionParams**: when the joint is in kinematic mode: the maximum allowed acceleration and jerk. When in dynamic mode with motion profile control enabled: the maximum allowed acceleration and jerk. Can be None/nil for default values. See also [joint.maxVelAccelJerk](../sim-2/property_joint_maxVelAccelJerk.md)

## Return values

No return values.

## See also

- [sim.getJointTargetVelocity](simGetJointTargetVelocity.md)
