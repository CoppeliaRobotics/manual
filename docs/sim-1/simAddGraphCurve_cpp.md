# simAddGraphCurve

Adds or updates a graph curve. A graph curve is persistent, but can be removed with [sim.destroyGraphCurve](simDestroyGraphCurve.md)

## Synopsis

```cpp
int simAddGraphCurve(int graphHandle, const char* curveName, int dim, const int* streamIds,
                     const double* defaultValues, const char* unitStr, int int options,
                     const float* color, int curveWidth)
```

## Parameters

- **graphHandle**: handle of the graph
- **curveName**: name of the curve
- **dim**: dimension of the curve. Valid values are 2 or 3
- **streamIds**: a pointer to 2 or 3 graph streams (x/y curves require 2 stream IDs, xyz curves require 3 stream IDs). Indicate -1 for a missing stream, in which case a default value will be used instead
- **defaultValues**: a pointer to 2 or 3 default values
- **unitStr**: string describing the unit of the curve. Can be nullptr
- **options**: bit-coded: bit0 is not used. If bit1 is set (2), the label is not visible. If bit2 is set (4), the points are not linked.
- **color**: rgb-triplet, with values in [0.0-1.0], indicating the color of the stream. Can be nullptr
- **curveWidth**: the width of an xyz curve

## Return values

- -1 if operation was not successful, otherwise the id of the created/updated curve

## See also

- [functions related to graphs](../apiFunctions-1.md#graphs)
