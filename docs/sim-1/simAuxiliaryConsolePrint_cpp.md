# simAuxiliaryConsolePrint

Prints to an auxiliary console window

## Synopsis

```cpp
int simAuxiliaryConsolePrint(int consoleHandle, const char* text)
```

## Parameters

- **consoleHandle**: handle of the console window, previously returned by the [simAuxiliaryConsoleOpen](simAuxiliaryConsoleOpen.md)
- **text**: text to append, or nullptr to clear the console window

## Return values

- -1 if operation was not successful. 0 if the console doesn't exist (anymore), in which case no error is generated. 1 if the operation was successful.

## See also

- [simAuxiliaryConsoleOpen](simAuxiliaryConsoleOpen_cpp.md)
