# sim.removeModel

Removes a model from the scene

## Synopsis

```lua
int removedCnt = sim.removeModel(int objectHandle, bool delayedRemoval = false)
```

```python
int removedCnt = sim.removeModel(int objectHandle, bool delayedRemoval = False)
```

## Parameters

- **objectHandle**: handle of the model (i.e. object tagged as model) to remove
- **delayedRemoval**: whether the removal should be delayed (e.g. when a script destroys itself). Defaults to false

## Return values

- **removedCnt**: number of removed objects (a model might contain several objects)

## See also

- [sim.removeObjects](simRemoveObjects.md)
