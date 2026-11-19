# Geometric Plugin

Performing [collision detection](collisionDetection.md) and [distance calculation](distanceCalculation.md) is easily handled via dedicated [scene object](objects.md) or [collection](collections.md) methods, e.g. such as [sceneObject:checkCollision](sim/sceneObject_checkCollision.htm), [collection:checkCollision](sim/collection_checkCollision.htm), [sceneObject:checkDistance](sim/sceneObject_checkDistance.htm) and [collection:checkDistance](sim/collection_checkDistance.htm).

The same functionality is however also available at a lower level, via the geometric plugin, and allows you to perform the same kind of calculations, but in an independent manner from CoppeliaSim scene objects, e.g. you are able to create mesh, OC-tree and point cloud data structures and perform collision detection or distance calculations on them, without having to create scene content. This works by directly interacting with the [geometric plugin's API](simGeom.htm).
