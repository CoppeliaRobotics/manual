# sim.setObjectParent

Sets an object's parent object. Dynamically simulated objects, together with their hierarchy tree, are dynamically reset (this however does not apply to static shapes)

## Synopsis

```lua
sim.setObjectParent(int objectHandle, int parentObjectHandle, bool keepInPlace)
```

```python
sim.setObjectParent(int objectHandle, int parentObjectHandle, bool keepInPlace)
```

## Parameters

- **objectHandle**: handle of the object that will become child of the parent object. Can be or-combined with [sim.handleflag_assembly](../apiConstants-1.md#specialHandleFlags) if an assembly operation is desired instead (in that case, **parentObjectHandle** can't be -1, and **keepInPlace** should be set to false)
- **parentObjectHandle**: handle of the object that will become parent, or -1 if the object should become parentless. In an assembly operation, the assembly dummy on the parent object should be specified instead
- **keepInPlace**: indicates whether the object's absolute pose should stay same

## Return values

No return values.

## See also

- [sim.getObjectParent](simGetObjectParent.md)
- [assembly operation](../assembly.md)
