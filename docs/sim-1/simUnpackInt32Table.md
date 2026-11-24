# sim.unpackInt32Table

Unpacks a string (or part of it) into an array of int32 numbers

## Synopsis

```lua
int[] int32Numbers = sim.unpackInt32Table(buffer data, int startInt32Index = 0, int int32Count = 0,
                                          int additionalByteOffset = 0)
```

```python
list int32Numbers = sim.unpackInt32Table(bytes data, int startInt32Index = 0, int int32Count = 0,
                                         int additionalByteOffset = 0)
```

## Parameters

- **data**: string (values between 0 and 255) that contains packed int32 numbers
- **startInt32Index**: zero-based index from which on data should be unpacked (from data[4*startInt32Index+1+additionalByteOffset]). Can be omitted in which case 0 is used
- **int32Count**: amount of int32s that should be unpacked. Can be omitted in which case 0 is used (which indicates that the maximum of int32s should be unpacked from the indicated startInt32Index)
- **additionalByteOffset**: byte offset that will be added before reading the int32s. Can be omitted, in which case 0 is used.

## Return values

- **int32Numbers**: array containing unpacked int32 numbers

## See also

- [sim.packInt32Table](simPackInt32Table.md)
- [packing/unpacking functions](../apiFunctions-1.md#packing)
