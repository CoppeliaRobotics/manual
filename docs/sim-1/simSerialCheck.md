# sim.serialCheck

Reads how many bytes are waiting to be read on a serial port (RS-232)

## Synopsis

```lua
int result = sim.serialCheck(int portHandle)
```

## Parameters

- **portHandle**: handle returned by the [simSerialOpen](simSerialOpen.md) function

## Return values

- **result**: the number of bytes that are waiting to be read

## See also

- [sim.serialRead](simSerialRead.md)
