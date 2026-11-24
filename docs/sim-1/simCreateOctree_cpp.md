# simCreateOctree

Creates an empty [OC tree](../octrees.md)

## Synopsis

```cpp
int simCreateOctree(double voxelSize, int options, double pointSize, void* reserved)
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
- **reserved**: reserved for future extensions. Set to nullptr

## Return values

- -1 if operation was not successful, otherwise the handle of the OC tree

## See also

- [simRemoveObjects](simRemoveObjects_cpp.md)
- [OC tree related functions](../apiFunctions-1.md#octree)
