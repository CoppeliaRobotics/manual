# loadPlugin

Lua only. Loads a CoppeliaSim [plugin](../plugins.md)

## Synopsis

```lua
map namespace = loadPlugin(string pluginName)
```

## Parameters

- **pluginName**: the name of the plugin, including version number, e.g. simIK, simIK-2-0, etc.

## Return values

- **namespace**: a map containing the variables and functions offered by the plugin

## See also

- [unloadPlugin](unloadPlugin.md)
