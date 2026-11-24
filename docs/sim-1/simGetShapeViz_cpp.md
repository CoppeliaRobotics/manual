# simGetShapeViz

Retrieves a shape's visual information.

## Synopsis

```cpp
int simGetShapeViz(int shapeHandle, int index, struct SShapeVizInfo* info)
```

## Parameters

- **shapeHandle**: handle of the shape. Can be combined with sim_handleflag_extended in order to retrieve extended data
- **index**: 0-based index of the shape element to retrieve (compound shapes contain more than one shape element)
- **info**: visual information about the shape:

    - **vertices**: array of vertices, relative to the shape's reference frame. The user is in charge of releasing this buffer with [simReleaseBuffer](simReleaseBuffer_cpp.md) if the return value is &gt; 0.
    - **verticesSize**: the size of the vertices array
    - **indices**: array of indices. The user is in charge of releasing this buffer with [simReleaseBuffer](simReleaseBuffer_cpp.md) if the return value is &gt; 0.
    - **indicesSize**: the size of the indices array
    - **normals**: array of normals, relative to the shape's reference frame. There are 3*indicesSize normals, i.e. 3 normals per triangle. The user is in charge of releasing this buffer with [simReleaseBuffer](simReleaseBuffer_cpp.md) if the return value is &gt; 0.
    - **shadingAngle**: the gouraud shading angle
    - **colors[9]**: array of colors: RGB for ambient-diffuse, specular, and emission.
    - **transparency**: transparency value (0.0 = opaque, 1.0 = fully transparent). To have this field written, combine shapeHandle with sim_handleflag_extended
    - **options**: bit-coded options (to have this field written, combine shapeHandle with sim_handleflag_extended):
      - bit0 set (1): backfaces are culled

    - **texture**: the RGBA texture (32bit/pixel). The user is in charge of releasing this buffer with [simReleaseBuffer](simReleaseBuffer_cpp.md) if the return value is &gt; 1.
    - **textureId**: a texture id (to identify textures shared among several shapes)
    - **textureRes[2]**: the resolution of the texture
    - **textureCoords**: the texture coordinates. There are 3*indicesSize texture coordinates, i.e. 3 coordinates per triangle. The user is in charge of releasing this buffer with [simReleaseBuffer](simReleaseBuffer_cpp.md) if the return value is &gt; 1.
    - **textureApplyMode**: 0=modulate, 1=decal, 2=add
    - **textureOptions**: bit-coded:
      - bit0 set (1): repeat U
      - bit1 set (2): repeat V
      - bit2 set (4): interpolate colors
      - bit3 set (8): wireframe

## Return values

- -1 if operation was not successful, 0 if there is no shape element at the given indexm, 1 if the shape element does not contain any texture, 2 if the shape element contains a texture
