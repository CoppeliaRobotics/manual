# simGetJointType

Retrieves the type of a joint

## Synopsis

```cpp
int simGetJointType(int objectHandle)
```

## Parameters

- **objectHandle**: handle of the joint

## Return values

- Type of the joint (sim.joint_revolute, sim.joint_prismatic or sim.joint_spherical), or -1 if operation was not successful
