# sim.packFloatTable

Packs an array of floating-point numbers into a string

## Synopsis

```lua
buffer data = sim.packFloatTable(float[] floatingNumbers, int startFloatIndex = 0,
                                 int floatCount = 0)
```

```python
bytes data = sim.packFloatTable(list floatingNumbers, int startFloatIndex = 0, int floatCount = 0)
```

## Parameters

- **floatingNumbers**: array containing floating-point numbers. Non-numbers will be packed as zero values
- **startFloatIndex**: zero-based index from which on data should be packed. Can be omitted in which case 0 is used
- **floatCount**: amount of floats that should be packed. Can be omitted in which case 0 is used (which indicates that the maximum available floats should be packed from the indicated startFloatIndex)

## Return values

- **data**: a buffer (values between 0 and 255) that contains packed floating-point numbers

## See also

- [sim.unpackFloatTable](simUnpackFloatTable.md)
- [packing/unpacking functions](../apiFunctions-1.md#packing)
