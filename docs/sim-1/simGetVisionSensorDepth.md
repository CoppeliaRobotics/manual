# sim.getVisionSensorDepth

Reads the depth buffer of a vision sensor. The returned data doesn't make sense if [sim.handleVisionSensor](simHandleVisionSensor.md) wasn't called previously

## Synopsis

```lua
buffer depth, int[2] resolution = sim.getVisionSensorDepth(int sensorHandle, int options = 0,
                                                           int[2] pos = {0, 0}, int[2] size = {0, 0})
```

```python
bytes depth = sim.getVisionSensorDepth(int sensorHandle, int options = 0, list pos = [0, 0],
                                       list size = [0, 0])
```

## Parameters

- **sensorHandle**: handle of the vision sensor
- **options**: options, bit-coded:

    - bit0 set (1): the returned values indicate distances in meters, otherwise return values are in the range of 0.0 - 1.0 (0.0 = closest to sensor (i.e. close clipping plane), 1.0 = farthest from sensor (i.e. far clipping plane))
- **pos**: position of the depth buffer portion to retrieve. Defaults to [0 0]
- **size**: size of the depth buffer portion to retrieve. Defaults to [0 0], which corresponds to [resolutionX resolutionY]

## Return values

- **depth**: the depth buffer. Use [sim.unpackFloatTable](simUnpackFloatTable.md) to obtain an array of values
- **resolution**: the vision sensor resolution

## See also

- [vision sensor related API functions](../apiFunctions-1.md#visionSensor)
