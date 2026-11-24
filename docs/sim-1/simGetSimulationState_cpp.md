# simGetSimulationState

Retrieves current [simulation state](../apiConstants-1.md#simulationStatus)

## Synopsis

```cpp
int simGetSimulationState()
```

## Parameters

No parameters.

## Return values

- The current state of the simulation (sim.simulation_stopped, sim.simulation_paused, etc. (see the [simulation state values](../apiConstants-1.md#simulationStatus))), or -1 in case of an error

## See also

- [simulation state diagram](../simulation.md)
