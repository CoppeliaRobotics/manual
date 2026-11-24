# sim.setObjectColor

Sets the color of a scene object

## Synopsis

```lua
sim.setObjectColor(int objectHandle, int index, int colorComponent, float[3] rgbData)
```

```python
sim.setObjectColor(int objectHandle, int index, int colorComponent, list rgbData)
```

## Parameters

- **objectHandle**: handle of the object
- **index**: zero-based index of the color, if the object has several colors
- **colorComponent**: [color component](../apiConstants-1.md#colorComponents)
- **rgbData**: red, green and blue components of the color (3 values)

## Return values

No return values.

## See also

- [rendering related functions](../apiFunctions-1.md#rendering)
