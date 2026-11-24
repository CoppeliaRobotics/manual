# sim.handleProximitySensor

Handles (performs sensing, etc. of) a registered proximity sensor object

## Synopsis

```lua
int res, float dist, float[3] point, int obj, float[3] n = sim.handleProximitySensor(int sensorHandle)
```

```python
int res, float dist, list point, int obj, list n = sim.handleProximitySensor(int sensorHandle)
```

## Parameters

- **sensorHandle**: handle of a proximity sensor object, or sim.handle_all or sim.handle_all_except_explicit

## Return values

- **res**: 0 if nothing was detected
- **dist**: distance to the detected point
- **point**: array of 3 numbers indicating the relative coordinates of the detected point
- **obj**: handle of the object that was detected
- **n**: array of normal vector (normalized) of the detected surface. Relative to the sensor reference frame

## See also

- [sim.readProximitySensor](simReadProximitySensor.md)
- [sim.checkProximitySensor](simCheckProximitySensor.md)
- [sim.resetProximitySensor](simResetProximitySensor.md)
