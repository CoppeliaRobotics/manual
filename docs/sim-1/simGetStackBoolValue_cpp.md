# simGetStackBoolValue

Tries to retrieve the value at the top of the stack, if that value is a bool

## Synopsis

```cpp
int simGetStackBoolValue(int stackHandle, bool* boolValue)
```

## Parameters

- **stackHandle**: a stack handle obtained with [simCreateStack](simCreateStack_cpp.md).
- **boolValue**: a pointer to a location receiving the bool value.

## Return values

- -1 in case of an error, 0 if the value is not a bool, 1 otherwise.

## See also

- [stack functions](../apiFunctions-1.md#stacks)
