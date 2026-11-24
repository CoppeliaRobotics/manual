# sim.yprToAbg

Converts Yaw-Pitch-Roll angles to CoppeliaSim's alpha-beta-gamma angles

## Synopsis

```lua
float[3] outAngles = sim.yprToAbg(float[3] inAngles)
```

```python
list outAngles = sim.yprToAbg(list inAngles)
```

## Parameters

- **inAngles**: 3 angles: yaw, pitch and roll

## Return values

- **outAngles**: 3 angles: alpha, beta and gamma

## See also

- [sim.abgToYpr](simAbgToYpr.md)
- [positions and orientations](../positionOrientationTransformation.md)
