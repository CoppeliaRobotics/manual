# simSaveModel

Saves a model (an object marked as "Object is model base" and all other objects in its hierarchy tree). Any existing file with same name will be overwritten

## Synopsis

```cpp
int simSaveModel(int baseOfModelHandle, const char* filename)
```

## Parameters

- **baseOfModelHandle**: handle of an object marked as "Object is model base"
- **filename**: model filename. The filename extension is required (*ttm*, or *simmodel.xml*)

## Return values

- -1 if operation was not successful

## See also

- [simLoadModel](simLoadModel_cpp.md)
- [simSaveScene](simSaveScene_cpp.md)
