# sim.changeEntityColor

Changes the color of an [entity](../entities.md), and returns its original color. Currently only takes into account [collections](../collections.md) and [shapes](../shapes.md)

## Synopsis

```lua
map[] originalColorData = sim.changeEntityColor(int entityHandle, float[3] newColor,
                                                int colorComponent = sim.colorcomponent_ambient_diffuse)
```

```python
list originalColorData = sim.changeEntityColor(int entityHandle, list newColor,
                                               int colorComponent = sim.colorcomponent_ambient_diffuse)
```

## Parameters

- **entityHandle**: handle of a entity
- **newColor**: array of 3 rgb values, each between 0.0 and 1.0
- **colorComponent**: a [color component](../apiConstants-1.md#colorComponents)

## Return values

- **originalColorData**: original color data, to be used as argument with [sim.restoreEntityColor](simRestoreEntityColor.md)

## See also

- [sim.restoreEntityColor](simRestoreEntityColor.md)
