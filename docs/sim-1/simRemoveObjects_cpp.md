# simRemoveObjects

Removes one or several objects from the scene

## Synopsis

```cpp
int simRemoveObjects(const int* objectHandles, int count)
```

## Parameters

- **objectHandles**: handles of the objects to remove
- **count**: number of objects to remove. Negative value indicates a delayed removal

## Return values

- -1 if operation was not successful

## See also

- [simRemoveModel](simRemoveModel_cpp.md)
