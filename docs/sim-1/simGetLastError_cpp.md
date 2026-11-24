# simGetLastError

Retrieves and clears the last generated API call error or warning message

## Synopsis

```cpp
char* simGetLastError()
```

## Parameters

No parameters.

## Return values

- Error or warning message buffer or nullptr if no error message is present. A warning starts with *warning@*. The user has to delete the returned buffer with a call to [simReleaseBuffer](simReleaseBuffer_cpp.md)

## See also

- [simSetLastError](simSetLastError_cpp.md)
- [sim.getStackTraceback](simGetStackTraceback.md)
