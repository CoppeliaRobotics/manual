# simComputeMassAndInertia

Computes and applies the mass and inertia matrix for a shape, based on its convex representation. When calling this function while the simulation is running, one should then call [sim.resetDynamicObject](simResetDynamicObject.md), for the changes to take effect

## Synopsis

```cpp
int simComputeMassAndInertia(int shapeHandle, double density))
```

## Parameters

- **shapeHandle**: handle of shape
- **density**: the density expressed in kg/m^3

## Return values

- -1 in case of an error, 0 if the shape is not convex, otherwise 1.

## See also

- [simGetShapeMass](simGetShapeMass_cpp.md)
- [simGetShapeInertia](simGetShapeInertia_cpp.md)
- [simConvexDecompose](simConvexDecompose_cpp.md)
