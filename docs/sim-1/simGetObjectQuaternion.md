# sim.getObjectQuaternion

Retrieves the quaternion of an object

## Synopsis

```lua
float[4] quaternion = sim.getObjectQuaternion(int objectHandle,
                                              int relativeToObjectHandle = sim.handle_world)
```

```python
list quaternion = sim.getObjectQuaternion(int objectHandle,
                                          int relativeToObjectHandle = sim.handle_world)
```

## Parameters

- **objectHandle**: handle of the object. Combine with sim.handleflag_wxyzquat to retrieve the quaternion as [qw qx qy qz] order instead of [qx qy qz qw] order. Can also be combined with sim.handleflag_reljointbaseframe (see next argument)
- **relativeToObjectHandle**: indicates relative to which reference frame we want the orientation. Specify sim.handle_world to retrieve the absolute orientation, sim.handle_parent to retrieve the orientation relative to the object's parent, or an object handle relative to whose reference frame you want the orientation. If this handle is the handle of a joint, then the quaternion relative to the joint's moving frame will be returned (unless **objectHandle** is combined with sim.handleflag_reljointbaseframe, in which case the quaternion relative to the joint's base frame will be returned).

## Return values

- **quaternion**: the quaternion [qx qy qz qw]

## See also

- [sim.setObjectQuaternion](simSetObjectQuaternion.md)
- [positions and orientations](../positionOrientationTransformation.md)
