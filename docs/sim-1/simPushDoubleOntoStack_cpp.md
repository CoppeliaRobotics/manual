# simPushDoubleOntoStack

Pushes a double precision value (i.e. a Lua number) onto the stack. The value will then be located at the top of the stack

## Synopsis

```cpp
int simPushDoubleOntoStack(int stackHandle, double value)
```

## Parameters

- **stackHandle**: stack handle obtained with [simCreateStack](simCreateStack_cpp.md).
- **value**: value to push.

## Return values

- -1 in case of an error.

## See also

- [stack functions](../apiFunctions-1.md#stacks)
