# sim.getVector2Property

Fetches a vector2 property (double[2])

## Synopsis

```lua
float[2] propertyState = sim.getVector2Property(int target, string propertyName, map options = {})
```

```python
list propertyState = sim.getVector2Property(int target, string propertyName, dict options = {})
```

## Parameters

- **target**: target item
- **propertyName**: property name
- **options**: an optional map. Set options.noError to true for silent errors

## Return values

- **propertyState**: property value

## See also

- [properties](../properties.md)
