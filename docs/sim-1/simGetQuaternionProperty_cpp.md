# simGetQuaternionProperty

Fetches a quaternion property (double[4]: qx, qy, qz, qw)

## Synopsis

```cpp
int simGetQuaternionProperty(long long target, const char* propertyName, double* propertyState)
```

## Parameters

- **target**: target item
- **propertyName**: property name
- **propertyState**: pointer to property value

## Return values

- 1 in case of success

## See also

- [properties](../properties.md)
