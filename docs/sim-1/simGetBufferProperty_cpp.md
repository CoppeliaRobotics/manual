# simGetBufferProperty

Fetches a buffer property

## Synopsis

```cpp
char* simGetBufferProperty(long long target, const char* propertyName, int* bufferLength)
```

## Parameters

- **target**: target item
- **propertyName**: property name
- **bufferLength**: buffer length

## Return values

- pointer to property value, if successful. The memory has to be released with [simReleaseBuffer](simReleaseBuffer_cpp.md)

## See also

- [properties](../properties.md)
- [packing/unpacking related functions](../apiFunctions-1.md#packing)
