# simPushFloatTableOntoStack

Pushes a float array onto the stack. The table will then be located at the top of the stack

## Synopsis

```cpp
int simPushFloatTableOntoStack(int stackHandle, const float* values, int valueCnt)
```

## Parameters

- **stackHandle**: stack handle obtained with [simCreateStack](simCreateStack_cpp.md).
- **values**: float array.
- **valueCnt**: size of the array.

## Return values

- -1 in case of an error.

## See also

- [stack functions](../apiFunctions-1.md#stacks)
