# sim.getVisionSensorImg

Reads the image of a vision sensor. The returned data doesn't make sense if [sim.handleVisionSensor](simHandleVisionSensor.md) wasn't called previously

## Synopsis

```lua
buffer image, int[2] resolution = sim.getVisionSensorImg(int sensorHandle, int options = 0,
                                                         float rgbaCutOff = 0.0, pos = {0, 0},
                                                         size = {0, 0})
```

```python
bytes image, list resolution = sim.getVisionSensorImg(int sensorHandle, int options = 0,
                                                      float rgbaCutOff = 0.0, list pos = [0, 0],
                                                      list size = [0, 0])
```

## Parameters

- **sensorHandle**: handle of the vision sensor
- **options**: options, bit-coded:

    - bit0 set (1): the returned image will by a greyscale image (1 byte per pixel), otherwise an RGB image
    - bit1 set (2): the returned image will have one additional byte per pixel, as alpha channel (RGBA or greyscale+A)
- **rgbaCutOff**: when an RGBA image is returned, the alpha component is 255 for all depth values below *rgbaCutOff*, and 0 for all depth values above *rgbaCutOff*. 0.0 corresponds to the near clipping plane, 1.0 to the far clipping plane
- **pos**: position of the image portion to retrieve. Default is [0 0]
- **size**: size of the image portion to retrieve. Default is [0 0], which corresponds to [resolutionX resolutionY]

## Return values

- **image**: the image buffer. Use [sim.unpackUInt8Table](simUnpackUInt8Table.md) to obtain an array of integer values
- **resolution**: the vision sensor resolution

## See also

- [sim.saveImage](simSaveImage.md)
- [vision sensor related API functions](../apiFunctions-1.md#visionSensor)
