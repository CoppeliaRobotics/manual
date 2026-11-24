# sim.registerScriptFuncHook

Registers a script function hook for [callback functions](../callbackFunctions.md), that will be executed before or after the specified function. Calling this function a second time with the same arguments will unregister a previous hook

## Synopsis

```lua
int result = sim.registerScriptFuncHook(string funcToHook, string userFunc, bool execBefore)
```

## Parameters

- **funcToHook**: function to hook
- **userFunc**: user function
- **execBefore**: if true, the user function is called before the function to hook. Otherwise it is called after

## Return values

- **result**: 1 if the hook registration was successful, or 0 if a previous hook was removed
