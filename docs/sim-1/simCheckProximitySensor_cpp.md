# simCheckProximitySensor

Checks whether the proximity sensor detects the indicated entity. Detection is silent (no visual feedback) compared to [sim.handleProximitySensor](simHandleProximitySensor.md). Also, the detectable flags of the entity are overridden if the entity is an object

## Synopsis

```cpp
int simCheckProximitySensor(int sensorHandle, int entityHandle, double* detectedPoint)
```

## Parameters

- **sensorHandle**: handle of the proximity sensor object
- **entityHandle**: handle of entity to detect (object or collection), or sim.handle_all to detect all detectable objects
- **detectedPoint**: coordinates of detected point relative to the sensor origin (detectedPoint[0]-detectedPoint[2]), and distance of detected point to the sensor origin (detectedPoint[3]). Can be nullptr

## Return values

- -1 if operation was not successful, otherwise 0 (no detection) or 1 (detection)

## See also

- [simReadProximitySensor](simReadProximitySensor_cpp.md)
