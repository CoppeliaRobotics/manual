# simDuplicateGraphCurveToStatic

Duplicates a graph stream or curve, and freezes it

## Synopsis

```cpp
int simDuplicateGraphCurveToStatic(int graphHandle, int curveId, const char* staticCurveName)
```

## Parameters

- **graphHandle**: handle of the graph
- **curveId**: the id of the stream or curve
- **staticCurveName**: name of the new static stream/curve

## Return values

- -1 if operation was not successful, otherwise the id of the created static stream or curve

## See also

- [functions related to graphs](../apiFunctions-1.md#graphs)
