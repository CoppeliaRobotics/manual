# simGetObjectParent

Retrieves the handle of an object's parent object

## Synopsis

```cpp
int simGetObjectParent(int objectHandle)
```

## Parameters

- **objectHandle**: handle of the object

## Return values

- handle of parent or -1 if the parent doesn't exist or in case of an error

## See also

- [simSetObjectParent](simSetObjectParent_cpp.md)
- [simGetObjectChild](simGetObjectChild_cpp.md)
