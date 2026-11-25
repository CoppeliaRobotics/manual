# Measurable objects

Measurable objects are [scene objects](objects.md) that can be used for [minimum distance calculation](distanceCalculation.md) against other measurable objects. They include:

- [Dummies](dummies.md)
- [Shapes](shapes.md)
- [OC trees](octrees.md)
- [Point clouds](pointClouds.md)

Measurable objects can have their *measurable property* individually enabled or disabled. This can be set in the [scene object common properties](sceneObjectPropertiesDialog.md#common) or through [`sceneObject.measurable`](sim-2/property_sceneObject_measurable.htm).

[Collections](collections.md) are also measurable, since they might contain measurable objects.

Additionally, measurable objects can have their *measurable property* overridden depending on their related *model properties* (if they are part of a [model](models.md)). Refer to the [model dialog](modelDialog.md) and see also [`sceneObject.model.notMeasurable`](sim-2/property_sceneObject_model_notMeasurable.htm).
