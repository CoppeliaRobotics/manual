# simGetFloatArrayProperty

Fetches a float array property (double[])

## Synopsis

```cpp
double* simGetFloatArrayProperty(long long target, const char* propertyName, int* propertyLength)
```

## Parameters

- **target**: target item
- **propertyName**: property name
- **propertyLength**: property length

## Return values

- pointer to property value, if successful. The memory has to be released with [simReleaseBuffer](simReleaseBuffer_cpp.md)

## See also

- [properties](../properties.md)
