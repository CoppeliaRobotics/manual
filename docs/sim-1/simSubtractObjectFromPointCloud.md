# sim.subtractObjectFromPointCloud

Removes an object from a [point cloud](../pointClouds.md), as a subtraction

## Synopsis

```lua
int totalPointCnt = sim.subtractObjectFromPointCloud(int pcHandle, int objectHandle, int options,
                                                     float tolerance)
```

```python
int totalPointCnt = sim.subtractObjectFromPointCloud(int pcHandle, int objectHandle, int options,
                                                     float tolerance)
```

## Parameters

- **pcHandle**: handle of the point cloud
- **objectHandle**: handle of the object to subtract. Only potentially [measurable objects](../measurableObjects.md) are supported
- **options**: reserved. Set to 0
- **tolerance**: distance used as a tolerance value

## Return values

- **totalPointCnt**: total number of points in the point cloud

## See also

- [sim.insertPointsIntoPointCloud](simInsertPointsIntoPointCloud.md)
- [sim.insertObjectIntoPointCloud](simInsertObjectIntoPointCloud.md)
- [sim.removePointsFromPointCloud](simRemovePointsFromPointCloud.md)
- [point cloud related functions](../apiFunctions-1.md#pointCloud)
