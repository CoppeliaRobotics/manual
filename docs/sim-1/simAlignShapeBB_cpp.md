# simAlignShapeBB

Reorients the bounding box of a shape, while keeping the shape frame in place. The shape's inertia properties are unaffected

## Synopsis

```cpp
int simAlignShapeBB(int shapeHandle, const double* pose)
```

## Parameters

- **shapeHandle**: handle of the shape
- **pose**: pose describing the new orientation of the shape's bounding box. The pose is expressed as [x y z qx qy qz qw], where the positional part is ignored. A nullptr pose, or a pose containing only zeros will align the bounding box with the mesh's natural bounding box

## Return values

- -1 if operation was not successful. 0 if the bounding box could not be reoriented (the bounding box of primitive shapes cannot be reoriented), otherwise 1.

## See also

- [simRelocateShapeFrame](simRelocateShapeFrame_cpp.md)
