# simSaveImage

Saves an image to file or to memory

## Synopsis

```cpp
simSaveImage(const unsigned char* image, const int* resolution, int options, const char* filename,
             int quality, void* reserved)
```

## Parameters

- **image**: a pointer to rgb, rgba or greyscale values.
- **resolution**: the x/y resolution of the provided image.
- **options**: bit-coded. If bit0 and bit1 represent the format of the provided image (0=rgb, 1=rgba, 2=greyscale).
- **filename**: the name of the file to write. The file extension indicates the format.
- **quality**: the quality of the written image: 0 for best compression, 100 for largest file. Use -1 for default behaviour.
- **reserved**: Reserved for future extension. Set to nullptr.

## Return values

- -1 if operation was not successful.

## See also

- [simLoadImage](simLoadImage_cpp.md)
- [simGetScaledImage](simGetScaledImage_cpp.md)
- [simGetVisionSensorImg](simGetVisionSensorImg_cpp.md)
