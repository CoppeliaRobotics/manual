# sim.createTexture

Creates a planar shape, that will be textured with a new, or imported texture

## Synopsis

```lua
int shape, int id, int[2] res = sim.createTexture(string fileName, int options, float[2] planeSizes = nil,
                                                  float[2] scalingUV = nil, float[2] xy_g = nil,
                                                  int fixedResolution = 0, int[2] resolution = nil)
```

```python
int shape, int id, list res = sim.createTexture(string fileName, int options, list planeSizes = None,
                                                list scalingUV = None, list xy_g = None,
                                                int fixedResolution = 0, list resolution = None)
```

## Parameters

- **fileName**: filename of the texure to import, or an empty string if you wish to create a new texture.
- **options**: bit-coded:

    - **bit0** set (1): do not interpolate adjacent color patches.
    - **bit1** set (2): apply the texture in decal-mode.
    - **bit2** set (4): repeat the texture along the U direction.
    - **bit3** set (8): repeat the texture along the V direction.
- **planeSizes**: array of 2 values: the dimensions of the planar shape that will be generated. Can be None/nil for default dimensions.
- **scalingUV**: array of 2 values: the desired scaling of the texture, along the U and V directions. Can be None/nil for default scalings.
- **xy_g**: array of 3 values: the texture x/y shift, and the texture gamma-rotation. Can be None/nil for default shift/rotation values.
- **fixedResolution**: 0 to import the shape with its original resolution. Otherwise, specify a power of 2 value which will be the maximum texture resolution (the texture will also be applied a power of 2 resolution).

## Return values

- **shape**: handle of the created planar shape
- **id**: new texture ID. If a same texture is already present, the old texture ID will be returned
- **res**: the effective texture resolution

## See also

- [sim.getTextureId](simGetTextureId.md)
- [sim.readTexture](simReadTexture.md)
- [sim.writeTexture](simWriteTexture.md)
- [sim.setShapeTexture](simSetShapeTexture.md)
