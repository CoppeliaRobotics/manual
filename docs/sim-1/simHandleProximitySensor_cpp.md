# simHandleProximitySensor

Handles (performs sensing, etc. of) a registered proximity sensor object

## Synopsis

```cpp
int simHandleProximitySensor(int sensorHandle, double* detectedPoint, int* detectedObjectHandle,
                             double* detectedSurfaceNormalVector)
```

## Parameters

- **sensorHandle**: handle of a proximity sensor object or sim.handle_all or sim.handle_all_except_explicit. (sim.handle_all will handle all proximity sensor objects, while sim.handle_all_except_explicit will only handle those that are not marked as "explicit handling")
- **detectedPoint**: coordinates of the closest detected point (x, y and z: detectedPoint[0]-detectedPoint[2]) relative to the sensor reference frame, and distance to the detected point (1 value: detectedPoint[3]). Can be nullptr
- **detectedObjectHandle**: handle of the object that was detected. Can be nullptr
- **detectedSurfaceNormalVector**: normal vector (normalized) of the detected surface. Relative to the sensor reference frame. Can be nullptr
- When several proximity sensors are handled at the same time (e.g. with the sim.handle_all argument), then the output values are relative to the closest detection distance

## Return values

- 0 if nothing was detected, -1 in case of an error.

## See also

- [simReadProximitySensor](simReadProximitySensor_cpp.md)
- [simCheckProximitySensor](simCheckProximitySensor_cpp.md)
- [simResetProximitySensor](simResetProximitySensor_cpp.md)
