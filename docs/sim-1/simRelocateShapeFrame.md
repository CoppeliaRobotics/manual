# sim.relocateShapeFrame

Repositions and reorients the reference frame of a shape, while keeping the mesh in place. The shape's inertia properties are unaffected.

## Synopsis

```lua
bool result = sim.relocateShapeFrame(int shapeHandle, float[7] pose)
```

```python
bool result = sim.relocateShapeframe(int shapeHandle, list pose)
```

## Parameters

- **shapeHandle**: handle of the shape
- **pose**: pose for the shape's reference frame. The pose is expressed as [x y z qx qy qz qw]. A pose containing only zeros relocates the frame to the center of the mesh's bounding box

## Return values

- **result**: 0 if the frame could not be relocated (the frame of primitive shapes cannot be relocated), otherwise 1.

## See also

- [sim.alignShapeBB](simAlignShapeBB.md)
