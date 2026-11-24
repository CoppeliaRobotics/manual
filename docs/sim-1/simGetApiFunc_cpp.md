# simGetApiFunc

Retrieves all API functions and variables that match a specific word. Useful for script code auto-completion functionality

## Synopsis

```cpp
char* simGetApiFunc(int scriptHandle, const char* apiWord)
```

## Parameters

- **scriptHandleOrType**: [handle of the script](simGetScript.md). Can be -1 to be script agnostic.
- **apiWord**: word that API functions and variables should match, e.g. "sim.getObj". Only matches up to the first dot are returned, if the apiWord does not contain any dot. To retrieve all functions and variables, leave apiWord empty. To retrieve only functions, add '+' as prefix. To retrieve only variables, add '-' as prefix.

## Return values

- nullptr in case of an error, or if there is no match. Otherwise all matching API functions and variables, space-separated. The user is in charge of releasing the returned buffer with [simReleaseBuffer](simReleaseBuffer_cpp.md).

## See also

- [simGetApiInfo](simGetApiInfo_cpp.md)
