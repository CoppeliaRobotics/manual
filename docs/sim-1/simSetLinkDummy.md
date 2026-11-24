# sim.setLinkDummy

Defines (or breaks) a dummy-dummy link pair. Useful to create dynamic loop closure constraints on the fly (among others)

## Synopsis

```lua
sim.setLinkDummy(int dummyHandle, int linkedDummyHandle)
```

```python
sim.setLinkDummy(int dummyHandle, int linkedDummyHandle)
```

## Parameters

- **dummyHandle**: handle of the first dummy in the dummy-dummy link pair
- **linkedDummyHandle**: handle of the second dummy in the dummy-dummy link pair. Set to -1 to unlink the first dummy

## Return values

No return values.

## See also

- [sim.getLinkDummy](simGetLinkDummy.md)
