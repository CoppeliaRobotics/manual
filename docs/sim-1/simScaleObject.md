# sim.scaleObject

Scales specified objects in a non-isometric fashion, if possible. Only non-compound shapes can be non-isometrically scaled. Some primitive shapes can have some constraints between their axes

## Synopsis

```lua
sim.scaleObject(int objectHandle, float xScale, float yScale, float zScale, int options = 0)
```

```python
sim.scaleObject(int objectHandle, float xScale, float yScale, float zScale, int options = 0)
```

## Parameters

- **objectHandle**: handle of the object to scale
- **xScale/yScale/zScale**: scaling factors along the object's x, y and z-axis
- **options**: keep at 0

## Return values

No return values.
