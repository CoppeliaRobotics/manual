# ROS Interfaces

There is a [ROS interface](rosInterf.md) and a [ROS2 interface](ros2Interface.md) available for CoppeliaSim, both duplicating the C++ ROS/ROS2 API with good fidelity. They are implemented via the [simROS plugin](https://github.com/CoppeliaRobotics/simROS) and [simROS2 plugin](https://github.com/CoppeliaRobotics/simROS2). Use the [catkin tools](http://catkin-tools.readthedocs.io/en/latest/) to build those packages, otherwise you might run into difficulties.

As an example, a [vision sensor](visionSensors.md) ROS2 publisher could look like:

```lua
import 'sim-2'
import 'simROS'

function sysCall_init()
    visionSensor = sim.self:getObject('/Vision_sensor')

    -- Enable an image publisher:
    pub = simROS2.createPublisher('/image', 'sensor_msgs/msg/Image')
    simROS2.publisherTreatUInt8ArrayAsString(pub)
end

function sysCall_sensing()
    -- Publish the image of the vision sensor:
    local img = visionSensor.image
    local resolution = visionSensor.resolution
    local data = {}
    data.header = {stamp = simROS2.getTime(), frame_id = 'a'}
    data.height = resolution[2]
    data.width = resolution[1]
    data.encoding = 'rgb8'
    data.is_bigendian = 1
    data.step = resolution[1] * 3
    data.data = img
    simROS2.publish(pub, data)
end

function sysCall_cleanup()
    simROS2.shutdownPublisher(pub)
end
```

The subscriber on the other hand could look like:

```lua
import 'sim-2'
import 'simROS'

function sysCall_init()
    -- Enable an image subscriber:
    sub = simROS2.createSubscription('/image', 'sensor_msgs/msg/Image', 'image_callback')
    simROS2.subscriptionTreatUInt8ArrayAsString(sub)
end

function image_callback(msg)
    -- Here we have received an image
end

function sysCall_cleanup()
    simROS2.shutdownSubscription(sub)
end
```

Have a look at the [ROS tutorial](rosTutorial.md) and the [external controller tutorial](externalControllerTutorial.md).
