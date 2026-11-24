# sim.executeScriptString

Executes some code in a specific script (from a [plugin](../plugins.md), [the main client application](../mainClientApplication.htm), or from another script). The target script must be initialized for this call to succeed, e.g. when calling [simulation scripts](../simulationScripts.md), then simulation must be running

From C/C++, data exchange between a plugin and a script happens via a [stack](../apiFunctions-1.md#stacks). Reading and writing arguments from/to the stack gives you a maximum of flexibility, and you wil be able to exchange also complex data structures. But it can also be tedious and error prone. Use instead the helper classes located in *programming/include/simStack*

## Synopsis

```lua
int result, executionResult = sim.executeScriptString(string stringToExecute, int scriptHandle)
```

```python
int result, executionResult = sim.executeScriptString(string stringToExecute, int scriptHandle)
```

## Parameters

- **stringToExecute**: a string representing the code to execute in the specified script. An optional @python or @lua can be appended, to force a specific language
- **scriptHandle**: handle of the script, or sim.handle_self to target the script itself.

## Return values

- **result**: 0 or 1
- **executionResult**: return value of the executed code

## See also

- [sim.callScriptFunction](simCallScriptFunction.md)
