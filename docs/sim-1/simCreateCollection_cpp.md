# simCreateCollection

Creates a new [collection](../collections.md). A collection created in a [simulation script](../simulationScripts.md), a [customization script](../customizationScripts.md) or in the [main script](../mainScript.md) are automatically destroyed when the script ends

## Synopsis

```cpp
int simCreateCollectionEx(int options)
```

## Parameters

- **options**: bit-coded options:

    - bit 0 set (1): collection overrides collidable, measurable, detectable properties, and also the visibility state of its objects.

## Return values

- -1 if operation was not successful, otherwise the handle of the new collection.

## See also

- [functions related to collections](../apiFunctions-1.md#collections)
