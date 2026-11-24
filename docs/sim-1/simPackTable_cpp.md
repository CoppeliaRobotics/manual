# simPackTable

Packs a table into a buffer. The table may contain other nested arrays, maps, None/nil, bool, number, string or matrix values. All other types (e.g. functions) will be considered as string or None/nil values. You can also use sim.packTable to quickly compare two tables

## Synopsis

```cpp
char* simPackTable(int stackHandle, int* bufferSize)
```

## Parameters

- **stackHandle**: stack handle obtained with [simCreateStack](simCreateStack_cpp.md). There must be a table located at the top of the stack.
- **bufferSize**: size of the returned buffer.

## Return values

- nullptr in case of an error, otherwise a data buffer. The user is in charge of releasing the returned buffer with [simReleaseBuffer](simReleaseBuffer_cpp.md).

## See also

- [simUnpackTable](simUnpackTable_cpp.md)
- [packing/unpacking functions](../apiFunctions-1.md#packing)
