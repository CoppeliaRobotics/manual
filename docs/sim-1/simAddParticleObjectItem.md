# sim.addParticleObjectItem

Adds an item (or clears all items) to a previously inserted particle object

## Synopsis

```lua
sim.addParticleObjectItem(int particleObjectHandle, float[] itemData)
```

```python
sim.addParticleObjectItem(int particleObjectHandle, list itemData)
```

## Parameters

- **objectHandle**: handle of a previously added particle object
- **itemData**: data relative to an item. All items (particles) require at least 6 values:p1x, p1y, p1z, p2x, p2y, p2z with p1 is the particle start position, p2-p1 is the particle initial velocity vector. Auxiliary values might be required depending on the particle object attributes. See the [particle object type combined with attributes](../apiConstants-1.md#particleObjects) for more information. If None/nil, the particle object is emptied of all its items

## Return values

No return values.

## See also

- [sim.addParticleObject](simAddParticleObject.md)
- [sim.removeParticleObject](simRemoveParticleObject.md)
