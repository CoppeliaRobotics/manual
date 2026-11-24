# sim.ruckigPos

Executes a call to the [Ruckig online trajectory generator](https://github.com/pantor/ruckig#readme). The Ruckig online trajectory generator provides instantaneous trajectory generation capabilities for motion control systems. This function prepares a position-based trajectory generation object, that can then be calculated with [sim.ruckigStep](simRuckigStep.md). When this object is not needed anymore, remove it with [sim.ruckigRemove](simRuckigRemove.md)

## Synopsis

```lua
int handle = sim.ruckigPos(int dofs, float baseCycleTime, int flags, float[] currentPosVelAccel,
                           float[] maxVelAccelJerk, int[] selection, float[] targetPosVel)
```

```python
int handle = sim.ruckigPos(int dofs, float baseCycleTime, int flags, list currentPosVelAccel,
                           list maxVelAccelJerk, list selection, list targetPosVel)
```

## Parameters

- **dofs**: number of degrees of freedom (n).
- **baseCycleTime**: smallest expected cycle time. The cycle time should always be a multiple of baseCycleTime. Use a value of 0.0001 (0.1ms).
- **flags**: [Ruckig flags](../apiConstants-1.md#ruckigFunctions). -1 for default flags.
- **currentPosVelAccel**: current position, velocity and acceleration: [pos_1 ... pos_n vel_1 ... vel_n accel_1 ... accel_n] (one value for each DoF)
- **maxVelAccelJerk**: maximum allowed velocity, acceleration and jerk: [maxV_1 ... maxV_n maxA_1 ... maxA_n maxJ_1 ... maxJ_n]. If sim.ruckig_minvel is specified in flags, then maxVelAccelJerk should contain following additional values: [minV_1 ... minV_n]. If sim.ruckig_minaccel is specified in flags, then maxVelAccelJerk should contain following additional values: [minA_1 ... minA_n]
- **selection**: selection vector (one value for each DoF). For a default behaviour, fill the vector with non-zero values.
- **targetPosVel**: target position and velocity: [tPos_1 ... tPos_n tVel_1 ... tVel_n]

## Return values

- **handle**: the handle to the created object

## See also

- [sim.ruckigVel](simRuckigVel.md)
- [sim.moveToPose](simMoveToPose.md)
- [sim.moveToConfig](simMoveToConfig.md)
