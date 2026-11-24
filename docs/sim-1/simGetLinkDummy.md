# sim.getLinkDummy

Retrieves the object handle of the dummy linked to this one

## Synopsis

```lua
int linkedDummyHandle = sim.getLinkDummy(int dummyHandle)
```

```python
int linkedDummyHandle = sim.getLinkDummy(int dummyHandle)
```

## Parameters

- **dummyHandle**: handle of the dummy whose linked dummy has to be retrieved

## Return values

- **linkedDummyHandle**: handle of the dummy linked to the specified dummy object, or -1 if the dummy is not linked

## See also

- [sim.setLinkDummy](simSetLinkDummy.md)
