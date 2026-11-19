# Accessing scene objects programmatically

When programming in and around CoppeliaSim, you will always need to reference [scene objects](objects.md). You do this via [script:getObject](sim/script_getObject.htm) or [sceneObject:getObject](sim/sceneObject_getObject.htm), which expect an object path as input argument. The object path can be expressed in an absolute manner, but also in a relative manner when called from a [script object](#fromScriptObject).

In both cases, the path to the object can often be simplified. You may also use wildcards, and optionally specify the object sequence or order, in a given scene hierarchy. Or simply fetch the n-th object that matches a specific path/name. See also [sceneObject.name](sim/property_sceneObject_name.htm) and [sceneObject:getName](sim/sceneObject_getName.htm).

## <a id="fromUnassociatedCode"></a>Access from *unassociated* code

*Unassociated* code is code that is not from a [script object](scriptObjects.md). This includes all the code written for [plugins](plugins.md), [add-ons](addOns.md), [remote API](remoteApiOverview.md) clients, external [ROS](rosInterfaces.md) nodes, and [the main script](mainScript.md).

In that case, you simply specify the object's **absolute** path, to retrieve it:

```cpp
// e.g. from within a c/c++ plugin:

// using the full object path:
int objectHandle = simGetObject("/path/to/object", -1, -1, 0);

// if the object has a unique name:
int objectHandle = simGetObject("/objectName", -1, -1, 0);

// handle of the first object with a specific name, in a given hierarchy level:
int robotHandle = simGetObject("/objectName[0]", -1, -1, 0);

// handle of the second object with a specific name, in a given hierarchy level:
int robotHandle = simGetObject("/objectName[1]", -1, -1, 0);

// handle of the fifth object with a specific name, in the scene:
int robotHandle = simGetObject("/objectName{4}", -1, -1, 0);
// or
int robotHandle = simGetObject("/objectName", 4, -1, 0);

// find all objects starting with a specific prefix:
int i = 0;
while (true)
{
    int objectHandle = simGetObject("/Mobile*", i++, -1, 1);
    if (objectHandle < 0)
        break;
}
```

```python
# e.g. from within a Python ZeroMQ remote API 2 client:

# using the full object path:
object = sim.scene.getObject("/path/to/object")

# if object has a unique name:
object = sim.scene.getObject("/objectName")

# the first object with a specific name, in a given hierarchy level:
object = sim.scene.getObject("/objectName[0]")

# the second object with a specific name, in a given hierarchy level:
object = sim.scene.getObject("/objectName[1]")

# the fifth object with a specific name, in the scene:
object = sim.scene.getObject("/objectName{4}")
```

## <a id="fromScriptObject"></a><a id="fromAssociatedCode"></a>Access from a script object (i.e. from *associated* code)

*Associated* code is code that runs in a [script object](scriptObjects.md), i.e. code that runs in a [simulation-](simulationScripts.md) or [customization script](customizationScripts.md).

In that case, in addition to accessing objects in an **absolute** manner as described above, you can also access them in a **relative** manner (relative to the current script object (*./* ), or relative to the model containing the current script (*:/*)):

```python
#python
# using sim-2
# from within a simulation- or customization script

# returns the current script object:
object = sim.self:getObject(".")

# returns the parent of this script:
parent = sim.self:getObject("..")

# returns the model this script is contained in:
model = sim.self:getObject(":")

# returns the parent model this script is contained in:
parentModel = sim.self:getObject("::")

# returns the first object in the current hierarchy, that starts with Object:
object = sim.self:getObject("./Object*")

# returns the first object with name Object, in the current model hierarchy:
object = sim.self:getObject(":/Object")

# returns the 4th object with name Leg, within a same hierarchy level, in the current model hierarchy:
leg = sim.self:getObject(":/Leg[3]")

# returns the 5th object with name Leg, in the current model hierarchy:
leg = sim.self:getObject(":/Leg{4}")

# parse through all Leg objects in the current model hierarchy:
i = 0
while True:
    leg = sim.self:getObject(":/Leg", {'index': i, 'noError': True})
    if leg == None:
        break
    i = i + 1
```

```lua
--lua

# from within a simulation- or customization script:
sim = require('sim-2')

-- returns the current script:
object = sim.self:getObject(".")

-- returns the parent of this script:
parent = sim.self:getObject("..")

-- returns the model this script is contained in:
model = sim.self:getObject(":")

-- returns the parent model this script is contained in:
parentModel = sim.self:getObject("::")

-- returns the first object in the current hierarchy, that starts with Object:
object = sim.self:getObject("./Object*")

-- returns the first object with name Object, in the current model hierarchy:
object = sim.self:getObject(":/Object")

-- returns the 4th object with name Leg, within a same hierarchy level, in the current model hierarchy:
leg = sim.self:getObject(":/Leg[3]")

-- returns the 5th object with name Leg, in the current model hierarchy:
leg = sim.self:getObject(":/Leg{4}")

-- parse through all Leg objects in the current model hierarchy:
local i = 0
while true do
    local leg = sim.self:getObject(":/Leg", {index = i, noError = true})
    if legHandle == nil then
        break
    end
    i = i + 1
end
```
