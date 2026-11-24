# sim.unpackDoubleTable

Unpacks a string (or part of it) into an array of double floating-point numbers

## Synopsis

```lua
float[] doubleNumbers = sim.unpackDoubleTable(buffer data, int startDoubleIndex = 0,
                                              int doubleCount = 0, int additionalByteOffset = 0)
```

```python
list doubleNumbers = sim.unpackDoubleTable(bytes data, int startDoubleIndex = 0, int doubleCount = 0,
                                           int additionalByteOffset = 0)
```

## Parameters

- **data**: string (values between 0 and 255) that contains packed floating-point numbers
- **startDoubleIndex**: zero-based index from which on data should be unpacked (from data[8*startDoubleIndex+1+additionalByteOffset]). Can be omitted in which case 0 is used
- **doubleCount**: amount of doubles that should be unpacked. Can be omitted in which case 0 is used (which indicates that the maximum of doubles should be unpacked from the indicated startIndex)
- **additionalByteOffset**: byte offset that will be added before reading the doubless. Can be omitted, in which case 0 is used.

## Return values

- **doubleNumbers**: array containing unpacked double floating-point numbers

## See also

- [sim.packDoubleTable](simPackDoubleTable.md)
- [packing/unpacking functions](../apiFunctions-1.md#packing)
