# sim.setShapeInertia

Applies a new inertia matrix to a shape. If simulation is running, the shape is dynamically reset (similar to calling [sim.resetDynamicObject](simResetDynamicObject.md) right after)

## Synopsis

```lua
sim.setShapeInertia(int shapeHandle, float[9] inertiaMatrix, float[12] transformationMatrix)
```

```python
sim.setShapeInertia(int shapeHandle, list inertiaMatrix, list transformationMatrix)
```

## Parameters

- **shapeHandle**: handle of the [shape object](../shapes.md)
- **inertiaMatrix**: new inertia matrix (9 values), expressed relative to *transformationMatrix* (itself expressed relative to the shape's reference frame)
- **transformationMatrix**: a transformation matrix (array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2]) expressed relative to the shape's reference frame. The matrix indicates the center of mass of the shape, and is the frame relative to which *inertiaMatrix* is expressed

## Return values

No return values.

## See also

- [sim.getShapeInertia](simGetShapeInertia.md)
- [sim.setShapeMass](simSetShapeMass.md)
- [sim.computeMassAndInertia](simComputeMassAndInertia.md)
