# sim.serialRead

Reads from a previously opened serial port (RS-232). The C version of the function cannot be blocking

## Synopsis

```lua
string data = sim.serialRead(int portHandle, int dataLengthToRead, bool blockingOperation,
                             string closingString = '', float timeout = 0)
```

## Parameters

- **portHandle**: handle returned by the [sim.serialOpen](simSerialOpen.md) function
- **dataLengthToRead**: maximum data length that should be read
- **blockingOperation**: if true and the calling script is running in a thread, then the function only returns when the desired data length was read (or if the closingString was met, or if there was a timeout (see next arguments)
- **closingString**: string (containing any byte value) can be specified, that will break from the blocking operation if a match was found in the incoming data. Useful when you know that a data packet is always ended with a given signature. Can be an empty string for default operation.
- **timeout**: duration after which the blocking operation will be aborted, or 0 if the timeout is infinite

## Return values

- **data**: a string containing read data (excluding the closingString if it was specified and found)

## See also

- [sim.serialCheck](simSerialCheck.md)
- [sim.serialSend](simSerialSend.md)
