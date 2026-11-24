# sim.auxiliaryConsoleOpen

Opens an auxiliary console window for text display. This console window is different from the application main console window. Console window handles are shared across all simulator scenes

## Synopsis

```lua
int consoleHandle = sim.auxiliaryConsoleOpen(string title, int maxLines, int mode,
                                             int[2] position = nil, int[2] size = nil,
                                             float[3] textColor = nil,
                                             float[3] backgroundColor = nil)
```

```python
int consoleHandle = sim.auxiliaryConsoleOpen(string title, int maxLines, int mode,
                                             list position = None, list size = None,
                                             list textColor = None, list backgroundColor = None)
```

## Parameters

- **title**: title of the console window
- **maxLines**: number of text lines that can be displayed and buffered
- **mode**: bit-coded value:

    - bit0 (1) set indicates that the console window automatically closes at simulation end
    - bit1 (2) set indicates that lines will be wrapped
    - bit2 (4) set indicates that the user can close the console window
    - bit3 (8) is not used
    - bit4 (16) set indicates that the console will not automatically hide when the user switches to another scene
- **position**: initial position of the console window (x and y value). Can be None/nil
- **size**: initial size of the console window (x and y value). Can be None/nil
- **textColor**: color of the text (rgb values, 0.0 - 1.0). Can be None/nil
- **backgroundColor**: background color of the console window (rgb values, 0.0 - 1.0 ). Can be None/nil

## Return values

- **consoleHandle**: console window handle

## See also

- [sim.auxiliaryConsolePrint](simAuxiliaryConsolePrint.md)
- [sim.auxiliaryConsoleClose](simAuxiliaryConsoleClose.md)
- [sim.addLog](simAddLog.md)
