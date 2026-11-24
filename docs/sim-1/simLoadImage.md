# sim.loadImage

Loads an image from file or memory

## Synopsis

```lua
buffer image, int[2] resolution = sim.loadImage(int options, string/buffer filenameOrBuffer)
```

```python
bytes image, list resolution = sim.loadImage(int options, string/bytes filenameOrBuffer)
```

## Parameters

- **options**: bit-coded:

    - bit0 is set (1): the returned image is rgba, otherwise it is rgb
- **filenameOrBuffer**: name of the file to read. The file extension indicates the format. To load an image from a buffer, simply prefix the buffer with "@mem"

## Return values

- **image**: buffer containing the image data
- **resolution**: the image resolution

## See also

- [sim.saveImage](simSaveImage.md)
- [sim.getScaledImage](simGetScaledImage.md)
- [sim.transformImage](simTransformImage.md)
- [sim.setVisionSensorImg](simSetVisionSensorImg.md)
