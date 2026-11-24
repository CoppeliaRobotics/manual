# sim.getPoseProperty

Fetches a pose property (double[7]: x, y, z, qx, qy, qz, qw)

## Synopsis

```lua
float[7] propertyState = sim.getPoseProperty(int target, string propertyName, map options = {})
```

```python
list propertyState = sim.getPoseProperty(int target, string propertyName, dict options = {})
```

## Parameters

- **target**: target item
- **propertyName**: property name
- **options**: an optional map. Set options.noError to true for silent errors

## Return values

- **propertyState**: property value

## See also

- [properties](../properties.md)
