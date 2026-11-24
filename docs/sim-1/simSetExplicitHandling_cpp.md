# simSetExplicitHandling

Sets the explicit handling flags for a scene object

## Synopsis

```cpp
int simSetExplicitHandling(int objectHandle, int explicitFlags)
```

## Parameters

- **objectHandle**: handle of a scene object.
- **explicitFlags**: explicit handling flags. For now only bit 0 is used

## Return values

- -1 if operation was not successful

## See also

- [simGetExplicitHandling](simGetExplicitHandling_cpp.md)
