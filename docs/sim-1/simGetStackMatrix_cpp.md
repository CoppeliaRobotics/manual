# simGetStackMatrix

Tries to retrieve the value at the top of the stack, if that value is a matrix

## Synopsis

```cpp
double* simGetStackMatrix(int stackHandle, int* rows, int* cols)
```

## Parameters

- **stackHandle**: a stack handle obtained with [simCreateStack](simCreateStack_cpp.md).
- **rows**: a pointer to a location receiving the number of rows. Can be nullptr
- **cols**: a pointer to a location receiving the number of columns. Can be nullptr

## Return values

- in case of an error, the return value is nullptr and *rows*/*cols* are set to -1. If the stack item is not a matrix, the return value is nullptr and *rows*/*cols* are set to 0. The user is in charge of releasing the returned buffer with [simReleaseBuffer](simReleaseBuffer_cpp.md))

## See also

- [stack functions](../apiFunctions-1.md#stacks)
