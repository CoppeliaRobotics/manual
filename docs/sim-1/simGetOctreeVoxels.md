# sim.getOctreeVoxels

Retrieves voxel positions from an [OC tree](../octrees.md)

## Synopsis

```lua
float[] voxels = sim.getOctreeVoxels(int octreeHandle)
```

```python
list voxels = sim.getOctreeVoxels(int octreeHandle)
```

## Parameters

- **octreeHandle**: handle of the OC tree

## Return values

- **voxels**: the voxel [x y z] positions, relative to the OC tree reference frame

## See also

- [OC tree related functions](../apiFunctions-1.md#octree)
