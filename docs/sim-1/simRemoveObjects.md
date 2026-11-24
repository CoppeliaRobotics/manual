# sim.removeObjects

Removes one or several objects from the scene

## Synopsis

```lua
sim.removeObjects(int[] objectHandles, bool delayedRemoval = false)
```

```python
sim.removeObjects(int[] objectHandles, bool delayedRemoval = False)
```

## Parameters

- **objectHandles**: handles of the objects to remove
- **delayedRemoval**: whether the removal should be delayed (e.g. when a script destroys itself). Defaults to false

## Return values

No return values.

## See also

- [sim.removeModel](simRemoveModel.md)
