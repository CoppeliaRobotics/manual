# Detectable objects

Detectable objects are [scene objects](objects.md) that can be detected by [proximity sensors](proximitySensors.md). They include:

- [Dummies](dummies.md)
- [Shapes](shapes.md)
- [OC trees](octrees.md)
- [Point clouds](pointClouds.md)

Dummies and point clouds cannot be detected by ray-type or randomized-type proximity sensors.

Detectable objects can have their *detectable property* individually enabled or disabled. This can be set in the [scene object common properties](sceneObjectPropertiesDialog.md#common) or through [`sceneObject.detectable`](sim-2/property_sceneObject_detectable.md).

[Collections](collections.md) are also detectable, since they might contain detectable objects.

Additionally, detectable objects can have their *detectable property* overridden depending on their related *model properties* (if they are part of a [model](models.md)). Refer to the [model dialog](modelDialog.md) and see also [`sceneObject.model.notDetectable`](sim-2/property_sceneObject_model_notDetectable.md).
