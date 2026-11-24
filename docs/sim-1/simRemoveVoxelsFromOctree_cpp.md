# simRemoveVoxelsFromOctree

Removes voxels from an [OC tree](../octrees.md)

## Synopsis

```cpp
int simRemoveVoxelsFromOctree(int octreeHandle, int options, const double* pts, int ptCnt,
                              void* reserved)
```

## Parameters

- **octreeHandle**: handle of the OC tree
- **options**: bit-coded:

    - bit0 set (1): specified points are relative to the OC tree reference frame, otherwise they are relative to the world reference frame
- **pts**: pointer to the voxel positions specified as x/y/z coordinates. Set to nullptr to remove all voxels
- **ptCnt**: number of point coordinates contained in pts
- **reserved**: reserved for future extensions. Set to nullptr

## Return values

- -1 if operation was not successful, otherwise the total number of voxels in the OC tree

## See also

- [simInsertVoxelsIntoOctree](simInsertVoxelsIntoOctree_cpp.md)
- [OC tree related functions](../apiFunctions-1.md#octree)
