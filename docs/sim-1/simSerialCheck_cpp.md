# simSerialCheck

Reads how many bytes are waiting to be read on a serial port (RS-232)

## Synopsis

```cpp
int simSerialCheck(int portHandle)
```

## Parameters

- **portHandle**: the handle returned by the [simSerialOpen](simSerialOpen.md) function

## Return values

- -1 if operation was not successful, otherwise the number of bytes that are waiting to be read

## See also

- [simSerialRead](simSerialRead_cpp.md)
