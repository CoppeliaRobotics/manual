# sim.handleGraph

Handles a graph object (i.e. records another value for each curve, given that such value was provided via [sim.setGraphStreamValue](simSetGraphStreamValue.md)

## Synopsis

```lua
sim.handleGraph(int graphHandle, float time)
```

```python
sim.handleGraph(int graphHandle, float time)
```

## Parameters

- **graphHandle**: handle of the graph object.
- **time**: time where next value will be recorded at, usually the simulation time

## Return values

No return values.

## See also

- [functions related to graphs](../apiFunctions-1.md#graphs)
