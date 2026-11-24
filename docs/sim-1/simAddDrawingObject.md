# sim.addDrawingObject

Adds a drawing object that will be displayed in the scene. Drawing objects are containers that hold several items of a given type. This can be used for several different applications (simulation of paint, simulation of welding seam, display of 3D objects, etc.). Drawing objects created in a [simulation script](../simulationScripts.md) will be automatically removed at simulation end

## Synopsis

```lua
int drawingObjectHandle = sim.addDrawingObject(int objectType, float size, float duplicateTolerance,
                                               int parentObjectHandle, int maxItemCount,
                                               float[3] color = nil)
```

```python
int drawingObjectHandle = sim.addDrawingObject(int objectType, float size, float duplicateTolerance,
                                               int parentObjectHandle, int maxItemCount,
                                               list color = None)
```

## Parameters

- **objectType**: a [drawing object type combined with attributes](../apiConstants-1.md#customDrawingObjects)
- **size**: size of the item (width of lines or size of points are in pixels, other sizes are in meters
- **duplicateTolerance**: if different from 0.0, then a call to [simAddDrawingObjectItem](simAddDrawingObjectItem.md) will only add the item if there is no other item within duplicateTolerance distance. Useful to avoid adding a too high density of points, is however not appropriate when using a large number of points (slower operation). Applicable only for single vertex items.
- **parentObjectHandle**: handle of the scene object where the drawing items should keep attached to (if the scene object moves, the drawing items will also move), or -1 if the drawing items are relative to the world (fixed)
- **maxItemCount**: maximum number of items this object can hold. 0 uses a default size of 1000.
- **color**: default color (3 rgb values). Can be None/nil

## Return values

- handle of the drawing object

## See also

- [sim.addDrawingObjectItem](simAddDrawingObjectItem.md)
- [sim.removeDrawingObject](simRemoveDrawingObject.md)
