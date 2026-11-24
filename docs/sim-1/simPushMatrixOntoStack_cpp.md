# simPushMatrixOntoStack

Pushes a matrix onto the stack. The matrix will then be located at the top of the stack

## Synopsis

```cpp
int simPushMatrixOntoStack(int stackHandle, const double* matrix, int rows, int cols)
```

## Parameters

- **stackHandle**: stack handle obtained with [simCreateStack](simCreateStack_cpp.md).
- **matrix**: the matrix in row-major order
- **rows**: the number of rows
- **cols**: the number of columns

## Return values

- -1 in case of an error.

## See also

- [stack functions](../apiFunctions-1.md#stacks)
