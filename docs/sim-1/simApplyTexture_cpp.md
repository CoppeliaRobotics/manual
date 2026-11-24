# simApplyTexture

Applies a texture via texture coordinates to a shape

## Synopsis

```cpp
int simApplyTexture(int shapeHandle, const double* textureCoordinates, int textCoordSize,
                    const unsigned char* texture, const int* textureResolution, int options)
```

## Parameters

- **shapeHandle**: handle of the shape
- **textureCoordinates**: UV texture coordinates. For each of the shape's triangle, there should be exactly 3 UV texture coordinate pairs
- **textCoordSize**: size of the textureCoordinate array
- **texture**: RGB or RGBA texture
- **textureResolution**: X/Y resolution of the texture
- **options**: bit-coded:

    - bit0: if set (1), then adjacent texture pixels are not interpolated
    - bit1: if set (2), then the texture is applied as a decal (its appearance won't be influenced by light conditions)
    - bit2: unused, keep unset
    - bit3: unused, keep unset
    - bit4: if set (16), then the texture is RGBA, otherwise it is RGB
    - bit5: if set (32), then the texture is horizontally flipped
    - bit6: if set (64), then the texture is vertically flipped

## Return values

- The ID of the texture, or -1 in case of an error

## See also

- [simSetShapeTexture](simSetShapeTexture_cpp.md)
