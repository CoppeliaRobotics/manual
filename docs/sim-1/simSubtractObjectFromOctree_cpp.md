# simSubtractObjectFromOctree

Removes an object from an [OC tree](../octrees.md), as voxel subtractions

## Synopsis

```cpp
int simSubtractObjectFromOctree(int octreeHandle, int objectHandle, int options, void* reserved)
```

## Parameters

- **octreeHandle**: handle of the OC tree
- **objectHandle**: handle of the object to subtract. Only potentially [collidable objects](../collidableObjects.md) are supported
- **options**: reserved. Set to 0
- **reserved**: reserved for future extensions. Set to nullptr

## Return values

- -1 if operation was not successful, otherwise the total number of voxels in the OC tree

## See also

- [simInsertObjectIntoOctree](simInsertObjectIntoOctree_cpp.md)
- [simRemoveVoxelsFromOctree](simRemoveVoxelsFromOctree_cpp.md)
- [OC tree related functions](../apiFunctions-1.md#octree)
