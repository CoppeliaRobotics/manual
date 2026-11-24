# simGetPropertyName

Fetches the name of a property, based on an index

## Synopsis

```cpp
char* simGetPropertyName(long long target, int index, SPropertyOptions* options)
```

## Parameters

- **target**: target item
- **index**: property index
- **options**: options (e.g. to specify a name prefix), can be nullptr

## Return values

- pointer to property name, if successful. The memory has to be released with [simReleaseBuffer](simReleaseBuffer_cpp.md)

## See also

- [properties](../properties.md)
