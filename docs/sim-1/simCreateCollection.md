# sim.createCollection

Creates a new [collection](../collections.md). A collection created in a [simulation script](../simulationScripts.md), a [customization script](../customizationScripts.md) or in the [main script](../mainScript.md) are automatically destroyed when the script ends

## Synopsis

```lua
int collectionHandle = sim.createCollection(int options = 0)
```

```python
int collectionHandle = sim.createCollection(int options)
```

## Parameters

- **options**: bit-coded options:

    - bit 0 set (1): collection overrides collidable, measurable, detectable properties, and also the visibility state of its objects.

## Return values

- **collectionHandle**: handle of the new collection

## See also

- [functions related to collections](../apiFunctions-1.md#collections)
