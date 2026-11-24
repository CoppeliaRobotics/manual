# simCallScriptFunctionEx

Calls a script function (from a [plugin](../plugins.md), [the main client application](../mainClientApplication.htm), or from another script). This represents a [user callback](../callbackFunctions.md) inside of a script. The target script must be initialized for this call to succeed, e.g. when calling [simulation scripts](../simulationScripts.md), then simulation must be running

Data exchange between a plugin and a script happens via a [stack](../apiFunctions-1.md#stacks). Reading and writing arguments from/to the stack gives you a maximum of flexibility, and you wil be able to exchange also complex data structures. But it can also be tedious and error prone. Use instead the helper classes located in *programming/include/simStack*: they will greatly simplify the task. Have a look at the example plugins [simSkeleton](https://github.com/CoppeliaRobotics/simSkeleton) and [simSkel](https://github.com/CoppeliaRobotics/simSkel)

## Synopsis

```cpp
int simCallScriptFunctionEx(int scriptHandle, const char* functionName,
                            int stackId)
```

## Parameters

- **scriptHandle**: the handle of the script, or -1 for the sandbox script, or -2 for the main script
- **functionName**: the function to call.
- **stackId**: a [stack handle](simCreateStack_cpp.md). The stack represents the function's in/out values. See also the [available stack functions](../apiFunctions-1.md#stacks).

## Return values

- -1 in case of an error

## See also

- [simExecuteScriptString](simExecuteScriptString_cpp.md)
- [simGetScriptHandleEx](simGetScriptHandleEx_cpp.md)
