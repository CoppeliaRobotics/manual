# simGetScriptHandleEx

Retrieves the handle of a script.

## Synopsis

```cpp
int simGetScriptHandleEx(int scriptType, int objectHandle, const char* scriptName)
```

## Parameters

- **scriptType**: the [type of the script](../apiConstants-1.md#scriptTypes).
- **objectHandle**: the object handle the script is attached to (in case of simulation- or customization scripts. Can be -1.
- **scriptName**: the path of the object the script is attached to (in case of simulation- or customization scripts), or the name of the add-on. Can be nullptr.

## Return values

- handle of the script, or -1 if the script does not exist.
