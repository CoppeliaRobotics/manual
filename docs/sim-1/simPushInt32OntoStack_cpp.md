# simPushInt32OntoStack

Pushes an int32 value (i.e. a Lua number) onto the stack. The value will then be located at the top of the stack

## Synopsis

```cpp
int simPushInt32OntoStack(int stackHandle, int value)
```

## Parameters

- **stackHandle**: stack handle obtained with [simCreateStack](simCreateStack_cpp.md).
- **value**: value to push.

## Return values

- -1 in case of an error.

## See also

- [stack functions](../apiFunctions-1.md#stacks)
