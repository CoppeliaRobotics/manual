# sim.handleVisionSensor

Handles (performs sensing, etc. of) a vision sensor object. It (1) clear previous computed image processing data, (2) reads an image and (3) performs image processing via the [vision callback functions](../visionCallbackFunctions.md) (if the vision sensor is using an **external input** only (1) is performed)

## Synopsis

```lua
int detectionCount, float[] packet1, float[] packet2, etc. = sim.handleVisionSensor(int visionSensorHandle)
```

```python
int detectionCount, list packet1, list packet2, etc. = sim.handleVisionSensor(int visionSensorHandle)
```

## Parameters

- **visionSensorHandle**: handle of a vision sensor object or sim.handle_all or sim.handle_all_except_explicit

## Return values

- **detectionCount**: number of detections (number of vision sensors that triggered a detection)
- **packet1**: default auxiliary value packet (15 auxiliary values: the minimum of [intensity red green blue depth], the maximum of [intensity red green blue depth], and the average of [intensity red green blue depth])
- **packet2**: additional auxiliary value packet (e.g. from an image processing component)
- **packet3**: etc. (the function returns as many arrays as there are auxiliary value packets)

## See also

- [sim.readVisionSensor](simReadVisionSensor.md)
- [sim.checkVisionSensor](simCheckVisionSensor.md)
- [sim.checkVisionSensorEx](simCheckVisionSensorEx.md)
- [sim.resetVisionSensor](simResetVisionSensor.md)
