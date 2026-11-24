# sim.createShape

Creates a mesh shape

## Synopsis

```lua
int objectHandle = sim.createShape(int options, float shadingAngle, float[] vertices, int[] indices,
                                   float[] normals = nil, float[] textureCoordinates = nil,
                                   string/buffer texture = nil, int[2] textureResolution = nil)
```

```python
int objectHandle = sim.createShape(int options, float shadingAngle, list vertices, list indices,
                                   list normals = None, list textureCoordinates = None,
                                   string/bytes texture = None, list textureResolution = None)
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
- **indices**: array of indices
- **normals**: optional array of normal vectors. Has to be 3 * len(indices) in length
- **textureCoordinates**: optional array of texture coordinates. Has to be 2 * len(indices) in length
- **texture**: optional texture, specified as RGB or RGBA
- **textureResolution**: resolution of the specified texture

## Return values

- **objectHandle**: handle of the newly created shape

## See also

- [sim.createPrimitiveShape](simCreatePrimitiveShape.md)
- [sim.createHeightfieldShape](simCreateHeightfieldShape.md)
- [sim.getShapeMesh](simGetShapeMesh.md)
- [sim.importMesh](simImportMesh.md)
