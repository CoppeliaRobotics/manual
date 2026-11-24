# simGetStringProperty

Fetches a string property (text)

## Synopsis

```cpp
char* simGetStringProperty(long long target, const char* propertyName)
```

## Parameters

- **target**: target item
- **propertyName**: property name

## Return values

- pointer to property value, if successful. The memory has to be released with [simReleaseBuffer](simReleaseBuffer_cpp.md)

## See also

- [properties](../properties.md)
