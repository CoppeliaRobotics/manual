# simGetScaledImage

Generates a scaled-up or scaled down version of the input image

## Synopsis

```cpp
unsigned char* simGetScaledImage(const unsigned char* imageIn, const int* resolutionIn,
                                 const int* resolutionOut, int options, void* reserved)
```

## Parameters

- **imageIn**: pointer to rgb or rgba values of the input image.
- **resolutionIn**: resolution of the input image.
- **resolutionOut**: desired resolution of the output image. The values will be replaced by the effective resolution of the output image
- **options**: bit-coded:

    - bit0 set (1): the input image is rgba, otherwise it is rgb
    - bit1 set (2): the returned image is rgba, otherwise it is rgb
    - bit2-3: 0:ignore aspect ratio, 4:keep aspect ratio (the effective resolution of the returned image will be different), 8:keep aspect ratio by expanding (the effective resolution of the returned image will be different)
    - bit4 set (16): no smooth transformation
- **reserved**: Reserved for future extension. Set to nullptr.

## Return values

- nullptr if operation was not successful, otherwise a buffer containing the output image data. The user is in charge of releasing the buffer with [simReleaseBuffer](simReleaseBuffer_cpp.md).

## See also

- [simTransformImage](simTransformImage_cpp.md)
- [simLoadImage](simLoadImage_cpp.md)
- [simSaveImage](simSaveImage_cpp.md)
- [simSetVisionSensorImg](simSetVisionSensorImg_cpp.md)
