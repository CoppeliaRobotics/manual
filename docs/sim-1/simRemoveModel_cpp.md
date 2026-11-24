# simRemoveModel

Removes a model from the scene

## Synopsis

```cpp
int simRemoveModel(int objectHandle)
```

## Parameters

- **objectHandle**: handle of the model (i.e. object tagged as model) to remove. A negative value indicates a delayed removal (in that case this argument should be -objectHandle -1

## Return values

- -1 if operation was not successful, otherwise the number of removed objects (a model might contain several objects)

## See also

- [simRemoveObjects](simRemoveObjects_cpp.md)
