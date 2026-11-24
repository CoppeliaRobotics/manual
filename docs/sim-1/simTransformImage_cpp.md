# simTransformImage

Transforms an image in various ways

## Synopsis

```cpp
int simTransformImage(unsigned char* image, const int* resolution, int options,
                      const double* floatParams, const int* intParams, void* reserved)
```

## Parameters

- **image**: pointer to rgb or rgba values of the image
- **resolution**: resolution of the image
- **options**: bit-coded:

    - bit0 set (1): the provided image is rgba (or a depth buffer, i.e. one double per image pixel), otherwise it is rgb
    - bit1 set (2): the image will be flipped on its x-axis
    - bit2 set (4): the image will be flipped on its y-axis
- **floatParams**: Reserved for future extension. Set to nullptr.
- **intParams**: Reserved for future extension. Set to nullptr.
- **reserved**: Reserved for future extension. Set to nullptr.

## Return values

- -1 if operation was not successful.

## See also

- [simLoadImage](simLoadImage_cpp.md)
- [simGetScaledImage](simGetScaledImage_cpp.md)
- [sim.transformBuffer](simTransformBuffer.md)
- [sim.combineRgbImages](simCombineRgbImages.md)
