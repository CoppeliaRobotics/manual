# simCloseScene

Closes current scene, and switches to another open scene. If there is no other open scene, a new scene is then created. Can only be called from an [add-on](../addOns.md), or from the sanbox script, when called from within CoppeliaSim

## Synopsis

```cpp
int simCloseScene()
```

## Parameters

No parameters.

## Return values

- -1 if operation was not successful, otherwise the current scene index.

## See also

- [simLoadScene](simLoadScene_cpp.md)
- [simSaveScene](simSaveScene_cpp.md)
