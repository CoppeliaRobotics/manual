# sim.scaleObjects

Scales specified objects. All related values are automatically scaled appropriately (e.g. masses, forces, etc.)

## Synopsis

```lua
sim.scaleObjects(int[] objectHandles, float scalingFactor, bool scalePositionsToo)
```

```python
sim.scaleObjects(list objectHandles, float scalingFactor, bool scalePositionsToo)
```

## Parameters

- **objectHandles**: array containing the handles of the objects to scale. If an object is a model base, all its child objects will also be scaled
- **scalingFactor**: scaling factor
- **scalePositionsToo**: if true, selected object's positions will also be scaled

## Return values

No return values.

## See also

- [size and scaling functions](../apiFunctions-1.md#size)
