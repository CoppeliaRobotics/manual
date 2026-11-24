# simCreateProximitySensor

Creates a [proximity sensor](../proximitySensors.md)

## Synopsis

```cpp
int simCreateProximitySensor(int sensorType, int subType, int options, const int* intParams,
                             const double* floatParams, const double* reserved)
```

## Parameters

- **sensorType**: desired [proximity sensor type](../apiConstants-1.md#sceneObjectSubTypes) (e.g. sim.proximitysensor_cone)
- **subType**: deprecated. Set to 16
- **options**: bit-coded options:

    - bit0 set (1): the sensor will be explicitly handled
    - bit1 set (2): reserved. Set to 0
    - bit2 set (4): the detection volume is not shown
    - bit3 set (8): front faces are not detected
    - bit4 set (16): back faces are not detected
    - bit5 set (32): fast detection (i.e. not exact detection)
    - bit6 set (64): the normal of the detected surface with the detection ray will have to lie below a specified threshold angle
    - bit8 set (256): smallest distance threshold will be active
    - bit9 set (512): randomized detection (only with ray-type proximity sensors)
- **intParams (input)**: 8 integer parameters:

    - intParams[0]: face count (volume description)
    - intParams[1]: face count far (volume description)
    - intParams[2]: subdivisions (volume description)
    - intParams[3]: subdivisions far (volume description)
    - intParams[4]: reserved. Set to 1
    - intParams[5]: reserved. Set to 1
    - intParams[6]: reserved. Set to 0
    - intParams[7]: reserved. Set to 0
- **floatParams (input)**: 15 floating point parameters:

    - floatParams[0]: offset (volume description)
    - floatParams[1]: range (volume description)
    - floatParams[2]: x size (volume description)
    - floatParams[3]: y size (volume description)
    - floatParams[4]: x size far (volume description)
    - floatParams[5]: y size far (volume description)
    - floatParams[6]: inside gap (volume description)
    - floatParams[7]: radius (volume description)
    - floatParams[8]: radius far (volume description)
    - floatParams[9]: angle (volume description)
    - floatParams[10]: threshold angle for limited angle detection (see bit 6 above)
    - floatParams[11]: smallest detection distance (see bit 8 above)
    - floatParams[12]: sensing point size
    - floatParams[13]: reserved. Set to 0.0
    - floatParams[14]: reserved. Set to 0.0
- **reserved**: set to nullptr

## Return values

- -1 if operation was not successful, otherwise the handle of the force sensor
