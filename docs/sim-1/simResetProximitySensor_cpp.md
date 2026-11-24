# simResetProximitySensor

Clears the detection state, detection color, detection segments, etc. of a proximity sensor object

## Synopsis

```cpp
int simResetProximitySensor(int sensorHandle)
```

## Parameters

- **sensorHandle**: handle of the proximity sensor object or sim.handle_all or sim.handle_all_except_explicit. (sim.handle_all will reset all proximity sensor objects, while sim.handle_all_except_explicit will only reset those that are not marked as "explicit handling")

## Return values

- -1 if operation was not successful

## See also

- [simHandleProximitySensor](simHandleProximitySensor_cpp.md)
