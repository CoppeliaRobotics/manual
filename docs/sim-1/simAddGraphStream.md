# sim.addGraphStream

Adds or updates a graph stream. A graph stream is persistent, but can be removed with [sim.destroyGraphCurve](simDestroyGraphCurve.md)

## Synopsis

```lua
int streamId = sim.addGraphStream(int graphHandle, string streamName, string unitStr = '',
                                  int options = 0, float[3] color = {1, 0, 0}, cyclicRange = 0)
```

```python
int streamId = sim.addGraphStream(int graphHandle, string streamName, string unitStr = '',
                                  int options = 0, list color = [1, 0, 0], cyclicRange = 0)
```

## Parameters

- **graphHandle**: handle of the graph
- **streamName**: name of the stream
- **unitStr**: string describing the unit of the stream. Can be None/nil
- **options**: bit-coded:

    - if bit0 is set (1), the stream is not visible
    - if bit1 is set (2), the label is not visible
    - if bit2 is set (4), the points are not linked
- **color**: rgb-triplet, with values between 0.0 and 1.0, indicating the color of the stream. Can be None/nil
- **cyclicRange**: can be used with cyclic values (e.g. angles) for correct data interpretation during [stream data transformation](simSetGraphStreamTransformation.md). Set to 0 if not used

## Return values

- **streamId**: id of the created/updated stream

## See also

- [functions related to graphs](../apiFunctions-1.md#graphs)
