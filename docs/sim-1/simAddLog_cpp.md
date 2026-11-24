# simAddLog

Adds a log message that will be output in the console or status bar

## Synopsis

```cpp
int simAddLog(const char* pluginName, int verbosity, const char* message)
```

## Parameters

- **pluginName**: the name of the plugin that outputs the message. e.g. *simIK*
- **verbosity**: the [verbosity level](../apiConstants-1.md#verbosity). Most appropriate values are sim.verbosity_errors (for errors), sim.verbosity_warnings (for warning) and sim.verbosity_infos.
- **message**: the message. Set to nullptr to clear the status bar

## Return values

- -1 if operation was not successful.
