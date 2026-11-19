# Coppelia Kinematics Routines

The [Coppelia Kinematics Routines](https://github.com/CoppeliaRobotics/coppeliaKinematicsRoutines) is a collection of C++ functions that allow you to solve forward/inverse kinematics tasks via Jacobian for any type of mechanism (redundant/non-redundant, containing nested loops, etc.). Those functions give CoppeliaSim its kinematics calculation capability.

You can embed and use the Coppelia Kinematics Routines in your stand-alone application, which then can programmatically set up complex kinematics tasks. Refer also to the [Coppelia Kinematics Routines C++ API documentation](coppeliaKinematicsRoutines-api.md).

The Coppelia Kinematics Routines source code is not directly part of CoppeliaSim, and carries separate licensing conditions. Refer to the source code for details, and [contact us](http://coppeliarobotics.com/contact).

The following is a simple example of how to set up an inverse kinematics task, and perform calculations from within an external application:

```cpp
#include "ik.h"

int main(int argc, char* argv[])
{
    // Create the IK environment:
    ikCreateEnvironment();

    // Create a simple 3 DoF kinematic chain:
    int tipHandle,targetHandle;
    int joint1Handle,joint2Handle,joint3Handle;
    ikCreateJoint(nullptr,ik_jointtype_revolute,&joint1Handle);
    ikCreateJoint(nullptr,ik_jointtype_revolute,&joint2Handle);
    CPose tr(C4Vector(1.57,0.0,0.0),C3Vector::zeroVector);
    ikSetObjectTransformation(joint2Handle,-1,&tr);
    ikSetObjectParent(joint2Handle,joint1Handle,true);
    ikCreateJoint(nullptr,ik_jointtype_revolute,&joint3Handle);
    tr.X=C3Vector(0.0,0.0,0.2);
    ikSetObjectTransformation(joint3Handle,-1,&tr);
    ikSetObjectParent(joint3Handle,joint2Handle,true);
    ikCreateDummy(nullptr,&tipHandle);
    tr.Q.clear();
    tr.X=C3Vector(0.0,0.0,0.4);
    ikSetObjectTransformation(tipHandle,-1,&tr);
    ikSetObjectParent(tipHandle,joint3Handle,true);
    ikCreateDummy(nullptr,&targetHandle);
    ikSetObjectTransformation(targetHandle,-1,&tr);
    ikSetLinkedDummy(tipHandle,targetHandle);
    // we now have: joint1 --> joint2 --> joint3 --> tipDummy <...> targetDummy

    // Create an IK group that constrains the chain tip to follow (in position)
    // the target dummy:
    int ikGroup;
    ikCreateGroup(nullptr,&ikGroup);
    int ikElementIndex;
    ikAddElement(ikGroup,tipHandle,&ikElementIndex);
    ikSetElementConstraints(ikGroup,ikElementIndex,ik_constraint_position);

    ikGetObjectTransformation(targetHandle,-1,&tr);
    while (true)
    {
        // Slightly move the target dummy:
        tr.X=tr.X+C3Vector(0.001,0.002,-0.0001);
        ikSetObjectTransformation(targetHandle,-1,&tr);

        // Solve IK:
        int result;
        ikHandleGroup(ikGroup,&result);
        if (result!=ik_result_success)
            break;

        // Read joint values:
        simReal joint1Angle,joint2Angle,joint3Angle;
        ikGetJointPosition(joint1Handle,&joint1Angle);
        ikGetJointPosition(joint2Handle,&joint2Angle);
        ikGetJointPosition(joint3Handle,&joint3Angle);
    }
    return(0);
}
```
