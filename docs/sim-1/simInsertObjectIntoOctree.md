# sim.insertObjectIntoOctree

Inserts an object into an [OC tree](../octrees.md), as voxels. Each voxel will store a color and a tag value

## Synopsis

```lua
int totalVoxelCnt = sim.insertObjectIntoOctree(int octreeHandle, int objectHandle, int options,
                                               int[] color = nil, int tag = 0)
```

```python
int totalVoxelCnt = sim.insertObjectIntoOctree(int octreeHandle, int objectHandle, int options,
                                               list color = None, int tag = 0)
```

## Parameters

- **octreeHandle**: handle of the OC tree
- **objectHandle**: handle of the object to insert. Only potentially [collidable objects](../collidableObjects.md) are supported
- **options**: reserved. Set to 0
- **color**: array of RGB triplet, specifying the red, green and blue color components (0 - 255). Can be None/nil
- **tag**: uint32 value, which is user-defined

## Return values

- **totalVoxelCnt**: the total number of voxels in the OC tree

## See also

- [sim.subtractObjectFromOctree](simSubtractObjectFromOctree.md)
- [sim.insertVoxelsIntoOctree](simInsertVoxelsIntoOctree.md)
- [OC tree related functions](../apiFunctions-1.md#octree)
