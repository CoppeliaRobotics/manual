# sim.getObjectChild

Retrieves the handle of an object's child object

## Synopsis

```lua
int childHandle = sim.getObjectChild(int objectHandle, int index)
```

```python
int childHandle = sim.getObjectChild(int objectHandle, int index)
```

## Parameters

- **objectHandle**: handle of the object, or sim.handle_scene to retrieve orphan objects
- **index**: zero-based index of the child's position. To retrieve all children of an object, call the function by increasing the index until the return value is -1

## Return values

- **childHandle**: handle of child object or -1 if the child doesn't exist at that index

## See also

- [sim.getObjectParent](simGetObjectParent.md)
- [sim.getObjectsInTree](simGetObjectsInTree.md)
