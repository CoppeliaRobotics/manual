# simUngroupShape

Ungroups a compound shape into several [shapes](../shapes.md)

## Synopsis

```cpp
int* simUngroupShape(int shapeHandle, int* shapeCount)
```

## Parameters

- **shapeHandle**: handles of the shape you wish to ungroup. If you specify for this argument (-2-handleOfShape), then the shape will be divided instead of ungrouped
- **shapeCount**: (output): size of the returned buffer

## Return values

- a pointer to an array holding the handles of the resulting shapes, or nullptr in case of an error. The user is in charge of releasing the array buffer with [simReleaseBuffer](simReleaseBuffer_cpp.md).

## See also

- [simGroupShapes](simGroupShapes_cpp.md)
- [simAlignShapeBB](simAlignShapeBB_cpp.md)
- [simRelocateShapeFrame](simRelocateShapeFrame_cpp.md)
