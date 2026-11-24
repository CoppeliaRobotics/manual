# sim.readProximitySensor

Reads the state of a proximity sensor. This function doesn't perform detection, it merely reads the result from a previous call to [sim.handleProximitySensor](simHandleProximitySensor.md)

## Synopsis

```lua
int res, float dist, float[3] point, int obj, float[3] n = sim.readProximitySensor(int sensorHandle)
```

```python
int res, float dist, list point, int obj, list n = sim.readProximitySensor(int sensorHandle)
```

## Parameters

- **sensorHandle**: handle of a proximity sensor

## Return values

- **res**: detection state (0 or 1)
- **dist**: distance to the detected point
- **point**: array of 3 numbers indicating the relative coordinates of the detected point
- **obj**: handle of the object that was detected
- **n**: normal vector (normalized) of the detected surface. Relative to the sensor reference frame

## See also

- [sim.checkProximitySensor](simCheckProximitySensor.md)
- [sim.resetProximitySensor](simResetProximitySensor.md)
