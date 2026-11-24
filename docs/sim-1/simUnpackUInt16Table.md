# sim.unpackUInt16Table

Unpacks a string (or part of it) into an array of uint16 numbers

## Synopsis

```lua
int[] uint16Numbers = sim.unpackUInt16Table(buffer data, int starUint16Index = 0,
                                            int uint16Count = 0, int additionalByteOffset)
```

```python
list uint16Numbers = sim.unpackUInt16Table(bytes data, int starUint16Index = 0, int uint16Count = 0,
                                           int additionalByteOffset)
```

## Parameters

- **data**: string (values between 0 and 255) that contains packed uint16 numbers
- **starUint16Index**: zero-based index from which on data should be unpacked (from data[2*starUint16Index+1+additionalByteOffset]). Can be omitted in which case 0 is used.
- **uint16Count**: amount of uint16s that should be unpacked. Can be omitted in which case 0 is used (which indicates that the maximum of uint16s should be unpacked from the indicated starUint16Index).
- **additionalByteOffset**: byte offset that will be added before reading the uint16s. Can be omitted, in which case 0 is used.

## Return values

- **uint16Numbers**: array containing unpacked uint16 numbers

## See also

- [sim.packUInt16Table](simPackUInt16Table.md)
- [packing/unpacking functions](../apiFunctions-1.md#packing)
