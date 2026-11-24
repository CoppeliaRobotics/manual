# simReadVisionSensor

Reads the state of a vision sensor. This function doesn't perform detection, it merely reads the result from a previous call to [sim.handleVisionSensor](simHandleVisionSensor.md)

## Synopsis

```cpp
int simReadVisionSensor(int visionSensorHandle, double** auxValues, int** auxValuesCount)
```

## Parameters

- **visionSensorHandle**: handle of a vision sensor object
- **auxValues**: by default CoppeliaSim returns one packet of 15 auxiliary values: the minimum of [intensity red green blue depth], the maximum of [intensity red green blue depth], and the average of [intensity red green blue depth]. Additional packets can be appended in the [vision callback function](../visionCallbackFunctions.md). AuxValues can be nullptr. The user is in charge of releasing the auxValues buffer with [simReleaseBuffer](simReleaseBuffer_cpp.md)(*auxValues).
- **auxValuesCount**: contains information about the number of auxiliary value packets and packet sizes returned in auxValues. The first value is the number of packets, the second is the size of packet1, the third is the size of packet2, etc. Can be nullptr if auxValues is also nullptr. The user is in charge of releasing the auxValuesCount buffer with [simReleaseBuffer](simReleaseBuffer_cpp.md)(*auxValuesCount).
- See [simHandleVisionSensor](simHandleVisionSensor.md) for a usage example

## Return values

- detection state (0 or 1), or -1 in case of an error, or if [simHandleVisionSensor](simHandleVisionSensor.md) was never called, or if [simResetVisionSensor](simResetVisionSensor.md) was previously called.

## See also

- [simCheckVisionSensor](simCheckVisionSensor_cpp.md)
- [simCheckVisionSensorEx](simCheckVisionSensorEx_cpp.md)
- [simResetVisionSensor](simResetVisionSensor_cpp.md)
