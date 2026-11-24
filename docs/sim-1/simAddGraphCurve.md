# sim.addGraphCurve

Adds or updates a graph curve. A graph curve is persistent, but can be removed with [sim.destroyGraphCurve](simDestroyGraphCurve.md)

## Synopsis

```lua
int curveId = sim.addGraphCurve(int graphHandle, string curveName, int dim, int[] streamIds,
                                float[] defaultValues, string unitStr, int options = 0,
                                float[3] color = {0, 1, 0}, int curveWidth = 2)
```

```python
int curveId = sim.addGraphCurve(int graphHandle, string curveName, int dim, list streamIds,
                                list defaultValues, string unitStr, int options = 0,
                                list color = [0 1, 0], int curveWidth = 2)
```

## Parameters

- **graphHandle**: handle of the graph
- **curveName**: name of the curve
- **dim**: dimension of the curve. Valid values are 2 or 3
- **streamIds**: array of 2 or 3 graph streams (x/y curves require 2 stream IDs, xyz curves require 3 stream IDs). Indicate -1 for a missing stream, in which case a default value will be used instead
- **defaultValues**: array of 2 or 3 default values
- **unitStr**: string describing the unit of the curve. Can be None/nil
- **options**: bit-coded:

    - bit0 is not used.
    - If bit1 is set (2), the label is not visible
    - If bit2 is set (4), the points are not linked
- **color**: rgb-triplet, with values between 0.0 and 1.0, indicating the color of the stream. Can be None/nil
- **curveWidth**: the width of an xyz curve

## Return values

- **curveId**: id of the created/updated curve

## See also

- [functions related to graphs](../apiFunctions-1.md#graphs)
