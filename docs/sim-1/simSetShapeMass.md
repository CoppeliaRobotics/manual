# sim.setShapeMass

Applies a new mass value to a shape. If simulation is running, the shape is dynamically reset (similar to calling [sim.resetDynamicObject](simResetDynamicObject.md) right after)

## Synopsis

```lua
sim.setShapeMass(int shapeHandle, float mass)
```

```python
sim.setShapeMass(int shapeHandle, float mass)
```

## Parameters

- **shapeHandle**: handle of the [shape object](../shapes.md)
- **mass**: new mass of the shape

## Return values

No return values.

## See also

- [sim.getShapeMass](simGetShapeMass.md)
- [sim.setShapeInertia](simSetShapeInertia.md)
- [sim.computeMassAndInertia](simComputeMassAndInertia.md)
