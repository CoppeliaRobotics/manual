# sim.getPathInterpolatedConfig

Returns an interpolated configuration from a path

## Synopsis

```lua
float[] config = sim.getPathInterpolatedConfig(float[] path, float[] pathLengths, float t,
                                               map method = {type = 'linear', strength = 1.0,
                                               forceOpen = false}, int[] types = nil)
```

```python
list config = sim.getPathInterpolatedConfig(list path, list pathLengths, float t,
                                            dict method = {'type': 'linear', 'strength': 1.0,
                                            'forceOpen': False}, list types = None)
```

## Parameters

- **path**: the path, specified in row-major order, e.g. a path containing two 3D poses (position+quaternion) would be [x1 y1 z1 qx1 qy1 qz1 qw1 x2 y2 z2 qx2 qy2 qz2 qw2]
- **pathLengths**: the lengths of a path. Each path point should have a corresponding length value (as the distance from the path's first point, along the path). See also [sim.getPathLengths](simGetPathLengths.md).
- **t**: the distance from the beginning of the path, where the interpolation point should be picked from
- **method**: an optional map specifying the type of interpolation (linear or quadraticBezier), whether the path should be considered as open, even if the first and last path points overlap, and the bezier strength (0.05-1.0)
- **types**: an optional array specifying the type of each configuration value/dimension: 0=cartesian value, 1=2pi-cyclic value, 2=quaternion value. e.g. a configuration representing 3D poses should use a types argument [0 0 0 2 2 2 2], a configuration representing revolute and cyclic joints should use a types argument [1 1 1 ...]

## Return values

- **config**: the interpolated path configuration

## See also

- [path related functions](../apiFunctions-1.md#paths)
