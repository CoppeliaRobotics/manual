# simGetTextureId

Retrieves the texture ID of a specific texture

## Synopsis

```cpp
int simGetTextureId(const char* textureName, int* resolution)
```

## Parameters

- **textureName**: name of the texture ID to be retrieved.
- **resolution**: pointer to 2 integer values representing the resolution of the texture. Can be nullptr.

## Return values

- The texture ID, or -1 if the texture does not exist or in case of an error

## See also

- [simReadTexture](simReadTexture_cpp.md)
- [simWriteTexture](simWriteTexture_cpp.md)
- [simCreateTexture](simCreateTexture_cpp.md)
