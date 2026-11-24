# sim.getShapeMesh

Retrieves a shape's mesh information

## Synopsis

```lua
float[] vertices, int[] indices, float[] normals = sim.getShapeMesh(int shapeHandle)
```

```python
list vertices, list indices, list normals = sim.getShapeMesh(int shapeHandle)
```

## Parameters

- **shapeHandle**: handle of the shape. See [sim.exportMesh](simExportMesh.md) for a usage example.

## Return values

- **vertices**: array of vertices
- **indices**: array of indices
- **normals**: array of normals

## See also

- [sim.getShapeViz](simGetShapeViz.md)
- [sim.createShape](simCreateShape.md)
- [sim.exportMesh](simExportMesh.md)
