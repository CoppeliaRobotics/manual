# sim.moduleEntry

Creates, modifies or destroys module menu entries. Those are user selectable items located in [Menu bar &gt; Modules]. When selected, the corresponding script will have its [sysCall_moduleEntry](../callbackFunctions.md) callback function triggered, or [sim_message_eventcallback_moduleentry](../apiConstants-1.md#simulatorMessages) triggered

## Synopsis

```lua
int handle = sim.moduleEntry(int handle, string label = nil, int state = -1)
```

```python
int handle = sim.moduleEntry(int handle, string label = None, int state = -1)
```

## Parameters

- **handle**: handle of a module menu entry, or -1 to create one.
- **label**: label of the module entry. If handle is -1, then a path can be specified, in order to build sub-menus, e.g. "Menu\\nSubmenu1\\nSubmenu2\\nLabel". Can be nullptr if handle is not -1.
- **state**: Bit-coded (is ignored if set to -1, -2 destroys an existing item):

    - bit0 is set (1): the item is enabled
    - bit1 is set (2): the item is checked
    - bit2 is set (4): the item is checkable

## Return values

- **handle**: the handle of the module menu entry
