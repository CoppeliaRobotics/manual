# simPopStackItem

Removes the top item in the stack, effectively reducing the stack size by one

## Synopsis

```cpp
int simPopStackItem(int stackHandle, int count)
```

## Parameters

- **stackHandle**: stack handle obtained with [simCreateStack](simCreateStack_cpp.md).
- **count**: number of items to pop, or 0 to clear the stack.

## Return values

- -1 in case of an error, otherwise the new size of the stack.

## See also

- [simMoveStackItemToTop](simMoveStackItemToTop_cpp.md)
- [stack functions](../apiFunctions-1.md#stacks)
