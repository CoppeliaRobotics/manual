# sim.setEventFilters

Specifies filters for the sysCall_event callback. Operates on a per script basis

## Synopsis

```lua
sim.setEventFilters(map filters)
```

```python
sim.setEventFilters(dict filters)
```

## Parameters

- **filters**: filters, e.g.:  
    filters = {[objectHandle] = {'pose', 'jointPosition', 'layer'}, [sim.handle_scene] = {'engineProperties'}}  
    filters = {[object1Handle] = {}, [object2Handle] = {'pose'}}  
    filters = {[sim.handle_sceneobject] = {'pose'}}

## Return values

No return values.

## See also

- [callback functions](../callbackFunctions.md)
