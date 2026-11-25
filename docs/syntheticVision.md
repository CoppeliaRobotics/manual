# Synthetic vision

Synthetic vision is achieved in CoppeliaSim via [vision sensors](visionSensors.md): they can perform offscreen rendering of the scene in different modes. The generated image can then be modified/processed in various ways, for instance from within a [vision callback function](visionCallbackFunctions.md):

- [Image processing with OpenCV](simIM/simIM.md) (via the [image plugin](https://github.com/CoppeliaRobotics/simIM))
- [Simple image processing](simVision/simVision.htm) via the [vision plugin](https://github.com/CoppeliaRobotics/simVision)
- [`sim.app:transformImage`](sim-2/app_transformImage.md)
- [`sim.app:transformBuffer`](sim-2/app_transformBuffer.md)

The following shows a vision callback function that illustrates 3 different ways to modify an acquired image:

```lua
--lua

function sysCall_init()
    sim = require('sim-2')
    simVision = require('simVision')
    simIM = require('simIM')
end

function sysCall_vision(inData)
    -- inData.sensor: the vision sensor
    -- inData.resolution: resolution of the vision sensor
    -- inData.clippingPlanes: near and far clipping plane of the vision sensor
    -- inData.viewAngle: the view angle if the vision sensor is in perspective operation
    -- inData.orthoSize: the size of the view if the vision sensor is in orthogonal operation
    -- inData.perspective: whether the vision sensor is in perspective operation

    -- e.g. use very simple functions from the vision plugin (simVision):
    simVision.sensorImgToWorkImg(inData.sensor.handle)
    simVision.edgeDetectionOnWorkImg(inData.sensor.handle, 0.2)
    simVision.swapWorkImgWithBuffer1(inData.sensor.handle)
    simVision.uniformImgToWorkImg(inData.sensor.handle, {0.5, 0.25, 0})
    simVision.addBuffer1ToWorkImg(inData.sensor.handle)
    simVision.workImgToSensorImg(inData.sensor.handle)

    -- and/or, use more powerful functions from the image plugin (simIM):
    local imgHandle = simIM.readFromVisionSensor(inData.sensor.handle)
    local center = {inData.resolution[1] / 2, inData.resolution[2] / 2}
    local radius = (inData.resolution[1] + inData.resolution[2]) / 8
    simIM.circle(imgHandle, center, radius, {255, 255, 0}, 4)
    simIM.writeToVisionSensor(imgHandle, inData.sensor.handle)
    simIM.destroy(imgHandle)

    -- Or you can directly operate on the image buffer:
    local image = inData.sensor.image
    image = sim.app:transformImage(image, inData.resolution, inData.resolution, {flipAxisY = true})
    image = sim.app:transformBuffer(image, 'rgb', 'bgr')
    inData.sensor.image = image

    outData = {}
    outData.trigger = true -- whether the sensor should trigger
    -- filters may append packets (in packed form, use sim.packFloatTable to pack) to this table:
    outData.packedPackets = {sim.app:packArray({1, 42, 57}, {type = 'float'})}
    return outData
end
```

Refer also to [`sim.scene:createObject`](sim-2/scene_createObject.md) and [vision sensor-related methods and properties](apiFunctions.md#methodsAndProperties_visionSensor).
