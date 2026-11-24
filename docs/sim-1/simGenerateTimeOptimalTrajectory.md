# sim.generateTimeOptimalTrajectory

Generates a time optimal trajectory, based on the TOPPRA library

## Synopsis

```lua
float[] outP, float[] times, int scriptHandle = sim.generateTimeOptimalTrajectory(float[] path,
                                                                float[] pathLengths,
                                                                float[] minMaxVel,
                                                                float[] minMaxAccel,
                                                                int trajPtSamples = 1000,
                                                                string boundaryCondition = 'not-a-knot',
                                                                float timeout = 5,
                                                                int calculationScriptHandle = nil)
```

```python
list outP, list times, int scriptHandle = sim.generateTimeOptimalTrajectory(list path, list pathLengths,
                                                          list minMaxVel, list minMaxAccel,
                                                          int trajPtSamples = 1000,
                                                          string boundaryCondition = 'not-a-knot',
                                                          float timeout = 5,
                                                          int calculationScriptHandle = None)
```

## Parameters

- **path**: path, specified in row-major order, e.g. a path containing two 3D positions would be [x1 y1 z1 x2 y2 z2]
- **pathLengths**: lengths of a path. Each path point should have a corresponding length value (as the distance from the path's first point, along the path). See also [sim.getPathLengths](simGetPathLengths.md).
- **minMaxVel**: minimum and maximum allowed velocity, for each dimension/axis, e.g. {xmin,xmax,ymin,ymax,zmin,zmax}
- **minMaxAccel**: minimum and maximum allowed acceleration, for each dimension/axis, e.g. [xmin xmax ymin ymax zmin zmax]
- **trajPtSamples**: desired number of path points/configurations
- **boundaryCondition**: boundary condition
- **timeout**: a timeout duration
- **calculationScriptHandle**: optional. Can indicate a script handle returned in a previous call to this function, including -1 to indicate that the created calculation script should be returned for future reuse

## Return values

- **outP**: generated path points
- **times**: generated times corresponding to path points
- **scriptHandle**: the handle of the calculation script for reuse in a subsequent call to this function

## See also

- [path related functions](../apiFunctions-1.md#paths)
