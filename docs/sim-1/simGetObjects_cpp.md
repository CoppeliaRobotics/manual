# simGetObjects

Retrieves object handles. Use this in a loop where index starts at 0 and is incremented to get all object handles in the scene

## Synopsis

```cpp
int simGetObjects(int index, int objectType)
```

## Parameters

- **index**: object index. First object is located at index 0
- **objectType**: object type (sim.sceneobject_shape, sim.sceneobject_joint, etc. (see the [object types](../apiConstants-1.md#sceneObjectTypes)) or sim.handle_all for any type of object

## Return values

- handle of the object or -1 if no object is located at that index or in case of an error

## See also

- [simGetObjectsInTree](simGetObjectsInTree_cpp.md)
