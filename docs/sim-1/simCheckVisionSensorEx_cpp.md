# simCheckVisionSensorEx

Checks whether the vision sensor detects the indicated entity. Detection is silent (no visual feedback) compared to [sim.handleVisionSensor](simHandleVisionSensor.md). The [vision callback functions](../visionCallbackFunctions.md) will be called on the acquired image. Also, the visibility state of the entity is overridden if the entity is an object

## Synopsis

```cpp
double* simCheckVisionSensorEx(int sensorHandle, int entityHandle, bool returnImage)
```

## Parameters

- **sensorHandle**: handle of the vision sensor object
- **entityHandle**: handle of entity to detect (object or collection), or sim.handle_all to detect all detectable objects
- **returnImage**: specifies what should be returned. If true, the sensor's image buffer is returned, otherwise its depth buffer is returned

## Return values

- image or depth buffer, or nullptr in case of an error. The user is in charge of releasing the returned buffer with [simReleaseBuffer](simReleaseBuffer_cpp.md)

## See also

- [simReadVisionSensor](simReadVisionSensor_cpp.md)
