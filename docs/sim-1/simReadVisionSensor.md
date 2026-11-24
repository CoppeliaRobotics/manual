# sim.readVisionSensor

Reads the state of a vision sensor. This function doesn't perform detection, it merely reads the result from a previous call to [sim.handleVisionSensor](simHandleVisionSensor.md)

## Synopsis

```lua
int result, float[] packet1, float[] packet2, etc. = sim.readVisionSensor(int visionSensorHandle)
```

```python
int result, list packet1, list packet2, etc. = sim.readVisionSensor(int visionSensorHandle)
```

## Parameters

- **visionSensorHandle**: handle of a vision sensor object

## Return values

- **result**: detection state (0 or 1), or -1 if [sim.handleVisionSensor](simHandleVisionSensor.md) was never called, or if [sim.resetVisionSensor](simResetVisionSensor.md) was previously called.
- **packet1**: default auxiliary packet of 15 auxiliary values: the minimum of [intensity red green blue depth], the maximum of [intensity red green blue depth], and the average of [intensity red green blue depth]
- **packet2**: additional auxiliary value packet (e.g. from an image processing component)
- **packet3**: etc. (the function returns as many tables as there are auxiliary value packets)

## See also

- [sim.checkVisionSensor](simCheckVisionSensor.md)
- [sim.checkVisionSensorEx](simCheckVisionSensorEx.md)
- [sim.resetVisionSensor](simResetVisionSensor.md)
