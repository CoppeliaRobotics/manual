# simWriteCustomDataBlock

Adds or removes custom data to be stored and saved together with an object, or the scene. If the tag name ends with the string "@tmp", then the data is not saved during a scene or model save operation. The data can also be saved globally for the application (for the current CoppeliaSim session)

## Synopsis

```cpp
int simWriteCustomDataBlock(int objectHandle, const char* tagName, const char* data, int dataSize)
```

## Parameters

- **objectHandle**: handle of the object where you want to store your data, or sim.handle_scene if you wish to store the data with the scene, or sim.handle_app if you wish to store the data with the application's current session.
- **tagName**: string that identifies the data. An empty string will remove all custom data blocks
- **data**: your custom data. If nullptr or empty, the current data under the specified dataName will be removed
- **dataSize**: size of your custom data

## Return values

- -1 if operation was not successful

## See also

- [simSetReferencedHandles](simSetReferencedHandles_cpp.md)
- [custom data block related functions](../apiFunctions-1.md#customDataBlocks)
- [data packing/unpacking functions](../apiFunctions-1.md#packing)
