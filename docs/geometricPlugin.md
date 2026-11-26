# Geometric Plugin

Performing [collision detection](collisionDetection.md) and [distance calculation](distanceCalculation.md) is easily handled via dedicated [scene object](objects.md) or [collection](collections.md) methods, e.g. such as [`sceneObject:checkCollision`](sim-2/sceneObject_checkCollision.md), [`collection:checkCollision`](sim-2/collection_checkCollision.md), [`sceneObject:checkDistance`](sim-2/sceneObject_checkDistance.md) and [`collection:checkDistance`](sim-2/collection_checkDistance.md).

The same functionality is however also available at a lower level, via the geometric plugin, and allows you to perform the same kind of calculations, but in an independent manner from CoppeliaSim scene objects, e.g. you are able to create mesh, OC-tree and point cloud data structures and perform collision detection or distance calculations on them, without having to create scene content. This works by directly interacting with the [geometric plugin's API](simGeom/simGeom.md).
