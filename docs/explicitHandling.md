# Explicit and non-explicit calls

Some objects, such as [proximity sensors](proximitySensors.md) or [vision sensors](visionSensors.md), normally require *handling* or calculations to be performed once per simulation step, to reflect a possible change in the scene. This handling can be done implicitly or explicitly, and those objects have a special setting related to that: an **explicit handling** flag. See also [`proximitySensor.explicitHandling`](sim-2/property_proximitySensor_explicitHandling.md) and [`visionSensor.explicitHandling`](sim-2/property_visionSensor_explicitHandling.md). By default that flag is unchecked, which means that the object is implicitly handled via the [main script](mainScript.md). Indeed the following main script code is executed and handles said objects once per simulation step:

```
-- lua
-- using lua-2

local proxSensors = sim.scene:getObjects({types = {'proximitySensor'}})
for i = 1, #proxSensors do
    local s = proxSensors[i]
    if not s.explicitHandling then
        s:handleSensor()
    end
end
```

The above code performs proximity sensor computations, and any other script can then read the up-to-date calculation results with e.g.:

```
-- lua

function sysCall_init()
    sim = require('sim-2')
    sensor = sim.self:getObject('/proximitySensor')
end

function sysCall_sensing()
    if sensor.detectedObject then
        print('Detected object: ' .. tostring(sensor.detectedObject))
        print('Detected distance: ' .. tostring(sensor.detectedDistance))
        print('Detected point: ' .. tostring(sensor.detectedPoint))
        print('Detected normal: ' .. tostring(sensor.detectedNormal))
    end
end
```

The above code, unlike the previous, does not compute anything, but just reads the calculation result. This is very convenient when calculations need to happen exactly once per simulation step and/or the calculation result is required by several scripts.

If, however, an object requires less or more frequent calculations (e.g. several calculations within a same simulation step), then the above mechanism does not work. In that case, the object should be flagged as **explicit handling**: from that moment on, the main script does not handle that object anymore, and it is the responsibility of another script to do this. For instance if the proximity sensor should only be handled once every other simulation step, a [simulation script](simulationScripts.md) could include the following code:

```lua
--lua

function sysCall_init()
    sim = require('sim-2')
    sensor = sim.self:getObject('/proximitySensor')
end

function sysCall_sensing()
    handleSensor = not handleSensor
    if handleSensor then
        sensor:handleSensor()
    end
end
```

If new calculations need to be performed several times within a same simulation step (e.g. because an object or the sensor itself is moved more frequently), you could write:

```lua
--lua

function sysCall_init()
    sim = require('sim-2')
    sensor = sim.self:getObject('/proximitySensor')
end

function sysCall_sensing()
    for i = 1, 10 do
        local pos = sensor.worldPosition
        pos[3] = i / 10
        sensor.worldPosition = pos -- e.g. move the sensor
        sensor:handleSensor()
    end
end
```
