# sim.getPointCloudPoints

Retrieves point positions from a [point cloud](../pointClouds.md)

## Synopsis

```lua
float[] points = sim.getPointCloudPoints(int pointCloudHandle)
```

```python
list points = sim.getPointCloudPoints(int pointCloudHandle)
```

## Parameters

- **pointCloudHandle**: handle of the point cloud

## Return values

- **points**: the point [x y z] positions, relative to the point cloud reference frame

## See also

- [point cloud related functions](../apiFunctions-1.md#pointCloud)
