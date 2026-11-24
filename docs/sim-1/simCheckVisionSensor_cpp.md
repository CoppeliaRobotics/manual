# simCheckVisionSensor

Checks whether the vision sensor detects the indicated entity. Detection is silent (no visual feedback) compared to [sim.handleVisionSensor](simHandleVisionSensor.md). The [vision callback functions](../visionCallbackFunctions.md) will be called on the acquired image. Also, the visibility state of the entity is overridden if the entity is an object

## Synopsis

```cpp
int simCheckVisionSensor(int sensorHandle, int entityHandle, double** auxValues,
                         int** auxValuesCount)
```

## Parameters

- **sensorHandle**: handle of the vision sensor object
- **entityHandle**: handle of entity to detect (object or collection), or sim.handle_all to detect all detectable objects
- **auxValues**: by default CoppeliaSim returns one packet of 15 auxiliary values: the minimum of intensity, red, green, blue, depth value, the maximum of intensity, red, green, blue, depth value, and the average of intensity, red, green, blue, depth value. Additional packets can be appended in the [vision callback functions](../visionCallbackFunctions.md). AuxValues can be nullptr. The user is in charge of releasing the auxValues buffer with [simReleaseBuffer](simReleaseBuffer_cpp.md)(*auxValues).
- **auxValuesCount**: contains information about the number of auxiliary value packets and packet sizes returned in auxValues. The first value is the number of packets, the second is the size of packet1, the third is the size of packet2, etc. Can be nullptr if auxValues is also nullptr. The user is in charge of releasing the auxValuesCount buffer with [simReleaseBuffer](simReleaseBuffer_cpp.md)(*auxValuesCount)

## Return values

- -1 if operation was not successful, otherwise 0 (no detection) or 1 (detection)

## Example

```cpp
double* auxValues = nullptr;
int* auxValuesCount = nullptr;
double averageColor[3] = {0.0, 0.0, 0.0};
if (simCheckVisionSensor(sensorHandle, entityHandle, &auxValues, &auxValuesCount) >= 0)
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
- [simCheckVisionSensorEx](simCheckVisionSensorEx_cpp.md)
