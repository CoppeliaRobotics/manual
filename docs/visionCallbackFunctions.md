# Vision callback functions

[Script objects](scriptObjects.md) can include a vision callback function (which is one of many [system callback functions](callbackFunctions.md#systemCallbacks)), when the script object parent is a [vision sensor](visionSensors.md). When present, then the system calls the callback function every time a new image was acquired or applied, allowing the user to perform image processing. This is the case with the following: [visionSensor:handleSensor](sim/visionSensor_handleSensor.htm), [visionSensor:checkSensor](sim/visionSensor_checkSensor.htm), [visionSensor:setImage](sim/visionSensor_setImage.htm) and [visionSensor.image](sim/property_visionSensor_image.htm).

The following represents an empty vision callback function:

```python
#python
# using sim-2

def sysCall_vision(inData):
    # We have:
    # inData['sensor'] : the vision sensor.
    # inData['resolution'] : the x/y resolution of the vision sensor
    # inData['clippingPlanes'] : the near and far clipping planes of the vision sensor
    # inData['viewAngle'] : the view angle of the vision sensor (if in persp. proj. mode)
    # inData['orthoSize'] : the ortho size of the vision sensor (if in orth. proj. mode)
    # inData['perspective'] : True if the sensor is in persp. proj. mode

    outData = {}
    outData['trigger'] = False  # True if the sensor should trigger
    outData['packedPackets'] = []  # a list of packed packets (packed as single precision floats).
                                   # Can be accessed via e.g. visionSensor.packet1, visionSensor.packet2
    return outData
```

```lua
--lua
-- using sim-2

function sysCall_vision(inData)
    -- We have:
    -- inData.sensor : the vision sensor.
    -- inData.resolution : the x/y resolution of the vision sensor
    -- inData.clippingPlanes : the near and far clipping planes of the vision sensor
    -- inData.viewAngle : the view angle of the vision sensor (if in persp. proj. mode)
    -- inData.orthoSize : the ortho size of the vision sensor (if in orth. proj. mode)
    -- inData.perspective : true if the sensor is in persp. proj. mode

    local outData = {}
    outData.trigger = false -- true if the sensor should trigger
    outData.packedPackets = {} -- a table of packed packets (packed as single precision floats). 
                               -- Can be accessed via e.g. visionSensor.packet1, visionSensor.packet2
    return outData
end
```

Image processing can be performed by using various API functions. The [vision plugin](syntheticVision.md) exports a few very simple image processing functions. Many more image processing functions are supported via the [image plugin](simIM/simIM.htm) (OpenCV wrapper).

The following represents a simple edge detection vision callback function, that triggers and returns a packet of data (based on the vision plugin functions):

```python
#python
# using sim-2

import struct

def sysCall_vision(inData):
    simVision.sensorImgToWorkImg(inData['sensor.handle'])
    simVision.edgeDetectionOnWorkImg(inData['sensor.handle'], 0.1)
    simVision.workImgToSensorImg(inData['sensor.handle'])

    outData = {}
    outData['trigger'] = True
    packetData = [1.0, 42.123, 129.3]
    outData['packedPackets'] = [struct.pack('ff', *packetData)]
    return outData
```

```lua
--lua
-- using sim-2

function sysCall_vision(inData)
    simVision.sensorImgToWorkImg(inData.sensor.handle)
    simVision.edgeDetectionOnWorkImg(inData.sensor.handle, 0.1)
    simVision.workImgToSensorImg(inData.sensor.handle)

    local outData = {}
    outData.trigger = true
    local packetData = {1.0, 42.123, 129.3}
    outData.packedPackets = {sim.app:packArray(packetData, {type = 'float'})}
    return outData
end
```

The following represents a vision callback function, that draws a circle onto the acquired image (based on the image plugin functions):

```python
#python
# using sim-2

def sysCall_vision(inData):
    imgHandle = simIM.readFromVisionSensor(inData['sensor.handle'])
    center = [inData['resolution'][0] / 2, inData['resolution'][1] / 2]
    radius = (inData['resolution'][0] + inData['resolution'][1]) / 8
    simIM.circle(imgHandle, center, radius, [255, 0, 255], 4)
    simIM.writeToVisionSensor(imgHandle, inData['sensor.handle'])
    simIM.destroy(imgHandle)
```

```lua
--lua
-- using sim-2

function sysCall_vision(inData)
    local imgHandle = simIM.readFromVisionSensor(inData.sensor.handle)
    local center = {inData.resolution[1] / 2, inData.resolution[2] / 2}
    local radius = (inData.resolution[1] + inData.resolution[2]) / 8
    simIM.circle(imgHandle, center, radius, {255, 0, 255}, 4)
    simIM.writeToVisionSensor(imgHandle, inData.sensor.handle)
    simIM.destroy(imgHandle)
end
```
