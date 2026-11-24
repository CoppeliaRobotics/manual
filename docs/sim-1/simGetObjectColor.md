# sim.getObjectColor

Retrieves the color of a scene object

## Synopsis

```lua
float[3] rgbData = sim.getObjectColor(int objectHandle, int index, int colorComponent)
```

```python
list rgbData = sim.getObjectColor(int objectHandle, int index, int colorComponent)
```

## Parameters

- **objectHandle**: handle of the object
- **index**: zero-based index of the color, if the object has several colors
- **colorComponent**: [color component](../apiConstants-1.md#colorComponents)

## Return values

- **rgbData**: red, green and blue components of the color (3 values)

## See also

- [rendering related functions](../apiFunctions-1.md#rendering)
