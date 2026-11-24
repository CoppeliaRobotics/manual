# simGetStackItemType

Returns the type of a specific stack item

## Synopsis

```cpp
int simGetStackItemType(int stackHandle, int cIndex)
```

## Parameters

- **stackHandle**: a stack handle obtained with [simCreateStack](simCreateStack_cpp.md).
- **cIndex**: the zero-based index of the stack item. Negative values indicate reverse counting from the top of the stack (i.e. -1 indicates the stack top)

## Return values

- -1 in case of an error, otherwise the [stack item type](../apiConstants-1.md#stackItemTypes)

## See also

- [stack functions](../apiFunctions-1.md#stacks)
