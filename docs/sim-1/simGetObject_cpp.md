# simGetObject

Retrieves an object handle based on its path and alias

## Synopsis

```cpp
int simGetObject(const char* objectPath, int index, int proxy, int options)
```

## Parameters

- **objectPath**: path and alias of the object to find. See the section on [accessing scene objects](../accessingSceneObjects.md) for details.
- **index**: fetches the n-th object (zero based index) that satisfies the object path. -1 returns the first object that satisfies the object path.
- **proxy**: if different from -1, specifies an object handle that identifies a hierarchy tree to search in.
- **options**: bit-coded. bit0 set (i.e. 1): errors are silent.

## Return values

- handle of object or -1 if operation was not successful

## See also

- [simIsHandle](simIsHandle_cpp.md)
- [simGetObjectUid](simGetObjectUid_cpp.md)
