# sim.getTextureId

Retrieves the texture ID of a specific texture

## Synopsis

```lua
int textureId, int[2] resolution = sim.getTextureId(string textureName)
```

```python
int textureId, list resolution = sim.getTextureId(string textureName)
```

## Parameters

- **textureName**: name of the texture ID to be retrieved

## Return values

- **textureId**: the texture ID, or -1 if the texture does not exist
- **resolution**: an array of 2 values representing the resolution of the texture

## See also

- [sim.readTexture](simReadTexture.md)
- [sim.writeTexture](simWriteTexture.md)
- [sim.createTexture](simCreateTexture.md)
