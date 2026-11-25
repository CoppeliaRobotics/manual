# OC trees

An OC-tree is an instance of the [ocTree type](mainObjectTypes.md#ocTree), which in turn derives from the [sceneObject type](mainObjectTypes.md#sceneObject). It represents a spacial partitioning. It is made up of a tree data structure in which each node has exactly eight children. Occupied leaf nodes are represented as voxels. OC trees can be used to offer a simplified representation for [shapes](shapes.md) or [point clouds](pointClouds.md), or can act as an occupancy grid/space:

![](images/octrees2.jpg)

*[OC tree]*

OC trees are [collidable](collidableObjects.md), [measurable](measurableObjects.md) and [detectable objects](detectableObjects.md). This means that OC trees:

- Can be used in [collision detections](collisionDetection.md) with other collidable objects.
- Can be used in [minimum distance calculations](distanceCalculation.md) with other measurable objects.
- Can be detected by [proximity sensors](proximitySensors.md).

Refer also to [`sceneObject.collidable`](sim-2/property_sceneObject_collidable.md), [`sceneObject.measurable`](sim-2/property_sceneObject_measurable.md) and [`sceneObject.detectable`](sim-2/property_sceneObject_detectable.md).

OC trees can be added to the [scene](scenes.md) with [Add > OC tree], and edited via the [OC tree dialog](octreePropertiesDialog.md). Refer also to [`sim.scene:createObject`](sim-2/scene_createObject.md) and [ocTree-related methods and properties](apiFunctions.md#methodsAndProperties_ocTree).

The OC tree calculations (i.e. collision, distance and proximity sensor calculations) available in CoppeliaSim are also available as stand-alone routines via the [Coppelia geometric routines](coppeliaGeometricRoutines.md). See also [`sceneObject:checkCollision`](sim-2/sceneObject_checkCollision.md), [`collection:checkCollision`](sim-2/collection_checkCollision.md), [`sceneObject:checkDistance`](sim-2/sceneObject_checkDistance.md), [`collection:checkDistance`](sim-2/collection_checkDistance.md) and [`proximitySensor:checkSensor`](sim-2/proximitySensor_checkSensor.md).
