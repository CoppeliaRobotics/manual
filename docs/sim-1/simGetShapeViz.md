# sim.getShapeViz

Retrieves a shape's visual information.

## Synopsis

```lua
table data = sim.getShapeViz(int shapeHandle, int index)
```

```python
dict data = sim.getShapeViz(int shapeHandle, int index)
```

## Parameters

- **shapeHandle**: handle of the shape.
- **index**: 0-based index of the shape element to retrieve (compound shapes contain more than one shape element)

## Return values

- **data.vertices**: array containing the vertices, relative to the shape's reference frame
- **data.indices**: array containing the indices
- **data.normals**: array containing the normals, relative to the shape's reference frame
- **data.colors**: array containing the colors: RGB for ambient-diffuse, specular, and emission.
- **data.shadingAngle**: the gouraud shading angle
- **data.transparency**: 1=transparent, 0= opaque
- **data.options**: bit-coded:

    - bit0 set (1): backface culling
    - bit1 set (2): wireframe
- **data.texture.texture**: string-coded RGBA texture. See also [sim.transformBuffer](simTransformBuffer.md)
- **data.texture.id**: texture id (to identify textures shared among several shapes)
- **data.texture.resolution**: resolution of the texture
- **data.texture.coordinates**: texture coordinates
- **data.texture.applyMode**: 0=modulate, 1=decal, 2=add
- **data.texture.options**: bit-coded:

    - bit0 set (1): repeat U
    - bit1 set (2): repeat V
    - bit2 set (4): interpolate colors
