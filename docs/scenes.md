# Scenes

Compared to [models](models.md), a scene can contain exactly the same type of elements, but additionally also includes the following elements, specific to scenes:

- [The environment](environment.md)
- [The main script](mainScript.md)
- [Pages and views](pagesAndViews.md)

A scene or scene image content can be seen through a [viewable object](viewableObjects.md) associated with a view, itself contained in a [page](pagesAndViews.md). When creating a new scene ([File > New Scene]), the default scene contains the following elements:

- Several [cameras](cameras.md) to display the scene (or parts of it).
- Several [lights](lights.md) to illuminate the scene.
- Several [views](pagesAndViews.md) to display what cameras *see*. Views are contained in pages.
- Several [pages](pagesAndViews.md) containing one or several views.
- [The environment](environment.md) holding properties such as ambient light, background color, etc.
- The floor, made up by [shapes](shapes.md) grouped in a model.
- The default [main script](mainScript.md) running code required by every scene. It is in charge of handling sensors, calling simulation and customization scripts, etc.

Scenes can be opened with [File > Open Scene...] and saved with [File > Save Scene] or [File > Save Scene as]. Scene files (*\*.ttt* files) also support drag and drop operations between the explorer window and the application window. They can also be double-clicked, in which case they will launch the CoppeliaSim application and be opened. Refer also to [sim.app:loadScene](sim/app_loadScene.htm), [sim.scene:remove](sim/scene_remove.htm).
