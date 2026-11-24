# sim.addItemToCollection

Adds an item to a [collection](../collections.md)

## Synopsis

```lua
sim.addItemToCollection(int collectionHandle, int what, int objectHandle, int options)
```

```python
sim.addItemToCollection(int collectionHandle, int what, int objectHandle, int options)
```

## Parameters

- **collectionHandle**: handle of a collection.
- **what**: type of object (or group of objects) to add. Following are allowed values:

    - *sim.handle_single* (for a single object)
    - *sim.handle_all* (for all objects in the scene)
    - *sim.handle_tree* (for a tree of objects)
    - *sim.handle_chain* (for a chain of objects (i.e. an inverted tree)).
- **objectHandle**: handle of an object
- **options**: bit-coded options:

    - bit 0 set (1): the specified object (or group of objects) is removed from the collection. Otherwise it is added.
    - bit 1 set (2): the specified object is not included in the group of objects, if sim.handle_tree or sim.handle_chain is specified (i.e. the tree base or tip is excluded).

## Return values

No return values.

## See also

- [functions related to collections](../apiFunctions-1.md#collections)
