# sim.packDoubleTable

Packs ab array of double floating-point numbers into a string

## Synopsis

```lua
buffer data = sim.packDoubleTable(float[] doubleNumbers, int startDoubleIndex = 0,
                                  int doubleCount = 0)
```

```python
bytes data = sim.packDoubleTable(list doubleNumbers, int startDoubleIndex = 0, int doubleCount = 0)
```

## Parameters

- **doubleNumbers**: array of double floating-point numbers. Non-numbers will be packed as zero values
- **startDoubleIndex**: zero-based index from which on data should be packed. Can be omitted in which case 0 is used
- **doubleCount**: amount of doubles that should be packed. Can be omitted in which case 0 is used (which indicates that the maximum available doubles should be packed from the indicated startDoubleIndex)

## Return values

- **data**: a buffer (values between 0 and 255) that contains packed double floating-point numbers

## See also

- [sim.unpackDoubleTable](simUnpackDoubleTable.md)
- [packing/unpacking functions](../apiFunctions-1.md#packing)
