# simResetVisionSensor

Clears the detection state, etc. of a proximity sensor object

## Synopsis

```cpp
int simResetVisionSensor(int sensorHandle)
```

## Parameters

- **sensorHandle**: handle of the vision sensor object or sim.handle_all or sim.handle_all_except_explicit. (sim.handle_all will reset all vision sensor objects, while sim.handle_all_except_explicit will only reset those that are not marked as "explicit handling")

## Return values

- -1 if operation was not successful

## See also

- [simHandleVisionSensor](simHandleVisionSensor_cpp.md)
