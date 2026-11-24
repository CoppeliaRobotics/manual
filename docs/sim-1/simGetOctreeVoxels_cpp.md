# simGetOctreeVoxels

Retrieves voxel positions from an [OC tree](../octrees.md)

## Synopsis

```cpp
const double* simGetOctreeVoxels(int octreeHandle, int* ptCnt, void* reserved)
```

## Parameters

- **octreeHandle**: handle of the OC tree
- **ptCnt**: a pointer receiving the number of voxels contained in the returned pointer.
- **reserved**: reserved for future extensions. Set to nullptr

## Return values

- nullptr if operation was not successful or if the OC tree doesn't contain any voxels. Otherwise a pointer to the voxel [x y z] positions, relative to the OC tree reference frame

## See also

- [OC tree related functions](../apiFunctions-1.md#octree)
