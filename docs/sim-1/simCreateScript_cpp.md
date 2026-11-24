# simCreateScript

Creates a [script object](../scriptObjects.md).

## Synopsis

```cpp
int simCreateScript(int scriptType, const char* scriptText, int options, const char* lang)
```

## Parameters

- **scriptType**: the [script type](../apiConstants-1.md#scriptTypes). Only simulation-, customization- or passive scripts are allowed
- **scriptText**: the content of the script
- **options**: bit-coded options:

    - bit 0 set (1): script is initially disabled
- **lang**: language. A value different from "lua" or "python" disables the script. nullptr defaults to "lua"

## Return values

- -1 if operation was not successful, otherwise the handle of the script object
