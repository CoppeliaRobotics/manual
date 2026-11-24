# simSetGraphStreamTransformation

Applies a transformation to a graph stream

## Synopsis

```cpp
int simSetGraphStreamTransformation(int graphHandle, int streamId, int trType, double mult,
                                    double off, int movingAvgPeriod)
```

## Parameters

- **graphHandle**: handle of the graph
- **streamId**: id of the stream
- **trType**: [stream transformation](../apiConstants-1.md#streamTransformations)
- **mult**: multiplication factor
- **off**: an offset
- **movingAvgPeriod**: moving average period. Set to 1 for no moving average

## Return values

- -1 if operation was not successful

## See also

- [functions related to graphs](../apiFunctions-1.md#graphs)
