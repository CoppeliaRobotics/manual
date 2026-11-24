# simSetVisionSensorImg

Writes the image of a vision sensor (and applies any image processing via the [vision callback functions](../visionCallbackFunctions.md)). Make sure the vision sensor is flagged as **external input**

## Synopsis

```cpp
int simSetVisionSensorImg(int sensorHandle, const unsigned char* img, int options, const int* pos,
                          const int* size)
```

## Parameters

- **sensorHandle**: handle of the vision sensor object
- **img**: buffer containing the image
- **options**: options, bit-coded:

    - bit0 set (1): the provided image is a greyscale image (1 byte per pixel), otherwise an RGB image (3 bytes per pixel)
    - bit1 set (2): the provided image has one additional byte per pixel, as alpha channel (RGBA or greyscale+A)
- **pos**: position of the image portion to write. Can be nullptr, which defaults to [0 0]
- **size**: size of the image portion to write. Can be nullptr which defaults to [0 0], which corresponds to [resolutionX resolutionY]

## Return values

- -1 if operation was not successful

## See also

- [vision sensor related API functions](../apiFunctions-1.md#visionSensor)
