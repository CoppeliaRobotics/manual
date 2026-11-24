# simReadProximitySensor

Reads the state of a proximity sensor. This function doesn't perform detection, it merely reads the result from a previous call to [sim.handleProximitySensor](simHandleProximitySensor.md)

## Synopsis

```cpp
int simReadProximitySensor(int sensorHandle, double* detectedPoint, int* detectedObjectHandle,
                           double* detectedSurfaceNormalVector)
```

## Parameters

- **sensorHandle**: handle of a proximity sensor object
- **detectedPoint**: coordinates of the closest detected point (x, y and z: detectedPoint[0]-detectedPoint[2]) relative to the sensor reference frame, and distance to the detected point (1 value: detectedPoint[3]). Can be nullptr
- **detectedObjectHandle**: handle of the object that was detected. Can be nullptr
- **detectedSurfaceNormalVector**: normal vector (normalized) of the detected surface. Relative to the sensor reference frame. Can be nullptr

## Return values

- detection state (0 or 1), or -1 in case of an error.

## See also

- [simCheckProximitySensor](simCheckProximitySensor_cpp.md)
- [simResetProximitySensor](simResetProximitySensor_cpp.md)
