# ROS Interface

The ROS Interface is part of the [CoppeliaSim API framework](apisOverview.md). It duplicates the C/C++ ROS API with a good fidelity. This makes it the ideal choice for very flexible communication via ROS. You can recognize ROS Interface API functions from the *simROS*- prefix.

ROS is a distributed pseudo operating system allowing for easy management and communication between multiple computers connected in a network. Please refer to the [official ROS documentation](http://www.ros.org) for details about ROS.

CoppeliaSim can act as a ROS node that other nodes can communicate with via ROS services, ROS publishers and ROS subscribers.

The ROS Interface functionality in CoppeliaSim is enabled via a plugin: *[libsimROS](https://github.com/CoppeliaRobotics/simROS).\**. The plugin can easily be adapted to your own needs. The plugin is loaded with:

```lua
--lua

simROS = require('simROS')
```

The load operation will only be successful if roscore was running at that time. Make sure to inspect CoppeliaSim's console window or terminal for details on plugin load operations.

Have a look at the following simulation scenes/models for a quick start with the ROS Interface:

- *scenes/messaging/rosInterfaceTopicPublisherAndSubscriber.ttt*
- *scenes/controlTypeExamples/controlledViaRos.ttt*
- *models/tools/rosInterface helper tool.ttm* (model allowing you to operate CoppeliaSim in [stepping mode](simulation.md#stepped), e.g. to manually step the simulation)

Have a look at the [ROS tutorial](rosTutorial.md) and the [external controller tutorial](externalControllerTutorial.md).
