# simGetObjectUid

Retrieves the unique identifier of an object: throughout a CoppeliaSim session, there won't be two identical unique identifiers. Unique identifiers are however not persistent (i.e. are not saved with the object)

## Synopsis

```cpp
long long int simGetObjectUid(int objectHandle)
```

## Parameters

- **objectHandle**: object handle

## Return values

- -1 if operation was not successful, otherwise the unique identifier

## See also

- [simGetObjectFromUid](simGetObjectFromUid_cpp.md)
