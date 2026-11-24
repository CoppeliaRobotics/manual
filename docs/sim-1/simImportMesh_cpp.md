# simImportMesh

Imports a mesh from a file

## Synopsis

```cpp
int simImportMesh(int fileformat, const char* pathAndFilename, int options,
                  double identicalVerticeTolerance, double scalingFactor, double*** vertices,
                  int** verticesSizes, int*** indices, int** indicesSizes, double*** reserved,
                  char*** names)
```

## Parameters

- **fileformat**: set to 0. Fileformat is automatically detected
- **pathAndFilename**: the location of the file to import.
- **options**: bit-coded: bit0 set (1): keep identical vertices, bit7 set (128): ignore up-vector coded in fileformat
- **identicalVerticeTolerance**: has no effect. set to zero
- **scalingFactor**: the scaling factor to apply to the imported vertices
- **vertices**: an array to vertice arrays. The import operation may generate several meshes depending on the fileformat. The user is in charge of releasing the memory. See the example below
- **verticesSizes**: an array indicating the individual vertice array sizes. The user is in charge of releasing the memory. See the example below
- **indices**: an array to indice arrays. The import operation may generate several meshes depending on the fileformat. The user is in charge of releasing the memory. Can be nullptr. See the example below
- **indicesSizes**: an array indicating the individual indice array sizes. The user is in charge of releasing the memory. Can be nullptr if indices is also nullptr. See the example below
- **reserved**: reserved for future extensions. Keep at nullptr.
- **names**: not used anymore. Set to nullptr

## Return values

- Number of imported meshes, or 0 or -1 if the operation was not successful

## Example

```cpp
double** vertices;
int* verticesSizes;
int** indices;
int* indicesSizes;
int elementCount = simImportMesh(1, "d:\\example.dxf", 0, 0.0001, 1.0, &vertices,
                                 &verticesSizes, &indices, &indicesSizes, nullptr, nullptr);
if (elementCount > 0)
{
    const double grey[3] = {0.5, 0.5, 0.5};
    for (int i = 0; i < elementCount; i++)
    {
        int shapeHandle = simCreateShape(2, 20.0 * 3.1415 / 180.0, vertices[i],
                               verticesSizes[i], indices[i], indicesSizes[i], nullptr,
                               nullptr, nullptr, nullptr);
        simSetShapeColor(shapeHandle, "", sim.colorcomponent_ambient, grey);
        simReleaseBuffer((char*)indices[i]);
        simReleaseBuffer((char*)vertices[i]);
    }
    simReleaseBuffer((char*)indicesSizes);
    simReleaseBuffer((char*)indices);
    simReleaseBuffer((char*)verticesSizes);
    simReleaseBuffer((char*)vertices);
}
```

## See also

- [simExportMesh](simExportMesh_cpp.md)
- [simImportShape](simImportShape_cpp.md)
- [simCreateShape](simCreateShape_cpp.md)
