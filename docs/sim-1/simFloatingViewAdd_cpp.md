# simFloatingViewAdd

Adds a floating view to current page

## Synopsis

```cpp
int simFloatingViewAdd(double posX, double posY, double sizeX, double sizeY, int options)
```

## Parameters

- **posX & posY**: relative position of the center of the floating view. Accepted values are between 0 and 1.
- **sizeX & sizeY**: relative size of the floating view. Accepted values are between 0 and 1.
- **options**: bit-coded:

    - bit0 set (1)=double click allows swapping the floating view with the main view
    - bit1 set (2)=the floating view doesn't have a close button
    - bit2 set (4)=the floating view cannot be shifted
    - bit3 set (8)=the floating view cannot be resized

## Return values

- Handle of the floating view, or -1 in case of an error.

## See also

- [simFloatingViewRemove](simFloatingViewRemove_cpp.md)
- [simAdjustView](simAdjustView_cpp.md)
- [simCameraFitToView](simCameraFitToView_cpp.md)
