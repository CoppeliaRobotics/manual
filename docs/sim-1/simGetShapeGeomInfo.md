# sim.getShapeGeomInfo

Retrieves geometric information related to a shape

## Synopsis

```lua
int result, int pureType, float[4] dimensions = sim.getShapeGeomInfo(int shapeHandle)
```

```python
int result, int pureType, list dimensions = sim.getShapeGeomInfo(int shapeHandle)
```

## Parameters

- **shapeHandle**: handle of the shape

## Return values

- **result**: bit-coded:

    - bit0 set (1): shape is a compound shape
    - bit1 set (2): shape is a primitive
    - bit2 set (4): shape is convex
- **pureType**: the [primitive type](../apiConstants-1.md#pureTypes) of the shape. Undefined if the shape is a compound shape.
- **dimensions**: array of 4 values giving information about the shape's dimensions (indexing (i) starts from 0 for Python and 1 for Lua):

    - dimensions[i+0]: X-size or diameter of the primitive shape. Undefined if the shape is a compound shape or not primitive
    - dimensions[i+1]: Y-size of the primitive shape. Undefined if the shape is a compound shape or not primitive
    - dimensions[i+2]: Z-size or height of the primitive shape. Undefined if the shape is a compound shape or not primitive
    - dimensions[i+3]: Inside scaling. Undefined if the shape is a compound shape or not primitive

## See also

- [sim.getShapeMesh](simGetShapeMesh.md)
