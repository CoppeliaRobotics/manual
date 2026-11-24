# sim.packUInt16Table

Packs an array of uint16 numbers into a string

## Synopsis

```lua
buffer data = sim.packUInt16Table(int[] uint16Numbers, int startUint16Index = 0, int uint16Count = 0)
```

```python
bytes data = sim.packUInt16Table(list uint16Numbers, int startUint16Index = 0, int uint16Count = 0)
```

## Parameters

- **uint16Numbers**: array containing uint16 numbers. Invalid uint16 numbers will be packed in an undefined manner.
- **startUint16Index**: zero-based index from which on data should be packed. Can be omitted in which case 0 is used
- **uint16Count**: amount of uint16s that should be packed. Can be omitted in which case 0 is used (which indicates that the maximum available uint16s should be packed from the indicated startUint16Index)

## Return values

- **data**: a buffer (values between 0 and 255) that contains packed uint16 numbers

## See also

- [sim.unpackUInt16Table](simUnpackUInt16Table.md)
- [packing/unpacking functions](../apiFunctions-1.md#packing)
