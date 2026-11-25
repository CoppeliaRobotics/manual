# Collidable objects

Collidable objects are [scene objects](objects.md) that can be tested for [collision](collisionDetection.md) against other collidable objects. Testing for collision does not induce a collision response. Collidable objects include:

- [Dummies](dummies.md)
- [Shapes](shapes.md)
- [OC trees](octrees.md)
- [Point clouds](pointClouds.md)

Dummies and point clouds can only be tested for collision against OC trees (which are volume-based).

Collidable objects can have their *collidable property* individually enabled or disabled. This can be set in the [scene object common properties](sceneObjectPropertiesDialog.md#common) or through [`sceneObject.collidable`](sim-2/property_sceneObject_collidable.md).

[Collections](collections.md) are also collidable, since they might contain collidable objects.

Additionally, collidable objects can have their *collidable property* overridden depending on their related *model properties* (if they are part of a [model](models.md)). Refer to the [model dialog](modelDialog.md) and see also [`sceneObject.model.notCollidable`](sim-2/property_sceneObject_model_notCollidable.md).
