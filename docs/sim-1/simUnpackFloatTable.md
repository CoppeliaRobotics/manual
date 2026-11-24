# sim.unpackFloatTable

Unpacks a string (or part of it) into an array of floating-point numbers

## Synopsis

```lua
float[] floatingNumbers = sim.unpackFloatTable(buffer data, int startFloatIndex = 0,
                                               int floatCount = 0, int additionalByteOffset = 0)
```

```python
list floatingNumbers = sim.unpackFloatTable(bytes data, int startFloatIndex = 0, int floatCount = 0,
                                            int additionalByteOffset = 0)
```

## Parameters

- **data**: string (values between 0 and 255) that contains packed floating-point numbers
- **startFloatIndex**: zero-based index from which on data should be unpacked (from data[4*startFloatIndex+1+additionalByteOffset]). Can be omitted in which case 0 is used
- **floatCount**: amount of floats that should be unpacked. Can be omitted in which case 0 is used (which indicates that the maximum of floats should be unpacked from the indicated startFloatIndex)
- **additionalByteOffset**: byte offset that will be added before reading the floats. Can be omitted, in which case 0 is used.

## Return values

- **floatingNumbers**: array containing unpacked floating-point numbers

## See also

- [sim.packFloatTable](simPackFloatTable.md)
- [packing/unpacking functions](../apiFunctions-1.md#packing)
