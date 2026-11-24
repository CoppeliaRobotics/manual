# simGetShapeColor

Retrieves the color of a shape

## Synopsis

```cpp
int simGetShapeColor(int shapeHandle, const char* colorName, int colorComponent, float* rgbData)
```

## Parameters

- **shapeHandle**: handle of the shape
- **colorName**: name of a color. If a name is provided, a specific color component will be retrieved (e.g. if a shape is a compound shape. Can be nullptr. If colorName is *@compound*, then rgb data for every component of a compound shape will be returned (in that case make sure to have enough space in *rgbData*, e.g. via [shape.meshes](../sim-2/property_shape_meshes.md))
- **colorComponent**: [color component](../apiConstants-1.md#colorComponents).
- **rgbData**: (output): red, green and blue components of the color (3 values), or the transparency value (1 value)

## Return values

- -1 if operation was not successful. 0 if the color name was not found in the shape. Otherwise, the operation was successful

## See also

- [rendering related functions](../apiFunctions-1.md#rendering)
