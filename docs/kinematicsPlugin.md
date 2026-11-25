# Kinematics Plugin

The kinematics plugin for CoppeliaSim (*simIK.dll* or similar) wraps the [Coppelia Kinematics Routines](coppeliaKinematicsRoutines.md). The plugin itself is wrapped in the [IK classes](mainObjectTypes.md#IK), offering methods and properties for [IK](apiFunctions.md#methodsAndProperties_IK), [IKGroup](apiFunctions.md#methodsAndProperties_IKGroup), [IKElement](apiFunctions.md#methodsAndProperties_IKElement), [IKObject](apiFunctions.md#methodsAndProperties_IKObject) and [IKJoint](apiFunctions.md#methodsAndProperties_IKJoint) objects; they allow you to create, handle and solve forward/inverse kinematics tasks via Jacobian for any type of mechanism (redundant/non-redundant, containing nested loops, etc.) fully programmatically.

Kinematics tasks can easily be set up from the scene's content like in the following example:

```lua
import 'sim-2'
simIK = require 'simIK-2'

-- set-up:
function sysCall_init()
    local simBase = sim.self:getObject('/base')
    local simTip = sim.self:getObject('/tip')
    local simTarget = sim.self:getObject('/target')
    ik = simIK()
    local ikGroup = ik:createGroup({method = 'dampedLeastSquares', damping = 0.01, maxIterations = 10})
    local ikElement = ikGroup:addElementFromScene(simBase, simTip, simTarget, ik.constraint_pose, {precision = {0.0005, 0.005 * math.pi / 180.0}})
end

-- IK calculation, and application to the scene:
function sysCall_actuation()
    ik:solve()
end
```

[`IKGroup:addElementFromScene`](sim-2/IKGroup_addElementFromScene.md) parses the scene given a base, tip and target object, and generates an appropriate IK element, with the given constraints. [`IK:solve`](sim-2/IK_solve.md) on the other hand synchronizes the IK world with the sim world, computes IK, then synchronizes the sim world back from the IK world.
