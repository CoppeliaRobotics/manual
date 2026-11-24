# simLoadScene

Loads a previously saved scene

## Synopsis

```cpp
int simLoadScene(const char* filename)
```

## Parameters

- **filename**: scene filename, including extension. An empty string loads the default scene. By default, the current scene is overwritten (append "@keepCurrent" to the filename to preserve current scene)

## Return values

- -1 if operation was not successful

## See also

- [simSaveScene](simSaveScene_cpp.md)
- [simLoadModel](simLoadModel_cpp.md)
- [simCloseScene](simCloseScene_cpp.md)
