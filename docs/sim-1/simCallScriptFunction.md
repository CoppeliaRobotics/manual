# sim.callScriptFunction

Calls a script function (from a [plugin](../plugins.md), [the main client application](../mainClientApplication.md), or from another script). This represents a [user callback](../callbackFunctions.md) inside of a script. The target script must be initialized for this call to succeed, e.g. when calling [simulation scripts](../simulationScripts.md), then simulation must be running

## Synopsis

```lua
... = sim.callScriptFunction(int scriptHandle, string functionName, ...)
```

```python
... = sim.callScriptFunction(int scriptHandle, string functionName, ...)
```

## Parameters

- **scriptHandle**: the handle of the script, or sim.handle_self to target the current script. See [sim.getScript](simGetScript.md)
- **functionName**: the function to call.
- **...**: any number of arguments that will be handed over to the called function.

## Return values

- **...**: any number of return values from the called function.

## See also

- [sim.getScriptFunctions](simGetScriptFunctions.md)
- [sim.executeScriptString](simExecuteScriptString.md)
