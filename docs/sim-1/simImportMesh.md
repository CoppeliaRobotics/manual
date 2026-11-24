# sim.importMesh

Imports a mesh from a file

## Synopsis

```lua
float[] vertices, int[] indices = sim.importMesh(int fileformat, string pathAndFilename, int options,
                                                 float identicalVerticeTolerance,
                                                 float scalingFactor)
```

```python
list vertices, list indices = sim.importMesh(int fileformat, string pathAndFilename, int options,
                                             float identicalVerticeTolerance, float scalingFactor)
```

## Parameters

- **fileformat**: set to 0. Fileformat is automatically detected
- **pathAndFilename**: the location of the file to import.
- **options**: bit-coded: bit0 set (1): keep identical vertices, bit7 set (128): ignore up-vector coded in fileformat
- **identicalVerticeTolerance**: has no effect. set to zero
- **scalingFactor**: the scaling factor to apply to the imported vertices

## Return values

- **vertices**: an array of vertice arrays. The import operation may generate several meshes depending on the fileformat
- **indices**: an array of index arrays. The import operation may generate several meshes depending on the fileformat

## Example

```lua
--lua

local vertices, indices, reserved, names = sim.importMesh(1, "d:\\example.dxf", 0, 0.0001, 1)
for i = 1, #vertices, 1 do
    h = sim.createShape(2, 20 * math.pi / 180, vertices[i], indices[i])
    sim.setShapeColor(h, "", sim.colorcomponent_ambient, {0.5, 0.5, 0.5})
    sim.setObjectAlias(h, names[i])
end
```

## See also

- [sim.exportMesh](simExportMesh.md)
- [sim.importShape](simImportShape.md)
- [sim.createShape](simCreateShape.md)
