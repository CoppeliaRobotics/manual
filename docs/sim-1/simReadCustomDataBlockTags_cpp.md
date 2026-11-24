# simReadCustomDataBlockTags

Reads the tags of all custom data that is stored inside of an object, a scene, or the application

## Synopsis

```cpp
char* simReadCustomDataBlockTags(int objectHandle, int* tagCount)
```

## Parameters

- **objectHandle**: handle of the object, sim.handle_scene or sim.handle_app.
- **tagCount**: pointer to an integer receiving the number of tag strings contained in the returned buffer.

## Return values

- the tags (each followed by the zero-char) or nullptr in case of an error (or if no tags are present). The user is in charge of releasing the returned buffer with [simReleaseBuffer](simReleaseBuffer_cpp.md).

## See also

- [simReadCustomDataBlock](simReadCustomDataBlock_cpp.md)
