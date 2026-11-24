# simInsertObjectIntoPointCloud

Inserts an object into a [point cloud](../pointClouds.md), as points

## Synopsis

```cpp
int simInsertObjectIntoPointCloud(int pointCloudHandle, int objectHandle, int options,
                                  double gridSize, const unsigned char* color, void* optionalValues)
```

## Parameters

- **pointCloudHandle**: handle of the point cloud
- **objectHandle**: handle of the object to insert. Only potentially [collidable objects](../collidableObjects.md) are supported
- **options**: reserved. Set to 0
- **gridSize**: when a shape is inserted, it will first be converted to an OC tree with a given grid or voxel size.
- **color**: pointer to one RGB triple, specifying the red, green and blue color components (0-255). Can be nullptr.
- **optionalValues**: can be used to specify additional parameters, or set to nullptr for default parameter values:

    - ((int*)optionalValues)[0]: integer value that is bit coded. Each bit indicates which additional parameter will be taken into account:
    - ((float*)optionalValues)[1]: **duplicateTolerance**: a minimum distance tolerance value that is used to avoid duplicate points. To have this parameter taken into account, set bit0 to 1 in ((int*)optionalValues)[0]. Point insertion is slower when the duplicate tolerance is &gt; then 0.0

## Return values

- -1 if operation was not successful, otherwise the total number of points in the point cloud

## See also

- [simInsertPointsIntoPointCloud](simInsertPointsIntoPointCloud_cpp.md)
- [point cloud related functions](../apiFunctions-1.md#pointCloud)
