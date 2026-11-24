# simAuxiliaryConsoleClose

Closes an auxiliary console window

## Synopsis

```cpp
int simAuxiliaryConsoleClose(int consoleHandle)
```

## Parameters

- **consoleHandle**: handle of the console window, previously returned by simAuxiliaryConsoleOpen

## Return values

- -1 if operation was not successful. 0 if the console doesn't exist (anymore), in which case no error is generated. 1 if the console window was closed.

## See also

- [simAuxiliaryConsoleOpen](simAuxiliaryConsoleOpen_cpp.md)
