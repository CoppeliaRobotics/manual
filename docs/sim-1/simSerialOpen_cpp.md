# simSerialOpen

Opens a serial port (RS-232) for communication. When called from a script, the function can only be called when the simulation is running (and in that case the port is automatically closed at simulation stop)

## Synopsis

```cpp
int simSerialOpen(char* portString, int baudRate, void* reserved1, void* reserved2)
```

## Parameters

- **portString**: string specifying the port to open. Under Windows, use something similar to "\\\\.\\COM1". Under MacOS and Linux, use something similar to "/dev/*" (check the "/dev" folder to know what file to specify). Under Linux, you might have to launch CoppeliaSim with super user priviledges in order to access the serial port.
- **baudRate**: baudrate
- **reserved1**: reserved for future extension. Keep at nullptr.
- **reserved2**: reserved for future extension. Keep at nullptr.

## Return values

- -1 if operation was not successful, otherwise a port handle

## See also

- [simSerialClose](simSerialClose_cpp.md)
- [simSerialSend](simSerialSend_cpp.md)
- [simSerialCheck](simSerialCheck_cpp.md)
- [simSerialRead](simSerialRead_cpp.md)
