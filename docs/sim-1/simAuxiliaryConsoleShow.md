# sim.auxiliaryConsoleShow

Shows or hides an auxiliary console window

## Synopsis

```lua
int result = sim.auxiliaryConsoleShow(int consoleHandle, bool showState)
```

```python
int result = sim.auxiliaryConsoleShow(int consoleHandle, bool showState)
```

## Parameters

- **consoleHandle**: handle of the console window, previously returned by [sim.auxiliaryConsoleOpen](simAuxiliaryConsoleOpen.md). When combined with *sim.handleflag_extended*, then the function will simply query the visibility state of the console.
- **showState**: indicates whether the console should be hidden (0) or shown (!=0)

## Return values

- **result**: 0 if the console doesn't exist (anymore), in which case no error is generated. 1 if the console window's show state was changed.

## See also

- [sim.auxiliaryConsoleOpen](simAuxiliaryConsoleOpen.md)
- [sim.auxiliaryConsoleClose](simAuxiliaryConsoleClose.md)
