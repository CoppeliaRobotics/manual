# sim.addDrawingObjectItem

Adds an item (or clears all items) to a previously inserted drawing object

## Synopsis

```lua
int result = sim.addDrawingObjectItem(int drawingObjectHandle, float[] itemData)
```

```python
int result = sim.addDrawingObjectItem(int drawingObjectHandle, list itemData)
```

## Parameters

- **objectHandle**: handle of a previously added drawing object. Can be combined with sim.handleflag_addmultiple to add several drawing items at once, or with sim.handleflag_codedstring, when one wishes to provide data as a float buffer
- **itemData**: data relative to an item. If the item is a point item, 3 values are required [x y z]. If the item is a line item, 6 values are required, etc. None/nil to empty the drawing object

## Return values

- **result**: If the point was added, the return value is &gt;0, if it was not added the return value is 0

## See also

- [sim.addDrawingObject](simAddDrawingObject.md)
- [sim.removeDrawingObject](simRemoveDrawingObject.md)
