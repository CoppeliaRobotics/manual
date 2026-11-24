# sim.serialSend

Writes data to a previously opened serial port (RS-232)

## Synopsis

```lua
int charsSent = sim.serialSend(int portHandle, buffer data)
```

## Parameters

- **portHandle**: handle returned by the [sim.serialOpen](simSerialOpen.md) function
- **data**: pointer to the data that should be sent

## Return values

- **charsSent**: the effective data length that was written

## See also

- [sim.serialRead](simSerialRead.md)
