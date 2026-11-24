# simCheckOctreePointOccupancy

Checks whether the provided points collide with the [OC tree](../octrees.md) voxels

## Synopsis

```cpp
int checkOctreePointOccupancy(int octreeHandle, int options, const double* pts, int ptCnt,
                              unsigned int* tag, unsigned long long int* location, void* reserved)
```

## Parameters

- **octreeHandle**: handle of the OC tree
- **options**: bit-coded:

    - bit0 set (1): specified points are relative to the OC tree reference frame, otherwise they are relative to the world reference frame
- **pts**: pointer to the points specified as x/y/z coordinates
- **ptCnt**: number of points contained in pts
- **tag**: pointer to a tag value, receiving the tag value of the voxel that collides with a single point. If several points are tested, then this pointer is ignored. Can be nullptr.
- **location**: pointer to a uint64 value, which specifies the location of the voxel that collides with a single point. If several points are tested, then this pointer is ignored. Can be nullptr. The location value is coded in following way:

    - bit0 - bit5: the depth level of the voxel in the OC tree structure (1-63).
    - bit6 - bit63: a triple bit-value for each depth level. triple bit-values represent the node location relative to the parent node:
      - 0: (-1,-1,-1)
      - 1: (+1,-1,-1)
      - 2: (-1,+1,-1)
      - 3: (+1,+1,-1)
      - 4: (-1,-1,+1)
      - 5: (+1,-1,+1)
      - 6: (-1,+1,+1)
      - 7: (+1,+1,+1)
- **reserved**: reserved for future extensions. Set to nullptr

## Return values

- -1 if operation was not successful, 0 if the points do not collide with the voxels, 1 if the points collide with the voxels

## See also

- [OC tree related functions](../apiFunctions-1.md#octree)
