# simGetJointInterval

Retrieves the interval parameters of a joint

## Synopsis

```cpp
int simGetJointInterval(int objectHandle, bool* cyclic, double* interval)
```

## Parameters

- **objectHandle**: handle of the joint
- **cyclic**: indicates whether the joint is cyclic (the joint varies between -pi and +pi in a cyclic manner)
- **interval**: interval of the joint. interval[0] is the joint minimum allowed value, interval[1] is the joint range (the maximum allowed value is interval[0]+interval[1]). When the joint is "cyclic", then the interval parameters don't have any meaning.

## Return values

- -1 if operation was not successful

## See also

- [simSetJointInterval](simSetJointInterval_cpp.md)
