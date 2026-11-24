# simCreatePrimitiveShape

Creates a primitive shape

## Synopsis

```cpp
int simCreatePrimitiveShape(int primitiveType, const double* sizes, int options)
```

## Parameters

- **primitiveType**: the [primitive type](../apiConstants-1.md#primitiveTypes) of the shape
- **sizes**: 3 values indicating the size of the shape
- **options**: Bit-coded:

    - bit0 is set (1): backfaces are culled
    - bit1 is set (2): edges appear sharp
    - bit2 is set (4): cylinder has open ends
    - bit3 is set (8): the primitive shape is not registered as such by CoppeliaSim, but rather as a random (maybe convex) shape

## Return values

- -1 if operation was not successful, otherwise the handle of the newly created shape

## See also

- [simCreateShape](simCreateShape_cpp.md)
- [simCreateHeightfieldShape](simCreateHeightfieldShape_cpp.md)
