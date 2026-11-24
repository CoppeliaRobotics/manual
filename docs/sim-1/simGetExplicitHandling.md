# sim.getExplicitHandling

Retrieves the explicit handling flags for a scene object

## Synopsis

```lua
int explicitHandlingFlags = sim.getExplicitHandling(int objectHandle)
```

```python
int explicitHandlingFlags = sim.getExplicitHandling(int objectHandle)
```

## Parameters

- **objectHandle**: handle of a scene object

## Return values

- **explicitHandlingFlags**: the explicit handling flags for the specified object (for now only bit 0 is used)

## See also

- [sim.setExplicitHandling](simSetExplicitHandling.md)
