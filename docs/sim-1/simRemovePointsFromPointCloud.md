# sim.removePointsFromPointCloud

Removes points from a [point cloud](../pointClouds.md). When a point cloud doesn't use an OC tree calculation structure, then individual points cannot be removed, only all points can be removed in that case

## Synopsis

```lua
int totalPointCnt = sim.removePointsFromPointCloud(int pointCloudHandle, int options, float[] points,
                                                   float tolerance)
```

```python
int totalPointCnt = sim.removePointsFromPointCloud(int pointCloudHandle, int options, list points,
                                                   float tolerance)
```

## Parameters

- **pointCloudHandle**: handle of the point cloud
- **options**: bit-coded:

    - bit0 set (1): specified points are relative to the point cloud reference frame, otherwise they are relative to the world reference frame
- **points**: point positions specified as x/y/z coordinates. Set to None/nil to remove all points
- **tolerance**: distance used as a tolerance value

## Return values

- **totalPointCnt**: total number of points in the point cloud

## See also

- [sim.insertPointsIntoPointCloud](simInsertPointsIntoPointCloud.md)
- [sim.setPointCloudOptions](simSetPointCloudOptions.md)
- [point cloud related functions](../apiFunctions-1.md#pointCloud)
