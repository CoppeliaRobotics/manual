# sim.createForceSensor

Creates a [force sensor](../forceSensors.md).

## Synopsis

```lua
int sensorHandle = sim.createForceSensor(int options, int[5] intParams, float[5] floatParams)
```

```python
int sensorHandle = sim.createForceSensor(int options, list intParams, list floatParams)
```

## Parameters

- **options**: bit-coded options:

    - bit 0 set (1): force threshold enabled
    - bit 1 set (2): torque threshold enabled
- **intParams**: 5 integer parameters (indexing (i) starts from 0 for Python and 1 for Lua):

    - intParams[i+0]: filter type (0=average, 1=median)
    - intParams[i+1]: value count the filter operates on
    - intParams[i+2]: number of consecutive threshold violation for the sensor to break
    - intParams[i+3]: reserved. Set to 0
    - intParams[i+4]: reserved. Set to 0
- **floatParams**: 5 floating point parameters (indexing (i) starts from 0 for Python and 1 for Lua):

    - floatParams[i+0]: sensor size
    - floatParams[i+1]: force threshold value
    - floatParams[i+2]: torque threshold value
    - floatParams[i+3]: reserved. Set to 0.0
    - floatParams[i+4]: reserved. Set to 0.0

## Return values

- **sensorHandle**: handle of the force sensor
