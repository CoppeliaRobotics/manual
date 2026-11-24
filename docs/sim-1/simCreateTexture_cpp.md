# simCreateTexture

Creates a planar shape, that will be textured with a new, or imported texture

## Synopsis

```cpp
int simCreateTexture(const char* fileName, int options, const double* planeSizes,
                     const double* scalingUV, const double* xy_g, int fixedResolution,
                     int* textureId, int* resolution, const void* reserved)
```

## Parameters

- **fileName**: filename of the texure to import, or an empty string if you wish to create a new texture.
- **options**: bit-coded:

    - **bit0** set (1): do not interpolate adjacent color patches.
    - **bit1** set (2): apply the texture in decal-mode.
    - **bit2** set (4): repeat the texture along the U direction.
    - **bit3** set (8): repeat the texture along the V direction.
- **planeSizes**: a pointer to 2 values: the dimensions of the planar shape that will be generated. Can be nullptr for default dimensions.
- **scalingUV**: a pointer to 2 values: the desired scaling of the texture, along the U and V directions. Can be nullptr for default scalings.
- **xy_g**: a pointer to 3 values: the texture x/y shift, and the texture gamma-rotation. Can be nullptr for default shift/rotation values.
- **fixedResolution**: 0 to import the shape with its original resolution. Otherwise, specify a power of 2 value which will be the maximum texture resolution (the texture will also be applied a power of 2 resolution).
- **resolution**: a pointer to 2 values representing the desired texture resolution when creating a new texture. The same pointer is used to return the effective resolution of the created/imported texture.
- **textureId**: a pointer to an integer that will be used to return the new texture ID. If a same texture is already present, the old texture ID will be returned. Can be nullptr.
- **reserved**: reserved. Set to nullptr.

## Return values

- -1 in case of an error, otherwise the object handle of the created planar shape.

## See also

- [simGetTextureId](simGetTextureId_cpp.md)
- [simReadTexture](simReadTexture_cpp.md)
- [simWriteTexture](simWriteTexture_cpp.md)
- [simSetShapeTexture](simSetShapeTexture_cpp.md)
