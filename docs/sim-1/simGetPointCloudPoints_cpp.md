# simGetPointCloudPoints

Retrieves point positions from a [point cloud](../pointClouds.md)

## Synopsis

```cpp
const double* simGetPointCloudPoints(int pointCloudHandle, int* ptCnt, void* reserved)
```

## Parameters

- **pointCloudHandle**: handle of the point cloud
- **ptCnt**: pointer receiving the number of points contained in the returned pointer.
- **reserved**: reserved for future extensions. Set to nullptr

## Return values

- nullptr if operation was not successful or if the point cloud doesn't contain any points. Otherwise a pointer to the point [x y z] positions, relative to the point cloud reference frame

## See also

- [point cloud related functions](../apiFunctions-1.md#pointCloud)
