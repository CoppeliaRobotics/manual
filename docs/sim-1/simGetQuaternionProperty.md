# sim.getQuaternionProperty

Fetches a quaternion property (double[4]: qx, qy, qz, qw)

## Synopsis

```lua
float[4] propertyState = sim.getQuaternionProperty(int target, string propertyName, map options = {})
```

```python
list propertyState = sim.getQuaternionProperty(int target, string propertyName, dict options = {})
```

## Parameters

- **target**: target item
- **propertyName**: property name
- **options**: an optional map. Set options.noError to true for silent errors

## Return values

- **propertyState**: property value

## See also

- [properties](../properties.md)
