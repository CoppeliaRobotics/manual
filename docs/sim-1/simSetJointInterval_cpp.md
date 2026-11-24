# simSetJointInterval

Sets the interval parameters of a joint (i.e. range values). The attributes or interval parameters might have no effect, depending on the joint-type

## Synopsis

```cpp
int simSetJointInterval(int objectHandle, bool cyclic, const double* interval)
```

## Parameters

- **objectHandle**: handle of the joint object
- **cyclic**: indicates whether the joint is cyclic. Only revolute joints with a lead of 0 can be cyclic
- **interval**: joint limits. The first value is the joint lower limit, the second value is the joint range (i.e. the upper limit is lower limit + range)

## Return values

- -1 if operation was not successful

## See also

- [simGetJointInterval](simGetJointInterval_cpp.md)
