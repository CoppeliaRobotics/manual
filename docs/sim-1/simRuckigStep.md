# sim.ruckigStep

Executes a call to the [Ruckig online trajectory generator](https://github.com/pantor/ruckig#readme). The Ruckig online trajectory generator provides instantaneous trajectory generation capabilities for motion control systems. This function steps forward a trajectory generation algorithm previously prepared via [sim.ruckigPos](simRuckigPos.md) or [sim.ruckigVel](simRuckigVel.md)

## Synopsis

```lua
int result, float[] newPosVelAccel, float synchronizationTime = sim.ruckigStep(int handle,
                                                                               float cycleTime)
```

```python
int result, list newPosVelAccel, float synchronizationTime = sim.ruckigStep(int handle,
                                                                            float cycleTime)
```

## Parameters

- **handle**: handle of the object created via [sim.ruckigPos](simRuckigPos.md) or [sim.ruckigVel](simRuckigVel.md).
- **cycleTime**: cycle time or simulation step. Should always be a multiple of the base cycle time

## Return values

- **result**: return value of the update function in the motion library:

    - 1: Result::Finished (final state reached)
    - 0: Result::Working (final state not yet reached)
    - -100: Result::ErrorInvalidInput
    - -101: Result::ErrorTrajectoryDuration
    - -110: Result::ErrorExecutionTimeCalculation
    - -111: Result::ErrorSynchronizationCalculation
- **newPosVelAccel**: new positions, velocities and accelerations, i.e. [p0 ... pn v0 ... vn a0 ... an]
