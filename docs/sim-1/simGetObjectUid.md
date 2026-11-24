# sim.getObjectUid

Retrieves the unique identifier of an object: throughout a CoppeliaSim session, there won't be two identical unique identifiers. Unique identifiers are however not persistent (i.e. are not saved with the object)

## Synopsis

```lua
int uid = sim.getObjectUid(int objectHandle)
```

```python
int uid = sim.getObjectUid(int objectHandle)
```

## Parameters

- **objectHandle**: object handle

## Return values

- **uid**: the unique identifier

## See also

- [sim.getObjectFromUid](simGetObjectFromUid.md)
