# simInsertObjectIntoOctree

Inserts an object into an [OC tree](../octrees.md), as voxels. Each voxel will store a color and a tag value

## Synopsis

```cpp
int simInsertObjectIntoOctree(int octreeHandle, int objectHandle, int options,
                              const unsigned char* color, unsigned int tag, void* reserved)
```

## Parameters

- **octreeHandle**: handle of the OC tree
- **objectHandle**: handle of the object to insert. Only potentially [collidable objects](../collidableObjects.md) are supported
- **options**: reserved. Set to 0
- **color**: pointer to one RGB triple, specifying the red, green and blue color components (0-255). Can be nullptr.
- **tag**: uint32 value, which is user-defined.
- **reserved**: reserved for future extensions. Set to nullptr

## Return values

- -1 if operation was not successful, otherwise the total number of voxels in the OC tree

## See also

- [simSubtractObjectFromOctree](simSubtractObjectFromOctree_cpp.md)
- [simInsertVoxelsIntoOctree](simInsertVoxelsIntoOctree_cpp.md)
- [OC tree related functions](../apiFunctions-1.md#octree)
