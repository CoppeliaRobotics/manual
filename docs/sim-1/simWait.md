# sim.wait

Waits for a certain amount of time

## Synopsis

```lua
float deltaTimeLeft = sim.wait(float deltaTime, bool simulationTime = true)
```

```python
float deltaTimeLeft = sim.wait(float deltaTime, bool simulationTime = True)
```

## Parameters

- **deltaTime**: minimum time duration to wait
- **simulationTime**: indicates whether we want to wait in terms of simulation- or real-time

## Return values

- **deltaTimeLeft**: "wait resolution" of this function is the simulation time step, and the sim.wait command may overshoot the requested waiting time. deltaTimeLeft is the negative overshoot time. If the function was called at simulation time X, and the function returned at simulation time Y, then deltaTimeLeft is deltaTime-(Y-X). deltaTimeLeft is also memorized internally on a thread-basis and used as compensation or correction factor in subsequent blocking commands. deltaTimeLeft is 0 if the simulationTime argument was false
