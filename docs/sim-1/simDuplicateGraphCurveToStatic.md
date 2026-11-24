# sim.duplicateGraphCurveToStatic

Duplicates a graph stream or curve, and freezes it

## Synopsis

```lua
int staticCurveId = sim.duplicateGraphCurveToStatic(int graphHandle, int curveId,
                                                    string staticCurveName)
```

```python
int staticCurveId = sim.duplicateGraphCurveToStatic(int graphHandle, int curveId,
                                                    string staticCurveName)
```

## Parameters

- **graphHandle**: handle of the graph
- **curveId**: id of the stream or curve
- **staticCurveName**: name of the new static stream/curve

## Return values

- **staticCurveId**: id of the created static stream or curve

## See also

- [functions related to graphs](../apiFunctions-1.md#graphs)
