# sim.getBufferProperty

Fetches a buffer property

## Synopsis

```lua
buffer propertyState = sim.getBufferProperty(int target, string propertyName, map options = {})
```

```python
bytes propertyState = sim.getBufferProperty(int target, string propertyName, dict options = {})
```

## Parameters

- **target**: target item
- **propertyName**: property name
- **options**: an optional map. Set options.noError to true for silent errors

## Return values

- **propertyState**: property value

## See also

- [properties](../properties.md)
- [packing/unpacking related functions](../apiFunctions-1.md#packing)
