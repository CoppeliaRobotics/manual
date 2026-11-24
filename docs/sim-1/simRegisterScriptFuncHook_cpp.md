# simRegisterScriptFuncHook

Registers a script function hook for [callback functions](../callbackFunctions.md), that will be executed before or after the specified function. Calling this function a second time with the same arguments will unregister a previous hook

## Synopsis

```cpp
int simRegisterScriptFuncHook(int scriptHandle, const char* funcToHook, const char* userFunc,
                              bool execBefore, int options)
```

## Parameters

- **scriptHandle**: handle of the script
- **funcToHook**: function to hook
- **userFunc**: user function
- **execBefore**: if true, the user function is called before the function to hook. Otherwise it is called after
- **options**: set to 0

## Return values

- 1 if the hook registration was successful, 0 if a previous hook was removed, and -1 in case of an error
