# simIsHandle

Checks whether a general object handle is still valid. When a general object is destroyed (e.g. programmatically or via the user interface), then its related handle is not valid anymore and will trigger an error when used. Use this function to avoid triggering an error

## Synopsis

```cpp
int simIsHandle(int objectHandle, int reserved = -1)
```

## Parameters

- **objectHandle**: handle of the object
- **reserved**: set to -1

## Return values

- -1 if operation was not successful, 0 if the handle is not valid anymore, or 1 if the handle is still valid.

## See also

- [simGetObject](simGetObject_cpp.md)
