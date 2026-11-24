# simExportMesh

Exports a mesh to a file

## Synopsis

```cpp
int simExportMesh(int fileformat, const char* pathAndFilename, int options, double scalingFactor,
                  int elementCount, double** vertices, const int* verticesSizes, int** indices,
                  const int* indicesSizes, double** reserved, char** names)
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
- **elementCount**: the number of meshes
- **vertices**: an array to vertice arrays. See the example below
- **verticesSizes**: an array indicating the individual vertice array sizes. See the example below
- **indices**: an array to indice arrays. See the example below
- **indicesSizes**: an array indicating the individual indice array sizes. See the example below
- **reserved**: reserved for future extensions. Keep at nullptr.
- **names**: Keep at nullptr

## Return values

- -1 if operation was not successful

## Example

```cpp
// Exports all shapes in the scene
int shapeCount = 0;
while (simGetObjects(shapeCount++, sim.sceneobject_shape) != -1);
shapeCount--;
double** vertices = new double*[shapeCount];
int* verticesSizes = new int[shapeCount];
int** indices = new int*[shapeCount];
int* indicesSizes = new int[shapeCount];
int index = 0;
while (true)
{
    int shapeHandle = simGetObjects(index++, sim.sceneobject_shape);
    if (shapeHandle < 0)
        break;
    double* vert;
    int vertS;
    int* ind;
    int indS;
    simGetShapeMesh(shapeHandle, &vert, &vertS, &ind, &indS, nullptr);
    vertices[index - 1] = vert;
    verticesSizes[index - 1] = vertS;
    indices[index - 1] = ind;
    indicesSizes[index - 1] = indS;
    double m[12];
    simGetObjectMatrix(shapeHandle, -1, m);
    for (int i = 0; i < vertS / 3; i++)
    {
        double v[3]={vert[3 * i + 0], vert[3 * i + 1], vert[3 * i + 2]};
        simTransformVector(m, v);
        vert[3 * i + 0] = v[0];
        vert[3 * i + 1] = v[1];
        vert[3 * i + 2] = v[2];
    }
}

simExportMesh(0, "d:\\example.obj", 0, 1, shapeCount, vertices,
                 verticesSizes, indices, indicesSizes, nullptr, nullptr);
for (int i = 0; i < shapeCount; i++)
{
    simReleaseBuffer((char*)vertices[i]);
    simReleaseBuffer((char*)indices[i]);
}

delete[] vertices;
delete[] verticesSizes;
delete[] indices;
delete[] indicesSizes;
```

## See also

- [simImportMesh](simImportMesh_cpp.md)
- [simGetShapeMesh](simGetShapeMesh_cpp.md)
