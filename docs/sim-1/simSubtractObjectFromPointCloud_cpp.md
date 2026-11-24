# simSubtractObjectFromPointCloud

Removes an object from a [point cloud](../pointClouds.md), as a subtraction

## Synopsis

```cpp
int simSubtractObjectFromPointCloud(int pointCloudHandle, int objectHandle, int options,
                                    double tolerance, void* reserved)
```

## Parameters

- **pointCloudHandle**: handle of the point cloud
- **objectHandle**: handle of the object to subtract. Only potentially [measurable objects](../measurableObjects.md) are supported
- **options**: reserved. Set to 0
- **tolerance**: distance used as a tolerance value
- **reserved**: reserved for future extensions. Set to nullptr

## Return values

- -1 if operation was not successful, otherwise the total number of points in the point cloud

## See also

- [simInsertPointsIntoPointCloud](simInsertPointsIntoPointCloud_cpp.md)
- [simInsertObjectIntoPointCloud](simInsertObjectIntoPointCloud_cpp.md)
- [simRemovePointsFromPointCloud](simRemovePointsFromPointCloud_cpp.md)
- [point cloud related functions](../apiFunctions-1.md#pointCloud)
