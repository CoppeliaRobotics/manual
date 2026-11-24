# sim.getShapeInertia

Retrieves the inertia information from a shape

## Synopsis

```lua
float[9] inertiaMatrix, float[12] com = sim.getShapeInertia(int shapeHandle)
```

```python
list inertiaMatrix, list com = sim.getShapeInertia(int shapeHandle)
```

## Parameters

- **shapeHandle**: handle of the [shape object](../shapes.md)

## Return values

- **inertiaMatrix**: (output): inertia matrix (9 values), expressed relative to the shape's reference frame orientation. The matrix is symmetric
- **com**: (output): a transformation matrix [0 0 0 P0 0 0 0 P1 0 0 0 P2] indicating the center of mass, expressed relative to the shape's reference frame. The matrix does not contain any rotational part (only the positional values are relevant).

## See also

- [sim.setShapeInertia](simSetShapeInertia.md)
- [sim.getShapeMass](simGetShapeMass.md)
- [sim.computeMassAndInertia](simComputeMassAndInertia.md)
