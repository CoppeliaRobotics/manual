# simRuckigStep

Executes a call to the [Ruckig online trajectory generator](https://github.com/pantor/ruckig#readme). The Ruckig online trajectory generator provides instantaneous trajectory generation capabilities for motion control systems. This function steps forward a trajectory generation algorithm previously prepared via [sim.ruckigPos](simRuckigPos.md) or [sim.ruckigVel](simRuckigVel.md)

## Synopsis

```cpp
int simRuckigStep(int handle, double cycleTime, double* newPos, double* newVel, double* newAccel,
                  double* syncTime, double* reserved1, int* reserved2)
```

## Parameters

- **handle**: handle of the object created via [simRuckigPos](simRuckigPos.md) or [simRuckigVel](simRuckigVel.md).
- **cycleTime**: cycle time or simulation step. Should always be a multiple of the base cycle time
- **newPos**: new position
- **newVel**: new velocity
- **newAccel**: new acceleration
- **syncTime**: synchronization time (output). This is the time needed to reach the desired state. This time does not include the cycle time of the current call to sim.RuckigStep)
- **reserved1**: reserved. Set to nullptr
- **reserved2**: reserved. Set to nullptr

## Return values

- -1 or -2 in case of an immediate error, otherwise the return value of the update function in the motion library:

  - 1: Finished (final state reached)
  - 0: Working (final state not yet reached)
  - -100: ErrorInvalidInput
  - -101: ErrorTrajectoryDuration
  - -110: ErrorExecutionTimeCalculation
  - -111: ErrorSynchronizationCalculation
