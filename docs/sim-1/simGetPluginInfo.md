# sim.getPluginInfo

Returns auxiliary information about a loaded plugin

## Synopsis

```lua
string/int info = sim.getPluginInfo(string pluginName, int infoType)
```

```python
string/int info = sim.getPluginInfo(string pluginName, int infoType)
```

## Parameters

- **pluginName**: name of the plugin. See [sim.getPluginName](simGetPluginName.md).
- **infoType**: [type of information](../apiConstants-1.md#pluginInfos) to retrieve

## Return values

- **info**: the retrieved information

## See also

- [sim.setPluginInfo](simSetPluginInfo.md)
- [sim.getPluginName](simGetPluginName.md)
