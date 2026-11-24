# sim.getLongProperty

Fetches an int64 property

## Synopsis

```lua
int propertyState = sim.getLongProperty(int target, string propertyName, map options = {})
```

```python
int propertyState = sim.getLongProperty(int target, string propertyName, dict options = {})
```

## Parameters

- **target**: target item
- **propertyName**: property name
- **options**: an optional map. Set options.noError to true for silent errors

## Return values

- **propertyState**: property value

## See also

- [properties](../properties.md)
