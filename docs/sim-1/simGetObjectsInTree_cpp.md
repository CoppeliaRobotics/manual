# simGetObjectsInTree

Retrieves object handles in a given hierarchy tree

## Synopsis

```cpp
int* simGetObjectsInTree(int treeBaseHandle, int objectType, int options, int* objectCount)
```

## Parameters

- **treeBaseHandle**: handle of the object that describes the hierarchy tree, or sim.handle_scene for all objects in the scene.
- **objectType**: [object type](../apiConstants-1.md#sceneObjectTypes) to retrieve or sim.handle_all for any type of object in the tree
- **options**: bit-coded:

    - bit0 set (1): exclude the tree base from the returned array
    - bit1 set (2): include in the returned array only the object's first children. If **treeBaseHandle** is sim.handle_scene, then only parentless objects will be included.
- **objectCount (out value)**: the number of returned object handles

## Return values

- a pointer to an array containing object handles, or nullptr in case of an error. The user is in charge of releasing the returned buffer with [simReleaseBuffer](simReleaseBuffer_cpp.md).

## See also

- [simGetObjects](simGetObjects_cpp.md)
