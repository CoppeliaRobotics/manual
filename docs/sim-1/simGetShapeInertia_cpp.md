# simGetShapeInertia

Retrieves the inertia information from a shape

## Synopsis

```cpp
int simGetShapeInertia(int shapeHandle, double* inertiaMatrix, double* com)
```

## Parameters

- **shapeHandle**: handle of the [shape object](../shapes.md)
- **inertiaMatrix**: (output): inertia matrix (9 values), expressed relative to the shape's reference frame orientation. The matrix is symmetric
- **com**: (output): a transformation matrix [0 0 0 P0 0 0 0 P1 0 0 0 P2] indicating the center of mass, expressed relative to the shape's reference frame. The matrix does not contain any rotational part (only the positional values are relevant).

## Return values

- -1 in case of an error

## See also

- [simSetShapeInertia](simSetShapeInertia_cpp.md)
- [simGetShapeMass](simGetShapeMass_cpp.md)
- [simComputeMassAndInertia](simComputeMassAndInertia_cpp.md)
