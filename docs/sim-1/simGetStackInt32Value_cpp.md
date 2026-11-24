# simGetStackInt32Value

Tries to retrieve the value at the top of the stack, if that value is a number

## Synopsis

```cpp
int simGetStackInt32Value(int stackHandle, int* numberValue)
```

## Parameters

- **stackHandle**: a stack handle obtained with [simCreateStack](simCreateStack_cpp.md).
- **numberValue**: a pointer to a location receiving the int32 value.

## Return values

- -1 in case of an error, 0 if the value is not a number, 1 otherwise.

## See also

- [stack functions](../apiFunctions-1.md#stacks)
