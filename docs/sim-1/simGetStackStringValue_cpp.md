# simGetStackStringValue

Tries to retrieve the value at the top of the stack, if that value is a string

## Synopsis

```cpp
char* simGetStackStringValue(int stackHandle, int* stringSize)
```

## Parameters

- **stackHandle**: a stack handle obtained with [simCreateStack](simCreateStack_cpp.md).
- **stringSize**: a pointer to a location receiving the size of the string. Can be nullptr if the string size is of no interest.

## Return values

- in case of an error, the return value is nullptr and *stringSize* is set to -1. If the stack item is not a string, the return value is nullptr and *stringSize* is set to 0. If the stack item is a string, the return value is not nullptr, and *stringSize* is the size of the string buffer (in that case, the user is in charge of releasing the returned buffer with [simReleaseBuffer](simReleaseBuffer_cpp.md))

## See also

- [stack functions](../apiFunctions-1.md#stacks)
