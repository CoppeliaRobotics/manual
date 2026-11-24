# sim.saveModel

Saves a model (an object marked as "Object is model base" and all other objects in its hierarchy tree). Any existing file with same name will be overwritten

## Synopsis

```lua
buffer modelData = sim.saveModel(int baseOfModelHandle, string filename = nil)
```

```python
bytes buffer = sim.saveModel(int baseOfModelHandle, string filename = None)
```

## Parameters

- **baseOfModelHandle**: handle of an object marked as "Object is model base"
- **filename**: model filename. The filename extension is required (*ttm*, or *simmodel.xml* ). If this argument is omitted, the model is saved to a buffer which is returned

## Return values

- **modelData**: a buffer containing the saved model, if the model was specified to be saved to memory

## See also

- [sim.loadModel](simLoadModel.md)
- [sim.saveScene](simSaveScene.md)
