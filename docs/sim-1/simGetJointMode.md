# sim.getJointMode

Retrieves the operation mode of a joint

## Synopsis

```lua
int jointMode = sim.getJointMode(int jointHandle)
```

```python
int jointMode = sim.getJointMode(int jointHandle)
```

## Parameters

- **jointHandle**: handle of the joint object

## Return values

- **jointMode**: the [joint mode](../apiConstants-1.md#jointModes)

## See also

- [sim.setJointMode](simSetJointMode.md)
- [joint.dynamics.ctrlMode](../sim-2/property_joint_dynamics_ctrlMode.md)
