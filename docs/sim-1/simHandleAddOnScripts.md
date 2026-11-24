# sim.handleAddOnScripts

Lua only. Calls a specific function in [add-ons](../addOns.md). Should only be called from the [main script](../mainScript.md)

## Synopsis

```lua
int count = sim.handleAddOnScripts(int callType)
```

## Parameters

- **callType**: desired system call type (e.g. *sysCall_actuation*).

## Return values

- **count**: number of called add-ons
