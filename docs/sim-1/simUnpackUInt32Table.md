# sim.unpackUInt32Table

Unpacks a string (or part of it) into an array of uint32 numbers

## Synopsis

```lua
int[] uint32Numbers = sim.unpackUInt32Table(buffer data, int startUint32Index = 0,
                                            int uint32Count = 0, int additionalByteOffset = 0)
```

```python
list uint32Numbers = sim.unpackUInt32Table(bytes data, int startUint32Index = 0, int uint32Count = 0,
                                           int additionalByteOffset = 0)
```

## Parameters

- **data**: string (values between 0 and 255) that contains packed uint32 numbers
- **startUint32Index**: zero-based index from which on data should be unpacked (from data[4*startUint32Index+1+additionalByteOffset]). Can be omitted in which case 0 is used
- **uint32Count**: amount of uint32s that should be unpacked. Can be omitted in which case 0 is used (which indicates that the maximum of uint32s should be unpacked from the indicated startUint32Index)
- **additionalByteOffset**: byte offset that will be added before reading the uint32s. Can be omitted, in which case 0 is used.

## Return values

- **integerNumbers**: array containing unpacked uint32 numbers

## See also

- [sim.packUInt32Table](simPackUInt32Table.md)
- [packing/unpacking functions](../apiFunctions-1.md#packing)
