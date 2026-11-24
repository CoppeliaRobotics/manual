# sim.getShapeBB

Returns the size and relative pose of a shape's bounding box

## Synopsis

```lua
float[3] size, float[7] pose = sim.getShapeBB(int shapeHandle)
```

```python
list size, list pose = sim.getShapeBB(int shapeHandle)
```

## Parameters

- **shapeHandle**: handle of the shape

## Return values

- **size**: size array [Sx Sy Sz]
- **pose**: pose array: [x y z qx qy qz qw]. The pose is relative to the shape's pose

## See also

- [sim.getObjectPose](simGetObjectPose.md)
- [positions and orientations](../positionOrientationTransformation.md)
