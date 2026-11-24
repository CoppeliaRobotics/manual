# simGetClosestPosOnPath

Returns the position or distance along a path that is closest to a specified point in space

## Synopsis

```cpp
double simGetClosestPosOnPath(const double* path, int pathSize, const double* pathLengths,
                              const double* absPt)
```

## Parameters

- **path**: path, specified in row-major order, with x/y/z values for each path point
- **pathSize**: size/length of the path pointer
- **pathLengths**: lengths of a path. Each path point should have a corresponding length value (as the distance from the path's first point, along the path). See also[sim.getPathLengths](simGetPathLengths.md).
- **absPt**: point in 3D space

## Return values

- position/distance along the path

## See also

- [path related functions](../apiFunctions-1.md#paths)
