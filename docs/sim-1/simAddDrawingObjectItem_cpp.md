# simAddDrawingObjectItem

Adds an item (or clears all items) to a previously inserted drawing object

## Synopsis

```cpp
int simAddDrawingObjectItem(int objectHandle, const double* itemData)
```

## Parameters

- **objectHandle**: handle of a previously added drawing object
- **itemData**: data relative to an item. If the item is a point item, 3 values are required (x;y;z). If the item is a line item, 6 values are required, etc. Specifying nullptr will empty the drawing object

## Return values

- -1 if operation was not successful. If the point was added, then the return value is &gt;0, if it was not added (e.g. drawing object is saturated or the item was merged with an existing item), then the return value will be 0.

## See also

- [simAddDrawingObject](simAddDrawingObject_cpp.md)
- [simRemoveDrawingObject](simRemoveDrawingObject_cpp.md)
