# Environment

The environment in CoppeliaSim defines properties and parameters that are part of a [scene](scenes.md), but that are not [scene objects](objects.md). Environment properties and parameters are not saved when a [model](models.md) is saved, but only when a scene is saved.

An environment defines the following properties and parameters:

- Background colors.
- Fog parameters. Fog parameters do not directly interact with scene objects, except with [cameras](cameras.md) or [vision sensors](visionSensors.md) if the corresponding option was selected.
- Ambient light. Refer also to [`scene.ambientLight`](sim-2/property_scene_ambientLight.htm).
- Scene creation information. Refer also to [`scene.acknowledgment`](sim-2/property_scene_acknowledgment.htm).
- Additional settings
