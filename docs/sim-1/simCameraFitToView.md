# sim.cameraFitToView

Shifts and adjusts a camera associated with a view to fill the view entirely with the specified objects or models

## Synopsis

```lua
int result = sim.cameraFitToView(int viewHandleOrIndex, int[] objectHandles = nil, int options = 0,
                                 float scaling = 1)
```

```python
int result = sim.cameraFitToView(int viewHandleOrIndex, list objectHandles = None, int options = 0,
                                 float scaling = 1)
```

## Parameters

- **viewHandleOrIndex**: handle of the view (can also be a floating view), or the index of the view. If the camera is not associated with any view, then you can specify the handle of the camera, together with the *sim.handleflag_camera* flag.
- **objectHandles**: object handles. Only visible objects will be taken into account. Can be None/nil, in which case the whole visible scene will be filling the view.
- **options**: bit-coded:

    - bit0 (1): if set, then individual objects will be filling the view. If not set, then models associated with model base objects will also be included
    - bit1 (2): if set, then the view proportions will be 1 by 1, independently on what the view size is
- **scaling**: scaling factor. Use 1.0 for normal behaviour.

## Return values

- **result**: 0 for a silent error (e.g. when the indicated view doesn't exist anymore), 1 for success

## See also

- [sim.adjustView](simAdjustView.md)
- [sim.floatingViewAdd](simFloatingViewAdd.md)
