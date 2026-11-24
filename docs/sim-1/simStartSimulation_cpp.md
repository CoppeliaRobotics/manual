# simStartSimulation

Requests a start of a simulation (or a resume of a paused simulation)

## Synopsis

```cpp
int simStartSimulation()
```

## Parameters

No parameters.

## Return values

- -1 in case of an error, 0 if the operation could not be performed. &gt;0 in case of success.

## See also

- [simPauseSimulation](simPauseSimulation_cpp.md)
- [simStopSimulation](simStopSimulation_cpp.md)
- [simGetSimulationState](simGetSimulationState_cpp.md)
- [simulation state diagram](../simulation.md)
