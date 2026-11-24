# simCreateForceSensor

Creates a [force sensor](../forceSensors.md).

## Synopsis

```cpp
int simCreateForceSensor(int options, const int* intParams, const double* floatParams,
                         const double* reserved)
```

## Parameters

- **options**: bit-coded options:

    - bit 0 set (1): force threshold enabled
    - bit 1 set (2): torque threshold enabled
- **intParams (input)**: 5 integer parameters:

    - intParams[0]: filter type (0=average, 1=median)
    - intParams[1]: value count the filter operates on
    - intParams[2]: number of consecutive threshold violation for the sensor to break
    - intParams[3]: reserved. Set to 0
    - intParams[4]: reserved. Set to 0
- **floatParams (input)**: 5 floating point parameters:

    - floatParams[0]: sensor size
    - floatParams[1]: force threshold value
    - floatParams[2]: torque threshold value
    - floatParams[3]: reserved. Set to 0.0
    - floatParams[4]: reserved. Set to 0.0
- **reserved**: set to nullptr

## Return values

- -1 if operation was not successful, otherwise the handle of the force sensor
