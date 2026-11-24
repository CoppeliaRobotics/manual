# sim.groupShapes

Groups (or merges) several shapes into a [compound shape](../shapes.md) (or [simple shape](../shapes.md))

## Synopsis

```lua
int shapeHandle = sim.groupShapes(int[] shapeHandles, bool merge = false)
```

```python
int shapeHandle = sim.groupShapes(list shapeHandles, bool merge = False)
```

## Parameters

- **shapeHandles**: handles of the shapes to be grouped or merged. The last handle represents the shape that will accept the other shapes
- **merge**: whether the shapes should be merged or grouped

## Return values

- **shapeHandle**: the handle of the resulting compound shape, which is the last shape in *shapeHandles*

## See also

- [sim.ungroupShape](simUngroupShape.md)
- [sim.alignShapeBB](simAlignShapeBB.md)
- [sim.relocateShapeFrame](simRelocateShapeFrame.md)
