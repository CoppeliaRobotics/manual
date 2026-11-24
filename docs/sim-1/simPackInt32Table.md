# sim.packInt32Table

Packs an array of int32 numbers into a string

## Synopsis

```lua
buffer data = sim.packInt32Table(int[] int32Numbers, int startInt32Index = 0, int int32Count = 0)
```

```python
bytes data = sim.packInt32Table(list int32Numbers, int startInt32Index = 0, int int32Count = 0)
```

## Parameters

- **int32Numbers**: array containing int32 numbers. Non-numbers will be packed as zero values
- **startInt32Index**: zero-based index from which on data should be packed. Can be omitted in which case 0 is used
- **int32Count**: amount of int32s that should be packed. Can be omitted in which case 0 is used (which indicates that the maximum available int32s should be packed from the indicated startInt32Index)

## Return values

- **data**: a buffer (values between 0 and 255) that contains packed int32 numbers

## See also

- [sim.unpackInt32Table](simUnpackInt32Table.md)
- [packing/unpacking functions](../apiFunctions-1.md#packing)
