# sim.getObjectsInTree

Retrieves object handles in a given hierarchy tree

## Synopsis

```lua
int[] objects = sim.getObjectsInTree(int treeBaseHandle, int objectType = sim.handle_all,
                                     int options = 0)
```

```python
list objects = sim.getObjectsInTree(int treeBaseHandle, int objectType = sim.handle_all,
                                    int options = 0)
```

## Parameters

- **treeBaseHandle**: handle of the object that describes the hierarchy tree, or sim.handle_scene for all objects in the scene.
- **objectType**: [object type](../apiConstants-1.md#sceneObjectTypes) to retrieve or sim.handle_all for any type of object in the tree
- **options**: bit-coded:

    - bit0 set (1): exclude the tree base from the returned array
    - bit1 set (2): include in the returned array only the object's first children. If **treeBaseHandle** is sim.handle_scene, then only parentless objects will be included.

## Return values

- **objects**: an array containing object handles

## See also

- [sim.getObjects](simGetObjects.md)
