# sim.floatingViewAdd

Adds a floating view to current page

## Synopsis

```lua
int floatingViewHandle = sim.floatingViewAdd(float posX, float posY, float sizeX, float sizeY,
                                             int options)
```

```python
int floatingViewHandle = sim.floatingViewAdd(float posX, float posY, float sizeX, float sizeY,
                                             int options)
```

## Parameters

- **posX & posY**: relative position of the center of the floating view. Accepted values are between 0.0 and 1.0
- **sizeX & sizeY**: relative size of the floating view. Accepted values are between 0.0 and 1.0
- **options**: bit-coded:

    - bit0 set (1): double click allows swapping the floating view with the main view
    - bit1 set (2): the floating view doesn't have a close button
    - bit2 set (4): the floating view cannot be shifted
    - bit3 set (8): the floating view cannot be resized

## Return values

- **floatingViewHandle**: handle of the floating view

## See also

- [sim.floatingViewRemove](simFloatingViewRemove.md)
- [sim.adjustView](simAdjustView.md)
- [sim.cameraFitToView](simCameraFitToView.md)
