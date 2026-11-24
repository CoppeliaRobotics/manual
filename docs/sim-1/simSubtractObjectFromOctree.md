# sim.subtractObjectFromOctree

Removes an object from an [OC tree](../octrees.md), as voxel subtractions

## Synopsis

```lua
int totalVoxelCnt = sim.subtractObjectFromOctree(int octreeHandle, int objectHandle, int options)
```

```python
int totalVoxelCnt = sim.subtractObjectFromOctree(int octreeHandle, int objectHandle, int options)
```

## Parameters

- **octreeHandle**: handle of the OC tree
- **objectHandle**: handle of the object to subtract. Only potentially [collidable objects](../collidableObjects.md) are supported
- **options**: reserved. Set to 0

## Return values

- **totalVoxelCnt**: total number of voxels in the OC tree

## See also

- [sim.insertObjectIntoOctree](simInsertObjectIntoOctree.md)
- [sim.removeVoxelsFromOctree](simRemoveVoxelsFromOctree.md)
- [OC tree related functions](../apiFunctions-1.md#octree)
