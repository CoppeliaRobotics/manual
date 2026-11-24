# sim.importShape

Imports a [shape](../shapes.md) from a file (first imports meshes, then groups/merges them into a shape)

## Synopsis

```lua
int shapeHandle = sim.importShape(int fileformat, string pathAndFilename, int options,
                                  float identicalVerticeTolerance, float scalingFactor)
```

```python
int shapeHandle = sim.importShape(int fileformat, string pathAndFilename, int options,
                                  float identicalVerticeTolerance, float scalingFactor)
```

## Parameters

- **fileformat**: set to 0. Fileformat is automatically detected
- **pathAndFilename**: the location of the file to import.
- **options**: bit-coded:

    - bit0 set (1): keep identical vertices
    - bit1 set (2): reserced. keep at 0.
    - bit2 set (4): reserved. keep at 0.
    - bit3 set (8): do not preserve colors
    - bit4 set (16): tries to preserve textures.
    - bit5 set (32): realigns the shape's bounding box with the world.
    - bit7 set (128): ignore up-vector coded in fileformat.
- **identicalVerticeTolerance**: not used. Set to 0
- **scalingFactor**: the scaling factor to apply to the imported vertices

## Return values

- **shapeHandle**: the handle of the imported shape

## See also

- [sim.importMesh](simImportMesh.md)
