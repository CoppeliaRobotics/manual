# sim.computeMassAndInertia

Computes and applies the mass and inertia matrix for a shape, based on its convex representation. When calling this function while the simulation is running, one should then call [sim.resetDynamicObject](simResetDynamicObject.md), for the changes to take effect

## Synopsis

```lua
int result = sim.computeMassAndInertia(int shapeHandle, float density)
```

```python
int result = sim.computeMassAndInertia(int shapeHandle, float density)
```

## Parameters

- **shapeHandle**: handle of shape
- **density**: density expressed in kg/m^3

## Return values

- **result**: 0 if the shape is not convex, otherwise 1

## See also

- [sim.getShapeMass](simGetShapeMass.md)
- [sim.getShapeInertia](simGetShapeInertia.md)
