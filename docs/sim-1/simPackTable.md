# sim.packTable

Packs a table into a buffer. The table may contain other nested arrays, maps, None/nil, bool, number, string or matrix values. All other types (e.g. functions) will be considered as string or None/nil values. You can also use sim.packTable to quickly compare two tables

## Synopsis

```lua
buffer buffer = sim.packTable(any[]/map aTable, int packingScheme = 0)
```

```python
bytes buffer = sim.packTable(list/dict aTable, int packingScheme = 0)
```

## Parameters

- **aTable**: array or map
- **packingScheme**: 0 for CoppeliaSim format, 1 for CBOR format, 2 for CBOR format where doubles are packed as floats. When CBOR format is selected, strings with an @:txt: suffix will be forcibly packed as text, and strings with an @:dat: suffix will be forcibly packed as byte buffer

## Return values

- **buffer**: a data buffer

## See also

- [sim.unpackTable](simUnpackTable.md)
- [packing/unpacking functions](../apiFunctions-1.md#packing)
