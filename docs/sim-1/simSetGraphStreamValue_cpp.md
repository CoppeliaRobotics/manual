# simSetGraphStreamValue

Sets the next value to be recorded for a graph stream

## Synopsis

```cpp
int simSetGraphStreamValue(int graphHandle, int streamId, double value)
```

## Parameters

- **graphHandle**: handle of the graph object
- **streamId**: id of the stream
- **value**: value to set. Omitting to set a value for a corresponding [sim.handleGraph](simHandleGraph.md) call, then the data point will be missing.

## Return values

- -1 if operation was not successful

## See also

- [functions related to graphs](../apiFunctions-1.md#graphs)
