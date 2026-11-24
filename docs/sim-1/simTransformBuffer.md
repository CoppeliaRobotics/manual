# sim.transformBuffer

Modifies a buffer than contains packed data

## Synopsis

```lua
a) buffer outBuff = sim.transformBuffer(buffer inBuffer, int inFormat, float mult, float off, int outFormat)
b) buffer[] outBuff = sim.transformBuffer(buffer inBuffer, sim.buffer_uint8, 0, int splitSize, sim.buffer_split)
```

```python
a) bytes outBuff = sim.transformBuffer(bytes inBuff, int inFormat, float mult, float off, int outFormat)
b) list outBuff = sim.transformBuffer(bytes inBuff, sim.buffer_uint8, 0, int splitSize, sim.buffer_split)
```

## Parameters

- **inBuff**: input buffer that contains packed data
- **inFormat**: [buffer type](../apiConstants-1.md#bufferTypes)
- **mult**: multiplier value. We have out = offset + multiplier * in
- **off/splitSize**: offset or split size value. We have out = offset + multiplier * in
- **outFormat**: desired [buffer type](../apiConstants-1.md#bufferTypes) for the returned buffer

## Return values

- a) **outBuff**: the modified buffer
- b) **outBuff**: the various split buffers

## See also

- [data packing/unpacking functions](../apiFunctions-1.md#packing)
