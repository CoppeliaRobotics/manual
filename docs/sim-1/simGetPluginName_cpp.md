# simGetPluginName

Retrieves a plugin name based on an index

## Synopsis

```cpp
char* simGetPluginName(int index)
```

## Parameters

- **index**: index to a plugin. To list-up all plugin names, start with index=0 and increment index until return value is nullptr

## Return values

- Name of the plugin or nullptr if no plugin is available at index position, or in case of an error. The user is in charge of destroying the returned name with [simReleaseBuffer](simReleaseBuffer_cpp.md)
