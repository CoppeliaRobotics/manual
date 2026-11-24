# sim.insertVoxelsIntoOctree

Inserts voxels into an [OC tree](../octrees.md). Each voxel will store a color and a tag value

## Synopsis

```lua
int totalVoxelCnt = sim.insertVoxelsIntoOctree(int octreeHandle, int options, float[] points,
                                               int[] color = nil, int[] tag = nil)
```

```python
int totalVoxelCnt = sim.insertVoxelsIntoOctree(int octreeHandle, int options, list points,
                                               list color = None, list tag = None)
```

## Parameters

- **octreeHandle**: handle of the OC tree, can be combined with sim.handleflag_codedstring, when one wishes to provide point data as a float buffer, color data as a char buffer and tag as an uint32 buffer
- **options**: bit-coded:

    - bit0 set (1): specified points are relative to the OC tree reference frame, otherwise they are relative to the world reference frame
    - bit1 set (2): the color array contains one RGB triple per point, and the tag array contains one value per point. Otherwise it the color array contains a single RGB triple, and the tag array contains a single value.
- **points**: array of voxel positions specified as x/y/z coordinates
- **color**: array of one or several RGB triplets, specifying the red, green and blue color components (0-255). Can be None/nil
- **tag**: array of one or several uint32 values, which are user-defined values. Can be None/nil

## Return values

- **totalVoxelCnt**: the total number of voxels in the OC tree

## See also

- [sim.removeVoxelsFromOctree](simRemoveVoxelsFromOctree.md)
- [OC tree related functions](../apiFunctions-1.md#octree)
