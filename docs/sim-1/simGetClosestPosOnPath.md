# sim.getClosestPosOnPath

Returns the position or distance along a path that is closest to a specified point in space

## Synopsis

```lua
float posAlongPath = sim.getClosestPosOnPath(float[] path, float[] pathLengths, float[3] absPt)
```

```python
float posAlongPath = sim.getClosestPosOnPath(list path, list pathLengths, list absPt)
```

## Parameters

- **path**: path, specified in row-major order, with x/y/z values for each path point
- **pathLengths**: lengths of a path. Each path point should have a corresponding length value (as the distance from the path's first point, along the path). See also[sim.getPathLengths](simGetPathLengths.md).
- **absPt**: point in 3D space

## Return values

- **posAlongPath**: position/distance along the path

## See also

- [path related functions](../apiFunctions-1.md#paths)
