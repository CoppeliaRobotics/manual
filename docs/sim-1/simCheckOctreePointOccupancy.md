# sim.checkOctreePointOccupancy

Checks whether the provided points collide with the [OC tree](../octrees.md) voxels

## Synopsis

```lua
int res, int tag, int locLow, int locHigh = sim.checkOctreePointOccupancy(int octreeHandle,
                                                                          int options, float[] points)
```

```python
int res, int tag, int locLow, int locHigh = sim.checkOctreePointOccupancy(int octreeHandle,
                                                                          int options, list points)
```

## Parameters

- **octreeHandle**: handle of the OC tree
- **options**: bit-coded:

    - bit0 set (1): specified points are relative to the OC tree reference frame, otherwise they are relative to the world reference frame
- **points**: points specified as x/y/z coordinates

## Return values

- **res**: 0 if the points do not collide with the voxels, 1 if the points collide with the voxels
- **tag**: tag value of the voxel that collides with a single point. If several points are tested, this return value should be ignored
- **loc**: value specifying the location of the voxel that collides with a single point. If several points are tested, then this return value should be ignored

## See also

- [OC tree related functions](../apiFunctions-1.md#octree)
