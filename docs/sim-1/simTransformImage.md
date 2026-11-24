# sim.transformImage

Transforms an image in various ways

## Synopsis

```lua
buffer newImage = sim.transformImage(buffer image, int[2] resolution, int options)
```

```python
bytes newImage = sim.transformImage(bytes image, list resolution, int options)
```

## Parameters

- **image**: buffer to rgb or rgba values of the image. Beware that in Lua, this image buffer will be modified!
- **resolution**: resolution of the image
- **options**: bit-coded:

    - bit0 set (1): the provided image is rgba (or a depth buffer, i.e. one double per image pixel), otherwise it is rgb
    - bit1 set (2): the image will be flipped on its x-axis
    - bit2 set (4): the image will be flipped on its y-axis

## Return values

- **newImage**: buffer of the transformed image

## See also

- [sim.loadImage](simLoadImage.md)
- [sim.getScaledImage](simGetScaledImage.md)
- [sim.transformBuffer](simTransformBuffer.md)
- [sim.combineRgbImages](simCombineRgbImages.md)
