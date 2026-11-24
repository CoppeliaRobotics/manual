# sim.getShapeTextureId

Retrieves the texture ID of a texture that is applied to a specific shape

## Synopsis

```lua
int textureId = sim.getShapeTextureId(int shapeHandle)
```

```python
int textureId = sim.getShapeTextureId(int shapeHandle)
```

## Parameters

- **shapeHandle**: handle of the shape.

## Return values

- **textureId**: texture ID, or -1 if texture does not exist

## See also

- [sim.getTextureId](simGetTextureId.md)
- [sim.setShapeTexture](simSetShapeTexture.md)
