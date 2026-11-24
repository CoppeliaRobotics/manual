# sim.setBufferProperty

Sets a buffer property

## Synopsis

```lua
sim.setBufferProperty(int target, string propertyName, buffer propertyState, map options = {})
```

```python
sim.setBufferProperty(int target, string propertyName, bytes propertyState, dict options = {})
```

## Parameters

- **target**: target item
- **propertyName**: property name
- **propertyState**: property value
- **options**: an optional map. Set options.noError to true for silent errors

## Return values

No return values.

## See also

- [properties](../properties.md)
- [packing/unpacking related functions](../apiFunctions-1.md#packing)
