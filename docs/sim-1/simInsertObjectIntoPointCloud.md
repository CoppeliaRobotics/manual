# sim.insertObjectIntoPointCloud

Inserts an object into a [point cloud](../pointClouds.md), as points

## Synopsis

```lua
int totalPointCnt = sim.insertObjectIntoPointCloud(int pointCloudHandle, int objectHandle,
                                                   int options, float gridSize, int[] color = nil,
                                                   float duplicateTolerance = nil)
```

```python
int totalPointCnt = sim.insertObjectIntoPointCloud(int pointCloudHandle, int objectHandle,
                                                   int options, float gridSize, list color = None,
                                                   float duplicateTolerance = None)
```

## Parameters

- **pointCloudHandle**: handle of the point cloud
- **objectHandle**: handle of the object to insert. Only potentially [collidable objects](../collidableObjects.md) are supported
- **options**: reserved. Set to 0
- **gridSize**: when a shape is inserted, it will first be converted to an OC tree with a given grid or voxel size
- **color**: array containing an RGB triplet, specifying the red, green and blue color components (0 - 255). Can be None/nil.
- **duplicateTolerance**: a minimum distance tolerance value that is used to avoid duplicate points

## Return values

- **totalPointCnt**: the total number of points in the point cloud

## See also

- [sim.insertPointsIntoPointCloud](simInsertPointsIntoPointCloud.md)
- [point cloud related functions](../apiFunctions-1.md#pointCloud)
