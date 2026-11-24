# sim.auxiliaryConsoleClose

Closes an auxiliary console window

## Synopsis

```lua
int result = sim.auxiliaryConsoleClose(int consoleHandle)
```

```python
int result = sim.auxiliaryConsoleClose(int consoleHandle)
```

## Parameters

- **consoleHandle**: handle of the console window, previously returned by sim.auxiliaryConsoleOpen

## Return values

- **result**: 0 if the console doesn't exist (anymore), in which case no error is generated. 1 if the console window was closed

## See also

- [sim.auxiliaryConsoleOpen](simAuxiliaryConsoleOpen.md)
