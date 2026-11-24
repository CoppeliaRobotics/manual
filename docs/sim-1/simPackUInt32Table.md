# sim.packUInt32Table

Packs an array of uint32 numbers into a string

## Synopsis

```lua
buffer data = sim.packUInt32Table(int[] uint32Numbers, int startUint32Index = 0, int uint32Count = 0)
```

```python
bytes data = sim.packUInt32Table(list uint32Numbers, int startUint32Index = 0, int uint32Count = 0)
```

## Parameters

- **uint32Numbers**: array containing uint32 numbers. Non-numbers will be packed as zero values
- **startUint32Index**: zero-based index from which on data should be packed. Can be omitted in which case 0 is used
- **uint32Count**: amount of uint32s that should be packed. Can be omitted in which case 0 is used (which indicates that the maximum available uint32s should be packed from the indicated startUint32Index)

## Return values

- **data**: a buffer (values between 0 and 255) that contains packed uint32 numbers

## See also

- [sim.unpackUInt32Table](simUnpackUInt32Table.md)
- [packing/unpacking functions](../apiFunctions-1.md#packing)
