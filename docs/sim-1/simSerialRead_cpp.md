# simSerialRead

Reads from a previously opened serial port (RS-232). The C version of the function cannot be blocking

## Synopsis

```cpp
int simSerialRead(int portHandle, char* buffer, int dataLengthToRead)
```

## Parameters

- **portHandle**: handle returned by the [simSerialOpen](simSerialOpen.md) function
- **buffer**: buffer that will be filled with read data
- **dataLengthToRead**: maximum data length that should be read

## Return values

- -1 if operation was not successful, otherwise the effective data length that was read

## See also

- [simSerialCheck](simSerialCheck_cpp.md)
- [simSerialSend](simSerialSend_cpp.md)
