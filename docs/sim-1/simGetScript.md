# sim.getScript

Retrieves the handle of a script. For script objects, use sim.getObject instead

## Synopsis

```lua
int scriptHandle = sim.getScript(int scriptType, string scriptName = '')
```

```python
int scriptHandle = sim.getScript(int scriptType, string scriptName = '')
```

## Parameters

- **scriptType**: [type of the script](../apiConstants-1.md#scriptTypes), or sim.handle_self
- **scriptName**: name of the add-on, in case of an add-on

## Return values

- **scriptHandle**: handle of the script
