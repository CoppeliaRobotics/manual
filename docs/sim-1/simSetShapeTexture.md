# sim.setShapeTexture

Applies/removes a texture to/from a shape

## Synopsis

```lua
sim.setShapeTexture(int shapeHandle, int textureId, int mappingMode, int options, float[2] uvScaling,
                    float[3] position = nil, float[3] orientation = nil)
```

```python
sim.setShapeTexture(int shapeHandle, int textureId, int mappingMode, int options, list uvScaling,
                    list position = None, list orientation = None)
```

## Parameters

- **shapeHandle**: handle of the shape.
- **textureId**: ID of the texture or -1 to remove any existing texture. See also [sim.getTextureId](simGetTextureId.md), [sim.getShapeTextureId](simGetShapeTextureId.md) and [sim.createTexture](simCreateTexture.md)
- **mappingMode**: [texture mapping mode](../apiConstants-1.md#textureMappingModes).
- **options**: bit-coded:

    - bit0: if set (1), then adjacent texture pixels are not interpolated.
    - bit1: if set (2), then the texture is applied as a decal (its appearance won't be influenced by light conditions).
    - bit2: if set (4), then the texture will be repeated along the U direction.
    - bit3: if set (8), then the texture will be repeated along the V direction.
- **uvScaling**: array of 2 values indicating the texture scaling factors along the U and V directions
- **position**: array of 3 values x/y/z indicating the texture position on the shape. Can be None/nil for default values
- **orientation**: array of 3 values (Euler angles) indicating the texture orientation on the shape. Can be None/nil for default values

## Return values

No return values.

## See also

- [sim.getTextureId](simGetTextureId.md)
- [sim.getShapeTextureId](simGetShapeTextureId.md)
- [sim.createTexture](simCreateTexture.md)
