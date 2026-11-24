# sim.isHandle

Checks whether a general object handle is still valid. When a general object is destroyed (e.g. programmatically or via the user interface), then its related handle is not valid anymore and will trigger an error when used. Use this function to avoid triggering an error

## Synopsis

```lua
bool result = sim.isHandle(int objectHandle)
```

```python
bool result = sim.isHandle(int objectHandle)
```

## Parameters

- **objectHandle**: handle of the object

## Return values

- **result**: whether the handle is valid

## See also

- [sim.getObject](simGetObject.md)
