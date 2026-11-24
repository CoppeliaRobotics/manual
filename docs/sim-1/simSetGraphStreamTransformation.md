# sim.setGraphStreamTransformation

Applies a transformation to a graph stream

## Synopsis

```lua
sim.setGraphStreamTransformation(int graphHandle, int streamId, int trType, float mult = 1.0,
                                 float off = 0.0, int movingAvgPeriod = 1)
```

```python
sim.setGraphStreamTransformation(int graphHandle, int streamId, int trType, float mult = 1.0,
                                 float off = 0.0, int movingAvgPeriod = 1)
```

## Parameters

- **graphHandle**: handle of the graph
- **streamId**: id of the stream
- **trType**: [stream transformation](../apiConstants-1.md#streamTransformations)
- **mult**: multiplication factor
- **off**: an offset
- **movingAvgPeriod**: moving average period. Set to 1 for no moving average

## Return values

No return values.

## See also

- [functions related to graphs](../apiFunctions-1.md#graphs)
