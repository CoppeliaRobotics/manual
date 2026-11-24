# simGetObjectSel

Retrieves the handles of selected objects

## Synopsis

```cpp
int* simGetObjectSel(int* cnt)
```

## Parameters

- **cnt**: the number of selected objects

## Return values

- a pointer to the selected objects. The user is in charge of releasing the buffer via [simReleaseBuffer](simReleaseBuffer_cpp.md)

## See also

- [simSetObjectSel](simSetObjectSel_cpp.md)
