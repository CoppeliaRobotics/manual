# sim.getFloatArrayProperty

Fetches a float array property (double[])

## Synopsis

```lua
float[] propertyState = sim.getFloatArrayProperty(int target, string propertyName, map options = {})
```

```python
list propertyState = sim.getFloatArrayProperty(int target, string propertyName, dict options = {})
```

## Parameters

- **target**: target item
- **propertyName**: property name
- **options**: an optional map. Set options.noError to true for silent errors

## Return values

- **propertyState**: property value

## See also

- [properties](../properties.md)
