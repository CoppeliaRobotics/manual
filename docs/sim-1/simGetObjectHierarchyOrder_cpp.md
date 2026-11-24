# simGetObjectHierarchyOrder

Retrieves the zero-based position of an object among its siblings in the scene hierarchy

## Synopsis

```cpp
int simGetObjectHierarchyOrder(int objectHandle, int* totalSiblingsCount)
```

## Parameters

- **objectHandle**: the handle of the object
- **totalSiblingsCount**: if not null, receives the total siblings count

## Return values

- -1 if operation was not successful, otherwise the position of the object
