# simGetPoseProperty

Fetches a pose property (double[7]: x, y, z, qx, qy, qz, qw)

## Synopsis

```cpp
int simGetPoseProperty(long long target, const char* propertyName, double* propertyState)
```

## Parameters

- **target**: target item
- **propertyName**: property name
- **propertyState**: pointer to property value

## Return values

- 1 in case of success

## See also

- [properties](../properties.md)
