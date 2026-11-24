# sim.getIntArrayProperty

Fetches an int array property (int[])

## Synopsis

```lua
int[] propertyState = sim.getIntArrayProperty(int target, string propertyName, map options = {})
```

```python
list propertyState = sim.getIntArrayProperty(int target, string propertyName, dict options = {})
```

## Parameters

- **target**: target item
- **propertyName**: property name
- **options**: an optional map. Set options.noError to true for silent errors

## Return values

- **propertyState**: property value

## See also

- [properties](../properties.md)
