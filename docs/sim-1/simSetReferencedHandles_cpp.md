# simSetReferencedHandles

Attaches a list of custom handles to a given scene object. Those custom handles are handles of other scene objects, that are linked to the given scene object (for whatever purpose). The advantage of storing references to other objects with this function is that CoppeliaSim will take care of correctly adjusting the references if needed: For instance, imagine *objectA* storing the handle of *objectB* via this function. If *objectB* is deleted, then the stored handle becomes -1. If *objectA* and *objectB* are duplicated at the same time, then the duplicate of *objectA* stores the handle of the duplicate of *objectB*. Optionally, if *sim.handleflag_keeporiginal* is specified, then linking to original objects is guaranteed, e.g. in above example, after a duplication of *objectA*, the duplicate of *objectA* will store the handle of the original *objectB* (if *objectB* still exists)

## Synopsis

```cpp
int simSetReferencedHandles(int objectHandle, int count, const int* referencedHandles,
                            const char* tag, const int* reserved)
```

## Parameters

- **objectHandle**: handle of the scene object that will store the list of handles. Can be optionally combined with *sim.handleflag_keeporiginal*, in which case the handles that link to originals are retrieved
- **count**: number of handles to store
- **referencedHandles**: list of scene object handles.
- **tag**: a tag: handles will be stored under this tag. nullptr defaults to an empty tag
- **reserved**: reserved for future extensions

## Return values

- -1 in case of an error.

## See also

- [simGetReferencedHandles](simGetReferencedHandles_cpp.md)
