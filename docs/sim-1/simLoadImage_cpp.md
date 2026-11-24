# simLoadImage

Loads an image from file or memory

## Synopsis

```cpp
unsigned char* simLoadImage(int* resolution, int options, const char* filenameOrBuffer,
                            void* reserved)
```

## Parameters

- **resolution**: pointer that will accept the image resolution.
- **options**: bit-coded:

    - bit0 is set (1): the returned image is rgba, otherwise it is rgb
- **filename**: name of the file to read. The file extension indicates the format. If you wish to load an image from a memory buffer, then have filename point to that memory buffer.
- **reserved**: Set to nullptr if you load an image from file. If you load an image from a memory buffer, this should be to an integer pointer where the first pointed integer is the size of the memory buffer.

## Return values

- nullptr if operation was not successful, otherwise a buffer containing the image data. The user is in charge of releasing the buffer with [simReleaseBuffer](simReleaseBuffer_cpp.md).

## See also

- [simSaveImage](simSaveImage_cpp.md)
- [simGetScaledImage](simGetScaledImage_cpp.md)
- [simTransformImage](simTransformImage_cpp.md)
- [simSetVisionSensorImg](simSetVisionSensorImg_cpp.md)
