# simInsertPointsIntoPointCloud

Inserts points into a [point cloud](../pointClouds.md)

## Synopsis

```cpp
int simInsertPointsIntoPointCloud(int pointCloudHandle, int options, const double* pts, int ptCnt,
                                  const unsigned char* color, void* optionalValues)
```

## Parameters

- **pointCloudHandle**: the handle of the point cloud
- **options**: bit-coded:

    - bit0 set (1): specified points are relative to the point cloud reference frame, otherwise they are relative to the world reference frame
    - bit1 set (2): the color array contains one RGB triple per point. Otherwise it contains a single RGB triple
- **pts**: a pointer to the point positions specified as x/y/z coordinates
- **ptCnt**: the number of point coordinates contained in pts
- **color**: a pointer to one or several RGB triplets, specifying the red, green and blue color components (0-255). Can be nullptr.
- **optionalValues**: can be used to specify additional parameters, or set to nullptr for default parameter values:

    - ((int*)optionalValues)[0]: an integer value that is bit coded. Each bit indicates which additional parameter will be taken into account:
    - ((float*)optionalValues)[1]: **duplicateTolerance**: a minimum distance tolerance value that is used to avoid duplicate points. To have this parameter taken into account, set bit0 to 1 in ((int*)optionalValues)[0]. Point insertion is slower when the duplicate tolerance is &gt; then 0.0

## Return values

- -1 if operation was not successful, otherwise the total number of points in the point cloud

## See also

- [simRemovePointsFromPointCloud](simRemovePointsFromPointCloud_cpp.md)
- [point cloud related functions](../apiFunctions-1.md#pointCloud)
