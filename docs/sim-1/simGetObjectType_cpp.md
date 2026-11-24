# simGetObjectType

Retrieves the type of an object

## Synopsis

```cpp
int simGetObjectType(int objectHandle)
```

## Parameters

- **objectHandle**: handle of the object

## Return values

- type of the object (sim.sceneobject_shape, sim.sceneobject_joint, etc. (see the [object types](../apiConstants-1.md#sceneObjectTypes)) or -1 in case of error
