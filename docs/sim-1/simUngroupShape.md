# sim.ungroupShape

Ungroups a compound shape into several [shapes](../shapes.md)

## Synopsis

```lua
int[] shapeHandles = sim.ungroupShape(int shapeHandle)
```

```python
list shapeHandles = sim.ungroupShape(int shapeHandle)
```

## Parameters

- **shapeHandle**: handles of the shape you wish to ungroup. If you specify for this argument (-2-handleOfShape), then the shape will be divided instead of ungrouped

## Return values

- **shapeHandles**: array holding the handles of the resulting shapes

## See also

- [sim.groupShapes](simGroupShapes.md)
- [sim.alignShapeBB](simAlignShapeBB.md)
- [sim.relocateShapeFrame](simRelocateShapeFrame.md)
