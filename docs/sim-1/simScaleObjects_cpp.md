# simScaleObjects

Scales specified objects. All related values are automatically scaled appropriately (e.g. masses, forces, etc.)

## Synopsis

```cpp
int simScaleObjects(const int* objectHandles, int objectCount, double scalingFactor,
                    bool scalePositionsToo)
```

## Parameters

- **objectHandles**: array containing the handles of the objects to scale. If an object is a model base, all its child objects will also be scaled.
- **objectCount**: number of handles in the objectHandles array.
- **scalingFactor**: scaling factor
- **scalePositionsToo**: if true, selected object's positions will also be scaled

## Return values

- -1 if operation was not successful

## See also

- [size and scaling functions](../apiFunctions-1.md#size)
