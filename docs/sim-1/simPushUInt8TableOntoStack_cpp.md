# simPushUInt8TableOntoStack

Pushes a uint8 array onto the stack, as a table filled with Lua numbers. The table will then be located at the top of the stack

## Synopsis

```cpp
int simPushUInt8TableOntoStack(int stackHandle, const unsigned char* values, int valueCnt)
```

## Parameters

- **stackHandle**: stack handle obtained with [simCreateStack](simCreateStack_cpp.md).
- **values**: uint8 array.
- **valueCnt**: size of the array.

## Return values

- -1 in case of an error.

## See also

- [stack functions](../apiFunctions-1.md#stacks)
