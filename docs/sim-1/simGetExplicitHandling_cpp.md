# simGetExplicitHandling

Retrieves the explicit handling flags for a scene object

## Synopsis

```cpp
int simGetExplicitHandling(int objectHandle)
```

## Parameters

- **objectHandle**: handle of a scene object.

## Return values

- -1 if command was not successful, otherwise the explicit handling flags for the specified object (for now only bit 0 is used).

## See also

- [simSetExplicitHandling](simSetExplicitHandling_cpp.md)
