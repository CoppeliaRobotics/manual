# simFloatingViewRemove

Removes a floating view previously added with [sim.floatingViewAdd](simFloatingViewAdd.md).

## Synopsis

```cpp
int simFloatingViewRemove(int floatingViewHandle)
```

## Parameters

- **floatingViewHandle**: handle of the floating view to be removed

## Return values

- -1 in case of an error, 0 if the floating view could not be found (e.g. because closed by the user), or 1 if the floating view was closed.
