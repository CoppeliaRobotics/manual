# sim.copyPasteObjects

Copies and pastes objects

## Synopsis

```lua
int[] copiedObjectHandles = sim.copyPasteObjects(int[] objectHandles, int options)
```

```python
list copiedObjectHandles = sim.copyPasteObjects(list objectHandles, int options)
```

## Parameters

- **objectHandles**: array of object handles to copy and paste
- **options**: bit-coded:

    - bit0 is set (i.e. 1): whole models are copied. In that case, all specified objects should be flagged as *model base*
    - bit1 is set (i.e. 2): all simulation and customization scripts are stripped away
    - bit2 is set (i.e. 4): all object [custom data properties](../properties.md#customData) are stripped away
    - bit3 is set (i.e. 8): all object references are stripped away
    - bit4 is set (i.e. 16): all textures are stripped away
    - bit5 is set (i.e. 32): model tags and DNA information is stripped away

## Return values

- **copiedObjectHandles**: the duplicate object handles, where original and copy have the same location in their respective arrays (when script objects are stripped away, the array could contain -1 values)

## See also

- [sim.removeObjects](simRemoveObjects.md)
- [sim.removeModel](simRemoveModel.md)
- [sim.saveModel](simSaveModel.md)
- [sim.loadModel](simLoadModel.md)
