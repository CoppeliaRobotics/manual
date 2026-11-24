# sim.unpackTable

Unpacks a buffer into a table

## Synopsis

```lua
any[]/map aTable = sim.unpackTable(buffer buffer, int packingScheme = 0)
```

```python
list/dict aTable = sim.unpackTable(bytes buffer, int packingScheme = 0)
```

## Parameters

- **buffer**: an input buffer
- **packingScheme**: 0 for CoppeliaSim format, 1 for CBOR format

## Return values

- **aTable**: the unpacked buffer

## See also

- [sim.packTable](simPackTable.md)
- [packing/unpacking functions](../apiFunctions-1.md#packing)
