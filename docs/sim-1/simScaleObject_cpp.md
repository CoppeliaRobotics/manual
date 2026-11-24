# simScaleObject

Scales specified objects in a non-isometric fashion, if possible. Only non-compound shapes can be non-isometrically scaled. Some primitive shapes can have some constraints between their axes

## Synopsis

```cpp
int simScaleObject(int objectHandle, double xScale, double yScale, double zScale, int options)
```

## Parameters

- **objectHandle**: handle of the object to scale
- **xScale/yScale/zScale**: scaling factors along the object's x, y and z-axis
- **options**: keep at 0

## Return values

- -1 if operation was not successful

## See also

- [size and scaling functions](../apiFunctions-1.md#size)
