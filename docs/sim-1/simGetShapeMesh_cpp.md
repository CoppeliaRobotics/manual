# simGetShapeMesh

Retrieves a shape's mesh information

## Synopsis

```cpp
int simGetShapeMesh(int shapeHandle, double** vertices, int* verticesSize, int** indices,
                    int* indicesSize, double** normals)
```

## Parameters

- **shapeHandle**: handle of the shape
- **vertices**: receives the vertices. The user is in charge of destroying the array with [simReleaseBuffer](simReleaseBuffer_cpp.md). See [simExportMesh](simExportMesh.md) for a usage example.
- **verticesSize**: receives the size of the vertices array. See [simExportMesh](simExportMesh.md) for a usage example.
- **indices**: receives the indices. The user is in charge of destroying the array with [simReleaseBuffer](simReleaseBuffer_cpp.md). See [simExportMesh](simExportMesh.md) for a usage example.
- **indicesSize**: receives the size of the indice array. See [simExportMesh](simExportMesh.md) for a usage example.
- **normals**: receives the normals (3 times the size of indicesSize). The user is in charge of destroying the array with [simReleaseBuffer](simReleaseBuffer_cpp.md). Can be nullptr.

## Return values

- -1 if operation was not successful

## See also

- [simGetShapeViz](simGetShapeViz_cpp.md)
- [simCreateShape](simCreateShape_cpp.md)
- [simExportMesh](simExportMesh_cpp.md)
