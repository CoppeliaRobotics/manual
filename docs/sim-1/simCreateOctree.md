# sim.createOctree

Creates an empty [OC tree](../octrees.md)

## Synopsis

```lua
int handle = sim.createOctree(float voxelSize, int options, float pointSize)
```

```python
int handle = sim.createOctree(float voxelSize, int options, float pointSize)
```

## Parameters

- **voxelSize**: size of the voxels
- **options**: bit-coded:

    - bit0 set (1): voxels have random colors
    - bit1 set (2): show OC tree structure
    - bit2 set (4): show points instead of voxels
    - bit3 set (8): reserved. keep unset
    - bit4 set (16): color is emissive
- **pointSize**: the size of the points in pixels, when voxels are rendered with points

## Return values

- **handle**: handle of the OC tree

## See also

- [sim.removeObjects](simRemoveObjects.md)
- [OC tree related functions](../apiFunctions-1.md#octree)
