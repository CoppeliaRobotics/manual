# simInitScript

Initializes/reinitializes a script. Operates in an asynchronous way, and cannot be called from within the script being reinitialized

## Synopsis

```cpp
int simInitScript(int scriptHandle)
```

## Parameters

- **scriptHandle**: handle of the script to initialize/reinitialize

## Return values

- -1 in case of an error
