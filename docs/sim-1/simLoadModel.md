# sim.loadModel

Loads a previously saved model, and selects it

## Synopsis

```lua
a) int objectHandle = sim.loadModel(string filename)
b) int objectHandle = sim.loadModel(buffer buffer)
c) buffer rgbaImage = sim.loadModel(string filename, bool onlyThumbnail)
d) buffer rgbaImage = sim.loadModel(buffer buffer, bool onlyThumbnail)
```

```python
a) int objectHandle = sim.loadModel(string filename)
b) int objectHandle = sim.loadModel(bytes buffer)
c) bytes rgbaImage = sim.loadModel(string filename, bool onlyThumbnail)
d) bytes rgbaImage = sim.loadModel(bytes buffer, bool onlyThumbnail)
```

## Parameters

- **filename**: model filename. The filename extension is required (*ttm*, or *simmodel.xml*).
- **buffer**: a buffer containing the model
- **onlyThumbnail**: when true, then only the thumbnail image of the model is loaded and returned

## Return values

- **objectHandle**: the handle of the model base object
- **rgbaImage**: the model thumbnail image (128 x 128 x 4, rgba)

## See also

- [sim.saveModel](simSaveModel.md)
- [sim.loadScene](simLoadScene.md)
