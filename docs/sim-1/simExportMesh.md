# sim.exportMesh

Exports a mesh to a file

## Synopsis

```lua
sim.exportMesh(int fileformat, string pathAndFilename, int options, float scalingFactor,
               float[] vertices, int[] indices)
```

```python
sim.exportMesh(int fileformat, string pathAndFilename, int options, float scalingFactor,
               list vertices, list indices)
```

## Parameters

- **fileformat**: the fileformat to export to:

    - 0: OBJ format
    - 3: TEXT STL format
    - 4: BINARY STL format
    - 5: COLLADA format
    - 6: TEXT PLY format
    - 7: BINARY PLY format
- **pathAndFilename**: the location of the file to create.
- **options**: keep at 0
- **scalingFactor**: the scaling factor to apply to the vertices to export
- **vertices**: an array of vertice arrays. See the example below
- **indices**: an array of indice arrays. See the example below

## Return values

No return values.

## Example

```lua
--lua

-- Exports all shapes in the scene
local allVertices = {}
local allIndices = {}
local shapeIndex = 0
while true do
    local h = sim.getObjects(shapeIndex, sim.sceneobject_shape)
    if h < 0 then
        break
    end
    shapeIndex = shapeIndex + 1
    local vertices, indices = sim.getShapeMesh(h)
    local m = sim.getObjectMatrix(h)
    for i = 1, #vertices // 3, 1 do
        local v = {vertices[3 * (i - 1) +1], vertices[3 * (i - 1) + 2], vertices[3 * (i - 1) + 3]}
        v = sim.multiplyVector(m, v)
        vertices[3 * (i - 1) + 1] = v[1]
        vertices[3 * (i - 1) + 2] = v[2]
        vertices[3 * (i - 1) + 3] = v[3]
    end
    table.insert(allVertices, vertices)
    table.insert(allIndices, indices)
end

if #allVertices > 0 then
    sim.exportMesh(0, "d:\\example.obj", 0, 1, allVertices, allIndices)
end
```

## See also

- [sim.importMesh](simImportMesh.md)
- [sim.getShapeMesh](simGetShapeMesh.md)
