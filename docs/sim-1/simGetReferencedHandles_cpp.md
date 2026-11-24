# simGetReferencedHandles

Retrieves a list of custom handles, linking a given scene object to other scene objects

## Synopsis

```cpp
int simGetReferencedHandles(int objectHandle, int** referencedHandles, const char* tag,
                            int** reserved)
```

## Parameters

- **objectHandle**: handle of the scene object that stores the list of handles. Can be optionally combined with *sim.handleflag_keeporiginal*, in which case the handles that link to originals are retrieved.
- **referencedHandles**: a pointer to a pointer that will be allocated and receive the list of scene object handles. The user is in charge of releasing that buffer with [simReleaseBuffer](simReleaseBuffer_cpp.md).
- **tag**: a tag: only handles stored within that tag are retrieved. nullptr defaults to an empty tag
- **reserved**: reserved for future extensions

## Return values

- -1 in case of an error. Otherwise, the number of handles returned.

## See also

- [simSetReferencedHandles](simSetReferencedHandles_cpp.md)
