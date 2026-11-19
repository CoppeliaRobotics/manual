# Trigger callback functions

[Script objects](scriptObjects.md) can include a trigger callback function (which is one of many [system callback functions](callbackFunctions.md#systemCallbacks)), when the script object parent is a [vision sensor](visionSensors.md), a [proximity sensor](proximitySensors.md), or a [force sensor](forceSensors.md).

A vision sensor can generate the trigger signal inside of the [vision callback function](visionCallbackFunctions.md). The trigger callback (if present) is then called as in the following example:

```lua
--lua
    
    function sysCall_trigger(inData)
    -- We have:
    -- inData.visionSensor : the vision sensor.
    -- inData.packedPackets : an array of data packets, packed (use sim.app:unpackArray to unpack to doubles)
    --    the first data packet always contains 15 auxiliary values about the acquired image:
    --    - minimum of {intensity, red, green blue and depth value}
    --    - maximum of {intensity, red, green blue and depth value}
    --    - average of {intensity, red, green blue and depth value}
    
    local outData = {}
    outData.trigger = true
    return outData
    end
```

A proximity sensor generates the trigger signal when an object is detected. The trigger callback (if present) is then called as in the following example:

```lua
--lua

function sysCall_trigger(inData)
    -- We have:
    -- inData.proximitySensor : the proximity sensor.
    -- inData.object : detected object
    -- inData.distance : detected distance
    -- inData.point : detected point, relative to sensor frame
    -- inData.normal : normal vector at detected point, relative to sensor frame

    local outData = {}
    outData.trigger = true
    return outData
end
```

A force sensor generates the trigger signal when the sensor trigger conditions are met. The trigger callback (if present) is then called as in the following example:

```lua
--lua

function sysCall_trigger(inData)
    -- We have:
    -- inData.forceSensor : the force sensor.
    -- inData.forceVector : the force vector
    -- inData.torqueVector : the torque vector
    -- inData.filteredForceVector : the filtered force vector
    -- inData.filteredTorqueVector : the filtered torque vector
    --
    -- The callback does not expect a return value
end
```
