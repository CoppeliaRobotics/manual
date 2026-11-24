# sim.setAutoYieldDelay

Allows specifying a thread interruption or yield delay, that will be automatically enforced by the system (preemptive threading). By default this value is 2 ms

## Synopsis

```lua
sim.setAutoYieldDelay(float dt)
```

```python
sim.setAutoYieldDelay(float dt)
```

## Parameters

- **dt**: desired execution time, before an interruption or yield occurs

## Return values

No return values.

## See also

- [thread related functions](../apiFunctions-1.md#threads)
