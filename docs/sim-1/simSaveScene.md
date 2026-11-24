# sim.saveScene

Saves a scene. Any existing file with same name will be overwritten

## Synopsis

```lua
buffer buffer = sim.saveScene(string filename = nil)
```

```python
bytes buffer = sim.saveScene(string filename = None)
```

## Parameters

- **filename**: scene filename. The filename extension is required. With None/nil, a buffer representing the serialized scene is returned

## Return values

- **buffer**: if filename is None/nil, a buffer representing the serialized scene

## See also

- [sim.loadScene](simLoadScene.md)
- [sim.closeScene](simCloseScene.md)
- [sim.saveModel](simSaveModel.md)
