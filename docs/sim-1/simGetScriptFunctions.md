# sim.getScriptFunctions

Retrieves a map of another script functions, that can be called

## Synopsis

```lua
map object = sim.getScriptFunctions(int scriptHandle)
```

## Parameters

- **scriptHandle**: the handle of the script. See [sim.getScript](simGetScript.md)

## Return values

- **object**: a meta object. Functions can be called with object:functionName()

## See also

- [sim.callScriptFunction](simCallScriptFunction.md)
