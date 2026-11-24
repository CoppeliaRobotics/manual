# sim.getObjectFromUid

Retrieves an object handle based on its unique identifier

## Synopsis

```lua
int objectHandle = sim.getObjectFromUid(int objectUid, table options = {})
```

```python
int objectHandle = sim.getObjectFromUid(int objectUid, dict options = {})
```

## Parameters

- **objectUid**: the object unique identifier.
- **options**: optional map indicating how the object should be searched. {**noError**=true} will generate a silent error if an object was not found.

## Return values

- **objectHandle**: handle of object

## See also

- [sim.getObjectUid](simGetObjectUid.md)
