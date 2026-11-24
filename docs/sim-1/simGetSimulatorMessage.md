# sim.getSimulatorMessage

Retrieves and removes the next message in the C/C++ or Lua message queues. Use this in a while-loop until all messages have been extracted. While the C/C++ interface has one single message queue, each Lua script has its own message queue. The C/C++ version of this function should only be called from the CoppeliaSim client application. A given message queue cannot hold more than 64 messages, unread messages will be discarded.

## Synopsis

```lua
int message, int[4] auxiliaryData, int[] auxiliaryData2 = sim.getSimulatorMessage()
```

```python
int message, list auxiliaryData, list auxiliaryData2 = sim.getSimulatorMessage()
```

## Parameters

No parameters.

## Return values

- **message**: [simulator message](../apiConstants-1.md#simulatorMessages)
- **auxiliaryData**: array of numbers that describe the returned message in more details
- **auxiliaryData2**: array of numbers that describe the returned message in more details
