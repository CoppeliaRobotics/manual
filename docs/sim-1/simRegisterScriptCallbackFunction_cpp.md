# simRegisterScriptCallbackFunction

Registers a custom script function, that calls back a c/c++ function. This function is useful for plugins that wish to provide their own or customized script functions. Should be called inside of simInit entry point

Data exchange between a script and the plugin happens via a [stack](../apiFunctions-1.md#stacks). Reading and writing arguments from/to the stack gives you a maximum of flexibility, and you wil be able to exchange also complex data structures. But it can also be tedious, if your data structures are anyway relatively simple. In that case you can use the helper classes *CScriptFunctionData* and *CScriptFunctionDataItem* located in *programming/include*: they will greatly simplify the task.

Use following 4 functions in the helper class: *readDataFromStack*, *getInDataPtr*, *pushOutData* and *writeDataToStack*

## Synopsis

```cpp
int simRegisterScriptCallbackFunction(const char* func, const char* reserved,
                                      void(*callBack)(struct SScriptCallBack* cb))
```

## Parameters

- **funct**: name of the function, without namespace
- **reserved**: set to nullptr
- **callback**: callback address that is called when the function is called from Lua. See further down for a simple way to call above function, using a helper class. The callback's first argument is a SScriptCallBack structure that holds:
- **int objectID**: handle of the object that the calling script is attached to, or -1 if the calling script is not a simulation script
- **int scriptID**: handle of the calling script
- **int stackID**: a [stack handle](simCreateStack_cpp.md). The stack is used to read arguments from the script, and to return data to the script. See also the [available stack functions](../apiFunctions-1.md#stacks).

## Return values

- 1 if function was registered, 0 if function was replaced (when that function name already existed), -1 in case of an error

## See also

- [simRegisterScriptVariable](simRegisterScriptVariable_cpp.md)
