# simGetVisionSensorDepth

Reads the depth buffer of a vision sensor. The returned data doesn't make sense if [sim.handleVisionSensor](simHandleVisionSensor.md) wasn't called previously

## Synopsis

```cpp
float* simGetVisionSensorDepth(int sensorHandle, int options, const int* pos, const int* size,
                               int* resolution)
```

## Parameters

- **sensorHandle**: handle of the vision sensor
- **options**: options, bit-coded:

    - bit0 set (1): the returned values indicate distances in meters, otherwise return values are in the range of 0.0 - 1.0 (0.0 = closest to sensor (i.e. close clipping plane), 1.0 = farthest from sensor (i.e. far clipping plane))
- **pos**: position of the depth buffer portion to retrieve. Can be nullptr, which defaults to [0 0]
- **size**: size of the depth buffer portion to retrieve. Can be nullptr, which defaults to [0 0], which corresponds to [resolutionX resolutionY]
- **resolution**: the returned vision sensor resolution. Can be nullptr

## Return values

- the depth buffer or nullptr in case of an error. The user is in charge of releasing the returned buffer with [simReleaseBuffer](simReleaseBuffer_cpp.md)

## See also

- [vision sensor related API functions](../apiFunctions-1.md#visionSensor)
