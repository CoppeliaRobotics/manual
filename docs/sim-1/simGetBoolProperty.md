# sim.getBoolProperty

Fetches a boolean property

## Synopsis

```lua
bool propertyState = sim.getBoolProperty(int target, string propertyName, map options = {})
```

```python
bool propertyState = sim.getBoolProperty(int target, string propertyName, dict options = {})
```

## Parameters

- **target**: target item
- **propertyName**: property name
- **options**: an optional map. Set options.noError to true for silent errors

## Return values

- **propertyState**: property value

## See also

- [properties](../properties.md)
