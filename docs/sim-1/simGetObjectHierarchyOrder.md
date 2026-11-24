# sim.getObjectHierarchyOrder

Retrieves the zero-based position of an object among its siblings in the scene hierarchy

## Synopsis

```lua
int order, int totalSiblingsCount = sim.getObjectHierarchyOrder(int objectHandle)
```

```python
int order, int totalSiblingsCount = sim.getObjectHierarchyOrder(int objectHandle)
```

## Parameters

- **objectHandle**: the handle of the object

## Return values

- **order**: the position of the object
- **totalSiblingsCount**: the total siblings count
