# sim.removeVoxelsFromOctree

Removes voxels from an [OC tree](../octrees.md)

## Synopsis

```lua
int totalVoxelCnt = sim.removeVoxelsFromOctree(int octreeHandle, int options, float[] points)
```

```python
int totalVoxelCnt = sim.removeVoxelsFromOctree(int octreeHandle, int options, list points)
```

## Parameters

- **octreeHandle**: handle of the OC tree
- **options**: bit-coded:

    - bit0 set (1): specified points are relative to the OC tree reference frame, otherwise they are relative to the world reference frame
- **points**: voxel positions specified as x/y/z coordinates. Set to None/nil to remove all voxels

## Return values

- **totalVoxelCnt**: total number of voxels in the OC tree

## See also

- [sim.insertVoxelsIntoOctree](simInsertVoxelsIntoOctree.md)
- [OC tree related functions](../apiFunctions-1.md#octree)
