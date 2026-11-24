# sim.getShapeColor

Retrieves the color of a shape

## Synopsis

```lua
int result, float[3] rgbData = sim.getShapeColor(int shapeHandle, string colorName,
                                                 int colorComponent)
```

```python
int result, list rgbData = sim.getShapeColor(int shapeHandle, string colorName, int colorComponent)
```

## Parameters

- **shapeHandle**: handle of the shape
- **colorName**: name of a color. If a non-empty name is provided, a specific color component is retrieved (e.g. if a shape is a compound shape. If colorName is *@compound*, then rgb data for every component of a compound shape is returned)
- **colorComponent**: [color component](../apiConstants-1.md#colorComponents)

## Return values

- **result**: 0 if the color name was not found in the shape, 1 otherwise
- **rgbData**: red, green and blue components of the color (3 values), or the transparency value (1 value)

## See also

- [rendering related functions](../apiFunctions-1.md#rendering)
