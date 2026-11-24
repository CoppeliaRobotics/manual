# sim.getApiInfo

Returns the call tip (or info text) for an API function

## Synopsis

```lua
string info = sim.getApiInfo(int scriptHandle, string apiWord)
```

```python
string info = sim.getApiInfo(int scriptHandle, string apiWord)
```

## Parameters

- **scriptHandle**: [handle of the script](simGetScript.md). Can be -1 to be script agnostic
- **apiWord**: API functions or variable to retrieve the info for, e.g. "sim.getObject"

## Return values

- **info**: information related to the API function or variable

## See also

- [sim.getApiFunc](simGetApiFunc.md)
