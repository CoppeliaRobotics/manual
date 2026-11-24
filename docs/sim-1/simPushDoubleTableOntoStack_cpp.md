# simPushDoubleTableOntoStack

Pushes a double-precision array onto the stack, as a table filled with Lua numbers. The table will then be located at the top of the stack

## Synopsis

```cpp
int simPushDoubleTableOntoStack(int stackHandle, const double* values, int valueCnt)
```

## Parameters

- **stackHandle**: stack handle obtained with [simCreateStack](simCreateStack_cpp.md).
- **values**: double-precision array.
- **valueCnt**: size of the array.

## Return values

- -1 in case of an error.

## See also

- [stack functions](../apiFunctions-1.md#stacks)
