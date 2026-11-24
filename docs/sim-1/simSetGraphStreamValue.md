# sim.setGraphStreamValue

Sets the next value to be recorded for a graph stream

## Synopsis

```lua
sim.setGraphStreamValue(int graphHandle, int streamId, float value)
```

```python
sim.setGraphStreamValue(int graphHandle, int streamId, float value)
```

## Parameters

- **graphHandle**: handle of the graph object
- **streamId**: id of the stream
- **value**: value to set. Omitting to set a value for a corresponding [sim.handleGraph](simHandleGraph.md) call, then the data point will be missing.

## Return values

No return values.

## See also

- [functions related to graphs](../apiFunctions-1.md#graphs)
