# simCreateHeightfieldShape

Creates a heightfield [shape](../shapes.md)

## Synopsis

```cpp
int simCreateHeightfieldShape(int options, double shadingAngle, int xPointCount, int yPointCount,
                              double xSize, const double* heights)
```

## Parameters

- **options**: bit-coded options:

    - bit0 set (1): back faces are culled
    - bit1 set (2): overlay mesh is visible
    - bit2 set (4): a simple shape is generated instead of a heightfield
    - bit3 set (8): the heightfield is not respondable
- **shadingAngle**: the shading angle
- **xPointCount/yPointCount**: the number of rows and lines of the heightfield.
- **xSize**: the length of the x side of the heightfield
- **heights**: a pointer to xPointCount*yPointCount height values.

## Return values

- -1 if operation was not successful, otherwise the handle of the newly created shape

## See also

- [simCreatePrimitiveShape](simCreatePrimitiveShape_cpp.md)
- [simCreateShape](simCreateShape_cpp.md)
