# sim.packUInt8Table

Packs an array of uint8 numbers into a string

## Synopsis

```lua
buffer data = sim.packUInt8Table(int[] uint8Numbers, int startUint8Index = 0, int uint8count = 0)
```

```python
bytes data = sim.packUInt8Table(list uint8Numbers, int startUint8Index = 0, int uint8count = 0)
```

## Parameters

- **uint8Numbers**: array containing uint8 numbers. Invalid byte number will be packed in an undefined manner.
- **startUint8Index**: zero-based index from which on data should be packed. Can be omitted in which case 0 is used
- **uint8count**: amount of uint8s that should be packed. Can be omitted in which case 0 is used (which indicates that the maximum available uint8s should be packed from the indicated startUint8Index)

## Return values

- **data**: a buffer (values between 0 and 255) that contains the uint8 numbers

## See also

- [sim.unpackUInt8Table](simUnpackUInt8Table.md)
- [packing/unpacking functions](../apiFunctions-1.md#packing)
