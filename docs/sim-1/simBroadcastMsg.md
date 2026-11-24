# sim.broadcastMsg

Broadcasts a message to all scripts, except for the emitting script. Messages are received synchronously via the sysCall_msg [callback function](../callbackFunctions.md)

## Synopsis

```lua
sim.broadcastMsg(map message, int options = 0)
```

```python
sim.broadcastMsg(dict message, int options = 0)
```

## Parameters

- **message**: message to broadcast. Best is to use following skeleton message: message = {'id': 'msgIdentifyingString', 'data': [...]}
- **options**: not used, keep at 0

## Return values

No return values.
