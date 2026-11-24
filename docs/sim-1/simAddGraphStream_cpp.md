# simAddGraphStream

Adds or updates a graph stream. A graph stream is persistent, but can be removed with [sim.destroyGraphCurve](simDestroyGraphCurve.md)

## Synopsis

```cpp
int simAddGraphStream(int graphHandle, const char* streamName, const char* unitStr, int options,
                      const float* color, double cyclicRange)
```

## Parameters

- **graphHandle**: handle of the graph
- **streamName**: name of the stream
- **unitStr**: string describing the unit of the stream. Can be nullptr
- **options**: bit-coded: if bit0 is set (1), the stream is not visible. If bit1 is set (2), the label is not visible. If bit2 is set (4), the points are not linked.
- **color**: rgb-triplet, with values in [0.0-1.0], indicating the color of the stream. Can be nullptr
- **cyclicRange**: can be used with cyclic values (e.g. angles) for correct data interpretation during [stream data transformation](simSetGraphStreamTransformation.md). Set to 0 if not used

## Return values

- -1 if operation was not successful, otherwise the id of the created/updated stream

## See also

- [functions related to graphs](../apiFunctions-1.md#graphs)
