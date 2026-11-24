# simSetObjectSel

Sets the object selection state

## Synopsis

```cpp
int simSetObjectSel(const int* handles, int cnt)
```

## Parameters

- **handles**: the handles of objects, or nullptr
- **cnt**: the number of objects

## Return values

- The number of selected objects, or -1 in case of an error

## See also

- [simGetObjectSel](simGetObjectSel_cpp.md)
