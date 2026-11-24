# sim.refreshDialogs

Refreshes CoppeliaSim's internal dialogs. Calling [sim.refreshDialogs](simRefreshDialogs.md) will not trigger a [sim.message_eventcallback_refreshdialogs](../apiConstants-1.md#simulatorMessages) message

## Synopsis

```lua
sim.refreshDialogs(int refreshDegree)
```

```python
sim.refreshDialogs(int refreshDegree)
```

## Parameters

- **refreshDegree**: refresh degree (0=light, 1=medium, 2=full)

## Return values

No return values.
