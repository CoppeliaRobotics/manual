# simInsertDataIntoStackTable

Inserts data into a table on the stack. The function expects a *value* at the top of the stack, a *key* one position below, and a table below that. The value and its associated key will be inserted into the table and removed from the stack. If successive values are inserted with consecutive number keys starting at 1, then the table values can be accessed via number indices in a script, and the table can be seen as an array. Otherwise, the table can be seen as a map or associative array

## Synopsis

```cpp
int simInsertDataIntoStackTable(int stackHandle)
```

## Parameters

- **stackHandle**: a stack handle obtained with [simCreateStack](simCreateStack_cpp.md).

## Return values

- -1 in case of an error.

## See also

- [stack functions](../apiFunctions-1.md#stacks)
