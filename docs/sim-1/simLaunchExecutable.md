# sim.launchExecutable

Launches an executable. Similar to os.execute or io.popen, but is system independent.

## Synopsis

```lua
sim.launchExecutable(string filename, string parameters = '', int showStatus = 1)
```

```python
sim.launchExecutable(string filename, string parameters = '', int showStatus = 1)
```

## Parameters

- **filename**: file name of the executable. If the filename starts with '@', then it will be considered as a system command, otherwise the current directory might be automatically prepended to the filename if it makes sense.
- **parameters**: optional input arguments
- **showStatus**: 0 to hide the application's window, 1 to show it. Works only with Windows OS.

## Return values

No return values.
