# sim.closeScene

Closes current scene, and switches to another open scene. If there is no other open scene, a new scene is then created. Can only be called from an [add-on](../addOns.md), or from the sanbox script, when called from within CoppeliaSim

## Synopsis

```lua
int result = sim.closeScene()
```

```python
int result = sim.closeScene()
```

## Parameters

No parameters.

## Return values

- **result**: the current scene index.

## See also

- [sim.loadScene](simLoadScene.md)
- [sim.saveScene](simSaveScene.md)
