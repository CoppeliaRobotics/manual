# unloadPlugin

Lua only. Unloads a CoppeliaSim plugin

## Synopsis

```lua
unloadPlugin(map namespace, map options = {})
```

## Parameters

- **namespace**: the map returned by [loadPlugin](loadPlugin.md)
- **options**: an optional map. If options.force is set, then the plugin will be forceably unloaded, even if other scripts still depend on it

## Return values

No return values.

## See also

- [loadPlugin](loadPlugin.md)
