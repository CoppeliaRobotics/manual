# simAdjustView

Adjusts parameters of a view

## Synopsis

```cpp
int simAdjustView(int viewHandleOrIndex, int associatedViewableObjectHandle, int options,
                  const char* viewLabel)
```

## Parameters

- **viewHandleOrIndex**: the handle of the view (can also be a floating view), or the index of the view.
- **associatedViewableObjectHandle**: handle of the object that you wish to associate with the view. Must be a viewable object. Can also be -1, in which case the view is emptied
- **options**: bit-coded:

    - **bit0-bit5**= 0
    - **bit6 (64)** set=floating view is removed at simulation end
    - **bit7 (128)** set=floating view is ignored during a scene save operation
    - **bit8 (256)** set=the view is not modified. The return value of the function indicates if the view still exists (2), or does not exist anymore (1). No error is generated.
    - **bit9 (512)** set=the view is not modified. The return value of the function represents the object associated with the view.
- **viewLabel**: a label that will be displayed at the top of a floating view. If nullptr is specified, then the name of the associated viewable object is taken as label.

## Return values

- a value &gt;0 in case of success

## See also

- [simFloatingViewAdd](simFloatingViewAdd_cpp.md)
- [simCameraFitToView](simCameraFitToView_cpp.md)
