# sim.getPropertyInfo

Fetches information about a specific property

## Synopsis

```lua
int type, int flags, string description = sim.getPropertyInfo(int target, string propertyName
                                                              map options = {})
```

```python
int type, int flags, string description = sim.getPropertyInfo(int target, string propertyName
                                                              dict options = {})
```

## Parameters

- **target**: target item
- **propertyName**: property name
- **options**: an optional map. Set options.shortInfoTxt to true to fetch a short version of the description text

## Return values

- **type**: [property type](../apiConstants-1.md#propertyTypes)
- **flags**: [property flags](../apiConstants-1.md#propertyFlags)
- **description**: property description

## See also

- [properties](../properties.md)
