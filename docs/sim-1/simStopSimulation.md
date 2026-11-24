# sim.stopSimulation

Requests a stop of the running simulation

## Synopsis

```lua
sim.stopSimulation(bool wait = false)
```

```python
sim.stopSimulation(bool wait = False)
```

## Parameters

- **wait**: if true, will wait until the simulation state is sim.simulation_stopped, otherwise only triggers a stop request. If true, calling script cannot be the main- or a simulation script, and should run threaded.

## Return values

No return values.

## See also

- [sim.startSimulation](simStartSimulation.md)
- [sim.pauseSimulation](simPauseSimulation.md)
- [sim.getSimulationState](simGetSimulationState.md)
- [simulation state diagram](../simulation.md)
