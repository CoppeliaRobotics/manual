# simGetPluginInfo

Returns auxiliary information about a loaded plugin

## Synopsis

```cpp
int simGetPluginInfo(const char* pluginName, int infoType, char** stringInfo, int* intInfo)
```

## Parameters

- **pluginName**: name of the plugin. See [sim.getPluginName](simGetPluginName.md).
- **infoType**: [type of information](../apiConstants-1.md#pluginInfos) to retrieve
- **stringInfo**: pointer to a string information, in case the information type is for a string. The user is in charge of releasing the string buffer with [sim.releaseBuffer](simReleaseBuffer_cpp.md)
- **intInfo**: pointer to an integer information, in case the information type is for an integer.

## Return values

- -1 in case of an error

## See also

- [simSetPluginInfo](simSetPluginInfo_cpp.md)
- [simGetPluginName](simGetPluginName_cpp.md)
