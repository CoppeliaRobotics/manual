# simGetShapeGeomInfo

Retrieves geometric information related to a shape

## Synopsis

```cpp
int simGetShapeGeomInfo(int shapeHandle, int* intData, double* floatData, void* reserved)
```

## Parameters

- **shapeHandle**: handle of the shape
- **intData (output)**: pointer to 5 integer values:
- intData[0]: the [primitive type](../apiConstants-1.md#primitiveTypes) of the shape. Undefined if the shape is a compound shape.
- **floatData (output)**: pointer to 5 double values:

    - floatData[0]: X-size or diameter of the primitive shape. Undefined if the shape is a compound shape or not primitive.
    - floatData[1]: Y-size of the primitive shape. Undefined if the shape is a compound shape or not primitive.
    - floatData[2]: Z-size or height of the primitive shape. Undefined if the shape is a compound shape or not primitive.
    - floatData[3]: Reserved.
- **reserved**: reserved for future extensions. Set to nullptr.

## Return values

- -1 in case of an error, otherwise bit-coded:

  - bit0 set (1): shape is a compound shape
  - bit1 set (2): shape is primitive
  - bit2 set (4): shape is convex

## See also

- [simGetShapeMesh](simGetShapeMesh_cpp.md)
