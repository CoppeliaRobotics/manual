# simInsertVoxelsIntoOctree

Inserts voxels into an [OC tree](../octrees.md). Each voxel will store a color and a tag value

## Synopsis

```cpp
int simInsertVoxelsIntoOctree(int octreeHandle, int options, const double* pts, int ptCnt,
                              const unsigned char* color, const unsigned int* tag, void* reserved)
```

## Parameters

- **octreeHandle**: handle of the OC tree
- **options**: bit-coded:

    - bit0 set (1): specified points are relative to the OC tree reference frame, otherwise they are relative to the world reference frame
    - bit1 set (2): the color array contains one RGB triple per point, and the tag array contains one value per point. Otherwise it the color array contains a single RGB triple, and the tag array contains a single value.
- **pts**: pointer to the voxel positions specified as x/y/z coordinates
- **ptCnt**: number of point coordinates contained in pts
- **color**: pointer to one or several RGB triplets, specifying the red, green and blue color components (0-255). Can be nullptr.
- **tag**: pointer to one or several uint32 values, which are user-defined values. Can be nullptr, and should be nullptr if *color* is nullptr.
- **reserved**: reserved for future extensions. Set to nullptr

## Return values

- -1 if operation was not successful, otherwise the total number of voxels in the OC tree

## See also

- [simRemoveVoxelsFromOctree](simRemoveVoxelsFromOctree_cpp.md)
- [OC tree related functions](../apiFunctions-1.md#octree)
