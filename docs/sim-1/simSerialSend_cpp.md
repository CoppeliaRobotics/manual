# simSerialSend

Writes data to a previously opened serial port (RS-232)

## Synopsis

```cpp
int simSerialSend(int portHandle, const char* data, int dataLength)
```

## Parameters

- **portHandle**: handle returned by the [simSerialOpen](simSerialOpen.md) function
- **data**: pointer to the data that should be sent
- **dataLength**: length of the data to be sent

## Return values

- -1 if operation was not successful, otherwise the effective data length that was written

## See also

- [simSerialRead](simSerialRead_cpp.md)
