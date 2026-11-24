# sim.ruckigVel

Executes a call to the [Ruckig online trajectory generator](https://github.com/pantor/ruckig#readme). The Ruckig online trajectory generator provides instantaneous trajectory generation capabilities for motion control systems. This function prepares a velocity-based trajectory generation object, that can then be calculated with [sim.ruckigStep](simRuckigStep.md). When this object is not needed anymore, remove it with [sim.ruckigRemove](simRuckigRemove.md)

## Synopsis

```lua
int handle = sim.ruckigVel(int dofs, float baseCycleTime, int flags, float[] currentPosVelAccel,
                           float[] maxAccelJerk, int[] selection, float[] targetVel)
```

```python
int handle = sim.ruckigVel(int dofs, float baseCycleTime, int flags, list currentPosVelAccel,
                           list maxAccelJerk, list selection, list targetVel)
```

## Parameters

- **dofs**: number of degrees of freedom (n).
- **baseCycleTime**: smallest expected cycle time. The cycle time should always be a multiple of baseCycleTime. Use a value of 0.0001 (0.1ms).
- **flags**: [Ruckig flags](../apiConstants-1.md#ruckigFunctions). -1 for default flags.
- **currentPosVelAccel**: current position, velocity and acceleration: [pos_1 ... pos_n vel_1 ... vel_n accel_1 ... accel_n] (one value for each DoF)
- **maxAccelJerk**: maximum allowed acceleration and jerk: [maxA_1 ... maxA_n maxJ_1 ... maxJ_n]. If sim.ruckig_minaccel is specified in flags, then maxAccelJerk should contain following additional values: [minA_1 ... minA_n]
- **selection**: selection vector (one value for each DoF). For a default behaviour, fill the vector with non-zero values.
- **targetVel**: target velocity (one value for each DoF)

## Return values

- **handle**: the handle of the created object

## See also

- [sim.ruckigPos](simRuckigPos.md)
