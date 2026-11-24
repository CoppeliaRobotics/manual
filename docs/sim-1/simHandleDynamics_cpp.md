# simHandleDynamics

Handles the dynamics functionality in a scene

## Synopsis

```cpp
int simHandleDynamics(double deltaTime)
```

## Parameters

- **deltaTime**: simulation time step, i.e. [simGetSimulationTimeStep](simGetSimulationTimeStep.md)()

## Return values

- -1 if operation was not successful. 0 if the sepcified physics engine could not be found, otherwise, the number of calculation steps performed by the physics engine.
