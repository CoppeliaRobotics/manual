# sim.getReferencedHandlesTags

Retrieves a list of all referenced handles tags

## Synopsis

```lua
string[] tags = sim.getReferencedHandlesTags(int objectHandle)
```

```python
list tags = sim.getReferencedHandlesTags(int objectHandle)
```

## Parameters

- **objectHandle**: handle of the scene object that stores the list of handles. Can be optionally combined with *sim.handleflag_keeporiginal*, in which case the handles that link to originals are retrieved.

## Return values

- **tags**: an array with found tags

## See also

- [sim.getReferencedHandles](simGetReferencedHandles.md)
