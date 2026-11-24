# sim.getStackTraceback

Lua only. Retrieves and clears the last generated stack traceback for a script

## Synopsis

```lua
string stackTraceback = sim.getStackTraceback(int scriptHandle)
```

## Parameters

- **scriptHandle**: the script handle from which the traceback is desired. If omitted, then the calling script's traceback will be retrieved and cleared.

## Return values

- **stackTraceback**: the stack traceback

## See also

- [sim.getScript](simGetScript.md)
