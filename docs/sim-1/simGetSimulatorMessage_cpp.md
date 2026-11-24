# simGetSimulatorMessage

Retrieves and removes the next message in the C/C++ or Lua message queues. Use this in a while-loop until all messages have been extracted. While the C/C++ interface has one single message queue, each Lua script has its own message queue. The C/C++ version of this function should only be called from the CoppeliaSim client application. A given message queue cannot hold more than 64 messages, unread messages will be discarded.

## Synopsis

```cpp
char* simGetSimulatorMessage(int* messageID, int* auxiliaryData, int* returnedDataSize)
```

## Parameters

- **messageID**: a simulator message (see the [simulator messages](../apiConstants-1.md#simulatorMessages)) or -1 if no message is available or in case of an error
- **auxiliaryData**: array of 4 integers that can describe the returned message in more details
- **returnedDataSize**: size of the returned buffer

## Return values

- nullptr if no buffer was returned, otherwise a buffer that should be released with [simReleaseBuffer](simReleaseBuffer_cpp.md)
