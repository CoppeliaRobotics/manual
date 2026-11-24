# sim.checkProximitySensor

Checks whether the proximity sensor detects the indicated entity. Detection is silent (no visual feedback) compared to [sim.handleProximitySensor](simHandleProximitySensor.md). Also, the detectable flags of the entity are overridden if the entity is an object

## Synopsis

```lua
int res, float dist, float[3] point, int obj, float[3] n = sim.checkProximitySensor(int sensorHandle,
                                                                                    int entityHandle)
```

```python
int res, float dist, list point, int obj, list n = sim.checkProximitySensor(int sensorHandle,
                                                                            int entityHandle)
```

## Parameters

- **sensorHandle**: handle of the proximity sensor object
- **entityHandle**: handle of entity to detect (object or collection), or sim.handle_all to detect all detectable objects

## Return values

- **res**: 0 (not detected) or 1 (detected)
- **dist**: distance from the sensor origin to the detected point. None/nil if result is different from 1
- **point**: position of the detected point relative to the sensor origin. None/nil if result is different from 1
- **obj**: handle of detected object. None/nil if result is different from 1
- **n**: normal vector of the surface where the point was detected. Normalized. Relative to the sensor reference frame. None/nil if result is different from 1

## See also

- [sim.readProximitySensor](simReadProximitySensor.md)
