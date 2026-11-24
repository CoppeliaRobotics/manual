# sim.getObjectPosition

Retrieves the position of an object

## Synopsis

```lua
float[3] position = sim.getObjectPosition(int objectHandle,
                                          int relativeToObjectHandle = sim.handle_world)
```

```python
list position = sim.getObjectPosition(int objectHandle,
                                      int relativeToObjectHandle = sim.handle_world)
```

## Parameters

- **objectHandle**: handle of the object. Can be combined with sim.handleflag_reljointbaseframe (see next argument)
- **relativeToObjectHandle**: indicates relative to which reference frame we want the position. Specify sim.handle_world to retrieve the absolute position, sim.handle_parent to retrieve the position relative to the object's parent, or an object handle relative to whose reference frame we want the position. If this handle is the handle of a joint, then the position relative to the joint's moving frame will be returned (unless **objectHandle** is combined with sim.handleflag_reljointbaseframe, in which case the position relative to the joint's base frame will be returned).

## Return values

- **position**: array of 3 values [x y z]

## See also

- [sim.setObjectPosition](simSetObjectPosition.md)
- [positions and orientations](../positionOrientationTransformation.md)
