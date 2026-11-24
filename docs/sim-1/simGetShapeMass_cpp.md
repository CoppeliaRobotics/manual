# simGetShapeMass

Retrieves the mass of a shape

## Synopsis

```cpp
int simGetShapeMass(int shapeHandle, double* mass)
```

## Parameters

- **shapeHandle**: handle of the [shape object](../shapes.md)
- **mass**: mass of the shape

## Return values

- -1 in case of an error

## See also

- [simSetShapeMass](simSetShapeMass_cpp.md)
- [simGetShapeInertia](simGetShapeInertia_cpp.md)
- [simComputeMassAndInertia](simComputeMassAndInertia_cpp.md)
