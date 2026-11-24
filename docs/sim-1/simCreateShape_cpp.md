# simCreateShape

Creates a mesh shape

## Synopsis

```cpp
int simCreateShape(int options, double shadingAngle, const double* vertices, int verticesSize,
                   const int* indices, int indicesSize, const double* normals,
                   const double* textureCoordinates, const unsigned char* texture,
                   const int* textureResolution)
```

## Parameters

- **options**: Bit-coded:

    - if bit0 is set (1), backfaces are culled
    - If bit1 is set (2), edges are visible
    - If bit2 is set (4), adjacent texture pixels are not interpolated
    - If bit3 is set (8), texture is applied as a decal
    - If bit4 is set (16), texture is RGBA, otherwise it is RGB
    - If bit5 is set (32), texture is horizontally flipped
    - If bit6 is set (64), texture is vertically flipped
- **shadingAngle**: shading angle
- **vertices**: array of vertices
- **verticesSize**: size of the vertice array
- **indices**: array of indices
- **indicesSize**: size of the indice array
- **normals**: optional array of normal vectors. Has to be 3*indicesSize in length
- **textureCoordinates**: optional array of texture coordinates. Has to be 2*indicesSize in length
- **texture**: optional texture, specified as RGB or RGBA
- **textureResolution**: resolution of the specified texture

## Return values

- -1 if operation was not successful, otherwise the handle of the newly created shape

## See also

- [simCreatePrimitiveShape](simCreatePrimitiveShape_cpp.md)
- [simCreateHeightfieldShape](simCreateHeightfieldShape_cpp.md)
- [simGetShapeMesh](simGetShapeMesh_cpp.md)
- [simImportMesh](simImportMesh_cpp.md)
