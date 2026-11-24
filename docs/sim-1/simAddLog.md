# sim.addLog

Adds a log message that will be output in the console or status bar

## Synopsis

```lua
sim.addLog(int verbosity, string message)
```

```python
sim.addLog(int verbosity, string message)
```

## Parameters

- **verbosity**: the [verbosity level](../apiConstants-1.md#verbosity). Most appropriate values are sim.verbosity_scripterrors (for errors), sim.verbosity_scriptwarnings (for warning) and sim.verbosity_scriptinfos. Combine with sim.verbosity_undecorated if you wish to output the naked message. sim.verbosity_scripterrors will additionaly raise an error.
- **message**: the message. None/nil clears the status bar

## Return values

No return values.
