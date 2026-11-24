# simRelocateShapeFrame

Repositions and reorients the reference frame of a shape, while keeping the mesh in place. The shape's inertia properties are unaffected.

## Synopsis

```cpp
int simRelocateShapeFrame(int shapeHandle, const double* pose)
```

## Parameters

- **shapeHandle**: handle of the shape
- **pose**: pose for the shape's reference frame. The pose is expressed as [x y z qx qy qz qw]. A nullptr pose or a pose containing only zeros will relocate the frame to the center of the mesh's bounding box

## Return values

- -1 if operation was not successful. 0 if the frame could not be relocated (the frame of primitive shapes cannot be relocated), otherwise 1.

## See also

- [simAlignShapeBB](simAlignShapeBB_cpp.md)
