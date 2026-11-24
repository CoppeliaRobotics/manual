# sim.handleEmbeddedScripts

Lua only. Calls a specific [system callback function](../callbackFunctions.md#systemCallbacks) in [simulation scripts](../simulationScripts.md) and [customization scripts](../customizationScripts.md). Simulation- and customization scripts will be executed in a [precise order](../scriptExecution.md). This function should only be called from the [main script](../mainScript.md)

## Synopsis

```lua
int scriptCount = sim.handleEmbeddedScripts(int callType)
```

## Parameters

- **callType**: desired system call type (e.g. *sysCall_actuation*)

## Return values

- **scriptCount**: number of called scripts
