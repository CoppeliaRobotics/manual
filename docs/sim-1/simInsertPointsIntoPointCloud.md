# sim.insertPointsIntoPointCloud

Inserts points into a [point cloud](../pointClouds.md)

## Synopsis

```lua
int totalPointCnt = sim.insertPointsIntoPointCloud(int pcHandle, int options, float[] points,
                                                   int[] color = nil, float duplicateTolerance = nil)
```

```python
int totalPointCnt = sim.insertPointsIntoPointCloud(int pcHandle, int options, list points,
                                                   list color = None,
                                                   float duplicateTolerance = None)
```

## Parameters

- **pcHandle**: handle of the point cloud, can be combined with sim.handleflag_codedstring, when one wishes to provide point data as a float buffer, and color data as a char buffer
- **options**: bit-coded:

    - bit0 set (1): specified points are relative to the point cloud reference frame, otherwise they are relative to the world reference frame
    - bit1 set (2): the color array contains one RGB triple per point. Otherwise it contains a single RGB triple
- **points**: array of point positions specified as x/y/z coordinates
- **color**: array of one or several RGB triplets, specifying the red, green and blue color components (0-255). Can be None/nil
- **duplicateTolerance**: a minimum distance tolerance value that is used to avoid duplicate points

## Return values

- **totalPointCnt**: the total number of points in the point cloud

## See also

- [sim.removePointsFromPointCloud](simRemovePointsFromPointCloud.md)
- [point cloud related functions](../apiFunctions-1.md#pointCloud)
