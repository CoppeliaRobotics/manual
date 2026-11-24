# sim.intersectPointsWithPointCloud

Removes points from a [point cloud](../pointClouds.md), that do not intersect with the provided points (i.e. the result in the point cloud will be the intersection between the two sets of points). When a point cloud doesn't use an OC tree calculation structure, then this operation cannot be performed

## Synopsis

```lua
int totalPointCnt = sim.intersectPointsWithPointCloud(int pcHandle, int options, float[] points,
                                                      float tolerance)
```

```python
int totalPointCnt = sim.intersectPointsWithPointCloud(int pcHandle, int options, list points,
                                                      float tolerance)
```

## Parameters

- **pcHandle**: handle of the point cloud
- **options**: bit-coded:

    - bit0 set (1): specified points are relative to the point cloud reference frame, otherwise they are relative to the world reference frame
- **points**: array of point positions specified as x/y/z coordinates
- **tolerance**: distance used as a tolerance value

## Return values

- **totalPointCnt**: the total number of points in the point cloud

## See also

- [sim.insertPointsIntoPointCloud](simInsertPointsIntoPointCloud.md)
- [sim.setPointCloudOptions](simSetPointCloudOptions.md)
- [point cloud related functions](../apiFunctions-1.md#pointCloud)
