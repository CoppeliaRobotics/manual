# simSetLastError

Sets a custom error message and possibly raises a script error

## Synopsis

```cpp
int simSetLastError(const char* setToNull, const char* errorMessage)
```

## Parameters

- **setToNull**: set to nullptr
- **errorMessage**: error message

## Return values

- -1 if operation was not successful

## See also

- [simGetLastError](simGetLastError_cpp.md)
