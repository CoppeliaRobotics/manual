# sim.getPluginName

Retrieves a plugin name based on an index

## Synopsis

```lua
string pluginName = sim.getPluginName(int index)
```

```python
string pluginName = sim.getPluginName(int index)
```

## Parameters

- **index**: index to a plugin. To list-up all plugin names, start with index=0 and increment index until return value is None/nil

## Return values

- **pluginName**: name of the plugin or None/nil if no plugin is available at that index position.
