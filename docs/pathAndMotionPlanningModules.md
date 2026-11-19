# Path/motion planning

CoppeliaSim offers path/motion planning functionality via a plugin wrapping the [OMPL library](http://ompl.kavrakilab.org/). The plugin, courtesy of Federico Ferri, exports several [API functions related to OMPL](simOMPL/simOMPL.htm). Its source code can be found [here](https://github.com/CoppeliaRobotics/simOMPL).

The following points should be considered when preparing a path/motion planning task:

- Decide on a start and goal state. When the path planning object is a serial manipulator, a goal pose (or end-effector position/orientation) is often provided instead of a goal state. In that case [IKGroup:findConfig](sim/IKGroup_findConfig.htm) can be used to find one or several goal states that satisfy the provided goal pose.
- Create a path planning task with [simOMPL.createTask](simOMPL/simOMPL.htm#createTask).
- Select an algorithm with [simOMPL.setAlgorithm](simOMPL/simOMPL.htm#setAlgorithm).
- Create the required state space, which can be composed as a compound object: [simOMPL.createStateSpace](simOMPL/simOMPL.htm#createStateSpace) and [simOMPL.setStateSpace](simOMPL/simOMPL.htm#setStateSpace).
- Specify which entities are not allowed to collide with [simOMPL.setCollisionPairs](simOMPL/simOMPL.htm#setCollisionPairs).
- Specify the start and goal state with [simOMPL.setStartState](simOMPL/simOMPL.htm#setStartState) and [simOMPL.setGoalState](simOMPL/simOMPL.htm#setGoalState).
- Call [simOMPL.setup](simOMPL/simOMPL.htm#setup) once to initialize OMPL's data structures.
- Compute one (or more) paths with [simOMPL.compute](simOMPL/simOMPL.htm#compute); when called multiple times it will reuse previously computed data, if the chosen algorithm supports it, e.g.: multi-query planners such as PRM.
- Destroy the path planning task with [simOMPL.destroyTask](simOMPL/simOMPL.htm#destroyTask).
- Often, path planning is used in combination with [inverse kinematics](kinematics.md): in a pick-and-place task for instance, the final approach should usually be a straight-line path.

The above procedure is the *regular* approach, which sometimes lacks flexibility. Additionally, the following callback functions can be set up:

- [simOMPL.setStateValidationCallback](simOMPL/simOMPL.htm#setStateValidationCallback)
- [simOMPL.setProjectionEvaluationCallback](simOMPL/simOMPL.htm#setProjectionEvaluationCallback)
- [simOMPL.setGoalCallback](simOMPL/simOMPL.htm#setGoalCallback)

## Path optimality

Most of the planners use randomized algorithms, which don't provide optimal (i.e. shortest) paths. Some of those are *optimizing* planners, meaning that they are still randomized, but will use the remaining planning time to improve the first solution found, thus giving an *asymptotic optimality* guarantee.

If a short path is preferable, then an optimizing planner (such as RRT\*, PRM\*, ...) should be used.

## Multi-query planners

When using multi-query planners (PRM, PRM\*, ...), just call [simOMPL.setStartState](simOMPL/simOMPL.htm#setStartState) and [simOMPL.compute](simOMPL/simOMPL.htm#compute) again. Planning will re-use and expand the previously built roadmap.

Make sure to refer to the following demo scenes for additional details:

- *scenes/kinematics/8-computingJointAnglesForRandomPoses.ttt*
- *scenes/3DoFHolonomicPathPlanning.ttt*
- *scenes/6DoFHolonomicPathPlanning.ttt*
- *motionPlanningDemo1*
- *motionPlanningAndGraspingDemo.ttt*
