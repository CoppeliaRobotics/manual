# sim.getJointVelocity

Retrieves the linear or angular velocity of a joint. The velocity is a measured velocity (i.e. from one simulation step to the next), and is available for all joints in the scene

## Synopsis

```lua
float velocity = sim.getJointVelocity(int jointHandle)
```

```python
float velocity = sim.getJointVelocity(int jointHandle)
```

## Parameters

- **jointHandle**: handle of a joint

## Return values

- **velocity**: the velocity
