# simHandleVisionSensor

Handles (performs sensing, etc. of) a vision sensor object. It (1) clear previous computed image processing data, (2) reads an image and (3) performs image processing via the [vision callback functions](../visionCallbackFunctions.md) (if the vision sensor is using an **external input** only (1) is performed)

## Synopsis

```cpp
int simHandleVisionSensor(int visionSensorHandle, double** auxValues, int** auxValuesCount)
```

## Parameters

- **visionSensorHandle**: handle of a vision sensor object or sim.handle_all or sim.handle_all_except_explicit. (sim.handle_all will handle all vision sensor objects, while sim.handle_all_except_explicit will only handle those that are not marked as "explicit handling")
- **auxValues**: by default CoppeliaSim returns one packet of 15 auxiliary values: the minimum of [intensity red green blue depth], the maximum of [intensity red green blue depth], and the average of [intensity red green blue depth]. If the [vision callback function](../visionCallbackFunctions.md) returns additional values, then they are appended as packets to the first packet. AuxValues can be nullptr. The user is in charge of releasing the auxValues buffer with [simReleaseBuffer](simReleaseBuffer_cpp.md)(*auxValues). If visionSensorHandle is sim.handle_all or sim.handle_all_except_explicit, nothing is returned in auxValues.
- **auxValuesCount**: contains information about the number of auxiliary value packets and packet sizes returned in auxValues. The first value is the number of packets, the second is the size of packet1, the third is the size of packet2, etc. Can be nullptr if auxValues is also nullptr. The user is in charge of releasing the auxValuesCount buffer with [simReleaseBuffer](simReleaseBuffer_cpp.md)(*auxValuesCount).

## Return values

- number of detections (number of vision sensors that triggered a detection), -1 in case of an error

## Example

```cpp
double* auxValues=nullptr;
int* auxValuesCount = nullptr;
double averageColor[3] = {0.0, 0.0, 0.0};
if (simHandleVisionSensor(visionSensorHandle, &auxValues, &auxValuesCount) >= 0)
{
    if ((auxValuesCount[0] > 0) || (auxValuesCount[1] >= 15))
    {
        averageColor[0] = auxValues[11];
        averageColor[1] = auxValues[12];
        averageColor[2] = auxValues[13];
    }
    simReleaseBuffer((char*)auxValues);
    simReleaseBuffer((char*)auxValuesCount);
}
```

## See also

- [simReadVisionSensor](simReadVisionSensor_cpp.md)
- [simCheckVisionSensor](simCheckVisionSensor_cpp.md)
- [simCheckVisionSensorEx](simCheckVisionSensorEx_cpp.md)
- [simResetVisionSensor](simResetVisionSensor_cpp.md)
