# simRemovePointsFromPointCloud

Removes points from a [point cloud](../pointClouds.md). When a point cloud doesn't use an OC tree calculation structure, then individual points cannot be removed, only all points can be removed in that case

## Synopsis

```cpp
int simRemovePointsFromPointCloud(int pointCloudHandle, int options, const double* pts, int ptCnt,
                                  double tolerance, void* reserved)
```

## Parameters

- **pointCloudHandle**: handle of the point cloud
- **options**: bit-coded:

    - bit0 set (1): specified points are relative to the point cloud reference frame, otherwise they are relative to the world reference frame
- **pts**: pointer to the point positions specified as x/y/z coordinates. Set to nullptr to remove all points
- **ptCnt**: number of point coordinates contained in pts
- **tolerance**: distance used as a tolerance value
- **reserved**: reserved for future extensions. Set to nullptr

## Return values

- -1 if operation was not successful, otherwise the total number of points in the point cloud

## See also

- [simInsertPointsIntoPointCloud](simInsertPointsIntoPointCloud_cpp.md)
- [simSetPointCloudOptions](simSetPointCloudOptions_cpp.md)
- [point cloud related functions](../apiFunctions-1.md#pointCloud)
