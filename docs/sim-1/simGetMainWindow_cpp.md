# simGetMainWindow

Retrieves the handle or pointer of the main window.

## Synopsis

```cpp
void* simGetMainWindow(int type)
```

## Parameters

- **type**: type of the desired return value. 0 for a native window handle, 1 for a pointer to a QWidget object.

## Return values

- a native window handle or a pointer to a QWidget object.
