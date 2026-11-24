# sim.auxiliaryConsolePrint

Prints to an auxiliary console window

## Synopsis

```lua
int result = sim.auxiliaryConsolePrint(int consoleHandle, string text)
```

```python
int result = sim.auxiliaryConsolePrint(int consoleHandle, string text)
```

## Parameters

- **consoleHandle**: handle of the console window, previously returned by the [sim.auxiliaryConsoleOpen](simAuxiliaryConsoleOpen.md)
- **text**: text to append, or None/nil to clear the console window

## Return values

- **result**: 0 if the console doesn't exist (anymore), in which case no error is generated. 1 if the operation was successful

## See also

- [sim.auxiliaryConsoleOpen](simAuxiliaryConsoleOpen.md)
