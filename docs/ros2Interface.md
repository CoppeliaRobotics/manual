# ROS2 Interface

The ROS 2 Interface is part of the [CoppeliaSim API framework](apisOverview.md). It duplicates the C++ ROS 2 API with a good fidelity. This makes it the ideal choice for very flexible communication via ROS2. You can recognize ROS2 Interface API functions from the *simROS2*- prefix.

ROS2 is a distributed pseudo operating system allowing for easy management and communication between multiple computers connected in a network. Please refer to the [official ROS2 documentation](https://index.ros.org/doc/ros2/) for details about ROS2.

CoppeliaSim can act as a ROS2 node that other nodes can communicate with via services, topics and actions.

The ROS2 Interface functionality in CoppeliaSim is enabled via a plugin: *[libsimROS2](https://github.com/CoppeliaRobotics/simROS).\**. The plugin can easily be adapted to your own needs. The plugin is loaded with:

```lua
import 'sim-2'
import 'simROS2'
```

Make sure to inspect CoppeliaSim's console window or terminal for details on plugin load operations.

Have a look at the following simulation scenes/models for a quick start with the ROS2 Interface:

- *scenes/messaging/ros2InterfaceTopicPublisherAndSubscriber.ttt*
- *scenes/messaging/controlTypeExamples/controlledViaRos2.ttt*
- *models/tools/ros2Interface helper tool.ttm* (model allowing you to operate CoppeliaSim in [stepping mode](simulation.md#stepped), e.g. to manually step the simulation)

Have a look at the [ROS2 tutorial](ros2Tutorial.md) and the [external controller tutorial](externalControllerTutorial.md).
