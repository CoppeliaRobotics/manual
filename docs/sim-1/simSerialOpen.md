# sim.serialOpen

Opens a serial port (RS-232) for communication. When called from a script, the function can only be called when the simulation is running (and in that case the port is automatically closed at simulation stop)

## Synopsis

```lua
int result = sim.serialOpen(string portString, int baudRate)
```

## Parameters

- **portString**: string specifying the port to open. Under Windows, use something similar to "\\\\.\\COM1". Under MacOS and Linux, use something similar to "/dev/*" (check the "/dev" folder to know what file to specify). Under Linux, you might have to launch CoppeliaSim with super user priviledges in order to access the serial port
- **baudRate**: baudrate

## Return values

- **result**: the port handle

## See also

- [sim.serialClose](simSerialClose.md)
- [sim.serialSend](simSerialSend.md)
- [sim.serialCheck](simSerialCheck.md)
- [sim.serialRead](simSerialRead.md)
