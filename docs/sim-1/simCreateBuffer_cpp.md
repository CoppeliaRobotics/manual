# simCreateBuffer

Creates a buffer. The buffer needs to be released with [simReleaseBuffer](simReleaseBuffer_cpp.md) except otherwise explicitly specified.

## Synopsis

```cpp
void* simCreateBuffer(int size)
```

## Parameters

- **size**: size of the buffer

## Return values

- buffer if operation was successful, nullptr otherwise
