# sim.createHeightfieldShape

Creates a heightfield [shape](../shapes.md)

## Synopsis

```lua
int objectHandle = sim.createHeightfieldShape(int options, float shadingAngle, int xPointCount,
                                              int yPointCount, float xSize, float[] heights)
```

```python
int objectHandle = sim.createHeightfieldShape(int options, float shadingAngle, int xPointCount,
                                              int yPointCount, float xSize, list heights)
```

## Parameters

- **options**: bit-coded options:

    - bit0 set (1): back faces are culled
    - bit1 set (2): overlay mesh is visible
    - bit2 set (4): a simple shape is generated instead of a heightfield
    - bit3 set (8): the heightfield is not respondable
- **shadingAngle**: shading angle
- **xPointCount/yPointCount**: number of rows and lines of the heightfield.
- **xSize**: length of the x side of the heightfield
- **heights**: array of xPointCount*yPointCount height values

## Return values

- **objectHandle**: handle of the newly created shape

## See also

- [sim.createPrimitiveShape](simCreatePrimitiveShape.md)
- [sim.createShape](simCreateShape.md)
