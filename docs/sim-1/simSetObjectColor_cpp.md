# simSetObjectColor

Sets the color of a scene object

## Synopsis

```cpp
int simSetObjectColor(int objectHandle, int index, int colorComponent, float* rgbData)
```

## Parameters

- **objectHandle**: handle of the object
- **index**: zero-based index of the color, if the object has several colors
- **colorComponent**: [color component](../apiConstants-1.md#colorComponents)
- **rgbData**: red, green and blue components of the color (3 values)

## Return values

- -1 if operation was not successful, 0 if the index was not found in the object, 1 otherwise.

## See also

- [rendering related functions](../apiFunctions-1.md#rendering)
