# sim.handleDynamics

Handles the dynamics functionality in a scene

## Synopsis

```lua
int result = sim.handleDynamics(float deltaTime)
```

```python
int result = sim.handleDynamics(float deltaTime)
```

## Parameters

- **deltaTime**: simulation time step, i.e. [sim.getSimulationTimeStep](simGetSimulationTimeStep.md)()

## Return values

- **result**: 0 if the sepcified physics engine could not be found, otherwise the number of calculation steps performed by the physics engine.
