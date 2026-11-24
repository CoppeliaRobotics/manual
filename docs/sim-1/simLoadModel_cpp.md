# simLoadModel

Loads a previously saved model, and selects it

## Synopsis

```cpp
int simLoadModel(const char* filename)
```

## Parameters

- **filename**: model filename. The filename extension is required (*ttm* or *simmodel.xml* ).

## Return values

- -1 if operation was not successful. Otherwise the handle of the model base object.

## See also

- [simSaveModel](simSaveModel_cpp.md)
- [simLoadScene](simLoadScene_cpp.md)
