# simPushStringOntoStack

Pushes an undifferentiated binary string onto the stack. The string may contain any values, including embedded zeros, and may represent text or any other data. The string will then be located at the top of the stack

## Synopsis

```cpp
int simPushStringOntoStack(int stackHandle, const char* value, int stringSize)
```

## Parameters

- **stackHandle**: stack handle obtained with [simCreateStack](simCreateStack_cpp.md).
- **value**: a binary string
- **stringSize**: length of the binary string.

## Return values

- -1 in case of an error.

## See also

- [simPushTextOntoStack](simPushTextOntoStack_cpp.md)
- [simPushBufferOntoStack](simPushBufferOntoStack_cpp.md)
- [stack functions](../apiFunctions-1.md#stacks)
