# Properties

In CoppeliaSim, all internal variables or states can be handled as properties: those can be queried or modified via [dedicated API functions](apiFunctions.md#properties).

Properties relate to an [object](mainObjectTypes.md#object), e.g. sim.app, sim.scene, sim.self, a script instance, a sceneObject instance:

```python
import sim

sim.app.paths.settings # get location of user settings file usrset.txt
sim.scene.dynamics.gravity # set zero-gravity
jointObject.bounds # get joint lower and upper limits
shapeObject.meshes # get meshes composing the shape
meshObject.vertices # get vertices of a mesh
```

```lua
import 'sim-2'

sim.app.paths.settings -- get location of user settings file usrset.txt
sim.scene.dynamics.gravity -- set zero-gravity
jointObject.bounds -- get joint lower and upper limits
shapeObject.meshes -- get meshes composing the shape
meshObject.vertices -- get vertices of a mesh
```

[This page lists all available properties and methods](apiFunctions.md#methodsAndProperties). A property is usually readable and writable, but depending on the property, it can also be read-only or write-only. Other properties can be removable, are constant, etc.:

```python
import sim

shapeObject.meshes # read-only property
shapeObject.applyColor.diffuse = [1, 0, 0, 1] # write-only property
sceneObject.removeProperty('customData.myFloatArray') # removable property
```

```lua
import 'sim-2'

shapeObject.meshes -- read-only property
shapeObject.applyColor.diffuse = Color('red') -- write-only property
sceneObject:removeProperty('customData.myFloatArray') -- removable property
```

Properties can conveniently be inspected via the Property Explorer add-on located at [Modules > Developer tools > Property explorer].

Most properties, when changed (explicitly or internally by CoppeliaSim), trigger an event, [which can be listened to via an event callback function](meansOfCommunication.md#events).

The following are particular types of properties:

- [Custom data](#customData)
- [signals](#signals)
- [Named parameters](#namedParams)

## <a id="customData"></a>Custom data

Custom data properties can be seen as persistent data (stored in an object, sometimes also to disk) with different scopes: globally (i.e., sim.app (stored to disk), within the current scene (sim.scene), or locally, specific to a scene object. Custom data properties are identified with a *customData.*-prefix, and they can be created/set, modified and removed. For example:

```python
import sim

# script 1 writes the data to a scene object:

myData = [1, 2, ["Hello", "world", True, {"value1": 63, "value2": "aString"}]]
sceneObject.customData.myTag = sim.app.pack(myData)
sceneObject.setBufferProperty('customData.myTag', myData) # same effect as above, but by using the related method
```

```lua
import 'sim-2'

-- script 1 writes the data to a scene object:

local myData = {1, 2, {"Hello", "world", true, {value1 = 63, value2 = "aString"}}}
sceneObject.customData.myTag = sim.app:pack(myData)
sceneObject:setBufferProperty('customData.myTag', myData) -- same effect as above, but by using the related method
```

```python
import sim

# script 2 reads the data from the scene object:

myData = sceneObject.customData.myTag
if myData:
    myData = sim.app.unpack(myData)
    # do something with the data
```

```lua
import 'sim-2'

-- script 2 reads the data from the scene object:

local myData = sceneObject.customData.myTag
if myData then
    myData = sim.app:unpack(myData)
    -- do something with the data
end
```

Unlike signals, custom data is not volatile nor removed if the script state that created/modified it is destroyed.

## <a id="signals"></a>Signals

Signal properties can be seen as variables with different scopes: globally (i.e., sim.app), within the current scene (sim.scene), or locally, specific to a scene object. Signal properties are identified with a *signal.*-prefix, and they can be created/set, modified and removed. For example:

```python
import sim

# script 1 writes the data to int signal 'myIntSignal':

sim.scene.signal.myIntSignal = 37
sim.scene.setIntProperty('signal.myIntSignal', 37) # same effect as above, but by using the related method
```

```lua
import 'sim-2'

-- script 1 writes the data to int signal 'myIntSignal':

sim.scene.signal.myIntSignal = 37
sim.scene:setIntProperty('signal.myIntSignal', 37) -- same effect as above, but by using the related method
```

```python
import sim

# script 2 reads the data from int signal 'myIntSignal':

myData = sim.scene.signal.myIntSignal
if myData != None:
    # do something with the data
```

```lua
import 'sim-2'

-- script 2 reads the data from int signal 'myIntSignal':

local myData = sim.scene.signal.myIntSignal
if myData then
    -- do something with the data
end
```

If the script state that created/modified a signal is destroyed, then that signal is automatically removed.

## <a id="namedParams"></a>Named parameters

Named parameters are volatile string properties related to CoppeliaSim in general (i.e. the target object is always sim.app). Named parameters are usually [user settings](commandLine.md#settingsFile), or user arguments set via the -G [command line](commandLine.md#commandLine) switch. For instance:

```python
import sim

arg = sim.app.namedParam.myCustomArgument
```

```lua
import 'sim-2'

local arg = sim.app.namedParam.myCustomArgument
```
