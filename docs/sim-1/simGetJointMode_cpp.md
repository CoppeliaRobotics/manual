# simGetJointMode

Retrieves the operation mode of a joint

## Synopsis

```cpp
int simGetJointMode(int jointHandle, int* options)
```

## Parameters

- **jointHandle**: handle of the joint object
- **options**: (output): not used

## Return values

- -1 if operation was not successful, otherwise the [joint mode](../apiConstants-1.md#jointModes).

## See also

- [simSetJointMode](simSetJointMode_cpp.md)
- [joint.dynamics.ctrlMode](../sim-2/property_joint_dynamics_ctrlMode.md)
