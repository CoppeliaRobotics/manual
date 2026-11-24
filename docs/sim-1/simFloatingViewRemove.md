# sim.floatingViewRemove

Removes a floating view previously added with [sim.floatingViewAdd](simFloatingViewAdd.md).

## Synopsis

```lua
int result = sim.floatingViewRemove(int floatingViewHandle)
```

```python
int result = sim.floatingViewRemove(int floatingViewHandle)
```

## Parameters

- **floatingViewHandle**: handle of the floating view to be removed

## Return values

- **result**: 0 if the floating view could not be found (e.g. because closed by the user), or 1 if the floating view was closed.
