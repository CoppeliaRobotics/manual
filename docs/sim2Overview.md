# sim-2

`sim-2` was introduced in CoppeliaSim V4.11 and is an object-oriented version of the CoppeliaSim API, entirely based on properties and methods. The following compares a simple example in sim-1:

```lua
sim = require('sim-1')

local robotHandle = sim.getObject('/robot')
local obstacleHandle = sim.getObject('/obstacle')
local worldPos = sim.getObjectPosition(robotHandle)
local relPos = sim.getObjectPosition(robotHandle, obstacleHandle)
local collectionHandle = sim.createCollection()
sim.addItemToCollection(collectionHandle, sim.handle_tree, robotHandle, 0)
local result, objPair = sim.checkCollision(collectionHandle, sim.handle_all)
if result then
    print('Following objects collide: ' ..
          sim.getObjectAlias(objPair[1], 5) ..
          ' with ' .. sim.getObjectAlias(objPair[2], 5))
end
```

and sim-2:

```lua
import 'sim-2'

local robot = sim.self:getObject('/robot')
local obstacle = sim.self:getObject('/obstacle')
local worldPos = robot.worldPosition
local relPos = robot:getPosition({relativeToObject = obstacle})
local collection = sim.scene:createObject({type = 'collection'})
collection:addItem(robot, {mode = 'tree'})
local result, objPair = collection:checkCollision()
if result then
    print('Following objects collide: ' ..
          objPair[1]:getName({mode = 'printPath'}) ..
          ' with ' .. objPair[2]:getName({mode = 'printPath'}))
end
```

`sim-2` is meant to replace `sim-1`; `sim-1` is declared deprecated and you should favor `sim-2` over `sim-1`. One may however use `sim-1` and `sim-2` in the same script, as shown in the following example:

```lua
import 'sim-2'
sim1 = require 'sim-1'

local robot = sim.self:getObject('/robot')
local worldPos = sim1.getObjectPosition(robot.handle)</code>
```

All objects derive from a common base class [object](apiFunctions.md#methodsAndProperties_object), as can be seen from the [class overview](mainObjectTypes.md). [`sim.app`](apiFunctions.md#methodsAndProperties_app) (a singleton) refers to the running CoppeliaSim instance, whereas [`sim.scene`](apiFunctions.md#methodsAndProperties_scene), also a singleton, refers to the current scene. From within a [script](scripts.md), [`sim.self`](apiFunctions.md#methodsAndProperties_script) points to the script itself.

This user manual was adjusted to reflect the usage of `sim-2`.
