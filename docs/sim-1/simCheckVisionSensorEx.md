# sim.checkVisionSensorEx

Checks whether the vision sensor detects the indicated entity. Detection is silent (no visual feedback) compared to [sim.handleVisionSensor](simHandleVisionSensor.md). The [vision callback functions](../visionCallbackFunctions.md) will be called on the acquired image. Also, the visibility state of the entity is overridden if the entity is an object

## Synopsis

```lua
float[] buff = sim.checkVisionSensorEx(int sensorHandle, int entityHandle, bool returnImage)
buffer buff = sim.checkVisionSensorEx(int sensorHandle, int entityHandle, bool returnImage)
```

```python
list buff = sim.checkVisionSensorEx(int sensorHandle, int entityHandle, bool returnImage)
bytes buff = sim.checkVisionSensorEx(int sensorHandle, int entityHandle, bool returnImage)
```

## Parameters

- **sensorHandle**: handle of the vision sensor object. Can be combined with [sim.handleflag_codedstring](../apiConstants-1.md#specialHandleFlags) if you wish to retrieve the image or depth map coded in a string (much faster)
- **entityHandle**: handle of entity to detect (object or collection), or sim.handle_all to detect all detectable objects
- **returnImage**: specifies what should be returned. If true, the sensor's image buffer is returned, otherwise its depth buffer is returned

## Return values

- image or depth buffer

## See also

- [sim.readVisionSensor](simReadVisionSensor.md)
