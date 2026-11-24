# sim.getProperty

Convenience functon to fetch a property

## Synopsis

```lua
any propertyState = sim.getProperty(int target, string propertyName, map options = {})
```

```python
any propertyState = sim.getProperty(int target, string propertyName, dict options = {})
```

## Parameters

- **target**: target item
- **propertyName**: property name
- **options**: an optional map. Set options.noError to true for silent errors

## Return values

- **propertyState**: property value

## See also

- [properties](../properties.md)
