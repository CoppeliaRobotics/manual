# simPushTextOntoStack

Pushes a text string onto the stack. The string will then be located at the top of the stack

## Synopsis

```cpp
int simPushTextOntoStack(int stackHandle, const char* value)
```

## Parameters

- **stackHandle**: stack handle obtained with [simCreateStack](simCreateStack_cpp.md).
- **value**: a text string

## Return values

- -1 in case of an error.

## See also

- [simPushBufferOntoStack](simPushBufferOntoStack_cpp.md)
- [stack functions](../apiFunctions-1.md#stacks)
