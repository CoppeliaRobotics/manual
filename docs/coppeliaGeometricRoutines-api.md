# Coppelia Geometric Routines, API reference

All units, unless otherwise indicated, are specified in meters and radians.

- [`geom_copyMesh`](#geom_copyMesh)
- [`geom_copyOctree`](#geom_copyOctree)
- [`geom_copyPtcloud`](#geom_copyPtcloud)
- [`geom_createMesh`](#geom_createMesh)
- [`geom_createOctreeFromColorPoints`](#geom_createOctreeFromColorPoints)
- [`geom_createOctreeFromMesh`](#geom_createOctreeFromMesh)
- [`geom_createOctreeFromOctree`](#geom_createOctreeFromOctree)
- [`geom_createOctreeFromPoints`](#geom_createOctreeFromPoints)
- [`geom_createPtcloudFromColorPoints`](#geom_createPtcloudFromColorPoints)
- [`geom_createPtcloudFromPoints`](#geom_createPtcloudFromPoints)
- [`geom_destroyMesh`](#geom_destroyMesh)
- [`geom_destroyOctree`](#geom_destroyOctree)
- [`geom_destroyPtcloud`](#geom_destroyPtcloud)
- [`geom_getApproxBoxBoxDistance`](#geom_getApproxBoxBoxDistance)
- [`geom_getBoxBoxCollision`](#geom_getBoxBoxCollision)
- [`geom_getBoxBoxDistanceIfSmaller`](#geom_getBoxBoxDistanceIfSmaller)
- [`geom_getBoxPointCollision`](#geom_getBoxPointCollision)
- [`geom_getBoxPointDistanceIfSmaller`](#geom_getBoxPointDistanceIfSmaller)
- [`geom_getBoxSegmentCollision`](#geom_getBoxSegmentCollision)
- [`geom_getBoxSegmentDistanceIfSmaller`](#geom_getBoxSegmentDistanceIfSmaller)
- [`geom_getBoxTriangleCollision`](#geom_getBoxTriangleCollision)
- [`geom_getBoxTriangleDistanceIfSmaller`](#geom_getBoxTriangleDistanceIfSmaller)
- [`geom_getMeshFromSerializationData`](#geom_getMeshFromSerializationData)
- [`geom_getMeshMeshCollision`](#geom_getMeshMeshCollision)
- [`geom_getMeshMeshDistanceIfSmaller`](#geom_getMeshMeshDistanceIfSmaller)
- [`geom_getMeshOctreeCollision`](#geom_getMeshOctreeCollision)
- [`geom_getMeshOctreeDistanceIfSmaller`](#geom_getMeshOctreeDistanceIfSmaller)
- [`geom_getMeshPointDistanceIfSmaller`](#geom_getMeshPointDistanceIfSmaller)
- [`geom_getMeshPtcloudDistanceIfSmaller`](#geom_getMeshPtcloudDistanceIfSmaller)
- [`geom_getMeshSegmentCollision`](#geom_getMeshSegmentCollision)
- [`geom_getMeshSegmentDistanceIfSmaller`](#geom_getMeshSegmentDistanceIfSmaller)
- [`geom_getMeshSerializationData`](#geom_getMeshSerializationData)
- [`geom_getMeshTriangleCollision`](#geom_getMeshTriangleCollision)
- [`geom_getMeshTriangleDistanceIfSmaller`](#geom_getMeshTriangleDistanceIfSmaller)
- [`geom_getOctreeFromSerializationData`](#geom_getOctreeFromSerializationData)
- [`geom_getOctreeOctreeCollision`](#geom_getOctreeOctreeCollision)
- [`geom_getOctreeOctreeDistanceIfSmaller`](#geom_getOctreeOctreeDistanceIfSmaller)
- [`geom_getOctreePointCollision`](#geom_getOctreePointCollision)
- [`geom_getOctreePointDistanceIfSmaller`](#geom_getOctreePointDistanceIfSmaller)
- [`geom_getOctreePtcloudCollision`](#geom_getOctreePtcloudCollision)
- [`geom_getOctreePtcloudDistanceIfSmaller`](#geom_getOctreePtcloudDistanceIfSmaller)
- [`geom_getOctreeSegmentCollision`](#geom_getOctreeSegmentCollision)
- [`geom_getOctreeSegmentDistanceIfSmaller`](#geom_getOctreeSegmentDistanceIfSmaller)
- [`geom_getOctreeSerializationData`](#geom_getOctreeSerializationData)
- [`geom_getOctreeTriangleCollision`](#geom_getOctreeTriangleCollision)
- [`geom_getOctreeTriangleDistanceIfSmaller`](#geom_getOctreeTriangleDistanceIfSmaller)
- [`geom_getOctreeVoxelData`](#geom_getOctreeVoxelData)
- [`geom_getPtcloudFromSerializationData`](#geom_getPtcloudFromSerializationData)
- [`geom_getPtcloudPointDistanceIfSmaller`](#geom_getPtcloudPointDistanceIfSmaller)
- [`geom_getPtcloudPoints`](#geom_getPtcloudPoints)
- [`geom_getPtcloudPtcloudDistanceIfSmaller`](#geom_getPtcloudPtcloudDistanceIfSmaller)
- [`geom_getPtcloudSegmentDistanceIfSmaller`](#geom_getPtcloudSegmentDistanceIfSmaller)
- [`geom_getPtcloudSerializationData`](#geom_getPtcloudSerializationData)
- [`geom_getPtcloudTriangleDistanceIfSmaller`](#geom_getPtcloudTriangleDistanceIfSmaller)
- [`geom_getSegmentPointDistanceIfSmaller`](#geom_getSegmentPointDistanceIfSmaller)
- [`geom_getSegmentSegmentDistanceIfSmaller`](#geom_getSegmentSegmentDistanceIfSmaller)
- [`geom_getTrianglePointDistanceIfSmaller`](#geom_getTrianglePointDistanceIfSmaller)
- [`geom_getTriangleSegmentCollision`](#geom_getTriangleSegmentCollision)
- [`geom_getTriangleSegmentDistanceIfSmaller`](#geom_getTriangleSegmentDistanceIfSmaller)
- [`geom_getTriangleTriangleCollision`](#geom_getTriangleTriangleCollision)
- [`geom_getTriangleTriangleDistanceIfSmaller`](#geom_getTriangleTriangleDistanceIfSmaller)
- [`geom_insertColorPointsIntoOctree`](#geom_insertColorPointsIntoOctree)
- [`geom_insertColorPointsIntoPtcloud`](#geom_insertColorPointsIntoPtcloud)
- [`geom_insertMeshIntoOctree`](#geom_insertMeshIntoOctree)
- [`geom_insertOctreeIntoOctree`](#geom_insertOctreeIntoOctree)
- [`geom_insertPointsIntoOctree`](#geom_insertPointsIntoOctree)
- [`geom_insertPointsIntoPtcloud`](#geom_insertPointsIntoPtcloud)
- [`geom_intersectPointsWithPtcloud`](#geom_intersectPointsWithPtcloud)
- [`geom_isPointInVolume`](#geom_isPointInVolume)
- [`geom_raySensorDetectMeshIfSmaller`](#geom_raySensorDetectMeshIfSmaller)
- [`geom_raySensorDetectOctreeIfSmaller`](#geom_raySensorDetectOctreeIfSmaller)
- [`geom_removeMeshFromOctree`](#geom_removeMeshFromOctree)
- [`geom_removeOctreeFromOctree`](#geom_removeOctreeFromOctree)
- [`geom_removePointsFromOctree`](#geom_removePointsFromOctree)
- [`geom_removeOctreeFromPtcloud`](#geom_removeOctreeFromPtcloud)
- [`geom_removePointsFromPtcloud`](#geom_removePointsFromPtcloud)
- [`geom_scaleMesh`](#geom_scaleMesh)
- [`geom_scaleOctree`](#geom_scaleOctree)
- [`geom_scalePtcloud`](#geom_scalePtcloud)
- [`geom_volumeSensorDetectMeshIfSmaller`](#geom_volumeSensorDetectMeshIfSmaller)
- [`geom_volumeSensorDetectOctreeIfSmaller`](#geom_volumeSensorDetectOctreeIfSmaller)
- [`geom_volumeSensorDetectPtcloudIfSmaller`](#geom_volumeSensorDetectPtcloudIfSmaller)
- [`geom_volumeSensorDetectSegmentIfSmaller`](#geom_volumeSensorDetectSegmentIfSmaller)
- [`geom_volumeSensorDetectTriangleIfSmaller`](#geom_volumeSensorDetectTriangleIfSmaller)

## <a id="meshCreation"></a>Mesh creation/destruction/manipulation/info

- [`geom_createMesh`](#geom_createMesh)
- [`geom_destroyMesh`](#geom_destroyMesh)
- [`geom_copyMesh`](#geom_copyMesh)
- [`geom_scaleMesh`](#geom_scaleMesh)
- [`geom_getMeshSerializationData`](#geom_getMeshSerializationData)
- [`geom_getMeshFromSerializationData`](#geom_getMeshFromSerializationData)
- [`geom_createOctreeFromMesh`](#geom_createOctreeFromMesh)
- [`geom_insertMeshIntoOctree`](#geom_insertMeshIntoOctree)
- [`geom_removeMeshFromOctree`](#geom_removeMeshFromOctree)

## <a id="octreeCreation"></a>OC-tree creation/destruction/manipulation/info

- [`geom_createOctreeFromPoints`](#geom_createOctreeFromPoints)
- [`geom_createOctreeFromColorPoints`](#geom_createOctreeFromColorPoints)
- [`geom_createOctreeFromMesh`](#geom_createOctreeFromMesh)
- [`geom_createOctreeFromOctree`](#geom_createOctreeFromOctree)
- [`geom_destroyOctree`](#geom_destroyOctree)
- [`geom_copyOctree`](#geom_copyOctree)
- [`geom_scaleOctree`](#geom_scaleOctree)
- [`geom_getOctreeSerializationData`](#geom_getOctreeSerializationData)
- [`geom_getOctreeFromSerializationData`](#geom_getOctreeFromSerializationData)
- [`geom_getOctreeVoxelData`](#geom_getOctreeVoxelData)
- [`geom_insertPointsIntoOctree`](#geom_insertPointsIntoOctree)
- [`geom_insertColorPointsIntoOctree`](#geom_insertColorPointsIntoOctree)
- [`geom_insertMeshIntoOctree`](#geom_insertMeshIntoOctree)
- [`geom_insertOctreeIntoOctree`](#geom_insertOctreeIntoOctree)
- [`geom_removePointsFromOctree`](#geom_removePointsFromOctree)
- [`geom_removeMeshFromOctree`](#geom_removeMeshFromOctree)
- [`geom_removeOctreeFromOctree`](#geom_removeOctreeFromOctree)

## <a id="ptcloudCreation"></a>Point-cloud creation/destruction/manipulation/info

- [`geom_createPtcloudFromPoints`](#geom_createPtcloudFromPoints)
- [`geom_createPtcloudFromColorPoints`](#geom_createPtcloudFromColorPoints)
- [`geom_destroyPtcloud`](#geom_destroyPtcloud)
- [`geom_copyPtcloud`](#geom_copyPtcloud)
- [`geom_scalePtcloud`](#geom_scalePtcloud)
- [`geom_getPtcloudSerializationData`](#geom_getPtcloudSerializationData)
- [`geom_getPtcloudFromSerializationData`](#geom_getPtcloudFromSerializationData)
- [`geom_getPtcloudPoints`](#geom_getPtcloudPoints)
- [`geom_insertPointsIntoPtcloud`](#geom_insertPointsIntoPtcloud)
- [`geom_insertColorPointsIntoPtcloud`](#geom_insertColorPointsIntoPtcloud)
- [`geom_removePointsFromPtcloud`](#geom_removePointsFromPtcloud)
- [`geom_removeOctreeFromPtcloud`](#geom_removeOctreeFromPtcloud)
- [`geom_intersectPointsWithPtcloud`](#geom_intersectPointsWithPtcloud)

## <a id="meshCollision"></a>Mesh collision detection

- [`geom_getMeshMeshCollision`](#geom_getMeshMeshCollision)
- [`geom_getMeshOctreeCollision`](#geom_getMeshOctreeCollision)
- [`geom_getMeshTriangleCollision`](#geom_getMeshTriangleCollision)
- [`geom_getMeshSegmentCollision`](#geom_getMeshSegmentCollision)

## <a id="octreeCollision"></a>OC-tree collision detection

- [`geom_getMeshOctreeCollision`](#geom_getMeshOctreeCollision)
- [`geom_getOctreeOctreeCollision`](#geom_getOctreeOctreeCollision)
- [`geom_getOctreePtcloudCollision`](#geom_getOctreePtcloudCollision)
- [`geom_getOctreeTriangleCollision`](#geom_getOctreeTriangleCollision)
- [`geom_getOctreeSegmentCollision`](#geom_getOctreeSegmentCollision)
- [`geom_getOctreePointCollision`](#geom_getOctreePointCollision)

## <a id="ptcloudCollision"></a>Point-cloud collision detection

```
geom_getOctreePtcloudCollision
```

## <a id="primitiveCollision"></a>Primitives collision detection

- [`geom_getMeshTriangleCollision`](#geom_getMeshTriangleCollision)
- [`geom_getMeshSegmentCollision`](#geom_getMeshSegmentCollision)
- [`geom_getOctreeTriangleCollision`](#geom_getOctreeTriangleCollision)
- [`geom_getOctreeSegmentCollision`](#geom_getOctreeSegmentCollision)
- [`geom_getOctreePointCollision`](#geom_getOctreePointCollision)
- [`geom_getBoxBoxCollision`](#geom_getBoxBoxCollision)
- [`geom_getBoxTriangleCollision`](#geom_getBoxTriangleCollision)
- [`geom_getBoxSegmentCollision`](#geom_getBoxSegmentCollision)
- [`geom_getBoxPointCollision`](#geom_getBoxPointCollision)
- [`geom_getTriangleTriangleCollision`](#geom_getTriangleTriangleCollision)
- [`geom_getTriangleSegmentCollision`](#geom_getTriangleSegmentCollision)

## <a id="meshDistance"></a>Mesh minimum distance calculation

- [`geom_getMeshMeshDistanceIfSmaller`](#geom_getMeshMeshDistanceIfSmaller)
- [`geom_getMeshOctreeDistanceIfSmaller`](#geom_getMeshOctreeDistanceIfSmaller)
- [`geom_getMeshPtcloudDistanceIfSmaller`](#geom_getMeshPtcloudDistanceIfSmaller)
- [`geom_getMeshTriangleDistanceIfSmaller`](#geom_getMeshTriangleDistanceIfSmaller)
- [`geom_getMeshSegmentDistanceIfSmaller`](#geom_getMeshSegmentDistanceIfSmaller)
- [`geom_getMeshPointDistanceIfSmaller`](#geom_getMeshPointDistanceIfSmaller)

## <a id="octreeDistance"></a>OC-tree minimum distance calculation

- [`geom_getMeshOctreeDistanceIfSmaller`](#geom_getMeshOctreeDistanceIfSmaller)
- [`geom_getOctreeOctreeDistanceIfSmaller`](#geom_getOctreeOctreeDistanceIfSmaller)
- [`geom_getOctreePtcloudDistanceIfSmaller`](#geom_getOctreePtcloudDistanceIfSmaller)
- [`geom_getOctreeTriangleDistanceIfSmaller`](#geom_getOctreeTriangleDistanceIfSmaller)
- [`geom_getOctreeSegmentDistanceIfSmaller`](#geom_getOctreeSegmentDistanceIfSmaller)
- [`geom_getOctreePointDistanceIfSmaller`](#geom_getOctreePointDistanceIfSmaller)

## <a id="ptcloudDistance"></a>Point-cloud minimum distance calculation

- [`geom_getMeshPtcloudDistanceIfSmaller`](#geom_getMeshPtcloudDistanceIfSmaller)
- [`geom_getOctreePtcloudDistanceIfSmaller`](#geom_getOctreePtcloudDistanceIfSmaller)
- [`geom_getPtcloudPtcloudDistanceIfSmaller`](#geom_getPtcloudPtcloudDistanceIfSmaller)
- [`geom_getPtcloudTriangleDistanceIfSmaller`](#geom_getPtcloudTriangleDistanceIfSmaller)
- [`geom_getPtcloudSegmentDistanceIfSmaller`](#geom_getPtcloudSegmentDistanceIfSmaller)
- [`geom_getPtcloudPointDistanceIfSmaller`](#geom_getPtcloudPointDistanceIfSmaller)

## <a id="primitiveDistance"></a>Primitives minimum distance calculation

- [`geom_getMeshTriangleDistanceIfSmaller`](#geom_getMeshTriangleDistanceIfSmaller)
- [`geom_getMeshSegmentDistanceIfSmaller`](#geom_getMeshSegmentDistanceIfSmaller)
- [`geom_getMeshPointDistanceIfSmaller`](#geom_getMeshPointDistanceIfSmaller)
- [`geom_getOctreeTriangleDistanceIfSmaller`](#geom_getOctreeTriangleDistanceIfSmaller)
- [`geom_getOctreeSegmentDistanceIfSmaller`](#geom_getOctreeSegmentDistanceIfSmaller)
- [`geom_getOctreePointDistanceIfSmaller`](#geom_getOctreePointDistanceIfSmaller)
- [`geom_getPtcloudTriangleDistanceIfSmaller`](#geom_getPtcloudTriangleDistanceIfSmaller)
- [`geom_getPtcloudSegmentDistanceIfSmaller`](#geom_getPtcloudSegmentDistanceIfSmaller)
- [`geom_getPtcloudPointDistanceIfSmaller`](#geom_getPtcloudPointDistanceIfSmaller)
- [`geom_getBoxBoxDistanceIfSmaller`](#geom_getBoxBoxDistanceIfSmaller)
- [`geom_getApproxBoxBoxDistance`](#geom_getApproxBoxBoxDistance)
- [`geom_getBoxTriangleDistanceIfSmaller`](#geom_getBoxTriangleDistanceIfSmaller)
- [`geom_getBoxSegmentDistanceIfSmaller`](#geom_getBoxSegmentDistanceIfSmaller)
- [`geom_getBoxPointDistanceIfSmaller`](#geom_getBoxPointDistanceIfSmaller)
- [`geom_getTriangleTriangleDistanceIfSmaller`](#geom_getTriangleTriangleDistanceIfSmaller)
- [`geom_getTriangleSegmentDistanceIfSmaller`](#geom_getTriangleSegmentDistanceIfSmaller)
- [`geom_getTrianglePointDistanceIfSmaller`](#geom_getTrianglePointDistanceIfSmaller)
- [`geom_getSegmentSegmentDistanceIfSmaller`](#geom_getSegmentSegmentDistanceIfSmaller)
- [`geom_getSegmentPointDistanceIfSmaller`](#geom_getSegmentPointDistanceIfSmaller)

## <a id="proximitySensor"></a>Proximity sensor simulation

- [`geom_volumeSensorDetectMeshIfSmaller`](#geom_volumeSensorDetectMeshIfSmaller)
- [`geom_volumeSensorDetectOctreeIfSmaller`](#geom_volumeSensorDetectOctreeIfSmaller)
- [`geom_volumeSensorDetectPtcloudIfSmaller`](#geom_volumeSensorDetectPtcloudIfSmaller)
- [`geom_volumeSensorDetectTriangleIfSmaller`](#geom_volumeSensorDetectTriangleIfSmaller)
- [`geom_volumeSensorDetectSegmentIfSmaller`](#geom_volumeSensorDetectSegmentIfSmaller)
- [`geom_isPointInVolume`](#geom_isPointInVolume)
- [`geom_raySensorDetectMeshIfSmaller`](#geom_raySensorDetectMeshIfSmaller)
- [`geom_raySensorDetectOctreeIfSmaller`](#geom_raySensorDetectOctreeIfSmaller)

## <a id="other"></a>Other API functions

```
geom_isPointInVolume
```

### <a id="geom_copyMesh"></a>geom_copyMesh

**Description**: Duplicates a mesh object.

**Synopsis**: `CObbStruct* geom_copyMesh(const CObbStruct* meshObbStruct)`

**Arguments**:

- **meshObbStruct**: the mesh object to duplicate.

**Return value**: A pointer to the duplicated mesh object in case of success, otherwise nullptr.

**See also**: [geom_createMesh](#geom_createMesh)

### <a id="geom_copyOctree"></a>geom_copyOctree

**Description**: Duplicates an OC-tree object.

**Synopsis**: `COcStruct* geom_copyOctree(const COcStruct* ocStruct)`

**Arguments**:

- **ocStruct**: the OC-tree object to duplicate.

**Return value**: A pointer to the duplicated OC-tree object in case of success, otherwise nullptr.

### <a id="geom_copyPtcloud"></a>geom_copyPtcloud

**Description**: Duplicates a point-cloud object.

**Synopsis**: `CPcStruct* geom_copyPtcloud(const CPcStruct* pcStruct)`

**Arguments**:

- **pcStruct**: the point-cloud object to duplicate.

**Return value**: A pointer to the duplicated point-cloud object in case of success, otherwise nullptr.

### <a id="geom_createMesh"></a>geom_createMesh

**Description**: Creates a mesh object.

**Synopsis**: `CObbStruct* geom_createMesh(const double* vertices,int verticesSize,const int* indices,int indicesSize,const CPose* meshOrigin=nullptr,double triangleEdgeMaxLength=0.3,int maxTrianglesInBoundingBox=8)`

**Arguments**:

- **vertices**: an array with the vertices of the mesh, expressed relative to the world origin.
- **verticesSize**: the size of the vertex array, i.e. 3\*vertexCount.
- **indices**: an array with the indices of the mesh.
- **indicesSize**: the size of the index array, i.e. each triangle takes 3 indices.
- **meshOrigin**: the transformation frame of the mesh. Can be nullptr, in which case the frame of the mesh is located at the world origin.
- **triangleEdgeMaxLength**: the maximum triangle size used internally for efficient calculations. A smaller size usually results in faster calculations, but larger calculation structures.
- **maxTrianglesInBoundingBox**: the maximum number of triangles in leaf bounding boxes, used internally for efficient calculations. A smaller value usually results in faster calculations, but larger calculation structures.

**Return value**: A pointer to the mesh object in case of success, nullptr otherwise.

**See also**: [geom_destroyMesh](#geom_destroyMesh), [geom_copyMesh](#geom_copyMesh), [geom_getMeshFromSerializationData](#geom_getMeshFromSerializationData)

### <a id="geom_createOctreeFromColorPoints"></a>geom_createOctreeFromColorPoints

**Description**: Creates an OC-tree object from several points with individual colors and individual user data.

**Synopsis**: `COcStruct* geom_createOctreeFromColorPoints(const double* points,int pointCnt,const CPose* octreeOrigin=nullptr,double cellS=0.05,const unsigned char* rgbData=nullptr,const unsigned int* usrData=nullptr)`

**Arguments**:

- **points**: an array with point data, expressed relative to the world origin.
- **pointCnt**: the number of provided points.
- **octreeOrigin**: the transformation frame of the OC-tree. Can be nullptr, in which case the frame of the OC-tree is located at the world origin.
- **cellS**: the desired OC-tree voxel size.
- **rgbData**: the RGB colors (0-255) of the various points (i.e. one color per point).
- **usrData**: the user data of the various points (i.e. one user data per point).

**Return value**: A pointer to an OC-tree object in case of success, otherwise nullptr.

**See also**: [geom_createOctreeFromPoints](#geom_createOctreeFromPoints), [geom_createOctreeFromMesh](#geom_createOctreeFromMesh), [geom_createOctreeFromOctree](#geom_createOctreeFromOctree), [geom_destroyOctree](#geom_destroyOctree), [geom_copyOctree](#geom_copyOctree), [geom_getOctreeFromSerializationData](#geom_getOctreeFromSerializationData), [geom_insertColorPointsIntoOctree](#geom_insertColorPointsIntoOctree)

### <a id="geom_createOctreeFromMesh"></a>geom_createOctreeFromMesh

**Description**: Creates an OC-tree object from a mesh object.

**Synopsis**: `COcStruct* geom_createOctreeFromMesh(const CObbStruct* meshObbStruct,const CPose& meshTransformation,const CPose* octreeOrigin=nullptr,double cellS=0.05,const unsigned char rgbData[3]=nullptr,unsigned int usrData=0)`

**Arguments**:

- **meshObbStruct**: the mesh object.
- **meshTransformation**: the transformation frame of the mesh object.
- **octreeOrigin**: the transformation frame of the OC-tree. Can be nullptr, in which case the frame of the OC-tree is located at the world origin.
- **cellS**: the desired OC-tree voxel size.
- **rgbData**: the RGB color (0-255) of the generated voxels.
- **usrData**: the user data of the generated voxels.

**Return value**: A pointer to an OC-tree object in case of success, otherwise nullptr.

**See also**: [geom_createOctreeFromPoints](#geom_createOctreeFromPoints),[geom_createOctreeFromColorPoints](#geom_createOctreeFromColorPoints), [geom_createOctreeFromOctree](#geom_createOctreeFromOctree), [geom_destroyOctree](#geom_destroyOctree), [geom_copyOctree](#geom_copyOctree), [geom_getOctreeFromSerializationData](#geom_getOctreeFromSerializationData)

### <a id="geom_createOctreeFromOctree"></a>geom_createOctreeFromOctree

**Description**: Creates an OC-tree object from another OC-tree object.

**Synopsis**: `COcStruct* geom_createOctreeFromOctree(const COcStruct* otherOctreeStruct,const CPose& otherOctreeTransformation,const CPose* newOctreeOrigin=nullptr,double newOctreeCellS=0.05,const unsigned char rgbData[3]=nullptr,unsigned int usrData=0)`

**Arguments**:

- **otherOctreeStruct**: the other OC-tree object.
- **otherOctreeTransformation**: the transformation frame of the other OC-tree object.
- **newOctreeOrigin**: the transformation frame of the new OC-tree. Can be nullptr, in which case the frame of the new OC-tree is located at the world origin.
- **newOctreeCellS**: the desired OC-tree voxel size.
- **rgbData**: the RGB color (0-255) of the generated voxels.
- **usrData**: the user data of the generated voxels.

**Return value**: A pointer to an OC-tree object in case of success, otherwise nullptr.

**See also**: [geom_createOctreeFromPoints](#geom_createOctreeFromPoints),[geom_createOctreeFromColorPoints](#geom_createOctreeFromColorPoints), [geom_createOctreeFromMesh](#geom_createOctreeFromMesh), [geom_destroyOctree](#geom_destroyOctree), [geom_copyOctree](#geom_copyOctree), [geom_getOctreeFromSerializationData](#geom_getOctreeFromSerializationData)

### <a id="geom_createOctreeFromPoints"></a>geom_createOctreeFromPoints

**Description**: Creates an OC-tree object from several points.

**Synopsis**: `COcStruct* geom_createOctreeFromPoints(const double* points,int pointCnt,const CPose* octreeOrigin=nullptr,double cellS=0.05,const unsigned char rgbData[3]=nullptr,unsigned int usrData=0)`

**Arguments**:

- **points**: an array with point data, expressed relative to the world origin.
- **pointCnt**: the number of provided points.
- **octreeOrigin**: the transformation frame of the OC-tree. Can be nullptr, in which case the frame of the OC-tree is located at the world origin.
- **cellS**: the desired OC-tree voxel size.
- **rgbData**: the RGB color (0-255) of the generated voxels.
- **usrData**: the user data of the generated voxels.

**Return value**: A pointer to an OC-tree object in case of success, otherwise nullptr.

**See also**: [geom_createOctreeFromColorPoints](#geom_createOctreeFromColorPoints), [geom_createOctreeFromMesh](#geom_createOctreeFromMesh), [geom_createOctreeFromOctree](#geom_createOctreeFromOctree), [geom_destroyOctree](#geom_destroyOctree), [geom_copyOctree](#geom_copyOctree), [geom_getOctreeFromSerializationData](#geom_getOctreeFromSerializationData), [geom_insertPointsIntoOctree](#geom_insertPointsIntoOctree)

### <a id="geom_createPtcloudFromColorPoints"></a>geom_createPtcloudFromColorPoints

**Description**: Creates a point-cloud object from several points with individual colors.

**Synopsis**: `CPcStruct* geom_createPtcloudFromColorPoints(const double* points,int pointCnt,const CPose* ptcloudOrigin=nullptr,double cellS=0.05,int maxPointCnt=20,const unsigned char* rgbData=nullptr,double proximityTol=0.005)`

**Arguments**:

- **points**: an array with point data, expressed relative to the world origin.
- **pointCnt**: the number of provided points.
- **ptcloudOrigin**: the transformation frame of the point-cloud. Can be nullptr, in which case the frame of the point-cloud is located at the world origin.
- **cellS**: the desired voxel size of the underlying OC-tree.
- **maxPointCnt**: the maximum number of points inside of an OC-tree voxel.
- **rgbData**: the RGB color (0-255) of the generated points. Specify one color per point.
- **proximityTol**: the distance tolerance to other points (i.e. point-point distances below the specified value are not permitted and points will be omitted).

**Return value**: A pointer to a point-cloud object in case of success, otherwise nullptr.

**See also**: [geom_createPtcloudFromPoints](#geom_createPtcloudFromPoints), [geom_destroyPtcloud](#geom_destroyPtcloud), [geom_copyPtcloud](#geom_copyPtcloud), [geom_getPtcloudFromSerializationData](#geom_getPtcloudFromSerializationData), [geom_insertColorPointsIntoPtcloud](#geom_insertColorPointsIntoPtcloud)

### <a id="geom_createPtcloudFromPoints"></a>geom_createPtcloudFromPoints

**Description**: Creates a point-cloud object from several points.

**Synopsis**: `CPcStruct* geom_createPtcloudFromPoints(const double* points,int pointCnt,const CPose* ptcloudOrigin=nullptr,double cellS=0.05,int maxPointCnt=20,const unsigned char rgbData[3]=nullptr,double proximityTol=0.005)`

**Arguments**:

- **points**: an array with point data, expressed relative to the world origin.
- **pointCnt**: the number of provided points.
- **ptcloudOrigin**: the transformation frame of the point-cloud. Can be nullptr, in which case the frame of the point-cloud is located at the world origin.
- **cellS**: the desired voxel size of the underlying OC-tree.
- **maxPointCnt**: the maximum number of points inside of an OC-tree voxel.
- **rgbData**: the RGB color (0-255) of the generated points.
- **proximityTol**: the distance tolerance to other points (i.e. point-point distances below the specified value are not permitted and points will be omitted).

**Return value**: A pointer to a point-cloud object in case of success, otherwise nullptr.

**See also**: [geom_createPtcloudFromColorPoints](#geom_createPtcloudFromColorPoints), [geom_destroyPtcloud](#geom_destroyPtcloud), [geom_copyPtcloud](#geom_copyPtcloud), [geom_getPtcloudFromSerializationData](#geom_getPtcloudFromSerializationData), [geom_insertPointsIntoPtcloud](#geom_insertPointsIntoPtcloud)

### <a id="geom_destroyMesh"></a>geom_destroyMesh

**Description**: Destroys a mesh object.

**Synopsis**: `void geom_destroyMesh(CObbStruct* meshObbStruct)`

**Arguments**:

- **meshObbStruct**: a pointer to the mesh object.

**See also**: [geom_createMesh](#geom_createMesh)

### <a id="geom_destroyOctree"></a>geom_destroyOctree

**Description**: Destroys an OC-tree object.

**Synopsis**: `void geom_destroyOctree(COcStruct* ocStruct)`

**Arguments**:

- **ocStruct**: a pointer to the OC-tree object.

**See also**: [geom_createOctreeFromPoints](#geom_createOctreeFromPoints)

### <a id="geom_destroyPtcloud"></a>geom_destroyPtcloud

**Description**: Destroys a point-cloud object.

**Synopsis**: `void geom_destroyPtcloud(CPcStruct* pcStruct)`

**Arguments**:

- **pcStruct**: a pointer to the point-cloud object.

**See also**: [geom_createPtcloudFromPoints](#geom_createPtcloudFromPoints)

### <a id="geom_getApproxBoxBoxDistance"></a>geom_getApproxBoxBoxDistance

**Description**: Computes a fast, approximate minimum distance between two cuboids. The approximate distance is always the same or smaller than the exact distance.

**Synopsis**: `double geom_getApproxBoxBoxDistance(const CPose& box1Transformation,const C3Vector& box1HalfSize,const CPose& box2Transformation,const C3Vector& box2HalfSize)`

**Arguments**:

- **box1Transformation**: the transformation frame of the first cuboid.
- **box1HalfSize**: the half-size of the first cuboid.
- **box2Transformation**: the transformation frame of the second cuboid.
- **box2HalfSize**: the half-size of the second cuboid.

**Return value**: the approximate minimum distance between the two cuboids. The approximate distance is always the same or smaller than the exact distance.

**See also**: [geom_getBoxBoxDistanceIfSmaller](#geom_getBoxBoxDistanceIfSmaller)

### <a id="geom_getBoxBoxCollision"></a>geom_getBoxBoxCollision

**Description**: Checks for collision between two cuboids.

**Synopsis**: `bool geom_getBoxBoxCollision(const CPose& box1Transformation,const C3Vector& box1HalfSize,const CPose& box2Transformation,const C3Vector& box2HalfSize,bool boxesAreSolid)`

**Arguments**:

- **box1Transformation**: the transformation frame of the first cuboid.
- **box1HalfSize**: the half-size of the first cuboid.
- **box2Transformation**: the transformation frame of the second cuboid.
- **box2HalfSize**: the half-size of the second cuboid.
- **boxesAreSolid**: whether the two cuboids are solid. If not, then cuboid A being fully encompassed by cuboid B will not lead to a collision detection.

**Return value**: the collision status

**See also**: [geom_getBoxTriangleCollision](#geom_getBoxTriangleCollision), [geom_getBoxSegmentCollision](#geom_getBoxSegmentCollision), [geom_getBoxPointCollision](#geom_getBoxPointCollision)

### <a id="geom_getBoxBoxDistanceIfSmaller"></a>geom_getBoxBoxDistanceIfSmaller

**Description**: Computes the minimum distance between two cuboids.

**Synopsis**: `bool geom_getBoxBoxDistanceIfSmaller(const CPose& box1Transformation,const C3Vector& box1HalfSize,const CPose& box2Transformation,const C3Vector& box2HalfSize,bool boxesAreSolid,double& dist,C3Vector* distSegPt1=nullptr,C3Vector* distSegPt2=nullptr,bool altRoutine=false)`

**Arguments**:

- **box1Transformation**: the transformation frame of the first cuboid.
- **box1HalfSize**: the half-size of the first cuboid.
- **box2Transformation**: the transformation frame of the second cuboid.
- **box2HalfSize**: the half-size of the second cuboid.
- **boxesAreSolid**: whether the two cuboids are solid. If true, then cuboid A being fully encompassed by cuboid B will always lead to a distance of zero between the two cuboids.
- **dist**: the distance threshold as input, and the minimum distance as output if it is below the threshold.
- **distSegPt1**: the minimum distance point on the first cuboid.
- **distSegPt2**: the minimum distance point on the second cuboid.
- **altRoutine**: if true, an alternative calculation routine will be used.

**Return value**: whether the minimum distance is smaller than the specified threshold

**See also**: [geom_getApproxBoxBoxDistance](#geom_getApproxBoxBoxDistance), [geom_getBoxTriangleDistanceIfSmaller](#geom_getBoxTriangleDistanceIfSmaller), [geom_getBoxSegmentDistanceIfSmaller](#geom_getBoxSegmentDistanceIfSmaller), [geom_getBoxPointDistanceIfSmaller](#geom_getBoxPointDistanceIfSmaller)

### <a id="geom_getBoxPointCollision"></a>geom_getBoxPointCollision

**Description**: Checks for collision between a cuboid and a point.

**Synopsis**: `bool geom_getBoxPointCollision(const CPose& boxTransformation,const C3Vector& boxHalfSize,const C3Vector& point)`

**Arguments**:

- **boxTransformation**: the transformation frame of the cuboid.
- **boxHalfSize**: the half-size of the cuboid.
- **point**: point position.

**Return value**: the collision status

**See also**: [geom_getOctreePointCollision](#geom_getOctreePointCollision), [geom_getBoxBoxCollision](#geom_getBoxBoxCollision), [geom_getBoxTriangleCollision](#geom_getBoxTriangleCollision), [geom_getBoxSegmentCollision](#geom_getBoxSegmentCollision)

### <a id="geom_getBoxPointDistanceIfSmaller"></a>geom_getBoxPointDistanceIfSmaller

**Description**: Computes the minimum distance between a cuboid and a point.

**Synopsis**: `bool geom_getBoxPointDistanceIfSmaller(const CPose& boxTransformation,const C3Vector& boxHalfSize,bool boxIsSolid,const C3Vector& point,double& dist,C3Vector* boxDistSegPt=nullptr)`

**Arguments**:

- **boxTransformation**: the transformation frame of the cuboid.
- **boxHalfSize**: the half-size of the cuboid.
- **boxIsSolid**: whether the cuboid is solid. If true, then the point being fully encompassed by the cuboid will always lead to a distance of zero.
- **point**: position of the point.
- **dist**: the distance threshold as input, and the minimum distance as output if it is below the threshold.
- **boxDistSegPt**: the minimum distance point on the cuboid.

**Return value**: whether the minimum distance is smaller than the specified threshold

**See also**: [geom_getMeshPointDistanceIfSmaller](#geom_getMeshPointDistanceIfSmaller), [geom_getOctreePointDistanceIfSmaller](#geom_getOctreePointDistanceIfSmaller), [geom_getPtcloudPointDistanceIfSmaller](#geom_getPtcloudPointDistanceIfSmaller), [geom_getBoxBoxDistanceIfSmaller](#geom_getBoxBoxDistanceIfSmaller), [geom_getBoxTriangleDistanceIfSmaller](#geom_getBoxTriangleDistanceIfSmaller), [geom_getBoxSegmentDistanceIfSmaller](#geom_getBoxSegmentDistanceIfSmaller), [geom_getTrianglePointDistanceIfSmaller](#geom_getTrianglePointDistanceIfSmaller), [geom_getSegmentPointDistanceIfSmaller](#geom_getSegmentPointDistanceIfSmaller)

### <a id="geom_getBoxSegmentCollision"></a>geom_getBoxSegmentCollision

**Description**: Checks for collision between a cuboid and a segment.

**Synopsis**: `bool geom_getBoxSegmentCollision(const CPose& boxTransformation,const C3Vector& boxHalfSize,bool boxIsSolid,const C3Vector& segmentEndPoint,const C3Vector& segmentVector)`

**Arguments**:

- **boxTransformation**: the transformation frame of the cuboid.
- **boxHalfSize**: the half-size of the cuboid.
- **boxIsSolid**: whether the cuboid is solid. If not, then the segment being fully encompassed by the cuboid will not lead to a collision detection.
- **segmentEndPoint**: position of vertex A on the segment.
- **segmentVector**: vector stretching from vertex A to vertex B on the segment.

**Return value**: the collision status

**See also**: [geom_getMeshSegmentCollision](#geom_getMeshSegmentCollision), [geom_getOctreeSegmentCollision](#geom_getOctreeSegmentCollision), [geom_getBoxBoxCollision](#geom_getBoxBoxCollision), [geom_getBoxTriangleCollision](#geom_getBoxTriangleCollision), [geom_getBoxPointCollision](#geom_getBoxPointCollision), [geom_getTriangleSegmentCollision](#geom_getTriangleSegmentCollision)

### <a id="geom_getBoxSegmentDistanceIfSmaller"></a>geom_getBoxSegmentDistanceIfSmaller

**Description**: Computes the minimum distance between a cuboid and a segment.

**Synopsis**: `bool geom_getBoxSegmentDistanceIfSmaller(const CPose& boxTransformation,const C3Vector& boxHalfSize,bool boxIsSolid,const C3Vector& segmentEndPoint,const C3Vector& segmentVector,double& dist,C3Vector* distSegPt1=nullptr,C3Vector* distSegPt2=nullptr,bool altRoutine=false)`

**Arguments**:

- **boxTransformation**: the transformation frame of the cuboid.
- **boxHalfSize**: the half-size of the cuboid.
- **boxIsSolid**: whether the cuboid is solid. If true, then the segment being fully encompassed by the cuboid will always lead to a distance of zero.
- **segmentEndPoint**: position of vertex A on the segment.
- **segmentVector**: vector stretching from vertex A to vertex B on the segment.
- **dist**: the distance threshold as input, and the minimum distance as output if it is below the threshold.
- **boxDistSegPt**: the minimum distance point on the cuboid.
- **segmentSegPt**: the minimum distance point on the segment.
- **altRoutine**: if true, an alternative calculation routine will be used.

**Return value**: whether the minimum distance is smaller than the specified threshold

**See also**: [geom_getMeshSegmentDistanceIfSmaller](#geom_getMeshSegmentDistanceIfSmaller), [geom_getOctreeSegmentDistanceIfSmaller](#geom_getOctreeSegmentDistanceIfSmaller), [geom_getPtcloudSegmentDistanceIfSmaller](#geom_getPtcloudSegmentDistanceIfSmaller), [geom_getBoxBoxDistanceIfSmaller](#geom_getBoxBoxDistanceIfSmaller), [geom_getBoxTriangleDistanceIfSmaller](#geom_getBoxTriangleDistanceIfSmaller), [geom_getBoxPointDistanceIfSmaller](#geom_getBoxPointDistanceIfSmaller), [geom_getTriangleSegmentDistanceIfSmaller](#geom_getTriangleSegmentDistanceIfSmaller), [geom_getSegmentSegmentDistanceIfSmaller](#geom_getSegmentSegmentDistanceIfSmaller), [geom_getSegmentPointDistanceIfSmaller](#geom_getSegmentPointDistanceIfSmaller)

### <a id="geom_getBoxTriangleCollision"></a>geom_getBoxTriangleCollision

**Description**: Checks for collision between a cuboid and a triangle.

**Synopsis**: `bool geom_getBoxTriangleCollision(const CPose& boxTransformation,const C3Vector& boxHalfSize,bool boxIsSolid,const C3Vector& p,const C3Vector& v,const C3Vector& w)`

**Arguments**:

- **boxTransformation**: the transformation frame of the cuboid.
- **boxHalfSize**: the half-size of the cuboid.
- **boxIsSolid**: whether the cuboid is solid. If not, then the triangle being fully encompassed by the cuboid will not lead to a collision detection.
- **p**: position of vertex A on the triangle.
- **v**: vector stretching from vertex A to vertex B on the triangle.
- **w**: vector stretching from vertex A to vertex C on the triangle.

**Return value**: the collision status

**See also**: [geom_getMeshTriangleCollision](#geom_getMeshTriangleCollision), [geom_getOctreeTriangleCollision](#geom_getOctreeTriangleCollision), [geom_getBoxBoxCollision](#geom_getBoxBoxCollision), [geom_getBoxSegmentCollision](#geom_getBoxSegmentCollision), [geom_getBoxPointCollision](#geom_getBoxPointCollision), [geom_getTriangleTriangleCollision](#geom_getTriangleTriangleCollision), [geom_getTriangleSegmentCollision](#geom_getTriangleSegmentCollision)

### <a id="geom_getBoxTriangleDistanceIfSmaller"></a>geom_getBoxTriangleDistanceIfSmaller

**Description**: Computes the minimum distance between a cuboid and a triangle.

**Synopsis**: `bool geom_getBoxTriangleDistanceIfSmaller(const CPose& boxTransformation,const C3Vector& boxHalfSize,bool boxIsSolid,const C3Vector& p,const C3Vector& v,const C3Vector& w,double& dist,C3Vector* boxDistSegPt=nullptr,C3Vector* triangleDistSegPt=nullptr,bool altRoutine=false)`

**Arguments**:

- **boxTransformation**: the transformation frame of the cuboid.
- **boxHalfSize**: the half-size of the cuboid.
- **boxIsSolid**: whether the cuboid is solid. If true, then the triangle being fully encompassed by the cuboid will always lead to a distance of zero.
- **p**: position of vertex A on the triangle.
- **v**: vector stretching from vertex A to vertex B on the triangle.
- **w**: vector stretching from vertex A to vertex C on the triangle.
- **dist**: the distance threshold as input, and the minimum distance as output if it is below the threshold.
- **boxDistSegPt**: the minimum distance point on the cuboid.
- **triangleDistSegPt**: the minimum distance point on the triangle.
- **altRoutine**: if true, an alternative calculation routine will be used.

**Return value**: whether the minimum distance is smaller than the specified threshold

**See also**: [geom_getMeshTriangleDistanceIfSmaller](#geom_getMeshTriangleDistanceIfSmaller), [geom_getOctreeTriangleDistanceIfSmaller](#geom_getOctreeTriangleDistanceIfSmaller), [geom_getPtcloudTriangleDistanceIfSmaller](#geom_getPtcloudTriangleDistanceIfSmaller), [geom_getBoxBoxDistanceIfSmaller](#geom_getBoxBoxDistanceIfSmaller), [geom_getBoxSegmentDistanceIfSmaller](#geom_getBoxSegmentDistanceIfSmaller), [geom_getBoxPointDistanceIfSmaller](#geom_getBoxPointDistanceIfSmaller), [geom_getTriangleTriangleDistanceIfSmaller](#geom_getTriangleTriangleDistanceIfSmaller), [geom_getTriangleSegmentDistanceIfSmaller](#geom_getTriangleSegmentDistanceIfSmaller), [geom_getTrianglePointDistanceIfSmaller](#geom_getTrianglePointDistanceIfSmaller)

### <a id="geom_getMeshFromSerializationData"></a>geom_getMeshFromSerializationData

**Description**: Creates a mesh object based on serialization data.

**Synopsis**: `CObbStruct* geom_getMeshFromSerializationData(const unsigned char* serializationData)`

**Arguments**:

- **serializationData**: the serialization data previously generated with [geom_getMeshSerializationData](#geom_getMeshSerializationData).

**Return value**: A pointer to the created mesh object in case of success, nullptr otherwise.

**See also**: [geom_getMeshSerializationData](#geom_getMeshSerializationData)

### <a id="geom_getMeshMeshCollision"></a>geom_getMeshMeshCollision

**Description**: Checks for collision between two mesh objects.

**Synopsis**: `bool geom_getMeshMeshCollision(const CObbStruct* mesh1ObbStruct,const CPose& mesh1Transformation,const CObbStruct* mesh2ObbStruct,const CPose& mesh2Transformation,std::vector<double>* intersections=nullptr,int* mesh1Caching=nullptr,int* mesh2Caching=nullptr)`

**Arguments**:

- **mesh1ObbStruct**: a pointer to the first mesh object.
- **mesh1Transformation**: the transformation frame of the first mesh.
- **mesh2ObbStruct**: a pointer to the second mesh object.
- **mesh2Transformation**: the transformation frame of the second mesh.
- **intersections**: if not nullptr, then all collisions will be extracted as interference segments (set to nullptr for fast operation).
- **mesh1Caching**: a value that can be used to speed up next collision checking between the same two entities (memorizes the colliding triangle in mesh 1).
- **mesh2Caching**: a value that can be used to speed up next collision checking between the same two entities (memorizes the colliding triangle in mesh 2).

**Return value**: the collision status

**See also**: [geom_getMeshOctreeCollision](#geom_getMeshOctreeCollision), [geom_getMeshTriangleCollision](#geom_getMeshTriangleCollision), [geom_getMeshSegmentCollision](#geom_getMeshSegmentCollision)

### <a id="geom_getMeshMeshDistanceIfSmaller"></a>geom_getMeshMeshDistanceIfSmaller

**Description**: Computes the minimum distance between two mesh objects.

**Synopsis**: `bool geom_getMeshMeshDistanceIfSmaller(const CObbStruct* mesh1ObbStruct,const CPose& mesh1Transformation,const CObbStruct* mesh2ObbStruct,const CPose& mesh2Transformation,double& dist,C3Vector* minDistSegPt1=nullptr,C3Vector* minDistSegPt2=nullptr,int* mesh1Caching=nullptr,int* mesh2Caching=nullptr)`

**Arguments**:

- **mesh1ObbStruct**: a pointer to the first mesh object.
- **mesh1Transformation**: the transformation frame of the first mesh.
- **mesh2ObbStruct**: a pointer to the second mesh object.
- **mesh2Transformation**: the transformation frame of the second mesh.
- **dist**: the distance threshold as input, and the minimum distance as output if it is below the threshold.
- **minDistSegPt1**: the minimum distance point on the first mesh.
- **minDistSegPt2**: the minimum distance point on the second mesh.
- **mesh1Caching**: a value that can be used to speed up next distance calculation between the same two entities (memorizes the triangle that holds the minimum distance point on the first mesh).
- **mesh2Caching**: a value that can be used to speed up next distance calculation between the same two entities (memorizes the triangle that holds the minimum distance point on the second mesh).

**Return value**: whether the minimum distance is smaller than the specified threshold

**See also**: [geom_getMeshOctreeDistanceIfSmaller](#geom_getMeshOctreeDistanceIfSmaller), [geom_getMeshPtcloudDistanceIfSmaller](#geom_getMeshPtcloudDistanceIfSmaller), [geom_getMeshTriangleDistanceIfSmaller](#geom_getMeshTriangleDistanceIfSmaller), [geom_getMeshSegmentDistanceIfSmaller](#geom_getMeshSegmentDistanceIfSmaller), [geom_getMeshPointDistanceIfSmaller](#geom_getMeshPointDistanceIfSmaller)

### <a id="geom_getMeshOctreeCollision"></a>geom_getMeshOctreeCollision

**Description**: Checks for collision between a mesh object and an OC-tree object.

**Synopsis**: `bool geom_getMeshOctreeCollision(const CObbStruct* meshObbStruct,const CPose& meshTransformation,const COcStruct* ocStruct,const CPose& octreeTransformation,int* meshCaching=nullptr,unsigned long long int* ocCaching=nullptr)`

**Arguments**:

- **meshObbStruct**: a pointer to the mesh object.
- **meshTransformation**: the transformation frame of the mesh.
- **ocStruct**: a pointer to the OC-tree object.
- **octreeTransformation**: the transformation frame of the OC-tree.
- **meshCaching**: a value that can be used to speed up next collision checking between the same two entities (memorizes the colliding triangle in the mesh).
- **ocCaching**: a value that can be used to speed up next collision checking between the same two entities (memorizes the colliding voxel in the OC-tree).

**Return value**: the collision status

**See also**: [geom_getMeshMeshCollision](#geom_getMeshMeshCollision), [geom_getMeshTriangleCollision](#geom_getMeshTriangleCollision), [geom_getMeshSegmentCollision](#geom_getMeshSegmentCollision), [geom_getOctreeOctreeCollision](#geom_getOctreeOctreeCollision), [geom_getOctreePtcloudCollision](#geom_getOctreePtcloudCollision), [geom_getOctreeTriangleCollision](#geom_getOctreeTriangleCollision), [geom_getOctreeSegmentCollision](#geom_getOctreeSegmentCollision), [geom_getOctreePointCollision](#geom_getOctreePointCollision)

### <a id="geom_getMeshOctreeDistanceIfSmaller"></a>geom_getMeshOctreeDistanceIfSmaller

**Description**: Computes the minimum distance between a mesh object and an OC-tree object.

**Synopsis**: `bool geom_getMeshOctreeDistanceIfSmaller(const CObbStruct* meshObbStruct,const CPose& meshTransformation,const COcStruct* ocStruct,const CPose& octreeTransformation,double& dist,C3Vector* meshMinDistPt=nullptr,C3Vector* ocMinDistPt=nullptr,int* meshCaching=nullptr,unsigned long long int* ocCaching=nullptr)`

**Arguments**:

- **meshObbStruct**: a pointer to the mesh object.
- **meshTransformation**: the transformation frame of the mesh.
- **ocStruct**: a pointer to the OC-tree object.
- **octreeTransformation**: the transformation frame of the OC-tree.
- **dist**: the distance threshold as input, and the minimum distance as output if it is below the threshold.
- **meshMinDistPt**: the minimum distance point on the mesh.
- **ocMinDistPt**: the minimum distance point on the OC-tree.
- **meshCaching**: a value that can be used to speed up next distance calculation between the same two entities (memorizes the triangle that holds the minimum distance point on the mesh).
- **ocCaching**: a value that can be used to speed up next distance calculation between the same two entities (memorizes the voxel that holds the minimum distance point on the OC-tree).

**Return value**: whether the minimum distance is smaller than the specified threshold

**See also**: [geom_getMeshMeshDistanceIfSmaller](#geom_getMeshMeshDistanceIfSmaller), [geom_getMeshPtcloudDistanceIfSmaller](#geom_getMeshPtcloudDistanceIfSmaller), [geom_getMeshTriangleDistanceIfSmaller](#geom_getMeshTriangleDistanceIfSmaller), [geom_getMeshSegmentDistanceIfSmaller](#geom_getMeshSegmentDistanceIfSmaller), [geom_getMeshPointDistanceIfSmaller](#geom_getMeshPointDistanceIfSmaller), [geom_getOctreeOctreeDistanceIfSmaller](#geom_getOctreeOctreeDistanceIfSmaller), [geom_getOctreePtcloudDistanceIfSmaller](#geom_getOctreePtcloudDistanceIfSmaller), [geom_getOctreeTriangleDistanceIfSmaller](#geom_getOctreeTriangleDistanceIfSmaller), [geom_getOctreeSegmentDistanceIfSmaller](#geom_getOctreeSegmentDistanceIfSmaller), [geom_getOctreePointDistanceIfSmaller](#geom_getOctreePointDistanceIfSmaller)

### <a id="geom_getMeshPointDistanceIfSmaller"></a>geom_getMeshPointDistanceIfSmaller

**Description**: Computes the minimum distance between a mesh object and a point.

**Synopsis**: `bool geom_getMeshPointDistanceIfSmaller(const CObbStruct* meshObbStruct,const CPose& meshTransformation,const C3Vector& point,double& dist,C3Vector* meshMinDistPt=nullptr,int* caching=nullptr)`

**Arguments**:

- **meshObbStruct**: a pointer to the mesh object.
- **meshTransformation**: the transformation frame of the mesh.
- **point**: the position of the point.
- **dist**: the distance threshold as input, and the minimum distance as output if it is below the threshold.
- **meshMinDistPt**: the minimum distance point on the mesh.
- **caching**: a value that can be used to speed up next distance calculation between the same two entities (memorizes the triangle that holds the minimum distance point on the mesh).

**Return value**: whether the minimum distance is smaller than the specified threshold

**See also**: [geom_getMeshMeshDistanceIfSmaller](#geom_getMeshMeshDistanceIfSmaller), [geom_getMeshOctreeDistanceIfSmaller](#geom_getMeshOctreeDistanceIfSmaller), [geom_getMeshPtcloudDistanceIfSmaller](#geom_getMeshPtcloudDistanceIfSmaller), [geom_getMeshTriangleDistanceIfSmaller](#geom_getMeshTriangleDistanceIfSmaller), [geom_getMeshSegmentDistanceIfSmaller](#geom_getMeshSegmentDistanceIfSmaller), [geom_getOctreePointDistanceIfSmaller](#geom_getOctreePointDistanceIfSmaller), [geom_getPtcloudPointDistanceIfSmaller](#geom_getPtcloudPointDistanceIfSmaller), [geom_getBoxPointDistanceIfSmaller](#geom_getBoxPointDistanceIfSmaller), [geom_getTrianglePointDistanceIfSmaller](#geom_getTrianglePointDistanceIfSmaller), [geom_getSegmentPointDistanceIfSmaller](#geom_getSegmentPointDistanceIfSmaller)

### <a id="geom_getMeshPtcloudDistanceIfSmaller"></a>geom_getMeshPtcloudDistanceIfSmaller

**Description**: Computes the minimum distance between a mesh object and a point-cloud object.

**Synopsis**: `bool geom_getMeshPtcloudDistanceIfSmaller(const CObbStruct* meshObbStruct,const CPose& meshTransformation,const CPcStruct* pcStruct,const CPose& pcTransformation,double& dist,C3Vector* meshMinDistPt=nullptr,C3Vector* pcMinDistPt=nullptr,int* meshCaching=nullptr,unsigned long long int* pcCaching=nullptr)`

**Arguments**:

- **meshObbStruct**: a pointer to the mesh object.
- **meshTransformation**: the transformation frame of the mesh.
- **pcStruct**: a pointer to the point-cloud object.
- **pcTransformation**: the transformation frame of the point-cloud.
- **dist**: the distance threshold as input, and the minimum distance as output if it is below the threshold.
- **meshMinDistPt**: the minimum distance point on the mesh.
- **pcMinDistPt**: the minimum distance point on the point-cloud.
- **meshCaching**: a value that can be used to speed up next distance calculation between the same two entities (memorizes the triangle that holds the minimum distance point on the mesh).
- **pcCaching**: a value that can be used to speed up next distance calculation between the same two entities (memorizes the point that holds the minimum distance on the point-cloud).

**Return value**: whether the minimum distance is smaller than the specified threshold

**See also**: [geom_getMeshMeshDistanceIfSmaller](#geom_getMeshMeshDistanceIfSmaller), [geom_getMeshOctreeDistanceIfSmaller](#geom_getMeshOctreeDistanceIfSmaller), [geom_getMeshTriangleDistanceIfSmaller](#geom_getMeshTriangleDistanceIfSmaller), [geom_getMeshSegmentDistanceIfSmaller](#geom_getMeshSegmentDistanceIfSmaller), [geom_getMeshPointDistanceIfSmaller](#geom_getMeshPointDistanceIfSmaller), [geom_getOctreePtcloudDistanceIfSmaller](#geom_getOctreePtcloudDistanceIfSmaller), [geom_getPtcloudPtcloudDistanceIfSmaller](#geom_getPtcloudPtcloudDistanceIfSmaller), [geom_getPtcloudTriangleDistanceIfSmaller](#geom_getPtcloudTriangleDistanceIfSmaller), [geom_getPtcloudSegmentDistanceIfSmaller](#geom_getPtcloudSegmentDistanceIfSmaller), [geom_getPtcloudPointDistanceIfSmaller](#geom_getPtcloudPointDistanceIfSmaller)

### <a id="geom_getMeshSegmentCollision"></a>geom_getMeshSegmentCollision

**Description**: Checks for collision between a mesh object and a segment.

**Synopsis**: `bool geom_getMeshSegmentCollision(const CObbStruct* meshObbStruct,const CPose& meshTransformation,const C3Vector& segmentExtremity,const C3Vector& segmentVector,std::vector<double>* intersections=nullptr,int* caching=nullptr)`

**Arguments**:

- **meshObbStruct**: a pointer to the mesh object.
- **meshTransformation**: the transformation frame of the mesh.
- **segmentExtremity**: position of vertex A on the segment.
- **segmentVector**: vector stretching from vertex A to vertex B on the segment.
- **intersections**: if not nullptr, then all collisions will be extracted as interference segments (where both segment points are always coincident) (set to nullptr for fast operation).
- **caching**: a value that can be used to speed up next collision checking between the same two entities (memorizes the colliding triangle in the mesh).

**Return value**: the collision status

**See also**: [geom_getMeshMeshCollision](#geom_getMeshMeshCollision), [geom_getMeshOctreeCollision](#geom_getMeshOctreeCollision), [geom_getMeshTriangleCollision](#geom_getMeshTriangleCollision), [geom_getOctreeSegmentCollision](#geom_getOctreeSegmentCollision), [geom_getBoxSegmentCollision](#geom_getBoxSegmentCollision), [geom_getTriangleSegmentCollision](#geom_getTriangleSegmentCollision)

### <a id="geom_getMeshSegmentDistanceIfSmaller"></a>geom_getMeshSegmentDistanceIfSmaller

**Description**: Computes the minimum distance between a mesh object and a segment.

**Synopsis**: `bool geom_getMeshSegmentDistanceIfSmaller(const CObbStruct* meshObbStruct,const CPose& meshTransformation,const C3Vector& segmentEndPoint,const C3Vector& segmentVector,double& dist,C3Vector* meshMinDistPt=nullptr,C3Vector* segmentDistSegPt=nullptr,int* caching=nullptr)`

**Arguments**:

- **meshObbStruct**: a pointer to the mesh object.
- **meshTransformation**: the transformation frame of the mesh.
- **segmentEndPoint**: position of vertex A on the segment.
- **segmentVector**: vector stretching from vertex A to vertex B on the segment.
- **dist**: the distance threshold as input, and the minimum distance as output if it is below the threshold.
- **meshMinDistPt**: the minimum distance point on the mesh.
- **segmentDistSegPt**: the minimum distance point on the segment.
- **caching**: a value that can be used to speed up next distance calculation between the same two entities (memorizes the triangle that holds the minimum distance point on the mesh).

**Return value**: whether the minimum distance is smaller than the specified threshold

**See also**: [geom_getMeshMeshDistanceIfSmaller](#geom_getMeshMeshDistanceIfSmaller), [geom_getMeshOctreeDistanceIfSmaller](#geom_getMeshOctreeDistanceIfSmaller), [geom_getMeshPtcloudDistanceIfSmaller](#geom_getMeshPtcloudDistanceIfSmaller), [geom_getMeshTriangleDistanceIfSmaller](#geom_getMeshTriangleDistanceIfSmaller), [geom_getMeshPointDistanceIfSmaller](#geom_getMeshPointDistanceIfSmaller), [geom_getOctreeSegmentDistanceIfSmaller](#geom_getOctreeSegmentDistanceIfSmaller), [geom_getPtcloudSegmentDistanceIfSmaller](#geom_getPtcloudSegmentDistanceIfSmaller), [geom_getBoxSegmentDistanceIfSmaller](#geom_getBoxSegmentDistanceIfSmaller), [geom_getTriangleSegmentDistanceIfSmaller](#geom_getTriangleSegmentDistanceIfSmaller), [geom_getSegmentSegmentDistanceIfSmaller](#geom_getSegmentSegmentDistanceIfSmaller), [geom_getSegmentPointDistanceIfSmaller](#geom_getSegmentPointDistanceIfSmaller)

### <a id="geom_getMeshSerializationData"></a>geom_getMeshSerializationData

**Description**: Retrieves the serialization data from a mesh object.

**Synopsis**: `void geom_getMeshSerializationData(const CObbStruct* meshObbStruct,std::vector<unsigned char>& serializationData)`

**Arguments**:

- **meshObbStruct**: a pointer to the mesh object.
- **serializationData**: the serialization data.

**See also**: [geom_getMeshFromSerializationData](#geom_getMeshFromSerializationData)

### <a id="geom_getMeshTriangleCollision"></a>geom_getMeshTriangleCollision

**Description**: Checks for collision between a mesh object and a triangle.

**Synopsis**: `bool geom_getMeshTriangleCollision(const CObbStruct* meshObbStruct,const CPose& meshTransformation,const C3Vector& p,const C3Vector& v,const C3Vector& w,std::vector<double>* intersections=nullptr,int* caching=nullptr)`

**Arguments**:

- **meshObbStruct**: a pointer to the mesh object.
- **meshTransformation**: the transformation frame of the mesh.
- **p**: position of vertex A on the triangle.
- **v**: vector stretching from vertex A to vertex B on the triangle.
- **w**: vector stretching from vertex A to vertex C on the triangle.
- **intersections**: if not nullptr, then all collisions will be extracted as interference segments (set to nullptr for fast operation).
- **caching**: a value that can be used to speed up next collision checking between the same two entities (memorizes the colliding triangle in the mesh).

**Return value**: the collision status

**See also**: [geom_getMeshMeshCollision](#geom_getMeshMeshCollision), [geom_getMeshOctreeCollision](#geom_getMeshOctreeCollision), [geom_getMeshSegmentCollision](#geom_getMeshSegmentCollision), [geom_getOctreeTriangleCollision](#geom_getOctreeTriangleCollision), [geom_getBoxTriangleCollision](#geom_getBoxTriangleCollision), [geom_getTriangleTriangleCollision](#geom_getTriangleTriangleCollision), [geom_getTriangleSegmentCollision](#geom_getTriangleSegmentCollision)

### <a id="geom_getMeshTriangleDistanceIfSmaller"></a>geom_getMeshTriangleDistanceIfSmaller

**Description**: Computes the minimum distance between a mesh object and a triangle.

**Synopsis**: `bool geom_getMeshTriangleDistanceIfSmaller(const CObbStruct* meshObbStruct,const CPose& meshTransformation,const C3Vector& p,const C3Vector& v,const C3Vector& w,double& dist,C3Vector* meshMinDistPt=nullptr,C3Vector* triangleMinDistPt=nullptr,int* caching=nullptr)`

**Arguments**:

- **meshObbStruct**: a pointer to the mesh object.
- **meshTransformation**: the transformation frame of the mesh.
- **p**: position of vertex A on the triangle.
- **v**: vector stretching from vertex A to vertex B on the triangle.
- **w**: vector stretching from vertex A to vertex C on the triangle.
- **dist**: the distance threshold as input, and the minimum distance as output if it is below the threshold.
- **meshMinDistPt**: the minimum distance point on the mesh.
- **triangleMinDistPt**: the minimum distance point on the triangle.
- **caching**: a value that can be used to speed up next distance calculation between the same two entities (memorizes the triangle that holds the minimum distance point on the mesh).

**Return value**: whether the minimum distance is smaller than the specified threshold

**See also**: [geom_getMeshMeshDistanceIfSmaller](#geom_getMeshMeshDistanceIfSmaller), [geom_getMeshOctreeDistanceIfSmaller](#geom_getMeshOctreeDistanceIfSmaller), [geom_getMeshPtcloudDistanceIfSmaller](#geom_getMeshPtcloudDistanceIfSmaller), [geom_getMeshSegmentDistanceIfSmaller](#geom_getMeshSegmentDistanceIfSmaller), [geom_getMeshPointDistanceIfSmaller](#geom_getMeshPointDistanceIfSmaller), [geom_getOctreeTriangleDistanceIfSmaller](#geom_getOctreeTriangleDistanceIfSmaller), [geom_getPtcloudTriangleDistanceIfSmaller](#geom_getPtcloudTriangleDistanceIfSmaller), [geom_getBoxTriangleDistanceIfSmaller](#geom_getBoxTriangleDistanceIfSmaller), [geom_getTriangleTriangleDistanceIfSmaller](#geom_getTriangleTriangleDistanceIfSmaller), [geom_getTriangleSegmentDistanceIfSmaller](#geom_getTriangleSegmentDistanceIfSmaller), [geom_getTrianglePointDistanceIfSmaller](#geom_getTrianglePointDistanceIfSmaller)

### <a id="geom_getOctreeFromSerializationData"></a>geom_getOctreeFromSerializationData

**Description**: Creates an OC-tree object based on serialization data.

**Synopsis**: `COcStruct* geom_getOctreeFromSerializationData(const unsigned char* serializationData)`

**Arguments**:

- **serializationData**: the serialization data previously generated with [geom_getOctreeSerializationData](#geom_getOctreeSerializationData).

**Return value**: A pointer to the created OC-tree object in case of success, nullptr otherwise.

**See also**: [geom_getOctreeSerializationData](#geom_getOctreeSerializationData)

### <a id="geom_getOctreeOctreeCollision"></a>geom_getOctreeOctreeCollision

**Description**: Checks for collision between two OC-tree objects.

**Synopsis**: `bool geom_getOctreeOctreeCollision(const COcStruct* oc1Struct,const CPose& octree1Transformation,const COcStruct* oc2Struct,const CPose& octree2Transformation,unsigned long long int* oc1Caching=nullptr,unsigned long long int* oc2Caching=nullptr)`

**Arguments**:

- **oc1Struct**: a pointer to the first OC-tree object.
- **octree1Transformation**: the transformation frame of the first OC-tree.
- **oc2Struct**: a pointer to the second OC-tree object.
- **octree2Transformation**: the transformation frame of the second OC-tree.
- **oc1Caching**: a value that can be used to speed-up next collision checking between the same two entities (memorizes the colliding voxel in OC-tree 1).
- **oc2Caching**: a value that can be used to speed-up next collision checking between the same two entities (memorizes the colliding voxel in OC-tree 2).

**Return value**: the collision status

**See also**: [geom_getMeshOctreeCollision](#geom_getMeshOctreeCollision), [geom_getOctreePtcloudCollision](#geom_getOctreePtcloudCollision), [geom_getOctreeTriangleCollision](#geom_getOctreeTriangleCollision), [geom_getOctreeSegmentCollision](#geom_getOctreeSegmentCollision), [geom_getOctreePointCollision](#geom_getOctreePointCollision)

### <a id="geom_getOctreeOctreeDistanceIfSmaller"></a>geom_getOctreeOctreeDistanceIfSmaller

**Description**: Computes the minimum distance between two OC-tree objects.

**Synopsis**: `bool geom_getOctreeOctreeDistanceIfSmaller(const COcStruct* oc1Struct,const CPose& octree1Transformation,const COcStruct* oc2Struct,const CPose& octree2Transformation,double& dist,C3Vector* oc1MinDistPt=nullptr,C3Vector* oc2MinDistPt=nullptr,unsigned long long int* oc1Caching=nullptr,unsigned long long int* oc2Caching=nullptr)`

**Arguments**:

- **oc1Struct**: a pointer to the first OC-tree object.
- **octree1Transformation**: the transformation frame of the first OC-tree.
- **oc2Struct**: a pointer to the second OC-tree object.
- **octree2Transformation**: the transformation frame of the second OC-tree.
- **dist**: the distance threshold as input, and the minimum distance as output if it is below the threshold.
- **oc1MinDistPt**: the minimum distance point on the first OC-tree.
- **oc2MinDistPt**: the minimum distance point on the second OC-tree.
- **oc1Caching**: a value that can be used to speed-up next distance calculation between the same two entities (memorizes the voxel that holds the minimum distance point on the first OC-tree).
- **oc2Caching**: a value that can be used to speed-up next distance calculation between the same two entities (memorizes the voxel that holds the minimum distance point on the second OC-tree).

**Return value**: whether the minimum distance is smaller than the specified threshold

**See also**: [geom_getMeshOctreeDistanceIfSmaller](#geom_getMeshOctreeDistanceIfSmaller), [geom_getOctreePtcloudDistanceIfSmaller](#geom_getOctreePtcloudDistanceIfSmaller), [geom_getOctreeTriangleDistanceIfSmaller](#geom_getOctreeTriangleDistanceIfSmaller), [geom_getOctreeSegmentDistanceIfSmaller](#geom_getOctreeSegmentDistanceIfSmaller), [geom_getOctreePointDistanceIfSmaller](#geom_getOctreePointDistanceIfSmaller)

### <a id="geom_getOctreePointCollision"></a>geom_getOctreePointCollision

**Description**: Checks for collision between an OC-tree object and a point.

**Synopsis**: `bool geom_getOctreePointCollision(const COcStruct* ocStruct,const CPose& octreeTransformation,const C3Vector& point,unsigned int* usrData=nullptr,unsigned long long int* caching=nullptr)`

**Arguments**:

- **ocStruct**: a pointer to the OC-tree object.
- **octreeTransformation**: the transformation frame of the OC-tree.
- **point**: a point expressed relative to the world reference frame.
- **usrData**: the user data of the colliding voxel.
- **caching**: a value that can be used to speed-up next collision checking between the same two entities (memorizes the colliding voxel in the OC-tree).

**Return value**: the collision status

**See also**: [geom_getMeshOctreeCollision](#geom_getMeshOctreeCollision), [geom_getOctreeOctreeCollision](#geom_getOctreeOctreeCollision), [geom_getOctreePtcloudCollision](#geom_getOctreePtcloudCollision), [geom_getOctreeTriangleCollision](#geom_getOctreeTriangleCollision), [geom_getOctreeSegmentCollision](#geom_getOctreeSegmentCollision), [geom_getBoxPointCollision](#geom_getBoxPointCollision)

### <a id="geom_getOctreePointDistanceIfSmaller"></a>geom_getOctreePointDistanceIfSmaller

**Description**: Computes the minimum distance between an OC-tree object and a point.

**Synopsis**: `bool geom_getOctreePointDistanceIfSmaller(const COcStruct* ocStruct,const CPose& octreeTransformation,const C3Vector& point,double& dist,C3Vector* ocMinDistPt=nullptr,unsigned long long int* ocCaching=nullptr)`

**Arguments**:

- **ocStruct**: a pointer to the OC-tree object.
- **octreeTransformation**: the transformation frame of the OC-tree.
- **point**: the position of the point.
- **dist**: the distance threshold as input, and the minimum distance as output if it is below the threshold.
- **ocMinDistPt**: the minimum distance point on the OC-tree.
- **ocCaching**: a value that can be used to speed-up next distance calculation between the same two entities (memorizes the voxel that holds the minimum distance point on the OC-tree).

**Return value**: whether the minimum distance is smaller than the specified threshold

**See also**: [geom_getMeshOctreeDistanceIfSmaller](#geom_getMeshOctreeDistanceIfSmaller), [geom_getMeshPointDistanceIfSmaller](#geom_getMeshPointDistanceIfSmaller), [geom_getOctreeOctreeDistanceIfSmaller](#geom_getOctreeOctreeDistanceIfSmaller), [geom_getOctreePtcloudDistanceIfSmaller](#geom_getOctreePtcloudDistanceIfSmaller), [geom_getOctreeTriangleDistanceIfSmaller](#geom_getOctreeTriangleDistanceIfSmaller), [geom_getOctreeSegmentDistanceIfSmaller](#geom_getOctreeSegmentDistanceIfSmaller), [geom_getPtcloudPointDistanceIfSmaller](#geom_getPtcloudPointDistanceIfSmaller), [geom_getBoxPointDistanceIfSmaller](#geom_getBoxPointDistanceIfSmaller), [geom_getTrianglePointDistanceIfSmaller](#geom_getTrianglePointDistanceIfSmaller), [geom_getSegmentPointDistanceIfSmaller](#geom_getSegmentPointDistanceIfSmaller)

### <a id="geom_getOctreePtcloudCollision"></a>geom_getOctreePtcloudCollision

**Description**: Checks for collision between an OC-tree object and a point-cloud object.

**Synopsis**: `bool geom_getOctreePtcloudCollision(const COcStruct* ocStruct,const CPose& octreeTransformation,const CPcStruct* pcStruct,const CPose& ptcloudTransformation,unsigned long long int* ocCaching=nullptr,unsigned long long int* pcCaching=nullptr)`

**Arguments**:

- **ocStruct**: a pointer to the OC-tree object.
- **octreeTransformation**: the transformation frame of the OC-tree.
- **pcStruct**: a pointer to the point-cloud object.
- **ptcloudTransformation**: the transformation frame of the point-cloud.
- **ocCaching**: a value that can be used to speed-up next collision checking between the same two entities (memorizes the colliding voxel in the OC-tree).
- **pcCaching**: a value that can be used to speed-up next collision checking between the same two entities (memorizes the colliding point in the point-cloud).

**Return value**: the collision status

**See also**: [geom_getMeshOctreeCollision](#geom_getMeshOctreeCollision), [geom_getOctreeOctreeCollision](#geom_getOctreeOctreeCollision), [geom_getOctreeTriangleCollision](#geom_getOctreeTriangleCollision), [geom_getOctreeSegmentCollision](#geom_getOctreeSegmentCollision), [geom_getOctreePointCollision](#geom_getOctreePointCollision)

### <a id="geom_getOctreePtcloudDistanceIfSmaller"></a>geom_getOctreePtcloudDistanceIfSmaller

**Description**: Computes the minimum distance between an OC-tree object and a point-cloud object.

**Synopsis**: `bool geom_getOctreePtcloudDistanceIfSmaller(const COcStruct* ocStruct,const CPose& octreeTransformation,const CPcStruct* pcStruct,const CPose& pcTransformation,double& dist,C3Vector* ocMinDistPt=nullptr,C3Vector* pcMinDistPt=nullptr,unsigned long long int* ocCaching=nullptr,unsigned long long int* pcCaching=nullptr)`

**Arguments**:

- **ocStruct**: a pointer to the OC-tree object.
- **octreeTransformation**: the transformation frame of the OC-tree.
- **pcStruct**: a pointer to the point-cloud object.
- **pcTransformation**: the transformation frame of the point-cloud.
- **dist**: the distance threshold as input, and the minimum distance as output if it is below the threshold.
- **ocMinDistPt**: the minimum distance point on the OC-tree.
- **pcMinDistPt**: the minimum distance point on the point-cloud.
- **ocCaching**: a value that can be used to speed-up next distance calculation between the same two entities (memorizes the voxel that holds the minimum distance point on the OC-tree).
- **pcCaching**: a value that can be used to speed-up next distance calculation between the same two entities (memorizes the point that holds the minimum distance on the point-cloud).

**Return value**: whether the minimum distance is smaller than the specified threshold

**See also**: [geom_getMeshPtcloudDistanceIfSmaller](#geom_getMeshPtcloudDistanceIfSmaller), [geom_getOctreeOctreeDistanceIfSmaller](#geom_getOctreeOctreeDistanceIfSmaller), [geom_getOctreeTriangleDistanceIfSmaller](#geom_getOctreeTriangleDistanceIfSmaller), [geom_getOctreeSegmentDistanceIfSmaller](#geom_getOctreeSegmentDistanceIfSmaller), [geom_getOctreePointDistanceIfSmaller](#geom_getOctreePointDistanceIfSmaller), [geom_getPtcloudPtcloudDistanceIfSmaller](#geom_getPtcloudPtcloudDistanceIfSmaller), [geom_getPtcloudTriangleDistanceIfSmaller](#geom_getPtcloudTriangleDistanceIfSmaller), [geom_getPtcloudSegmentDistanceIfSmaller](#geom_getPtcloudSegmentDistanceIfSmaller), [geom_getPtcloudPointDistanceIfSmaller](#geom_getPtcloudPointDistanceIfSmaller)

### <a id="geom_getOctreeSegmentCollision"></a>geom_getOctreeSegmentCollision

**Description**: Checks for collision between an OC-tree object and a segment.

**Synopsis**: `bool geom_getOctreeSegmentCollision(const COcStruct* ocStruct,const CPose& octreeTransformation,const C3Vector& segmentExtremity,const C3Vector& segmentVector,unsigned long long int* caching=nullptr)`

**Arguments**:

- **ocStruct**: a pointer to the OC-tree object.
- **octreeTransformation**: the transformation frame of the OC-tree.
- **segmentExtremity**: position of vertex A on the segment.
- **segmentVector**: vector stretching from vertex A to vertex B on the segment.
- **caching**: a value that can be used to speed-up next collision checking between the same two entities (memorizes the colliding voxel in the OC-tree).

**Return value**: the collision status

**See also**: [geom_getMeshOctreeCollision](#geom_getMeshOctreeCollision), [geom_getMeshSegmentCollision](#geom_getMeshSegmentCollision), [geom_getOctreeOctreeCollision](#geom_getOctreeOctreeCollision), [geom_getOctreePtcloudCollision](#geom_getOctreePtcloudCollision), [geom_getOctreeTriangleCollision](#geom_getOctreeTriangleCollision), [geom_getOctreePointCollision](#geom_getOctreePointCollision), [geom_getBoxSegmentCollision](#geom_getBoxSegmentCollision), [geom_getTriangleSegmentCollision](#geom_getTriangleSegmentCollision)

### <a id="geom_getOctreeSegmentDistanceIfSmaller"></a>geom_getOctreeSegmentDistanceIfSmaller

**Description**: Computes the minimum distance between an OC-tree object and a segment.

**Synopsis**: `bool geom_getOctreeSegmentDistanceIfSmaller(const COcStruct* ocStruct,const CPose& octreeTransformation,const C3Vector& segmentEndPoint,const C3Vector& segmentVector,double& dist,C3Vector* ocMinDistPt=nullptr,C3Vector* segmentDistSegPt=nullptr,unsigned long long int* ocCaching=nullptr)`

**Arguments**:

- **ocStruct**: a pointer to the OC-tree object.
- **octreeTransformation**: the transformation frame of the OC-tree.
- **segmentEndPoint**: position of vertex A on the segment.
- **segmentVector**: vector stretching from vertex A to vertex B on the segment.
- **dist**: the distance threshold as input, and the minimum distance as output if it is below the threshold.
- **ocMinDistPt**: the minimum distance point on the OC-tree.
- **segmentDistSegPt**: the minimum distance point on the segment.
- **ocCaching**: a value that can be used to speed-up next distance calculation between the same two entities (memorizes the voxel that holds the minimum distance point on the OC-tree).

**Return value**: whether the minimum distance is smaller than the specified threshold

**See also**: [geom_getMeshOctreeDistanceIfSmaller](#geom_getMeshOctreeDistanceIfSmaller), [geom_getMeshSegmentDistanceIfSmaller](#geom_getMeshSegmentDistanceIfSmaller), [geom_getOctreeOctreeDistanceIfSmaller](#geom_getOctreeOctreeDistanceIfSmaller), [geom_getOctreePtcloudDistanceIfSmaller](#geom_getOctreePtcloudDistanceIfSmaller), [geom_getOctreeTriangleDistanceIfSmaller](#geom_getOctreeTriangleDistanceIfSmaller), [geom_getOctreePointDistanceIfSmaller](#geom_getOctreePointDistanceIfSmaller), [geom_getPtcloudSegmentDistanceIfSmaller](#geom_getPtcloudSegmentDistanceIfSmaller), [geom_getBoxSegmentDistanceIfSmaller](#geom_getBoxSegmentDistanceIfSmaller), [geom_getTriangleSegmentDistanceIfSmaller](#geom_getTriangleSegmentDistanceIfSmaller), [geom_getSegmentSegmentDistanceIfSmaller](#geom_getSegmentSegmentDistanceIfSmaller), [geom_getSegmentPointDistanceIfSmaller](#geom_getSegmentPointDistanceIfSmaller)

### <a id="geom_getOctreeSerializationData"></a>geom_getOctreeSerializationData

**Description**: Retrieves the serialization data from an OC-tree object.

**Synopsis**: `void geom_getOctreeSerializationData(const COcStruct* ocStruct,std::vector<unsigned char>& serializationData)`

**Arguments**:

- **ocStruct**: a pointer to the OC-tree object.
- **serializationData**: the serialization data.

**See also**: [geom_getOctreeFromSerializationData](#geom_getOctreeFromSerializationData)

### <a id="geom_getOctreeTriangleCollision"></a>geom_getOctreeTriangleCollision

**Description**: Checks for collision between an OC-tree object and a triangle.

**Synopsis**: `bool geom_getOctreeTriangleCollision(const COcStruct* ocStruct,const CPose& octreeTransformation,const C3Vector& p,const C3Vector& v,const C3Vector& w,unsigned long long int* caching=nullptr)`

**Arguments**:

- **ocStruct**: a pointer to the OC-tree object.
- **octreeTransformation**: the transformation frame of the OC-tree.
- **p**: position of vertex A on the triangle.
- **v**: vector stretching from vertex A to vertex B on the triangle.
- **w**: vector stretching from vertex A to vertex C on the triangle.
- **caching**: a value that can be used to speed-up next collision checking between the same two entities (memorizes the colliding voxel in the OC-tree).

**Return value**: the collision status

**See also**: [geom_getMeshOctreeCollision](#geom_getMeshOctreeCollision), [geom_getMeshTriangleCollision](#geom_getMeshTriangleCollision), [geom_getOctreeOctreeCollision](#geom_getOctreeOctreeCollision), [geom_getOctreePtcloudCollision](#geom_getOctreePtcloudCollision), [geom_getOctreeSegmentCollision](#geom_getOctreeSegmentCollision), [geom_getOctreePointCollision](#geom_getOctreePointCollision), [geom_getBoxTriangleCollision](#geom_getBoxTriangleCollision), [geom_getTriangleTriangleCollision](#geom_getTriangleTriangleCollision), [geom_getTriangleSegmentCollision](#geom_getTriangleSegmentCollision)

### <a id="geom_getOctreeTriangleDistanceIfSmaller"></a>geom_getOctreeTriangleDistanceIfSmaller

**Description**: Computes the minimum distance between an OC-tree object and a triangle.

**Synopsis**: `bool geom_getOctreeTriangleDistanceIfSmaller(const COcStruct* ocStruct,const CPose& octreeTransformation,const C3Vector& p,const C3Vector& v,const C3Vector& w,double& dist,C3Vector* ocMinDistPt=nullptr,C3Vector* triangleMinDistPt=nullptr,unsigned long long int* ocCaching=nullptr)`

**Arguments**:

- **ocStruct**: a pointer to the OC-tree object.
- **octreeTransformation**: the transformation frame of the OC-tree.
- **p**: position of vertex A on the triangle.
- **v**: vector stretching from vertex A to vertex B on the triangle.
- **w**: vector stretching from vertex A to vertex C on the triangle.
- **dist**: the distance threshold as input, and the minimum distance as output if it is below the threshold.
- **ocMinDistPt**: the minimum distance point on the OC-tree.
- **triangleMinDistPt**: the minimum distance point on the triangle.
- **ocCaching**: a value that can be used to speed-up next distance calculation between the same two entities (memorizes the voxel that holds the minimum distance point on the OC-tree).

**Return value**: whether the minimum distance is smaller than the specified threshold

**See also**: [geom_getMeshOctreeDistanceIfSmaller](#geom_getMeshOctreeDistanceIfSmaller), [geom_getMeshTriangleDistanceIfSmaller](#geom_getMeshTriangleDistanceIfSmaller), [geom_getOctreeOctreeDistanceIfSmaller](#geom_getOctreeOctreeDistanceIfSmaller), [geom_getOctreePtcloudDistanceIfSmaller](#geom_getOctreePtcloudDistanceIfSmaller), [geom_getOctreeSegmentDistanceIfSmaller](#geom_getOctreeSegmentDistanceIfSmaller), [geom_getOctreePointDistanceIfSmaller](#geom_getOctreePointDistanceIfSmaller), [geom_getPtcloudTriangleDistanceIfSmaller](#geom_getPtcloudTriangleDistanceIfSmaller), [geom_getBoxTriangleDistanceIfSmaller](#geom_getBoxTriangleDistanceIfSmaller), [geom_getTriangleTriangleDistanceIfSmaller](#geom_getTriangleTriangleDistanceIfSmaller), [geom_getTriangleSegmentDistanceIfSmaller](#geom_getTriangleSegmentDistanceIfSmaller), [geom_getTrianglePointDistanceIfSmaller](#geom_getTrianglePointDistanceIfSmaller)

### <a id="geom_getOctreeVoxelData"></a>geom_getOctreeVoxelData

**Description**: Retrieves voxel data and optionally user data from an OC-tree.

**Synopsis**: `void geom_getOctreeVoxelData(const COcStruct* ocStruct,std::vector<double>& voxelData,std::vector<unsigned int>* userData=nullptr)`

**Arguments**:

- **ocStruct**: a pointer to the OC-tree object.
- **voxelData**: the voxel data: for each voxel, there are 3 position values (XYZ) and 3 color values (RGB, 0-1).
- **userData**: the user data: for each voxel, there is one user data value.

### <a id="geom_getPtcloudFromSerializationData"></a>geom_getPtcloudFromSerializationData

**Description**: Creates a point-cloud object based on serialization data.

**Synopsis**: `CPcStruct* geom_getPtcloudFromSerializationData(const unsigned char* serializationData)`

**Arguments**:

- **serializationData**: the serialization data previously generated with [geom_getPtcloudSerializationData](#geom_getPtcloudSerializationData).

**Return value**: A pointer to the created point-cloud object in case of success, nullptr otherwise.

**See also**: [geom_getPtcloudSerializationData](#geom_getPtcloudSerializationData)

### <a id="geom_getPtcloudPointDistanceIfSmaller"></a>geom_getPtcloudPointDistanceIfSmaller

**Description**: Computes the minimum distance between a point-cloud object and a point.

**Synopsis**: `bool geom_getPtcloudPointDistanceIfSmaller(const CPcStruct* pcStruct,const CPose& pcTransformation,const C3Vector& point,double& dist,C3Vector* pcMinDistPt=nullptr,unsigned long long int* pcCaching=nullptr)`

**Arguments**:

- **pcStruct**: a pointer to the point-cloud object.
- **pcTransformation**: the transformation frame of the point-cloud.
- **point**: the position of the point.
- **dist**: the distance threshold as input, and the minimum distance as output if it is below the threshold.
- **pcMinDistPt**: the minimum distance point on the point-cloud.
- **pcCaching**: a value that can be used to speed-up next distance calculation between the same two entities (memorizes the point that holds the minimum distance point on the point-cloud).

**Return value**: whether the minimum distance is smaller than the specified threshold

**See also**: [geom_getMeshPtcloudDistanceIfSmaller](#geom_getMeshPtcloudDistanceIfSmaller), [geom_getMeshPointDistanceIfSmaller](#geom_getMeshPointDistanceIfSmaller), [geom_getOctreePtcloudDistanceIfSmaller](#geom_getOctreePtcloudDistanceIfSmaller), [geom_getOctreePointDistanceIfSmaller](#geom_getOctreePointDistanceIfSmaller), [geom_getPtcloudPtcloudDistanceIfSmaller](#geom_getPtcloudPtcloudDistanceIfSmaller), [geom_getPtcloudTriangleDistanceIfSmaller](#geom_getPtcloudTriangleDistanceIfSmaller), [geom_getPtcloudSegmentDistanceIfSmaller](#geom_getPtcloudSegmentDistanceIfSmaller), [geom_getBoxPointDistanceIfSmaller](#geom_getBoxPointDistanceIfSmaller), [geom_getTrianglePointDistanceIfSmaller](#geom_getTrianglePointDistanceIfSmaller), [geom_getSegmentPointDistanceIfSmaller](#geom_getSegmentPointDistanceIfSmaller)

### <a id="geom_getPtcloudPoints"></a>geom_getPtcloudPoints

**Description**: Retrieves point data from a point-cloud.

**Synopsis**: `void geom_getPtcloudPoints(const CPcStruct* pcStruct,std::vector<double>& pointData,double prop=1.0)`

**Arguments**:

- **pcStruct**: a pointer to the point-cloud object.
- **pointData**: the point data: for each point, there are 3 position values (XYZ) and 3 color values (RGB, 0-1).
- **prop**: the proportion of data to retrieve, on a voxel-basis. 1.0 retrieves all data, while 0.25 retrieves 25% of the data.

### <a id="geom_getPtcloudPtcloudDistanceIfSmaller"></a>geom_getPtcloudPtcloudDistanceIfSmaller

**Description**: Computes the minimum distance between two point-cloud objects.

**Synopsis**: `bool geom_getPtcloudPtcloudDistanceIfSmaller(const CPcStruct* pc1Struct,const CPose& pc1Transformation,const CPcStruct* pc2Struct,const CPose& pc2Transformation,double& dist,C3Vector* pc1MinDistPt=nullptr,C3Vector* pc2MinDistPt=nullptr,unsigned long long int* pc1Caching=nullptr,unsigned long long int* pc2Caching=nullptr)`

**Arguments**:

- **pc1Struct**: a pointer to the first point-cloud object.
- **pc1Transformation**: the transformation frame of the first point-cloud.
- **pc2Struct**: a pointer to the second point-cloud object.
- **pc2Transformation**: the transformation frame of the second point-cloud.
- **dist**: the distance threshold as input, and the minimum distance as output if it is below the threshold.
- **pc1MinDistPt**: the minimum distance point on the first point-cloud.
- **pc2MinDistPt**: the minimum distance point on the second point-cloud.
- **pc1Caching**: a value that can be used to speed-up next distance calculation between the same two entities (memorizes the point that holds the minimum distance point on the first point-cloud).
- **pc2Caching**: a value that can be used to speed-up next distance calculation between the same two entities (memorizes the point that holds the minimum distance point on the second point-cloud).

**Return value**: whether the minimum distance is smaller than the specified threshold

**See also**: [geom_getMeshPtcloudDistanceIfSmaller](#geom_getMeshPtcloudDistanceIfSmaller), [geom_getOctreePtcloudDistanceIfSmaller](#geom_getOctreePtcloudDistanceIfSmaller), [geom_getPtcloudTriangleDistanceIfSmaller](#geom_getPtcloudTriangleDistanceIfSmaller), [geom_getPtcloudSegmentDistanceIfSmaller](#geom_getPtcloudSegmentDistanceIfSmaller), [geom_getPtcloudPointDistanceIfSmaller](#geom_getPtcloudPointDistanceIfSmaller)

### <a id="geom_getPtcloudSegmentDistanceIfSmaller"></a>geom_getPtcloudSegmentDistanceIfSmaller

**Description**: Computes the minimum distance between a point-cloud and a segment.

**Synopsis**: `bool geom_getPtcloudSegmentDistanceIfSmaller(const CPcStruct* pcStruct,const CPose& pcTransformation,const C3Vector& segmentEndPoint,const C3Vector& segmentVector,double& dist,C3Vector* pcMinDistPt=nullptr,C3Vector* segmentDistSegPt=nullptr,unsigned long long int* pcCaching=nullptr)`

**Arguments**:

- **pcStruct**: a pointer to the point-cloud object.
- **pcTransformation**: the transformation frame of the point-cloud.
- **segmentEndPoint**: position of vertex A on the segment.
- **segmentVector**: vector stretching from vertex A to vertex B on the segment.
- **dist**: the distance threshold as input, and the minimum distance as output if it is below the threshold.
- **pcMinDistPt**: the minimum distance point on the point-cloud.
- **segmentDistSegPt**: the minimum distance point on the segment.
- **pcCaching**: a value that can be used to speed-up next distance calculation between the same two entities (memorizes the point that holds the minimum distance point on the point-cloud).

**Return value**: whether the minimum distance is smaller than the specified threshold

**See also**: [geom_getMeshPtcloudDistanceIfSmaller](#geom_getMeshPtcloudDistanceIfSmaller), [geom_getMeshSegmentDistanceIfSmaller](#geom_getMeshSegmentDistanceIfSmaller), [geom_getOctreePtcloudDistanceIfSmaller](#geom_getOctreePtcloudDistanceIfSmaller), [geom_getOctreeSegmentDistanceIfSmaller](#geom_getOctreeSegmentDistanceIfSmaller), [geom_getPtcloudPtcloudDistanceIfSmaller](#geom_getPtcloudPtcloudDistanceIfSmaller), [geom_getPtcloudTriangleDistanceIfSmaller](#geom_getPtcloudTriangleDistanceIfSmaller), [geom_getPtcloudPointDistanceIfSmaller](#geom_getPtcloudPointDistanceIfSmaller), [geom_getBoxSegmentDistanceIfSmaller](#geom_getBoxSegmentDistanceIfSmaller), [geom_getTriangleSegmentDistanceIfSmaller](#geom_getTriangleSegmentDistanceIfSmaller), [geom_getSegmentSegmentDistanceIfSmaller](#geom_getSegmentSegmentDistanceIfSmaller), [geom_getSegmentPointDistanceIfSmaller](#geom_getSegmentPointDistanceIfSmaller)

### <a id="geom_getPtcloudSerializationData"></a>geom_getPtcloudSerializationData

**Description**: Retrieves the serialization data from a point-cloud object.

**Synopsis**: `void geom_getPtcloudSerializationData(const CPcStruct* pcStruct,std::vector<unsigned char>& serializationData)`

**Arguments**:

- **pcStruct**: a pointer to the point-cloud object.
- **serializationData**: the serialization data.

**See also**: [geom_getPtcloudFromSerializationData](#geom_getPtcloudFromSerializationData)

### <a id="geom_getPtcloudTriangleDistanceIfSmaller"></a>geom_getPtcloudTriangleDistanceIfSmaller

**Description**: Computes the minimum distance between a point-cloud object and a triangle.

**Synopsis**: `bool geom_getPtcloudTriangleDistanceIfSmaller(const CPcStruct* pcStruct,const CPose& pcTransformation,const C3Vector& p,const C3Vector& v,const C3Vector& w,double& dist,C3Vector* pcMinDistPt=nullptr,C3Vector* triangleMinDistPt=nullptr,unsigned long long int* pcCaching=nullptr)`

**Arguments**:

- **pcStruct**: a pointer to the point-cloud object.
- **pcTransformation**: the transformation frame of the point-cloud.
- **p**: position of vertex A on the triangle.
- **v**: vector stretching from vertex A to vertex B on the triangle.
- **w**: vector stretching from vertex A to vertex C on the triangle.
- **dist**: the distance threshold as input, and the minimum distance as output if it is below the threshold.
- **pcMinDistPt**: the minimum distance point on the point-cloud.
- **triangleMinDistPt**: the minimum distance point on the triangle.
- **pcCaching**: a value that can be used to speed up next distance calculation between the same two entities (memorizes the point that holds the minimum distance point on the point-cloud).

**Return value**: whether the minimum distance is smaller than the specified threshold

**See also**: [geom_getMeshPtcloudDistanceIfSmaller](#geom_getMeshPtcloudDistanceIfSmaller), [geom_getOctreePtcloudDistanceIfSmaller](#geom_getOctreePtcloudDistanceIfSmaller), [geom_getPtcloudPtcloudDistanceIfSmaller](#geom_getPtcloudPtcloudDistanceIfSmaller), [geom_getPtcloudSegmentDistanceIfSmaller](#geom_getPtcloudSegmentDistanceIfSmaller), [geom_getPtcloudPointDistanceIfSmaller](#geom_getPtcloudPointDistanceIfSmaller), [geom_getBoxTriangleDistanceIfSmaller](#geom_getBoxTriangleDistanceIfSmaller), [geom_getTriangleTriangleDistanceIfSmaller](#geom_getTriangleTriangleDistanceIfSmaller), [geom_getTriangleSegmentDistanceIfSmaller](#geom_getTriangleSegmentDistanceIfSmaller), [geom_getTrianglePointDistanceIfSmaller](#geom_getTrianglePointDistanceIfSmaller)

### <a id="geom_getSegmentPointDistanceIfSmaller"></a>geom_getSegmentPointDistanceIfSmaller

**Description**: Computes the minimum distance between a segment and a point.

**Synopsis**: `bool geom_getSegmentPointDistanceIfSmaller(const C3Vector& segmentEndPoint,const C3Vector& segmentVector,const C3Vector& point,double& dist,C3Vector* segmentDistSegPt=nullptr)`

**Arguments**:

- **segmentEndPoint**: position of vertex A on the segment.
- **segmentVector**: vector stretching from vertex A to vertex B on the segment.
- **point**: position of the point.
- **dist**: the distance threshold as input, and the minimum distance as output if it is below the threshold.
- **segmentDistSegPt**: the minimum distance point on the segment.

**Return value**: whether the minimum distance is smaller than the specified threshold

**See also**: [geom_getMeshSegmentDistanceIfSmaller](#geom_getMeshSegmentDistanceIfSmaller), [geom_getMeshPointDistanceIfSmaller](#geom_getMeshPointDistanceIfSmaller), [geom_getOctreeSegmentDistanceIfSmaller](#geom_getOctreeSegmentDistanceIfSmaller), [geom_getOctreePointDistanceIfSmaller](#geom_getOctreePointDistanceIfSmaller), [geom_getPtcloudSegmentDistanceIfSmaller](#geom_getPtcloudSegmentDistanceIfSmaller), [geom_getPtcloudPointDistanceIfSmaller](#geom_getPtcloudPointDistanceIfSmaller), [geom_getBoxSegmentDistanceIfSmaller](#geom_getBoxSegmentDistanceIfSmaller), [geom_getBoxPointDistanceIfSmaller](#geom_getBoxPointDistanceIfSmaller), [geom_getTriangleSegmentDistanceIfSmaller](#geom_getTriangleSegmentDistanceIfSmaller), [geom_getTrianglePointDistanceIfSmaller](#geom_getTrianglePointDistanceIfSmaller), [geom_getSegmentSegmentDistanceIfSmaller](#geom_getSegmentSegmentDistanceIfSmaller)

### <a id="geom_getSegmentSegmentDistanceIfSmaller"></a>geom_getSegmentSegmentDistanceIfSmaller

**Description**: Computes the minimum distance between two segments.

**Synopsis**: `bool geom_getSegmentSegmentDistanceIfSmaller(const C3Vector& segment1EndPoint,const C3Vector& segment1Vector,const C3Vector& segment2EndPoint,const C3Vector& segment2Vector,double& dist,C3Vector* segment1DistSegPt=nullptr,C3Vector* segment2DistSegPt=nullptr)`

**Arguments**:

- **segment1EndPoint**: position of point A on the first segment.
- **segment1Vector**: vector stretching from point A to point B on the first segment.
- **segment2EndPoint**: position of point A on the second segment.
- **segment2Vector**: vector stretching from point A to point B on the second segment.
- **dist**: the distance threshold as input, and the minimum distance as output if it is below the threshold.
- **segment1DistSegPt**: the minimum distance point on the first segment.
- **segment2DistSegPt**: the minimum distance point on the second segment.

**Return value**: whether the minimum distance is smaller than the specified threshold

**See also**: [geom_getMeshSegmentDistanceIfSmaller](#geom_getMeshSegmentDistanceIfSmaller), [geom_getOctreeSegmentDistanceIfSmaller](#geom_getOctreeSegmentDistanceIfSmaller), [geom_getPtcloudSegmentDistanceIfSmaller](#geom_getPtcloudSegmentDistanceIfSmaller), [geom_getBoxSegmentDistanceIfSmaller](#geom_getBoxSegmentDistanceIfSmaller), [geom_getTriangleSegmentDistanceIfSmaller](#geom_getTriangleSegmentDistanceIfSmaller), [geom_getSegmentPointDistanceIfSmaller](#geom_getSegmentPointDistanceIfSmaller)

### <a id="geom_getTrianglePointDistanceIfSmaller"></a>geom_getTrianglePointDistanceIfSmaller

**Description**: Computes the minimum distance between a triangle and a point.

**Synopsis**: `bool geom_getTrianglePointDistanceIfSmaller(const C3Vector& p,const C3Vector& v,const C3Vector& w,const C3Vector& point,double& dist,C3Vector* triangleDistSegPt=nullptr)`

**Arguments**:

- **p**: position of vertex A on the triangle.
- **v**: vector stretching from vertex A to vertex B on the triangle.
- **w**: vector stretching from vertex A to vertex C on the triangle.
- **point**: position of the point.
- **dist**: the distance threshold as input, and the minimum distance as output if it is below the threshold.
- **triangleDistSegPt**: the minimum distance point on the triangle.

**Return value**: whether the minimum distance is smaller than the specified threshold

**See also**: [geom_getMeshTriangleDistanceIfSmaller](#geom_getMeshTriangleDistanceIfSmaller), [geom_getMeshPointDistanceIfSmaller](#geom_getMeshPointDistanceIfSmaller), [geom_getOctreeTriangleDistanceIfSmaller](#geom_getOctreeTriangleDistanceIfSmaller), [geom_getOctreePointDistanceIfSmaller](#geom_getOctreePointDistanceIfSmaller), [geom_getPtcloudTriangleDistanceIfSmaller](#geom_getPtcloudTriangleDistanceIfSmaller), [geom_getPtcloudPointDistanceIfSmaller](#geom_getPtcloudPointDistanceIfSmaller), [geom_getBoxTriangleDistanceIfSmaller](#geom_getBoxTriangleDistanceIfSmaller), [geom_getBoxPointDistanceIfSmaller](#geom_getBoxPointDistanceIfSmaller), [geom_getTriangleTriangleDistanceIfSmaller](#geom_getTriangleTriangleDistanceIfSmaller), [geom_getTriangleSegmentDistanceIfSmaller](#geom_getTriangleSegmentDistanceIfSmaller), [geom_getSegmentPointDistanceIfSmaller](#geom_getSegmentPointDistanceIfSmaller)

### <a id="geom_getTriangleSegmentCollision"></a>geom_getTriangleSegmentCollision

**Description**: Checks for collision between a triangle and a segment.

**Synopsis**: `bool geom_getTriangleSegmentCollision(const C3Vector& p,const C3Vector& v,const C3Vector& w,const C3Vector& segmentEndPoint,const C3Vector& segmentVector,std::vector<double>* intersections=nullptr)`

**Arguments**:

- **p**: position of vertex A on the triangle.
- **v**: vector stretching from vertex A to vertex B on the triangle.
- **w**: vector stretching from vertex A to vertex C on the triangle.
- **segmentEndPoint**: position of vertex A on the segment.
- **segmentVector**: vector stretching from vertex A to vertex B on the segment.
- **intersections**: if not nullptr, then a possible collision will be extracted as interference segment (where both segment points are always coincident) (set to nullptr for fast operation).

**Return value**: the collision status

**See also**: [geom_getMeshTriangleCollision](#geom_getMeshTriangleCollision), [geom_getMeshSegmentCollision](#geom_getMeshSegmentCollision), [geom_getOctreeTriangleCollision](#geom_getOctreeTriangleCollision), [geom_getOctreeSegmentCollision](#geom_getOctreeSegmentCollision), [geom_getBoxTriangleCollision](#geom_getBoxTriangleCollision), [geom_getBoxSegmentCollision](#geom_getBoxSegmentCollision), [geom_getTriangleTriangleCollision](#geom_getTriangleTriangleCollision)

### <a id="geom_getTriangleSegmentDistanceIfSmaller"></a>geom_getTriangleSegmentDistanceIfSmaller

**Description**: Computes the minimum distance between a triangle and a segment.

**Synopsis**: `bool geom_getTriangleSegmentDistanceIfSmaller(const C3Vector& p,const C3Vector& v,const C3Vector& w,const C3Vector& segmentEndPoint,const C3Vector& segmentVector,double& dist,C3Vector* triangleDistSegPt=nullptr,C3Vector* segmentDistSegPt=nullptr)`

**Arguments**:

- **p**: position of vertex A on the triangle.
- **v**: vector stretching from vertex A to vertex B on the triangle.
- **w**: vector stretching from vertex A to vertex C on the triangle.
- **segmentEndPoint**: position of vertex A on the segment.
- **segmentVector**: vector stretching from vertex A to vertex B on the segment.
- **dist**: the distance threshold as input, and the minimum distance as output if it is below the threshold.
- **triangleDistSegPt**: the minimum distance point on the triangle.
- **segmentDistSegPt**: the minimum distance point on the segment.

**Return value**: whether the minimum distance is smaller than the specified threshold

**See also**: [geom_getMeshTriangleDistanceIfSmaller](#geom_getMeshTriangleDistanceIfSmaller), [geom_getMeshSegmentDistanceIfSmaller](#geom_getMeshSegmentDistanceIfSmaller), [geom_getOctreeTriangleDistanceIfSmaller](#geom_getOctreeTriangleDistanceIfSmaller), [geom_getOctreeSegmentDistanceIfSmaller](#geom_getOctreeSegmentDistanceIfSmaller), [geom_getPtcloudTriangleDistanceIfSmaller](#geom_getPtcloudTriangleDistanceIfSmaller), [geom_getPtcloudSegmentDistanceIfSmaller](#geom_getPtcloudSegmentDistanceIfSmaller), [geom_getBoxTriangleDistanceIfSmaller](#geom_getBoxTriangleDistanceIfSmaller), [geom_getBoxSegmentDistanceIfSmaller](#geom_getBoxSegmentDistanceIfSmaller), [geom_getTriangleTriangleDistanceIfSmaller](#geom_getTriangleTriangleDistanceIfSmaller), [geom_getTrianglePointDistanceIfSmaller](#geom_getTrianglePointDistanceIfSmaller), [geom_getSegmentSegmentDistanceIfSmaller](#geom_getSegmentSegmentDistanceIfSmaller), [geom_getSegmentPointDistanceIfSmaller](#geom_getSegmentPointDistanceIfSmaller)

### <a id="geom_getTriangleTriangleCollision"></a>geom_getTriangleTriangleCollision

**Description**: Checks for collision between two triangles.

**Synopsis**: `bool geom_getTriangleTriangleCollision(const C3Vector& p1,const C3Vector& v1,const C3Vector& w1,const C3Vector& p2,const C3Vector& v2,const C3Vector& w2,std::vector<double>* intersections=nullptr)`

**Arguments**:

- **p1**: position of point A on triangle 1.
- **v1**: vector stretching from point A to point B on triangle 1.
- **w1**: vector stretching from point A to point C on triangle 1.
- **p2**: position of point A on triangle 2.
- **v2**: vector stretching from point A to point B on triangle 2.
- **w2**: vector stretching from point A to point C on triangle 2.
- **intersections**: if not nullptr, then all collisions will be extracted as interference segments (set to nullptr for fast operation).

**Return value**: the collision status

**See also**: [geom_getMeshTriangleCollision](#geom_getMeshTriangleCollision), [geom_getOctreeTriangleCollision](#geom_getOctreeTriangleCollision), [geom_getBoxTriangleCollision](#geom_getBoxTriangleCollision), [geom_getTriangleSegmentCollision](#geom_getTriangleSegmentCollision)

### <a id="geom_getTriangleTriangleDistanceIfSmaller"></a>geom_getTriangleTriangleDistanceIfSmaller

**Description**: Computes the minimum distance between two triangles.

**Synopsis**: `bool geom_getTriangleTriangleDistanceIfSmaller(const C3Vector& p1,const C3Vector& v1,const C3Vector& w1,const C3Vector& p2,const C3Vector& v2,const C3Vector& w2,double& dist,C3Vector* triangle1DistSegPt=nullptr,C3Vector* triangle2DistSegPt=nullptr)`

**Arguments**:

- **p1**: position of point A on triangle 1.
- **v1**: vector stretching from point A to point B on triangle 1.
- **w1**: vector stretching from point A to point C on triangle 1.
- **p2**: position of point A on triangle 2.
- **v2**: vector stretching from point A to point B on triangle 2.
- **w2**: vector stretching from point A to point C on triangle 2.
- **dist**: the distance threshold as input, and the minimum distance as output if it is below the threshold.
- **triangle1DistSegPt**: the minimum distance point on the first triangle.
- **triangle2DistSegPt**: the minimum distance point on the second triangle.

**Return value**: whether the minimum distance is smaller than the specified threshold

**See also**: [geom_getMeshTriangleDistanceIfSmaller](#geom_getMeshTriangleDistanceIfSmaller), [geom_getOctreeTriangleDistanceIfSmaller](#geom_getOctreeTriangleDistanceIfSmaller), [geom_getPtcloudTriangleDistanceIfSmaller](#geom_getPtcloudTriangleDistanceIfSmaller), [geom_getBoxTriangleDistanceIfSmaller](#geom_getBoxTriangleDistanceIfSmaller), [geom_getTriangleSegmentDistanceIfSmaller](#geom_getTriangleSegmentDistanceIfSmaller), [geom_getTrianglePointDistanceIfSmaller](#geom_getTrianglePointDistanceIfSmaller)

### <a id="geom_insertColorPointsIntoOctree"></a>geom_insertColorPointsIntoOctree

**Description**: Inserts points (with individual colors) into an OC-tree, effectively creating OC-tree voxels.

**Synopsis**: `void geom_insertColorPointsIntoOctree(COcStruct* ocStruct,const CPose& octreeTransformation,const double* points,int pointCnt,const unsigned char* rgbData=nullptr,const unsigned int* usrData=nullptr)`

**Arguments**:

- **ocStruct**: a pointer to the OC-tree object.
- **octreeTransformation**: the transformation frame of the OC-tree.
- **points**: an array of point values (XYZ-triplets). Points are expressed relative to the world reference frame.
- **pointCnt**: the number of points.
- **rgbData**: the RGB colors (0-255)of the various points (i.e. one color per point).
- **usrData**: the user data of the various points (i.e. one user data per point).

**See also**: [geom_insertPointsIntoOctree](#geom_insertPointsIntoOctree), [geom_insertMeshIntoOctree](#geom_insertMeshIntoOctree), [geom_insertOctreeIntoOctree](#geom_insertOctreeIntoOctree), [geom_removePointsFromOctree](#geom_removePointsFromOctree)

### <a id="geom_insertColorPointsIntoPtcloud"></a>geom_insertColorPointsIntoPtcloud

**Description**: Inserts points (with individual colors) into a point-cloud object.

**Synopsis**: `void geom_insertColorPointsIntoPtcloud(CPcStruct* pcStruct,const CPose& ptcloudTransformation,const double* points,int pointCnt,const unsigned char* rgbData=nullptr,double proximityTol=0.001`

**Arguments**:

- **pcStruct**: a pointer to the point-cloud object.
- **ptcloudTransformation**: the transformation frame of the point-cloud.
- **points**: an array of point values (XYZ-triplets). Points are expressed relative to the world reference frame.
- **pointCnt**: the number of points.
- **rgbData**: the RGB colors (0-255)of the various points (i.e. one color per point).
- **proximityTol**: the distance tolerance to other points (i.e. point-point distances below the specified value are not permitted and points will be omitted).

**See also**: [geom_insertPointsIntoPtcloud](#geom_insertPointsIntoPtcloud), [geom_removePointsFromPtcloud](#geom_removePointsFromPtcloud), [geom_removeOctreeFromPtcloud](#geom_removeOctreeFromPtcloud), [geom_intersectPointsWithPtcloud](#geom_intersectPointsWithPtcloud)

### <a id="geom_insertMeshIntoOctree"></a>geom_insertMeshIntoOctree

**Description**: Inserts a mesh object into an OC-tree, effectively creating OC-tree voxels.

**Synopsis**: `void geom_insertMeshIntoOctree(COcStruct* ocStruct,const CPose& octreeTransformation,const CObbStruct* obbStruct,const CPose& meshTransformation,const unsigned char rgbData[3]=nullptr,unsigned int usrData=0)`

**Arguments**:

- **ocStruct**: a pointer to the OC-tree object.
- **octreeTransformation**: the transformation frame of the OC-tree.
- **obbStruct**: a pointer to the mesh object.
- **meshTransformation**: the transformation frame of the mesh.
- **rgbData**: the RGB color (0-255) of the generated voxels.
- **usrData**: the user data of the generated voxels.

**See also**: [geom_insertPointsIntoOctree](#geom_insertPointsIntoOctree), [geom_insertColorPointsIntoOctree](#geom_insertColorPointsIntoOctree), [geom_insertOctreeIntoOctree](#geom_insertOctreeIntoOctree), [geom_removeMeshFromOctree](#geom_removeMeshFromOctree)

### <a id="geom_insertOctreeIntoOctree"></a>geom_insertOctreeIntoOctree

**Description**: Inserts an OC-tree object into another OC-tree object, effectively creating OC-tree voxels in the second OC-tree object.

**Synopsis**: `void geom_insertOctreeIntoOctree(COcStruct* oc1Struct,const CPose& octree1Transformation,const COcStruct* oc2Struct,const CPose& octree2Transformation,const unsigned char rgbData[3]=nullptr,unsigned int usrData=0)`

**Arguments**:

- **oc1Struct**: a pointer to the OC-tree object.
- **octree1Transformation**: the transformation frame of the OC-tree.
- **oc2Struct**: a pointer to the other OC-tree object.
- **octree2Transformation**: the transformation frame of the other OC-tree object.
- **rgbData**: the RGB color (0-255) of the generated voxels.
- **usrData**: the user data of the generated voxels.

**See also**: [geom_insertPointsIntoOctree](#geom_insertPointsIntoOctree), [geom_insertColorPointsIntoOctree](#geom_insertColorPointsIntoOctree), [geom_insertMeshIntoOctree](#geom_insertMeshIntoOctree), [geom_removeOctreeFromOctree](#geom_removeOctreeFromOctree)

### <a id="geom_insertPointsIntoOctree"></a>geom_insertPointsIntoOctree

**Description**: Inserts points into an OC-tree, effectively creating OC-tree voxels.

**Synopsis**: `void geom_insertPointsIntoOctree(COcStruct* ocStruct,const CPose& octreeTransformation,const double* points,int pointCnt,const unsigned char rgbData[3]=nullptr,unsigned int usrData=0)`

**Arguments**:

- **ocStruct**: a pointer to the OC-tree object.
- **octreeTransformation**: the transformation frame of the OC-tree.
- **points**: an array of point values (XYZ-triplets). Points are expressed relative to the world reference frame.
- **pointCnt**: the number of points.
- **rgbData**: the RGB color (0-255) of the generated voxels.
- **usrData**: the user data of the generated voxels.

**See also**: [geom_insertColorPointsIntoOctree](#geom_insertColorPointsIntoOctree), [geom_insertMeshIntoOctree](#geom_insertMeshIntoOctree), [geom_insertOctreeIntoOctree](#geom_insertOctreeIntoOctree), [geom_removePointsFromOctree](#geom_removePointsFromOctree)

### <a id="geom_insertPointsIntoPtcloud"></a>geom_insertPointsIntoPtcloud

**Description**: Inserts points into a point-cloud object.

**Synopsis**: `void geom_insertPointsIntoPtcloud(CPcStruct* pcStruct,const CPose& ptcloudTransformation,const double* points,int pointCnt,const unsigned char rgbData[3]=nullptr,double proximityTol=0.001)`

**Arguments**:

- **pcStruct**: a pointer to the point-cloud object.
- **ptcloudTransformation**: the transformation frame of the point-cloud.
- **points**: an array of point values (XYZ-triplets). Points are expressed relative to the world reference frame.
- **pointCnt**: the number of points.
- **rgbData**: the RGB color (0-255) of the generated points.
- **proximityTol**: the distance tolerance to other points (i.e. point-point distances below the specified value are not permitted and points will be omitted).

**See also**: [geom_insertColorPointsIntoPtcloud](#geom_insertColorPointsIntoPtcloud), [geom_removePointsFromPtcloud](#geom_removePointsFromPtcloud), [geom_removeOctreeFromPtcloud](#geom_removeOctreeFromPtcloud), [geom_intersectPointsWithPtcloud](#geom_intersectPointsWithPtcloud)

### <a id="geom_intersectPointsWithPtcloud"></a>geom_intersectPointsWithPtcloud

**Description**: Performs an intersection operation between a point-cloud and specific points: point-cloud points within a certain tolerance to the specified points will be kept, while others will be removed.

**Synopsis**: `bool geom_intersectPointsWithPtcloud(CPcStruct* pcStruct,const CPose& ptcloudTransformation,const double* points,int pointCnt,double proximityTol=0.001)`

**Arguments**:

- **pcStruct**: a pointer to the point-cloud object.
- **ptcloudTransformation**: the transformation frame of the point-cloud.
- **points**: an array of point values (XYZ-triplets). Points are expressed relative to the world reference frame.
- **pointCnt**: the number of points.
- **proximityTol**: the distance tolerance to other points (i.e. point-point distances above the specified value will result in removal of those point-cloud points.

### <a id="geom_isPointInVolume"></a>geom_isPointInVolume

**Description**: Checks whether a point lies within a proximity sensor volume.

**Synopsis**: `bool geom_isPointInVolume(const double* planesIn,int planesInSize,const CPose& sensorTransformation,const C3Vector& point)`

**Arguments**:

- **planesIn**: an array describing a convex volume, via planes. Each plane is defined by 4 values: (Nx,Ny,Nz,D), where a point (Px,Py,Pz) lies on the inside if N\*P+D>=0. N is the normal vector of the plane, pointing towards the volume inside.
- **planesInSize**: the number of values in the planesIn array.
- **sensorTransformation**: the transformation frame of the volume.
- **point**: the point to test.

**Return value**: whether the point lies within the sensor's volume.

### <a id="geom_raySensorDetectMeshIfSmaller"></a>geom_raySensorDetectMeshIfSmaller

**Description**: Computes the distance from a ray-type proximity sensor to a mesh object.

**Synopsis**: `bool geom_raySensorDetectMeshIfSmaller(const CPose& sensorTransformation,double rayOffset,double rayLength,const CObbStruct* meshObbStruct,const CPose& meshTransformation,double& dist,double forbiddenDist=0.0,bool fast=false,bool frontDetection=true,bool backDetection=true,double maxAngle=0.0,C3Vector* detectPt=nullptr,C3Vector* triN=nullptr,bool* forbiddenDistTouched=nullptr)`

**Arguments**:

- **sensorTransformation**: the transformation frame of the sensor.
- **rayOffset**: the offset of the ray (i.e. where the ray starts), along its frame's Z-axis.
- **rayLength**: the length of the ray.
- **meshObbStruct**: a pointer to the mesh object.
- **meshTransformation**: the transformation frame of the mesh.
- **dist**: the distance threshold as input, and the minimum distance as output if it is below the threshold.
- **forbiddenDist**: the distance threshold along the sensor's Z-axis, where detection is forbidden. If something is detected in that section of the ray, then the return will be false.
- **fast**: if true, calculation will be faster, however only the first encountered feature that satisfies the detection requirements will be returned (and not the closest of those features).
- **frontDetection**: if true, front faces of the mesh will be detected.
- **backDetection**: if true, back faces of the mesh will be detected.
- **maxAngle**: the maximum allowed angle between detection ray and normal vector of the detected face. Zero to ignore the maximum angle.
- **detectPt**: the position of the detected point, if return value is true.
- **triN**: the normal vector of the detected face, if return value is true.
- **forbiddenDistTouched**: if something was detected in the forbidden section of the sensor, then the value pointed to by this pointer will be true.

**Return value**: whether the sensor detected something and the distance is smaller than the specified threshold

**See also**: [geom_raySensorDetectOctreeIfSmaller](#geom_raySensorDetectOctreeIfSmaller), [geom_getMeshSegmentDistanceIfSmaller](#geom_getMeshSegmentDistanceIfSmaller), [geom_getMeshPointDistanceIfSmaller](#geom_getMeshPointDistanceIfSmaller)

### <a id="geom_raySensorDetectOctreeIfSmaller"></a>geom_raySensorDetectOctreeIfSmaller

**Description**: Computes the distance from a ray-type proximity sensor to an OC-tree object.

**Synopsis**: `bool geom_raySensorDetectOctreeIfSmaller(const CPose& sensorTransformation,double rayOffset,double rayLength,const COcStruct* ocStruct,const CPose& octreeTransformation,double& dist,double forbiddenDist=0.0,bool fast=false,bool frontDetection=true,bool backDetection=true,double maxAngle=0.0,C3Vector* detectPt=nullptr,C3Vector* triN=nullptr,bool* forbiddenDistTouched=nullptr)`

**Arguments**:

- **sensorTransformation**: the transformation frame of the sensor.
- **rayOffset**: the offset of the ray (i.e. where the ray starts), along its frame's Z-axis.
- **rayLength**: the length of the ray.
- **ocStruct**: a pointer to the OC-tree object.
- **octreeTransformation**: the transformation frame of the OC-tree.
- **dist**: the distance threshold as input, and the minimum distance as output if it is below the threshold.
- **forbiddenDist**: the distance threshold along the sensor's Z-axis, where detection is forbidden. If something is detected in that section of the ray, then the return will be false.
- **fast**: if true, calculation will be faster, however only the first encountered feature that satisfies the detection requirements will be returned (and not the closest of those features).
- **frontDetection**: if true, front faces of the OC-tree will be detected.
- **backDetection**: if true, back faces of the OC-tree will be detected.
- **maxAngle**: the maximum allowed angle between detection ray and normal vector of the detected face. Zero to ignore the maximum angle.
- **detectPt**: the position of the detected point, if return value is true.
- **triN**: the normal vector of the detected face, if return value is true.
- **forbiddenDistTouched**: if something was detected in the forbidden section of the sensor, then the value pointed to by this pointer will be true.

**Return value**: whether the sensor detected something and the distance is smaller than the specified threshold

**See also**: [geom_raySensorDetectMeshIfSmaller](#geom_raySensorDetectMeshIfSmaller), [geom_getOctreeSegmentDistanceIfSmaller](#geom_getOctreeSegmentDistanceIfSmaller), [geom_getOctreePointDistanceIfSmaller](#geom_getOctreePointDistanceIfSmaller)

### <a id="geom_removeMeshFromOctree"></a>geom_removeMeshFromOctree

**Description**: Deletes OC-tree voxels that occupy the space of the specified mesh.

**Synopsis**: `bool geom_removeMeshFromOctree(COcStruct* ocStruct,const CPose& octreeTransformation,const CObbStruct* obbStruct,const CPose& meshTransformation)`

**Arguments**:

- **ocStruct**: a pointer to the OC-tree object.
- **octreeTransformation**: the transformation frame of the OC-tree.
- **obbStruct**: a pointer to the mesh object.
- **meshTransformation**: the transformation frame of the mesh.

**Return value**: true if the OC-tree does not contain any voxels anymore, after this operation. false otherwise.

**See also**: [geom_removePointsFromOctree](#geom_removePointsFromOctree), [geom_removeOctreeFromOctree](#geom_removeOctreeFromOctree), [geom_insertMeshIntoOctree](#geom_insertMeshIntoOctree)

### <a id="geom_removeOctreeFromOctree"></a>geom_removeOctreeFromOctree

**Description**: Deletes OC-tree voxels that occupy the space of the other specified OC-tree.

**Synopsis**: `bool geom_removeOctreeFromOctree(COcStruct* oc1Struct,const CPose& octree1Transformation,const COcStruct* oc2Struct,const CPose& octree2Transformation)`

**Arguments**:

- **oc1Struct**: a pointer to the OC-tree object.
- **octree1Transformation**: the transformation frame of the OC-tree.
- **oc2Struct**: a pointer to the other OC-tree object.
- **octree2Transformation**: the transformation frame of the other OC-tree.

**Return value**: true if the OC-tree does not contain any voxels anymore, after this operation. false otherwise.

**See also**: [geom_removePointsFromOctree](#geom_removePointsFromOctree), [geom_removeMeshFromOctree](#geom_removeMeshFromOctree), [geom_insertOctreeIntoOctree](#geom_insertOctreeIntoOctree)

### <a id="geom_removePointsFromOctree"></a>geom_removePointsFromOctree

**Description**: Deletes OC-tree voxels that occupy the space of the specified points.

**Synopsis**: `bool geom_removePointsFromOctree(COcStruct* ocStruct,const CPose& octreeTransformation,const double* points,int pointCnt)`

**Arguments**:

- **ocStruct**: a pointer to the OC-tree object.
- **octreeTransformation**: the transformation frame of the OC-tree.
- **points**: an array of point values (XYZ-triplets). Points are expressed relative to the world reference frame.
- **pointCnt**: the number of points.

**Return value**: true if the OC-tree does not contain any voxels anymore, after this operation. false otherwise.

**See also**: [geom_removeMeshFromOctree](#geom_removeMeshFromOctree), [geom_removeOctreeFromOctree](#geom_removeOctreeFromOctree), [geom_insertPointsIntoOctree](#geom_insertPointsIntoOctree)

### <a id="geom_removeOctreeFromPtcloud"></a>geom_removeOctreeFromPtcloud

**Description**: Deletes point-cloud points that occupy the space of the specified OC-tree voxels.

**Synopsis**: `bool geom_removeOctreeFromPtcloud(CPcStruct* pcStruct,const CPose& ptcloudTransformation,const COcStruct* ocStruct,const CPose& octreeTransformation,int* countRemoved=nullptr)`

**Arguments**:

- **pcStruct**: a pointer to the point-cloud object.
- **ptcloudTransformation**: the transformation frame of the point-cloud.
- **ocStruct**: a pointer to the OC-tree object.
- **octreeTransformation**: the transformation frame of the OC-tree.
- **countRemoved**: the number of removed points.

**Return value**: true if the point-cloud does not contain any points anymore, after this operation. false otherwise.

**See also**: [geom_removePointsFromPtcloud](#geom_removePointsFromPtcloud), [geom_insertPointsIntoPtcloud](#geom_insertPointsIntoPtcloud), [geom_intersectPointsWithPtcloud](#geom_intersectPointsWithPtcloud)

### <a id="geom_removePointsFromPtcloud"></a>geom_removePointsFromPtcloud

**Description**: Deletes point-cloud points that occupy the proximity space of the specified points.

**Synopsis**: `bool geom_removePointsFromPtcloud(CPcStruct* pcStruct,const CPose& ptcloudTransformation,const double* points,int pointCnt,double proximityTol,int* countRemoved=nullptr)`

**Arguments**:

- **pcStruct**: a pointer to the point-cloud object.
- **ptcloudTransformation**: the transformation frame of the point-cloud.
- **points**: an array of point values (XYZ-triplets). Points are expressed relative to the world reference frame.
- **pointCnt**: the number of points.
- **proximityTol**: the proximity tolerance.
- **countRemoved**: the number of removed points.

**Return value**: true if the point-cloud does not contain any points anymore, after this operation. false otherwise.

**See also**: [geom_removeOctreeFromPtcloud](#geom_removeOctreeFromPtcloud), [geom_insertPointsIntoPtcloud](#geom_insertPointsIntoPtcloud), [geom_intersectPointsWithPtcloud](#geom_intersectPointsWithPtcloud)

### <a id="geom_scaleMesh"></a>geom_scaleMesh

**Description**: Scales a mesh object.

**Synopsis**: `void geom_scaleMesh(CObbStruct* meshObbStruct,double scalingFactor)`

**Arguments**:

- **meshObbStruct**: a pointer to the mesh object.
- **scalingFactor**: the scaling factor.

### <a id="geom_scaleOctree"></a>geom_scaleOctree

**Description**: Scales an OC-tree object.

**Synopsis**: `void geom_scaleOctree(COcStruct* ocStruct,double scalingFactor)`

**Arguments**:

- **ocStruct**: a pointer to the OC-tree object.
- **scalingFactor**: the scaling factor.

### <a id="geom_scalePtcloud"></a>geom_scalePtcloud

**Description**: Scales a point-cloud object.

**Synopsis**: `void geom_scalePtcloud(CPcStruct* pcStruct,double scalingFactor)`

**Arguments**:

- **pcStruct**: a pointer to the point-cloud object.
- **scalingFactor**: the scaling factor.

### <a id="geom_volumeSensorDetectMeshIfSmaller"></a>geom_volumeSensorDetectMeshIfSmaller

**Description**: Computes the distance from a proximity sensor to parts of a mesh object that lie within the sensor's detection volume.

**Synopsis**: `bool geom_volumeSensorDetectMeshIfSmaller(const double* planesIn,int planesInSize,const double* planesOut,int planesOutSize,const CPose& sensorTransformation,const CObbStruct* obbStruct,const CPose& meshTransformation,double& dist,bool fast=false,bool frontDetection=true,bool backDetection=true,double maxAngle=0.0,C3Vector* detectPt=nullptr,C3Vector* triN=nullptr)`

**Arguments**:

- **planesIn**: an array describing a convex volume, via planes. The mesh object (or parts of it) inside the volume, and outside of volume planesOut, is detected. Each plane is defined by 4 values: (Nx,Ny,Nz,D), where a point (Px,Py,Pz) lies on the inside if N\*P+D>=0. N is the normal vector of the plane, pointing towards the volume inside.
- **planesInSize**: the number of values in the planesIn array.
- **planesOut**: an array describing a convex volume, via planes. The mesh object (or parts of it) outside the volume and inside volume planesIn, is detected. Each plane is defined by 4 values: (Nx,Ny,Nz,D), where a point (Px,Py,Pz) lies on the outside if N\*P+D&lt;0. N is the normal vector of the plane, pointing towards the volume inside. planesOut can be nullptr if planesOutSize is 0.
- **planesOutSize**: the number of values in the planesOut array.
- **sensorTransformation**: the transformation frame of the sensor (also transforms the sensor's volumes).
- **meshObbStruct**: a pointer to the mesh object.
- **meshTransformation**: the transformation frame of the mesh.
- **dist**: the distance threshold as input, and the minimum distance as output if it is below the threshold.
- **fast**: if true, calculation will be faster, however only the first encountered feature that satisfies the detection requirements will be returned (and not the closest of those features).
- **frontDetection**: if true, front faces of the mesh will be detected.
- **backDetection**: if true, back faces of the mesh will be detected.
- **maxAngle**: the maximum allowed angle between detection ray and normal vector of the detected face. Zero to ignore the maximum angle.
- **detectPt**: the position of the detected point, if return value is true.
- **triN**: the normal vector of the detected face, if return value is true.

**Return value**: whether the sensor detected something and the distance is smaller than the specified threshold

**See also**: [geom_volumeSensorDetectOctreeIfSmaller](#geom_volumeSensorDetectOctreeIfSmaller), [geom_volumeSensorDetectPtcloudIfSmaller](#geom_volumeSensorDetectPtcloudIfSmaller), [geom_volumeSensorDetectTriangleIfSmaller](#geom_volumeSensorDetectTriangleIfSmaller), [geom_volumeSensorDetectSegmentIfSmaller](#geom_volumeSensorDetectSegmentIfSmaller), [geom_raySensorDetectMeshIfSmaller](#geom_raySensorDetectMeshIfSmaller), [geom_isPointInVolume](#geom_isPointInVolume), [geom_getMeshPointDistanceIfSmaller](#geom_getMeshPointDistanceIfSmaller)

### <a id="geom_volumeSensorDetectOctreeIfSmaller"></a>geom_volumeSensorDetectOctreeIfSmaller

**Description**: Computes the distance from a proximity sensor to parts of an OC-tree object that lie within the sensor's detection volume.

**Synopsis**: `bool geom_volumeSensorDetectOctreeIfSmaller(const double* planesIn,int planesInSize,const double* planesOut,int planesOutSize,const CPose& sensorTransformation,const COcStruct* ocStruct,const CPose& octreeTransformation,double& dist,bool fast=false,bool frontDetection=true,bool backDetection=true,double maxAngle=0.0,C3Vector* detectPt=nullptr,C3Vector* triN=nullptr)`

**Arguments**:

- **planesIn**: an array describing a convex volume, via planes. The OC-tree object (or parts of it) inside the volume, and outside of volume planesOut, is detected. Each plane is defined by 4 values: (Nx,Ny,Nz,D), where a point (Px,Py,Pz) lies on the inside if N\*P+D>=0. N is the normal vector of the plane, pointing towards the volume inside.
- **planesInSize**: the number of values in the planesIn array.
- **planesOut**: an array describing a convex volume, via planes. The OC-tree object (or parts of it) outside the volume and inside volume planesIn, is detected. Each plane is defined by 4 values: (Nx,Ny,Nz,D), where a point (Px,Py,Pz) lies on the outside if N\*P+D&lt;0. N is the normal vector of the plane, pointing towards the volume inside. planesOut can be nullptr if planesOutSize is 0.
- **planesOutSize**: the number of values in the planesOut array.
- **sensorTransformation**: the transformation frame of the sensor (also transforms the sensor's volumes).
- **ocStruct**: a pointer to the OC-tree object.
- **octreeTransformation**: the transformation frame of the OC-tree.
- **dist**: the distance threshold as input, and the minimum distance as output if it is below the threshold.
- **fast**: if true, calculation will be faster, however only the first encountered feature that satisfies the detection requirements will be returned (and not the closest of those features).
- **frontDetection**: if true, front faces of the OC-tree will be detected.
- **backDetection**: if true, back faces of the OC-tree will be detected.
- **maxAngle**: the maximum allowed angle between detection ray and normal vector of the detected face. Zero to ignore the maximum angle.
- **detectPt**: the position of the detected point, if return value is true.
- **triN**: the normal vector of the detected face, if return value is true.

**Return value**: whether the sensor detected something and the distance is smaller than the specified threshold

**See also**: [geom_volumeSensorDetectMeshIfSmaller](#geom_volumeSensorDetectMeshIfSmaller), [geom_volumeSensorDetectPtcloudIfSmaller](#geom_volumeSensorDetectPtcloudIfSmaller), [geom_volumeSensorDetectTriangleIfSmaller](#geom_volumeSensorDetectTriangleIfSmaller), [geom_volumeSensorDetectSegmentIfSmaller](#geom_volumeSensorDetectSegmentIfSmaller), [geom_raySensorDetectOctreeIfSmaller](#geom_raySensorDetectOctreeIfSmaller), [geom_isPointInVolume](#geom_isPointInVolume), [geom_getOctreePointDistanceIfSmaller](#geom_getOctreePointDistanceIfSmaller)

### <a id="geom_volumeSensorDetectPtcloudIfSmaller"></a>geom_volumeSensorDetectPtcloudIfSmaller

**Description**: Computes the distance from a proximity sensor to parts of a point-cloud object that lie within the sensor's detection volume.

**Synopsis**: `bool geom_volumeSensorDetectPtcloudIfSmaller(const double* planesIn,int planesInSize,const double* planesOut,int planesOutSize,const CPose& sensorTransformation,const CPcStruct* pcStruct,const CPose& ptcloudTransformation,double& dist,bool fast=false,C3Vector* detectPt=nullptr)`

**Arguments**:

- **planesIn**: an array describing a convex volume, via planes. The point-cloud object (or parts of it) inside the volume, and outside of volume planesOut, is detected. Each plane is defined by 4 values: (Nx,Ny,Nz,D), where a point (Px,Py,Pz) lies on the inside if N\*P+D>=0. N is the normal vector of the plane, pointing towards the volume inside.
- **planesInSize**: the number of values in the planesIn array.
- **planesOut**: an array describing a convex volume, via planes. The point-cloud object (or parts of it) outside the volume and inside volume planesIn, is detected. Each plane is defined by 4 values: (Nx,Ny,Nz,D), where a point (Px,Py,Pz) lies on the outside if N\*P+D&lt;0. N is the normal vector of the plane, pointing towards the volume inside. planesOut can be nullptr if planesOutSize is 0.
- **planesOutSize**: the number of values in the planesOut array.
- **sensorTransformation**: the transformation frame of the sensor (also transforms the sensor's volumes).
- **pcStruct**: a pointer to the point-cloud object.
- **ptcloudTransformation**: the transformation frame of the point-cloud.
- **dist**: the distance threshold as input, and the minimum distance as output if it is below the threshold.
- **fast**: if true, calculation will be faster, however only the first encountered feature that satisfies the detection requirements will be returned (and not the closest of those features).
- **detectPt**: the position of the detected point, if return value is true.

**Return value**: whether the sensor detected something and the distance is smaller than the specified threshold

**See also**: [geom_volumeSensorDetectMeshIfSmaller](#geom_volumeSensorDetectMeshIfSmaller), [geom_volumeSensorDetectOctreeIfSmaller](#geom_volumeSensorDetectOctreeIfSmaller), [geom_volumeSensorDetectTriangleIfSmaller](#geom_volumeSensorDetectTriangleIfSmaller), [geom_volumeSensorDetectSegmentIfSmaller](#geom_volumeSensorDetectSegmentIfSmaller), [geom_isPointInVolume](#geom_isPointInVolume), [geom_getPtcloudPointDistanceIfSmaller](#geom_getPtcloudPointDistanceIfSmaller)

### <a id="geom_volumeSensorDetectSegmentIfSmaller"></a>geom_volumeSensorDetectSegmentIfSmaller

**Description**: Computes the distance from a proximity sensor to parts of a segment that lie within the sensor's detection volume.

**Synopsis**: `bool geom_volumeSensorDetectSegmentIfSmaller(const double* planesIn,int planesInSize,const double* planesOut,int planesOutSize,const CPose& sensorTransformation,const C3Vector& segmentEndPoint,const C3Vector& segmentVector,double& dist,double maxAngle=0.0,C3Vector* detectPt=nullptr)`

**Arguments**:

- **planesIn**: an array describing a convex volume, via planes. The segment (or parts of it) inside the volume, and outside of volume planesOut, is detected. Each plane is defined by 4 values: (Nx,Ny,Nz,D), where a point (Px,Py,Pz) lies on the inside if N\*P+D>=0. N is the normal vector of the plane, pointing towards the volume inside.
- **planesInSize**: the number of values in the planesIn array.
- **planesOut**: an array describing a convex volume, via planes. The segment (or parts of it) outside the volume and inside volume planesIn, is detected. Each plane is defined by 4 values: (Nx,Ny,Nz,D), where a point (Px,Py,Pz) lies on the outside if N\*P+D&lt;0. N is the normal vector of the plane, pointing towards the volume inside. planesOut can be nullptr if planesOutSize is 0.
- **planesOutSize**: the number of values in the planesOut array.
- **sensorTransformation**: the transformation frame of the sensor (also transforms the sensor's volumes).
- **segmentEndPoint**: position of vertex A on the segment.
- **segmentVector**: vector stretching from vertex A to vertex B on the segment.
- **dist**: the distance threshold as input, and the minimum distance as output if it is below the threshold.
- **maxAngle**: the maximum allowed angle between detection ray and a perpendicular vector of the segment. Zero to ignore the maximum angle.
- **detectPt**: the position of the detected point, if return value is true.

**Return value**: whether the sensor detected something and the distance is smaller than the specified threshold

**See also**: [geom_volumeSensorDetectMeshIfSmaller](#geom_volumeSensorDetectMeshIfSmaller), [geom_volumeSensorDetectOctreeIfSmaller](#geom_volumeSensorDetectOctreeIfSmaller), [geom_volumeSensorDetectPtcloudIfSmaller](#geom_volumeSensorDetectPtcloudIfSmaller), [geom_volumeSensorDetectTriangleIfSmaller](#geom_volumeSensorDetectTriangleIfSmaller), [geom_isPointInVolume](#geom_isPointInVolume), [geom_getSegmentPointDistanceIfSmaller](#geom_getSegmentPointDistanceIfSmaller)

### <a id="geom_volumeSensorDetectTriangleIfSmaller"></a>geom_volumeSensorDetectTriangleIfSmaller

**Description**: Computes the distance from a proximity sensor to parts of a triangle that lie within the sensor's detection volume.

**Synopsis**: `bool geom_volumeSensorDetectTriangleIfSmaller(const double* planesIn,int planesInSize,const double* planesOut,int planesOutSize,const CPose& sensorTransformation,const C3Vector& p,const C3Vector& v,const C3Vector& w,double& dist,bool frontDetection=true,bool backDetection=true,double maxAngle=0.0,C3Vector* detectPt=nullptr,C3Vector* triN=nullptr)`

**Arguments**:

- **planesIn**: an array describing a convex volume, via planes. The triangle (or parts of it) inside the volume, and outside of volume planesOut, is detected. Each plane is defined by 4 values: (Nx,Ny,Nz,D), where a point (Px,Py,Pz) lies on the inside if N\*P+D>=0. N is the normal vector of the plane, pointing towards the volume inside.
- **planesInSize**: the number of values in the planesIn array.
- **planesOut**: an array describing a convex volume, via planes. The triangle (or parts of it) outside the volume and inside volume planesIn, is detected. Each plane is defined by 4 values: (Nx,Ny,Nz,D), where a point (Px,Py,Pz) lies on the outside if N\*P+D&lt;0. N is the normal vector of the plane, pointing towards the volume inside. planesOut can be nullptr if planesOutSize is 0.
- **planesOutSize**: the number of values in the planesOut array.
- **sensorTransformation**: the transformation frame of the sensor (also transforms the sensor's volumes).
- **p**: position of vertex A on the triangle.
- **v**: vector stretching from vertex A to vertex B on the triangle.
- **w**: vector stretching from vertex A to vertex C on the triangle.
- **dist**: the distance threshold as input, and the minimum distance as output if it is below the threshold.
- **frontDetection**: if true, the front of the triangle will be detected.
- **backDetection**: if true, the back of the triangle will be detected.
- **maxAngle**: the maximum allowed angle between detection ray and normal vector of the triangle. Zero to ignore the maximum angle.
- **detectPt**: the position of the detected point, if return value is true.
- **triN**: the normal vector of the triangle, if return value is true.

**Return value**: whether the sensor detected something and the distance is smaller than the specified threshold

**See also**: [geom_volumeSensorDetectMeshIfSmaller](#geom_volumeSensorDetectMeshIfSmaller), [geom_volumeSensorDetectOctreeIfSmaller](#geom_volumeSensorDetectOctreeIfSmaller), [geom_volumeSensorDetectPtcloudIfSmaller](#geom_volumeSensorDetectPtcloudIfSmaller), [geom_volumeSensorDetectSegmentIfSmaller](#geom_volumeSensorDetectSegmentIfSmaller), [geom_isPointInVolume](#geom_isPointInVolume), [geom_getTrianglePointDistanceIfSmaller](#geom_getTrianglePointDistanceIfSmaller)
