# sim.moveToConfig_step

Steps a motion object

## Synopsis

```lua
int res, table data = sim.moveToConfig_step(table motionObject)
```

```python
int res, dict data = sim.moveToConfig_step(dict motionObject)
```

## Parameters

- **motionObject**: a motion object

## Return values

- **res**: step result:

    - **negative**: error
    - **0**: step successful, motion is still ongoing
    - **1**: step successful, motion ended
    - **2**: motion aborted
- **data**: current motion state

## See also

- [sim.moveToConfig_init](simMoveToConfig_init.md)
- [sim.moveToConfig_cleanup](simMoveToConfig_cleanup.md)
