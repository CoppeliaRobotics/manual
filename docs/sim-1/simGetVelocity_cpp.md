# simGetVelocity

Retrieves the linear and/or angular velocity of the center of mass of a non-static shape. Data is provided by the selected physics engine

## Synopsis

```cpp
int simGetVelocity(int shapeHandle, double* linearVelocity, double* angularVelocity)
```

## Parameters

- **shapeHandle**: handle of a dynamically enabled shape
- **linearVelocity**: pointer to 3 values that will receive the linear velocity in absolute coordinates. Can be nullptr
- **angularVelocity**: pointer to 3 values that will receive the angular velocity in absolute coordinates. The length of the vector represents the rotation speed, and the vector direction represents the rotation axis passing through the center of mass of the shape. Can be nullptr

## Return values

- -1 if operation was not successful

## See also

- [simGetObjectVelocity](simGetObjectVelocity_cpp.md)
