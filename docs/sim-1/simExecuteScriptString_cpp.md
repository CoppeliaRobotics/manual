# simExecuteScriptString

Executes some code in a specific script (from a [plugin](../plugins.md), [the main client application](../mainClientApplication.md), or from another script). The target script must be initialized for this call to succeed, e.g. when calling [simulation scripts](../simulationScripts.md), then simulation must be running

From C/C++, data exchange between a plugin and a script happens via a [stack](../apiFunctions-1.md#stacks). Reading and writing arguments from/to the stack gives you a maximum of flexibility, and you wil be able to exchange also complex data structures. But it can also be tedious and error prone. Use instead the helper classes located in *programming/include/simStack*

## Synopsis

```cpp
int simExecuteScriptString(int scriptHandle, const char* stringToExecute, int stackId)
```

## Parameters

- **scriptHandle**: the handle of the script
- **stringToExecute**: a string representing the code to execute in the specified script
- **stackId**: 0 (for no stack) or a [stack handle](simCreateStack_cpp.md). The stack holds possible out values. See also the [available stack functions](../apiFunctions-1.md#stacks).

## Return values

- -1 in case of an error

## See also

- [sim.callScriptFunction](simCallScriptFunction.md)
