# simSetShapeMass

Applies a new mass value to a shape. If simulation is running, the shape is dynamically reset (similar to calling [sim.resetDynamicObject](simResetDynamicObject.md) right after)

## Synopsis

```cpp
int simSetShapeMass(int shapeHandle, double mass)
```

## Parameters

- **shapeHandle**: handle of the [shape object](../shapes.md)
- **mass**: new mass of the shape

## Return values

- -1 in case of an error

## See also

- [simGetShapeMass](simGetShapeMass_cpp.md)
- [simSetShapeInertia](simSetShapeInertia_cpp.md)
- [simComputeMassAndInertia](simComputeMassAndInertia_cpp.md)
