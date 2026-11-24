# simCreateVisionSensor

Creates a [vision sensor](../visionSensors.md).

## Synopsis

```cpp
int simCreateVisionSensor(int options, const int* intParams, const double* floatParams,
                          const double* reserved)
```

## Parameters

- **options**: bit-coded options:

    - bit 0 set (1): the sensor will be explicitly handled
    - bit 1 set (2): the sensor will be in perspective operation mode
    - bit 2 set (4): the view frustum will not be shown
    - bit 3 set (8): reserved. Set to 0
    - bit 4 set (16): the sensor will be passive (use an external image)
    - bit 5 set (32): the sensor will use local lights
    - bit 6 set (64): the sensor will not render any fog
    - bit 7 set (128): the sensor will use a specific color for default background (i.e. null pixels)
- **intParams (input)**: 4 integer parameters:

    - intParams[0]: sensor resolution x
    - intParams[1]: sensor resolution y
    - intParams[2]: reserved. Set to 0
    - intParams[3]: reserved. Set to 0
- **floatParams (input)**: 11 floating point parameters:

    - floatParams[0]: near clipping plane
    - floatParams[1]: far clipping plane
    - floatParams[2]: view angle / ortho view size
    - floatParams[3]: sensor size x
    - floatParams[4]: reserved. Set to 0.0
    - floatParams[5]: reserved. Set to 0.0
    - floatParams[6]: null pixel red-value
    - floatParams[7]: null pixel green-value
    - floatParams[8]: null pixel blue-value
    - floatParams[9]: reserved. Set to 0.0
    - floatParams[10]: reserved. Set to 0.0
- **reserved**: set to nullptr

## Return values

- -1 if operation was not successful, otherwise the handle of the force sensor
