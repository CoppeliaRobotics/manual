# simSetPluginInfo

Attaches additional information to a loaded plugin

## Synopsis

```lua
sim.setPluginInfo(string pluginName, int infoType, string/int info)
```

```python
sim.setPluginInfo(string pluginName, int infoType, string/int info)
```

## Parameters

- **pluginName**: name of the plugin. See [sim.getPluginName](simGetPluginName.md)
- **infoType**: [the type of information](../apiConstants-1.md#pluginInfos) to set
- **info**: string or integer information value

## Return values

No return values.

## See also

- [sim.getPluginInfo](simGetPluginInfo.md)
