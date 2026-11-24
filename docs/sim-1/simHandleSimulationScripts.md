# sim.handleSimulationScripts

Lua only. Calls a specific [system callback function](../callbackFunctions.md#systemCallbacks) in [simulation scripts](../simulationScripts.md). Simulation scripts will be executed in a [precise order](../scriptExecution.md). This function should only be called from the [main script](../mainScript.md).

## Synopsis

```lua
int scriptCount = sim.handleSimulationScripts(int callType)
```

## Parameters

- **callType**: the desired system call type (e.g. *sysCall_actuation*)

## Return values

- **scriptCount**: number of called simulation scripts
