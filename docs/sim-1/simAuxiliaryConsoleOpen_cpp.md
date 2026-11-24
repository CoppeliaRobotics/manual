# simAuxiliaryConsoleOpen

Opens an auxiliary console window for text display. This console window is different from the application main console window. Console window handles are shared across all simulator scenes

## Synopsis

```cpp
int simAuxiliaryConsoleOpen(const char* title, int maxLines, int mode, const int* position,
                            const int* size, const float* textColor, const float* backgroundColor)
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
- **position**: initial position of the console window (x and y value). Can be nullptr
- **size**: initial size of the console window (x and y value). Can be nullptr
- **textColor**: color of the text (rgb values, 0.0 - 1.0). Can be nullptr
- **backgroundColor**: background color of the console window (rgb values, 0.0 - 1.0). Can be nullptr

## Return values

- -1 if operation was not successful. Otherwise a console window handle

## See also

- [simAuxiliaryConsolePrint](simAuxiliaryConsolePrint_cpp.md)
- [simAuxiliaryConsoleClose](simAuxiliaryConsoleClose_cpp.md)
- [simAddLog](simAddLog_cpp.md)
