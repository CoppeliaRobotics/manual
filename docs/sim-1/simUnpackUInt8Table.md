# sim.unpackUInt8Table

Unpacks a string (or part of it) into an array of uint8 numbers

## Synopsis

```lua
int[] uint8Numbers = sim.unpackUInt8Table(buffer data, int startUint8Index = 0, int uint8Count = 0)
```

```python
list uint8Numbers = sim.unpackUInt8Table(bytes data, int startUint8Index = 0, int uint8Count = 0)
```

## Parameters

- **data**: string (values between 0 and 255) that contains uint8 numbers
- **startUint8Index**: zero-based index from which on data should be unpacked (from data[startUint8Index]). Can be omitted in which case 0 is used.
- **uint8Count**: amount of uint8s that should be unpacked. Can be omitted in which case 0 is used (which indicates that the maximum of uint8s should be unpacked from the indicated startUint8Index).

## Return values

- **uint8Numbers**: array containing uint8 numbers

## See also

- [sim.packUInt8Table](simPackUInt8Table.md)
- [packing/unpacking functions](../apiFunctions-1.md#packing)
