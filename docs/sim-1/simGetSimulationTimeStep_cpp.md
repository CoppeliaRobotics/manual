# simGetSimulationTimeStep

Retrieves the simulation time step (the simulation time (i.e. not real-time) that passes at each main script simulation pass). This value might not be constant for a given simulation.

## Synopsis

```cpp
double simGetSimulationTimeStep()
```

## Parameters

No parameters.

## Return values

- negative value (-1.0) if operation not successful, otherwise the simulation time step
