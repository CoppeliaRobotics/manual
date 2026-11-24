# simPushBufferOntoStack

Pushes a binary data buffer onto the stack. The buffer will then be located at the top of the stack

## Synopsis

```cpp
int simPushBufferOntoStack(int stackHandle, const char* value, int bufferSize)
```

## Parameters

- **stackHandle**: stack handle obtained with [simCreateStack](simCreateStack_cpp.md).
- **value**: a binary data buffer
- **stringSize**: length of the buffer.

## Return values

- -1 in case of an error.

## See also

- [simPushTextOntoStack](simPushTextOntoStack_cpp.md)
- [stack functions](../apiFunctions-1.md#stacks)
