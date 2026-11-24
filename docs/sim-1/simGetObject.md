# sim.getObject

Retrieves an object handle based on its path and alias

## Synopsis

```lua
int objectHandle = sim.getObject(string objectPath, table options = {})
```

```python
int objectHandle = sim.getObject(string objectPath, dict options = {})
```

## Parameters

- **objectPath**: path and alias of the object to find. See the section on [accessing scene objects](../accessingSceneObjects.md) for details.
- **options**: optional map indicating how the object should be searched:

    - noError(bool): can generate a silent error if an object was not found
    - index(int): fetches the n-th object (zero based index) that satisfies the specified objectPath
    - proxy(int):allows to search the hierarchy tree of the specified proxy object

## Return values

- **objectHandle**: handle of object or -1

## See also

- [sim.isHandle](simIsHandle.md)
- [sim.getObjectUid](simGetObjectUid.md)
