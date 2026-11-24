# simRegisterScriptVariable

Registers a script variable. Should be called inside of simInit entry point

## Synopsis

```cpp
int simRegisterScriptVariable(const char* var, const char* val, int stackhandle)
```

## Parameters

- **var**: name of the variable, without namespace
- **val**: value of the variable. Can be nullptr, in which case the value of the variable will be the top item of the provided stack
- **stackHandle**: a stack handle obtained with [simCreateStack](simCreateStack_cpp.md). Set to 0 if *varValue* is not nullptr. If a stack is provided, it will be released at a later point by CoppeliaSim.

## Return values

- 1 if the variable was registered, 0 if the variable was replaced because it already existed, -1 in case of an error

## See also

- [simRegisterScriptCallbackFunction](simRegisterScriptCallbackFunction_cpp.md)
