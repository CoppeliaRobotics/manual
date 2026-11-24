# sim.checkVisionSensor

Checks whether the vision sensor detects the indicated entity. Detection is silent (no visual feedback) compared to [sim.handleVisionSensor](simHandleVisionSensor.md). The [vision callback functions](../visionCallbackFunctions.md) will be called on the acquired image. Also, the visibility state of the entity is overridden if the entity is an object

## Synopsis

```lua
int result, float[] auxPacket1, float[] auxPacket2, etc. = sim.checkVisionSensor(int sensorHandle
                                                                                 int entityHandle)
```

```python
int result, list auxPacket1, list auxPacket2, etc. = sim.checkVisionSensor(int sensorHandle
                                                                           int entityHandle)
```

## Parameters

- **sensorHandle**: handle of the vision sensor object
- **entityHandle**: handle of entity to detect (object or collection), or sim.handle_all to detect all detectable objects

## Return values

- **result**: 0 (no detection) or 1 (detection)
- **auxPacket1**: packet of 15 auxiliary values: the minimum of intensity, red, green, blue, depth value, the maximum of intensity, red, green, blue, depth value, and the average of intensity, red, green, blue, depth value
- **auxPacket2**: additional auxiliary value packet (e.g. from an image processing component)
- **auxPacket3**: etc. (the function returns as many tables as there are auxiliary value packets)

## See also

- [sim.readVisionSensor](simReadVisionSensor.md)
- [sim.checkVisionSensorEx](simCheckVisionSensorEx.md)
