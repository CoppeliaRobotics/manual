# sim.getObjectOrientation

Retrieves the orientation ([Euler angles](../positionOrientationTransformation.md#euler)) of an object

## Synopsis

```lua
float[3] eulerAngles = sim.getObjectOrientation(int objectHandle,
                                                int relativeToObjectHandle = sim.handle_world)
```

```python
list eulerAngles = sim.getObjectOrientation(int objectHandle,
                                            int relativeToObjectHandle = sim.handle_world)
```

## Parameters

- **objectHandle**: handle of the object. Can be combined with sim.handleflag_reljointbaseframe (see next argument)
- **relativeToObjectHandle**: indicates relative to which reference frame we want the orientation. Specify sim.handle_world to retrieve the absolute orientation, sim.handle_parent to retrieve the orientation relative to the object's parent, or an object handle relative to whose reference frame you want the orientation. If this handle is the handle of a joint, then the orientation relative to the joint's moving frame will be returned (unless **objectHandle** is combined with sim.handleflag_reljointbaseframe, in which case the orientation relative to the joint's base frame will be returned).

## Return values

- **eulerAngles**: Euler angles [alpha beta gamma]

## See also

- [sim.setObjectOrientation](simSetObjectOrientation.md)
- [positions and orientations](../positionOrientationTransformation.md)
