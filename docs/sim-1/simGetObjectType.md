# sim.getObjectType

Retrieves the type of an object

## Synopsis

```lua
int objectType = sim.getObjectType(int objectHandle)
```

```python
int objectType = sim.getObjectType(int objectHandle)
```

## Parameters

- **objectHandle**: handle of the object

## Return values

- **objectType**: type of the object (sim.sceneobject_shape, sim.sceneobject_joint, etc. (see the [object types](../apiConstants-1.md#sceneObjectTypes))
