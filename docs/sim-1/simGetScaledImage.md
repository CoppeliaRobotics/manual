# sim.getScaledImage

Generates a scaled-up or scaled down version of the input image

## Synopsis

```lua
buffer imageOut, int[2] effectiveResolutionOut = sim.getScaledImage(buffer imageIn,
                                                                    int[2] resolutionIn,
                                                                    int[2] desiredResolutionOut,
                                                                    int options)
```

```python
bytes imageOut, list effectiveRolutionOut = sim.getScaledImage(bytes imageIn, list resolutionIn,
                                                               list desiredResolutionOut,
                                                               int options)
```

## Parameters

- **imageIn**: image buffer (rgb or rgba values)
- **resolutionIn**: resolution of the input image
- **options**: bit-coded:

    - bit0 set (1): the input image is rgba, otherwise it is rgb
    - bit1 set (2): the returned image is rgba, otherwise it is rgb
    - bit2-3: 0:ignore aspect ratio, 4:keep aspect ratio (the effective resolution of the returned image will be different), 8:keep aspect ratio by expanding (the effective resolution of the returned image will be different)
    - bit4 set (16): no smooth transformation

## Return values

- **imageOut**: buffer containing the output image data
- **effectiveResolutionOut**: resolution of the generated image

## See also

- [sim.transformImage](simTransformImage.md)
- [sim.loadImage](simLoadImage.md)
- [sim.saveImage](simSaveImage.md)
- [sim.setVisionSensorImg](simSetVisionSensorImg.md)
