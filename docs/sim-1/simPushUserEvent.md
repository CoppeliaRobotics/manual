# sim.pushUserEvent

Pushes a user-triggered event. Messages are received asynchronously via the sysCall_event [callback function](../callbackFunctions.md) and via the plugin [sim_message_eventcallback_events](../apiConstants-1.md#simulatorMessages) message call

## Synopsis

```lua
sim.pushUserEvent(string event, int handle int uid, table eventData, int options = 0)
```

```python
sim.pushUserEvent(string event, int handle int uid, dict eventData, int options = 0)
```

## Parameters

- **event**: event name
- **handle**: optional handle associated with the event. Can be -1
- **uid**: optional unique id associated with the event. Can be -1
- **eventData**: event data
- **options**: bit-coded:

    - bit0 set (1): event can be merged with a previous, same event

## Return values

No return values.
