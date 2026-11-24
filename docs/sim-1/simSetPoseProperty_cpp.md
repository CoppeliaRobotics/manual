# simSetPoseProperty

Sets a pose property (double[7]: x, y, z, qx, qy, qz, qw)

## Synopsis

```cpp
int simSetPoseProperty(long long target, const char* propertyName, const double* propertyState)
```

## Parameters

- **target**: target item
- **propertyName**: property name
- **propertyState**: pointer to property value

## Return values

- 1 in case of success

## See also

- [properties](../properties.md)
