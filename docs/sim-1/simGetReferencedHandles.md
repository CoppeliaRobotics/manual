# sim.getReferencedHandles

Retrieves a list of custom handles, linking a given scene object to other scene objects

## Synopsis

```lua
int[] referencedHandles = sim.getReferencedHandles(int objectHandle, string tag = '')
```

```python
list referencedHandles = sim.getReferencedHandles(int objectHandle, string tag = '')
```

## Parameters

- **objectHandle**: handle of the scene object that stores the list of handles. Can be optionally combined with *sim.handleflag_keeporiginal*, in which case the handles that link to originals are retrieved.
- **tag**: a tag: only handles stored within that tag are retrieved. defaults to an empty tag

## Return values

- **referencedHandles**: an array with scene object handles

## See also

- [sim.setReferencedHandles](simSetReferencedHandles.md)
