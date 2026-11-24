# sim.getStringProperty

Fetches a string property (text)

## Synopsis

```lua
string propertyState = sim.getStringProperty(int target, string propertyName, map options = {})
```

```python
string propertyState = sim.getStringProperty(int target, string propertyName, dict options = {})
```

## Parameters

- **target**: target item
- **propertyName**: property name
- **options**: an optional map. Set options.noError to true for silent errors

## Return values

- **propertyState**: property value

## See also

- [properties](../properties.md)
