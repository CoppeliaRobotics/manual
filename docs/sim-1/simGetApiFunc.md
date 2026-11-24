# sim.getApiFunc

Retrieves all API functions and variables that match a specific word. Useful for script code auto-completion functionality

## Synopsis

```lua
string[] funcsAndVars = sim.getApiFunc(int scriptHandle, string apiWord)
```

```python
list funcsAndVars = sim.getApiFunc(int scriptHandle, string apiWord)
```

## Parameters

- **scriptHandleOrType**: [handle of the script](simGetScript.md). Can be -1 to be script agnostic
- **apiWord**: word that API functions and variables should match, e.g. "sim.getObj". Only matches up to the first dot are returned, if the apiWord does not contain any dot. To retrieve all functions and variables, leave apiWord empty. To retrieve only functions, add '+' as prefix. To retrieve only variables, add '-' as prefix.

## Return values

- **funcsAndVars**: array containing all matching API functions and variables.

## See also

- [sim.getApiInfo](simGetApiInfo.md)
