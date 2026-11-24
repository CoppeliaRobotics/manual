# simSetShapeTexture

Applies/removes a texture to/from a shape

## Synopsis

```cpp
int simSetShapeTexture(int h, int tId, int mode, int opt, const double* uvScaling, const double* pos,
                       const double* orient)
```

## Parameters

- **h**: handle of the shape.
- **tId**: ID of the texture or -1 to remove any existing texture. See also [simGetTextureId](simGetTextureId.md), [simGetShapeTextureId](simGetShapeTextureId.md) and [simCreateTexture](simCreateTexture.md).
- **mode**: [texture mapping mode](../apiConstants-1.md#textureMappingModes).
- **opt**: bit-coded:

    - bit0: if set (1), then adjacent texture pixels are not interpolated.
    - bit1: if set (2), then the texture is applied as a decal (its appearance won't be influenced by light conditions).
    - bit2: if set (4), then the texture will be repeated along the U direction.
    - bit3: if set (8), then the texture will be repeated along the V direction.
- **uvScaling**: pointer to 2 values that indicate the texture scaling factors along the U and V directions.
- **pos**: pointer to 3 values (x,y,z) that indicate the texture position on the shape. Can be nullptr for default values.
- **orient**: pointer to 3 values (Euler angles) that indicate the texture orientation on the shape. Can be nullptr for default values.

## Return values

- -1 in case of an error.

## See also

- [simGetTextureId](simGetTextureId_cpp.md)
- [simGetShapeTextureId](simGetShapeTextureId_cpp.md)
- [simCreateTexture](simCreateTexture_cpp.md)
- [simApplyTexture](simApplyTexture_cpp.md)
