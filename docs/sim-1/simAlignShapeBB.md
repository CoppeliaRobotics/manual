# sim.alignShapeBB

Reorients the bounding box of a shape, while keeping the shape frame in place. The shape's inertia properties are unaffected

## Synopsis

```lua
bool result = sim.alignShapeBB(int shapeHandle, float[7] pose)
```

```python
bool result = sim.alignShapeBB(int shapeHandle, list pose)
```

## Parameters

- **shapeHandle**: handle of the shape
- **pose**: pose describing the new orientation of the shape's bounding box. The pose is expressed as [x y z qx qy qz qw], where the positional part is ignored. A pose containing only zeros aligns the bounding box with the mesh's natural bounding box

## Return values

- **result**: 0 if the bounding box could not be reoriented (the bounding box of primitive shapes cannot be reoriented), otherwise 1.

## See also

- [sim.relocateShapeFrame](simRelocateShapeFrame.md)
