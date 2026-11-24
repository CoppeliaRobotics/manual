# simGetCollectionObjects

Retrieves the object handles that compose a [collection](../collections.md)

## Synopsis

```cpp
int* simGetCollectionObjects(int collectionHandle, int* objectCount)
```

## Parameters

- **collectionHandle**: handle of the collection
- **objectCount**: pointer to a value receiving the number of returned object handles

## Return values

- pointer to n object handles, or nullptr if an error occurred. The user is in charge of destroying the returned buffer with [simReleaseBuffer](simReleaseBuffer_cpp.md)

## See also

- [functions related to collections](../apiFunctions-1.md#collections)
