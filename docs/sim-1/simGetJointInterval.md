# sim.getJointInterval

Retrieves the interval parameters of a joint

## Synopsis

```lua
bool cyclic, float[2] interval = sim.getJointInterval(int objectHandle)
```

```python
bool cyclic, list interval = sim.getJointInterval(int objectHandle)
```

## Parameters

- **objectHandle**: handle of the joint

## Return values

- **cyclic**: indicates whether the joint is cyclic (the joint varies between -pi and +pi in a cyclic manner).
- **interval**: interval of the joint. interval[1] is the joint minimum allowed value, interval[2] is the joint range (the maximum allowed value is interval[1]+interval[2]). When the joint is "cyclic", then the interval parameters don't have any meaning.

## See also

- [sim.setJointInterval](simSetJointInterval.md)
