# simCopyPasteObjects

Copies and pastes objects

## Synopsis

```cpp
int simCopyPasteObjects(int* objectHandles, int objectCount, int options)
```

## Parameters

- **objectHandles**: array containing the handles of the objects to copy and paste. The same array will receive the copied object handles, with the same correspondency.
- **objectCount**: the number of handles contained in the objectHandles array.
- **options**: bit-coded. If bit0 is set (i.e. 1), then whole models will be copied. In that case, all specified objects should be flagged as *model base*. If bit1 is set (i.e. 2), then all simulation and customization scripts are stripped away. If bit2 is set (i.e. 4), then all object [custom data properties](../properties.md#customData) are stripped away. If bit3 is set (i.e. 8), then all object references are stripped away. If bit4 is set (i.e. 16), then all textures are stripped away. If bit5 is set (i.e. 32), then model tags and DNA information is stripped away.

## Return values

- -1 if operation was not successful.

## See also

- [simRemoveObjects](simRemoveObjects_cpp.md)
- [simRemoveModel](simRemoveModel_cpp.md)
- [simSaveModel](simSaveModel_cpp.md)
- [simLoadModel](simLoadModel_cpp.md)
