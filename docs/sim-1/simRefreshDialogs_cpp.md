# simRefreshDialogs

Refreshes CoppeliaSim's internal dialogs. Calling [sim.refreshDialogs](simRefreshDialogs.md) will not trigger a [sim.message_eventcallback_refreshdialogs](../apiConstants-1.md#simulatorMessages) message

## Synopsis

```cpp
int simRefreshDialogs(int refreshDegree)
```

## Parameters

- **refreshDegree**: refresh degree (0=light, 1=medium, 2=full)

## Return values

- -1 if operation was not successful
