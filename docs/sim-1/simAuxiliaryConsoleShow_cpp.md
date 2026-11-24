# simAuxiliaryConsoleShow

Shows or hides an auxiliary console window

## Synopsis

```cpp
int simAuxiliaryConsoleShow(int consoleHandle, bool showState)
```

## Parameters

- **consoleHandle**: handle of the console window, previously returned by [simAuxiliaryConsoleOpen](simAuxiliaryConsoleOpen.md). When combined with *sim.handleflag_extended*, then the function will simply query the visibility state of the console.
- **showState**: indicates whether the console should be hidden (0) or shown (!=0)

## Return values

- -1 if operation was not successful. 0 if the console doesn't exist (anymore), in which case no error is generated. 1 if the console window's show state was changed.

## See also

- [simAuxiliaryConsoleOpen](simAuxiliaryConsoleOpen_cpp.md)
- [simAuxiliaryConsoleClose](simAuxiliaryConsoleClose_cpp.md)
