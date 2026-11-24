# simUnpackTable

Unpacks a buffer into a table

## Synopsis

```cpp
int simUnpackTable(int stackHandle, const char* buffer, int bufferSize)
```

## Parameters

- **stackHandle**: stack handle obtained with [simCreateStack](simCreateStack_cpp.md). The unpacked table will be pushed onto the stack.
- **buffer**: packed table (buffer)
- **bufferSize**: size of the buffer

## Return values

- -1 in case of an error.

## See also

- [simPackTable](simPackTable_cpp.md)
- [packing/unpacking functions](../apiFunctions-1.md#packing)
