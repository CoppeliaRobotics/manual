# sim.readTexture

Retrieves the RGB data (or a portion of it) related to a specific texture

## Synopsis

```lua
buffer textureData = sim.readTexture(int textureId, int options, int posX = 0, int posY = 0,
                                     int sizeX = 0, int sizeY = 0)
```

```python
bytes textureData = sim.readTexture(int textureId, int options, int posX = 0, int posY = 0,
                                    int sizeX = 0, int sizeY = 0)
```

## Parameters

- **textureId**: ID of the texture. See also [simGetTextureId](simGetTextureId.md).
- **options**: reserved for future functionality. Set to zero.
- **posX / posY**: x/y position of the texture portion to retrieve. Set to [0 0] to retrieve the full texture
- **sizeX / sizeY**: x/y size of the texture portion to retrieve. Set to [0 0] to retrieve the full texture

## Return values

- **textureData**: texture data

## See also

- [sim.getTextureId](simGetTextureId.md)
- [sim.writeTexture](simWriteTexture.md)
- [sim.createTexture](simCreateTexture.md)
