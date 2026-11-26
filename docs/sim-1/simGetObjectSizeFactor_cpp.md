# simGetObjectSizeFactor

Retrieves the size factor of a scene object. The size factor is different from the real object size. Use this to be able to adapt to scaling operations

## Synopsis

```cpp
double simGetObjectSizeFactor(int objectHandle)
```

## Parameters

- **objectHandle**: handle of the scene object

## Return values

- size factor or negative value in case of an error
