# simCreatePointCloud

Creates an empty [point cloud](../pointClouds.md)

## Synopsis

```cpp
int simCreatePointCloud(double maxVoxelSize, int maxPtCntPerVoxel, int options, double pointSize,
                        void* reserved)
```

## Parameters

- **maxVoxelSize**: maximum size of the OC tree voxels containing points
- **maxPtCntPerVoxel**: maximum number of points allowed in a same OC tree voxel
- **options**: bit-coded:

    - bit0 set (1): points have random colors
    - bit1 set (2): show OC tree structure
    - bit2 set (4): reserved. keep unset
    - bit3 set (8): do not use an OC tree structure. When enabled, point cloud operations are limited, and point clouds will not be [collidable](../collidableObjects.md), [measurable](../measurableObjects.md) or [detectable](../detectableObjects.md) anymore, but adding points will be much faster
    - bit4 set (16): color is emissive
- **pointSize**: size of the points, in pixels
- **reserved**: reserved for future extensions. Set to nullptr

## Return values

- -1 if operation was not successful, otherwise the handle of the point cloud

## See also

- [simRemoveObjects](simRemoveObjects_cpp.md)
- [point cloud functions](../apiFunctions-1.md#pointCloud)
