# simRuckigPos

Executes a call to the [Ruckig online trajectory generator](https://github.com/pantor/ruckig#readme). The Ruckig online trajectory generator provides instantaneous trajectory generation capabilities for motion control systems. This function prepares a position-based trajectory generation object, that can then be calculated with [sim.ruckigStep](simRuckigStep.md). When this object is not needed anymore, remove it with [sim.ruckigRemove](simRuckigRemove.md)

## Synopsis

```cpp
int simRuckigPos(int dofs, double baseCycleTime, int flags, const double* currentPos,
                 const double* currentVel, const double* currentAccel, const double* maxVel,
                 const double* maxAccel, const double* maxJerk, const bool* selection,
                 const double* targetPos, const double* targetVe, double* reserved1, int* reserved2l)
```

## Parameters

- **dofs**: number of degrees of freedom (n).
- **baseCycleTime**: smallest expected cycle time. The cycle time should always be a multiple of baseCycleTime. Use a value of 0.0001 (0.1ms).
- **flags**: [Ruckig flags](../apiConstants-1.md#ruckigFunctions). -1 for default flags.
- **currentPos**: current position (one value for each DoF)
- **currentVel**: current velocity (one value for each DoF)
- **currentAccel**: current acceleration (one value for each DoF)
- **maxVel**: maximum allowed velocity (one value for each DoF, i.e. [maxV_1 ... maxV_n]). If sim.ruckig_minvel is specified in flags, then maxVel should contain [maxV_1 ... maxV_n minV_1 ... minV_n]
- **maxAccel**: maximum allowed acceleration (one value for each DoF, i.e. [maxA_1 ... maxA_n]). If sim.ruckig_minaccel is specified in flags, then maxAccel should contain [maxA_1 ... maxA_n minA_1 ... minA_n]
- **maxJerk**: maximum allowed jerk (one value for each DoF)
- **selection**: selection vector (one value for each DoF). For a default behaviour, fill the vector with non-zero values.
- **targetPos**: target position (one value for each DoF)
- **targetVel**: target velocity (one value for each DoF)
- **reserved1**: reserved. Set to nullptr
- **reserved2**: reserved. Set to nullptr

## Return values

- A negative value in case of an error, otherwise the handle of the created object

## See also

- [simRuckigVel](simRuckigVel_cpp.md)
- [sim.moveToPose](simMoveToPose.md)
- [sim.moveToConfig](simMoveToConfig.md)
