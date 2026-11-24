# simSetShapeInertia

Applies a new inertia matrix to a shape. If simulation is running, the shape is dynamically reset (similar to calling [sim.resetDynamicObject](simResetDynamicObject.md) right after)

## Synopsis

```cpp
int simSetShapeInertia(int shapeHandle, const double* inertiaMatrix,
                       const double* transformationMatrix)
```

## Parameters

- **shapeHandle**: handle of the [shape object](../shapes.md)
- **inertiaMatrix**: new inertia matrix (9 values), expressed relative to *transformationMatrix* (itself expressed relative to the shape's reference frame)
- **transformationMatrix**: a transformation matrix (array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2]) expressed relative to the shape's reference frame. The matrix indicates the center of mass of the shape, and is the frame relative to which *inertiaMatrix* is expressed

## Return values

- -1 in case of an error

## See also

- [simGetShapeInertia](simGetShapeInertia_cpp.md)
- [simSetShapeMass](simSetShapeMass_cpp.md)
- [simComputeMassAndInertia](simComputeMassAndInertia_cpp.md)
