# sim.getVelocity

Retrieves the linear and/or angular velocity of the center of mass of a non-static shape. Data is provided by the selected physics engine

## Synopsis

```lua
float[3] linearVelocity, float[3] angularVelocity = sim.getVelocity(int shapeHandle)
```

```python
list linearVelocity, list angularVelocity = sim.getVelocity(int shapeHandle)
```

## Parameters

- **shapeHandle**: handle of a dynamically enabled shape

## Return values

- **linearVelocity**: array of 3 values that represent the linear velocity in absolute coordinates
- **angularVelocity**: array of 3 values that represent the angular velocity in absolute coordinates. The length of the vector represents the rotation speed, and the vector direction represents the rotation axis passing through the center of mass of the shape

## See also

- [sim.getObjectVelocity](simGetObjectVelocity.md)
