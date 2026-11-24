# simGetQHull

Retrieves the convex hull mesh from the specified vertices

## Synopsis

```cpp
int simGetQHull(const double* inVertices, int inVerticesL, double** verticesOut, int* verticesOutL,
                int** indicesOut, int* indicesOutL, int reserved1, const double* reserved2)
```

## Parameters

- **inVertices**: pointer to the input vertices (succession of x/y/z values).
- **inVerticesL**: number of input vertices times 3.
- **verticesOut**: pointer to a pointer to the output vertices. The output vertices are allocated by CoppeliaSim and the user is in charge of releasing the buffer via [simReleaseBuffer](simReleaseBuffer_cpp.md).
- **verticesOutL**: pointer to the number of output vertices times 3.
- **indicesOut**: pointer to a pointer to the output indices. The output indices are allocated by CoppeliaSim and the user is in charge of releasing the buffer via [simReleaseBuffer](simReleaseBuffer_cpp.md).
- **indicesOutL**: pointer to the number of output indices (i.e. the number of triangles times 3).
- **reserved1**: reserved, set to 0.
- **reserved2**: reserved, set to nullptr.

## Return values

- -1 or 0 if operation was not successful.

## See also

- [simConvexDecompose](simConvexDecompose_cpp.md)
- [simGetDecimatedMesh](simGetDecimatedMesh_cpp.md)
