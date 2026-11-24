# simSetShapeColor

Sets the color of a shape

## Synopsis

```cpp
int simSetShapeColor(int shapeHandle, char* colorName, int colorComponent, float* rgbData)
```

## Parameters

- **shapeHandle**: handle of the shape
- **colorName**: name of a color. Can be nullptr, but if a name is provided, only shapes (or sub-entities of them) with a same color name will be modified. If colorName is *@compound*, then all individual colors of a compound shape can be set at once.
- **colorComponent**: [color component](../apiConstants-1.md#colorComponents)
- **rgbData**: red, green and blue components of the color (3 values), or the transparency value (1 value)

## Return values

- -1 if operation was not successful

## See also

- [rendering related functions](../apiFunctions-1.md#rendering)
