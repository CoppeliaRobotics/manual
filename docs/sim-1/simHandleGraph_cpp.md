# simHandleGraph

Handles a graph object (i.e. records another value for each curve, given that such value was provided via [sim.setGraphStreamValue](simSetGraphStreamValue.md)

## Synopsis

```cpp
int simHandleGraph(int graphHandle, double time)
```

## Parameters

- **graphHandle**: handle of the graph object.
- **time**: the time where next value will be recorded at, usually the simulation time.

## Return values

- -1 if operation was not successful

## See also

- [functions related to graphs](../apiFunctions-1.md#graphs)
