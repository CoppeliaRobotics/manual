# simReadTexture

Retrieves the RGB data (or a portion of it) related to a specific texture

## Synopsis

```cpp
char* simReadTexture(int textureId, int options, int posX, int posY, int sizeX, int sizeY)
```

## Parameters

- **textureId**: ID of the texture. See also [simGetTextureId](simGetTextureId.md).
- **options**: reserved for future functionality. Set to zero.
- **posX / posY**: x/y position of the texture portion to retrieve. Set to [0 0] to retrieve the full texture
- **sizeX / sizeY**: x/y size of the texture portion to retrieve. Set to [0 0] to retrieve the full texture

## Return values

- The texture data, or nullptr in case of an error. The texture data contains RGB values between 0-255 (3 bytes per pixel). The user is in charge of releasing the returned buffer with [simReleaseBuffer](simReleaseBuffer_cpp.md).

## See also

- [simGetTextureId](simGetTextureId_cpp.md)
- [simWriteTexture](simWriteTexture_cpp.md)
- [simCreateTexture](simCreateTexture_cpp.md)
