# sim.scheduleExecution

Schedules execution of a function

## Synopsis

```lua
int id = sim.scheduleExecution(func f, any[] args, float timePoint, bool simTime = false)
```

```python
int id = sim.scheduleExecution(func f, list args, float timePoint, bool simTime = False)
```

## Parameters

- **f**: function to call
- **args**: arguments to the function
- **timePoint**: time when the function should execute
- **simTime**: simulation or real-time scheduling

## Return values

- **id**: id of the scheduled execution function

## See also

- [sim.cancelScheduledExecution](simCancelScheduledExecution.md)
- [sim.getSystemTime](simGetSystemTime.md)
- [sim.getSimulationTime](simGetSimulationTime.md)
