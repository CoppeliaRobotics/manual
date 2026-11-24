# sim.setQuaternionProperty

Sets a quaternion property (double[4]: qx, qy, qz, qw)

## Synopsis

```lua
sim.setQuaternionProperty(int target, string propertyName, float[4] propertyState, map options = {})
```

```python
sim.setQuaternionProperty(int target, string propertyName, list propertyState, dict options = {})
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
