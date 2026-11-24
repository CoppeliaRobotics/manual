# simGetLinkDummy

Retrieves the object handle of the dummy linked to this one

## Synopsis

```cpp
int simGetLinkDummy(int dummyHandle)
```

## Parameters

- **dummyHandle**: handle of the dummy whose linked dummy has to be retrieved.

## Return values

- Handle of the dummy linked to the specified dummy object, or -1 if the dummy is not linked or in case of an error

## See also

- [simSetLinkDummy](simSetLinkDummy_cpp.md)
