# sim.getObjectParent

Retrieves the handle of an object's parent object

## Synopsis

```lua
int parentHandle = sim.getObjectParent(int objectHandle)
```

```python
int parentHandle = sim.getObjectParent(int objectHandle)
```

## Parameters

- **objectHandle**: handle of the object

## Return values

- **parentHandle**: handle of parent or -1 if the parent doesn't exist

## See also

- [sim.setObjectParent](simSetObjectParent.md)
- [sim.getObjectChild](simGetObjectChild.md)
