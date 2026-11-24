# simGetObjectChild

Retrieves the handle of an object's child object

## Synopsis

```cpp
int simGetObjectChild(int objectHandle, int index)
```

## Parameters

- **objectHandle**: handle of the object, or sim_handle_scene to retrieve orphan objects
- **index**: zero-based index of the child's position. To retrieve all children of an object, call the function by increasing the index until the return value is -1

## Return values

- handle of child object or -1 if the child doesn't exist at that index or in case of an error

## See also

- [simGetObjectParent](simGetObjectParent_cpp.md)
- [simGetObjectsInTree](simGetObjectsInTree_cpp.md)
