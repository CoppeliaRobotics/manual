# sim.setStepping

Enables or disables the stepping operation mode for a threaded script. If enabled, then the current script has to trigger each simulation step explicitly, via [sim.step](simStep.md). Is applied cumulatively, i.e. if the stepping operation mode is enabled n times, it needs to be disabled n times to return to the initial state

(Lua specific: in stepping operation mode, automatic thread interruptions, i.e. preemptive threading, is supressed)

## Synopsis

```lua
int prevStepLevel = sim.setStepping(bool enable / int desiredStepLevel)
```

```python
int prevStepLevel = sim.setStepping(bool enable)
```

## Parameters

- **enable**: enable state of thread interruption
- **desiredStepLevel**: the desired level of thread interruption

## Return values

- **prevStepLevel**: previous level of thread interruption. When 0, thread interruption was not enabled previously

## See also

- [thread related functions](../apiFunctions-1.md#threads)
