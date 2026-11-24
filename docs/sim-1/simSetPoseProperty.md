# sim.setPoseProperty

Sets a pose property (double[7]: x, y, z, qx, qy, qz, qw)

## Synopsis

```lua
sim.setPoseProperty(int target, string propertyName, float[7] propertyState, map options = {})
```

```python
sim.setPoseProperty(int target, string propertyName, list propertyState, dict options = {})
```

## Parameters

- **target**: target item
- **propertyName**: property name
- **propertyState**: property value
- **options**: an optional map. Set options.noError to true for silent errors

## Return values

No return values.

## See also

- [properties](../properties.md)
