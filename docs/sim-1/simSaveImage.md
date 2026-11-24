# sim.saveImage

Saves an image to file or to memory

## Synopsis

```lua
buffer imgBuffer = sim.saveImage(buffer image, int[2] resolution, int options, string filename,
                                 int quality)
```

```python
bytes imgBuffer = sim.saveImage(bytes image, list resolution, int options, string filename,
                                int quality)
```

## Parameters

- **image**: image (in rgb, rgba or greyscale format)
- **resolution**: x/y resolution of the provided image.
- **options**: bit-coded:

    - bit0 - bit1: format of the provided image (0=rgb, 1=rgba, 2=greyscale)
- **filename**: name of the file to write. The file extension indicates the format. If the filename only contains '.ext', where ext represents the file format, then the image will be saved to memory
- **quality**: quality of the written image: 0 for best compression, 100 for largest file. Use -1 for default behaviour.

## Return values

- **imgBuffer**: a buffer containing the image in packed format (e.g. png, jpg, etc.), if the image was specified to be saved to memory.

## See also

- [sim.loadImage](simLoadImage.md)
- [sim.getScaledImage](simGetScaledImage.md)
- [sim.getVisionSensorImg](simGetVisionSensorImg.md)
