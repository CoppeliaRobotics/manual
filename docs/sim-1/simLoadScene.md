# sim.loadScene

Loads a previously saved scene

## Synopsis

```lua
sim.loadScene(string/buffer filenameOrBuffer)
```

```python
sim.loadScene(string/bytes filenameOrBuffer)
```

## Parameters

- **filename**: scene buffer or scene filename, including extension. An empty string loads the default scene. By default, the current scene is overwritten (append "@keepCurrent" to the filename to preserve current scene). An empty string loads the default scene

## Return values

No return values.

## See also

- [sim.saveScene](simSaveScene.md)
- [sim.loadModel](simLoadModel.md)
- [sim.closeScene](simCloseScene.md)
