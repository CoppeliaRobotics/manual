# simGetStackTableInfo

Tries to retrieve information about a possible table at the top of the stack

## Synopsis

```cpp
int simGetStackTableInfo(int stackHandle, int infoType)
```

## Parameters

- **stackHandle**: stack handle obtained with [simCreateStack](simCreateStack_cpp.md).
- **infoType**: type of information desired:

    - **0**: whether we have a table, whether the table is an array-type or map-type, and the size of the array-type table
    - **1**: whether the table contains only null values
    - **2**: whether the table contains only number values
    - **3**: whether the table contains only bool values
    - **4**: whether the table contains only string values
    - **5**: whether the table contains only table values
    - **6**: whether the table contains only matrices

## Return values

- -1 in case of an error, otherwise one of following:

  - if *infoType* is 0: a [stack table information value](../apiConstants-1.md#stackTableInfo). If the returned value is &gt;0, then this means the table is an array-type table, containing value-key pairs, where all the keys are numbers, consecutive, and starting at 1. Use [simUnfoldStackTable](simUnfoldStackTable_cpp.md) to read the content of the table
  - if *infoType* is 1: 1 if the table contains only null values
  - if *infoType* is 2: 1 if the table contains only number values
  - if *infoType* is 3: 1 if the table contains only bool values
  - if *infoType* is 4: 1 if the table contains only string values
  - if *infoType* is 5: 1 if the table contains only table values
  - if *infoType* is 6: 1 if the table contains only matrices

## See also

- [stack functions](../apiFunctions-1.md#stacks)
