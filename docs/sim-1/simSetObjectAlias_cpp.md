# simSetObjectAlias

Sets the alias of an object

## Synopsis

```cpp
int simSetObjectAlias(int objectHandle, const char* objectAlias, int options = 0)
```

## Parameters

- **objectHandle**: handle of the object
- **objectAlias**: alias of the object. Allowed characters include 0-9, a-z, A-Z, and underscores. Illegal characters are replaced with underscores

## Return values

- -1 if operation was not successful

## See also

- [simGetObjectAlias](simGetObjectAlias_cpp.md)
