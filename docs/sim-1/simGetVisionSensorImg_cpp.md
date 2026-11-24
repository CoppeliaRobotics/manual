# simGetVisionSensorImg

Reads the image of a vision sensor. The returned data doesn't make sense if [sim.handleVisionSensor](simHandleVisionSensor.md) wasn't called previously

## Synopsis

```cpp
unsigned char* simGetVisionSensorImg(int sensorHandle, int options, double rgbaCutOff,
                                     const int* pos, const int* size, int* resolution)
```

## Parameters

- **sensorHandle**: handle of the vision sensor
- **options**: options, bit-coded:

    - bit0 set (1): the returned image will by a greyscale image (1 byte per pixel), otherwise an RGB image
    - bit1 set (2): the returned image will have one additional byte per pixel, as alpha channel (RGBA or greyscale+A)
- **rgbaCutOff**: when an RGBA image is returned, the alpha component will be 255 for all depth values below *rgbaCutOff*, and 0 for all depth values above *rgbaCutOff*. 0 corresponds to the near clipping plane, 1 to the far clipping plane
- **pos**: position of the image portion to retrieve. Can be nullptr, which defaults to [0 0]
- **size**: size of the image portion to retrieve. Can be nullptr which defaults to [0 0], which corresponds to [resolutionX resolutionY]
- **resolution**: the returned vision sensor resolution. Can be nullptr

## Return values

- the image buffer or nullptr in case of an error. The user is in charge of releasing the returned buffer with [simReleaseBuffer](simReleaseBuffer_cpp.md)

## See also

- [simSaveImage](simSaveImage_cpp.md)
- [vision sensor related API functions](../apiFunctions-1.md#visionSensor)
