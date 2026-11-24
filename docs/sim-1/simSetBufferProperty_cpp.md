# simSetBufferProperty

Sets a buffer property

## Synopsis

```cpp
int simSetBufferProperty(long long target, const char* propertyName, const char* bufferPointer
                         int bufferLength)
```

## Parameters

- **target**: target item
- **propertyName**: property name
- **bufferPointer**: pointer to buffer value
- **bufferLength**: buffer length

## Return values

- 1 in case of success

## See also

- [properties](../properties.md)
- [packing/unpacking related functions](../apiFunctions-1.md#packing)
