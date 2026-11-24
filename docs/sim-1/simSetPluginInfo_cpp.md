# simSetPluginInfo

Attaches additional information to a loaded plugin

## Synopsis

```cpp
int simSetPluginInfo(const char* pluginName, int infoType, const char* stringInfo, int intInfo)
```

## Parameters

- **pluginName**: name of the plugin. See [sim.getPluginName](simGetPluginName.md).
- **infoType**: [the type of information](../apiConstants-1.md#pluginInfos) to set
- **stringInfo**: string information value, in case the information type is for a string.
- **intInfo**: integer information value, in case the information type is for an integer.

## Return values

- -1 in case of an error

## See also

- [simGetPluginInfo](simGetPluginInfo_cpp.md)
