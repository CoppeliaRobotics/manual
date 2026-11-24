# simGetPropertyInfo

Fetches information about a specific property

## Synopsis

```cpp
int simGetPropertyInfo(long long target, const char* propertyName, SPropertyInfo* infos
                       SPropertyOptions* options)
```

## Parameters

- **target**: target item
- **propertyName**: property name
- **infos**: information about the property (e.g. type, flags, description)
- **options**: options, can be nullptr

## Return values

- 1 in case of success

## See also

- [properties](../properties.md)
