# simDebugStack

Prints the content of the specified stack to the console

## Synopsis

```cpp
int simDebugStack(int stackHandle, int cIndex)
```

## Parameters

- **stackHandle**: a stack handle obtained with [simCreateStack](simCreateStack_cpp.md).
- **cIndex**: the zero-based index of the stack location to print, or -1 to print the full stack.

## Return values

- -1 in case of an error.

## See also

- [stack functions](../apiFunctions-1.md#stacks)
