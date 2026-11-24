# sim.getVector3Property

Fetches a vector3 property (double[3])

## Synopsis

```lua
float[3] propertyState = sim.getVector3Property(int target, string propertyName, map options = {})
```

```python
list propertyState = sim.getVector3Property(int target, string propertyName, dict options = {})
```

## Parameters

- **target**: target item
- **propertyName**: property name
- **options**: an optional map. Set options.noError to true for silent errors

## Return values

- **propertyState**: property value

## See also

- [properties](../properties.md)
