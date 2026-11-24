# simGetApiInfo

Returns the call tip (or info text) for an API function

## Synopsis

```cpp
char* simGetApiInfo(int scriptHandle, const char* apiWord)
```

## Parameters

- **scriptHandle**: [handle of the script](simGetScript.md). Can be -1 to be script agnostic
- **apiWord**: API functions or variable to retrieve the info for, e.g. "sim.getObject"

## Return values

- nullptr in case of an error. Otherwise the information related to the API function or variable. The user is in charge of releasing the returned buffer with [simReleaseBuffer](simReleaseBuffer_cpp.md).

## See also

- [simGetApiFunc](simGetApiFunc_cpp.md)
