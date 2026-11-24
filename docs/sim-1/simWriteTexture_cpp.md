# simWriteTexture

Overwrites a specific texture (or a portion of it) with RGB data

## Synopsis

```cpp
int simWriteTexture(int textureId, int options, const char* textureData, int posX, int posY,
                    int sizeX, int sizeY, double interpolation)
```

## Parameters

- **textureId**: ID of the texture. See also [simGetTextureId](simGetTextureId.md)
- **options**: bit-coded:

    - **bit0** reserved. Do not set
    - **bit1** reserved. Do not set
    - **bit2** set (4)=only an elliptical/circular portion of the texture data will be written
- **textureData**: RGB data to write onto the texture. Each pixel is represented with 3 bytes (0-255)
- **posX / posY**: x/y position where to copy the RGB data. Set to 0/0 to overwrite the full texture
- **sizeX / sizeY**: x/y size of the RGB data. Set to 0/0 to overwrite the full texture
- **interpolation**: fade or interpolation factor. 0 for no fade

## Return values

- -1 in case of an error.

## See also

- [simGetTextureId](simGetTextureId_cpp.md)
- [simReadTexture](simReadTexture_cpp.md)
- [simCreateTexture](simCreateTexture_cpp.md)
