# simGroupShapes

Groups (or merges) several shapes into a [compound shape](../shapes.md) (or [simple shape](../shapes.md))

## Synopsis

```cpp
int simGroupShapes(const int* shapeHandles, int shapeCount)
```

## Parameters

- **shapeHandles**: the handles of the shapes to be grouped or merged. The last handle represents the shape that will accept the other shapes.
- **shapeCount**: the size of the **shapeHandles** array. A negative number indicates that we want to merge the shapes instead of grouping them.

## Return values

- -1 if operation was not successful. Otherwise the handle of the resulting compound shape, which is the last shape in shapeHandles.

## See also

- [simUngroupShape](simUngroupShape_cpp.md)
- [simAlignShapeBB](simAlignShapeBB_cpp.md)
- [simRelocateShapeFrame](simRelocateShapeFrame_cpp.md)
