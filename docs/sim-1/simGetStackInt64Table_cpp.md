# simGetStackInt64Table

Retrieves an int64 array from an array-type table at the top of the stack. Table values that are not numbers are converted to 0

## Synopsis

```cpp
int simGetStackInt64Table(int stackHandle, long long int* array, int count)
```

## Parameters

- **stackHandle**: a stack handle obtained with [simCreateStack](simCreateStack_cpp.md).
- **array**: a pointer to a location receiving the integer values. Use [simGetStackTableInfo](simGetStackTableInfo_cpp.md) to determine the number of values the table contains.
- **count**: the size of the array. If the array is bigger than the table, it will be padded with 0.

## Return values

- -1 in case of an error, 0 if item is not an array or does not contain only numbers, 1 otherwise.

## See also

- [simGetStackTableInfo](simGetStackTableInfo_cpp.md)
- [stack functions](../apiFunctions-1.md#stacks)
