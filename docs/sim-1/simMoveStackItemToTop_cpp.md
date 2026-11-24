# simMoveStackItemToTop

Moves a stack into to the top of the stack

## Synopsis

```cpp
int simMoveStackItemToTop(int stackHandle, int cIndex)
```

## Parameters

- **stackHandle**: a stack handle obtained with [simCreateStack](simCreateStack_cpp.md).
- **cIndex**: the zero-based index of the item to move. Negative values indicate reverse counting from the top of the stack (i.e. -1 indicates the stack top)

## Return values

- -1 in case of an error.

## See also

- [simPopStackItem](simPopStackItem_cpp.md)
- [stack functions](../apiFunctions-1.md#stacks)
