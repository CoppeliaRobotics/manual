# sim.getColorProperty

Fetches a color property (float[3])

## Synopsis

```lua
float[3] propertyState = sim.getColorProperty(int target, string propertyName, map options = {})
```

```python
list propertyState = sim.getColorProperty(int target, string propertyName, dict options = {})
```

## Parameters

- **target**: target item
- **propertyName**: property name
- **options**: an optional map. Set options.noError to true for silent errors

## Return values

- **propertyState**: property value

## See also

- [properties](../properties.md)
