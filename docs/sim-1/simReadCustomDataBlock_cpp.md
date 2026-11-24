# simReadCustomDataBlock

Reads custom data that is stored inside of an object or the scene. Reads also custom data for the application's currrent session

## Synopsis

```cpp
char* simReadCustomDataBlock(int objectHandle, const char* tagName, int* dataSize)
```

## Parameters

- **objectHandle**: handle of the object, or sim.handle_scene if the data is stored in the scene, or sim.handle_app if the data is stored in the application's current session.
- **tagName**: string that identifies the data.
- **dataSize**: pointer to an integer receiving the size of the returned buffer.

## Return values

- the custom data block, or nullptr in case of an error (or if the data is not present). The user is in charge of releasing the returned buffer with [simReleaseBuffer](simReleaseBuffer_cpp.md).

## See also

- [custom data block related functions](../apiFunctions-1.md#customDataBlocks)
- [data packing/unpacking functions](../apiFunctions-1.md#packing)
