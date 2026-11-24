# simGetObjectFromUid

Retrieves an object handle based on its unique identifier

## Synopsis

```cpp
int simGetObjectfromUid(long long int objectUid, int options)
```

## Parameters

- **objectUid**: the object unique identifier.
- **options**: bit-coded. bit0 set (i.e. 1): errors are silent.

## Return values

- handle of object or -1 if operation was not successful

## See also

- [simGetObjectUid](simGetObjectUid_cpp.md)
