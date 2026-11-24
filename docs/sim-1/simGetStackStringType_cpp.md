# simGetStackStringType

Returns the type of a specific stack string

## Synopsis

```cpp
int simGetStackStringType(int stackHandle, int cIndex)
```

## Parameters

- **stackHandle**: a stack handle obtained with [simCreateStack](simCreateStack_cpp.md).
- **cIndex**: the zero-based index of the stack string. Negative values indicate reverse counting from the top of the stack (i.e. -1 indicates the stack top)

## Return values

- -1 in case of an error, otherwise the [string type](../apiConstants-1.md#stringTypes)

## See also

- [stack functions](../apiFunctions-1.md#stacks)
