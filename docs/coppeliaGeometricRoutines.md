# Coppelia Geometric Routines

The [Coppelia Geometric Routines](https://github.com/CoppeliaRobotics/coppeliaGeometricRoutines) is a collection of C++ functions that allow you to perform the same geometric calculations as you are able to do from within CoppeliaSim (i.e. [collision detection](collisionDetection.md), [minimum distance calculation](distanceCalculation.md), and [proximity sensor](proximitySensors.md) simulation on [meshes](shapes.md), [oc-trees](octrees.md) and [point clouds](pointClouds.md)). Those functions give CoppeliaSim its geometric calculation capability.

You can embed and use the Coppelia Geometric Routines in your stand-alone application, which then can programmatically set up complex calculation tasks. Refer also to the [Coppelia Geometric Routines C++ API documentation](coppeliaGeometricRoutines/coppeliaGeometricRoutines-api.md).

The Coppelia Geometric Routines source code is not directly part of CoppeliaSim, and carries separate licensing conditions. Refer to the source code for details, and [contact us](http://coppeliarobotics.com/contact).

The following very simple example illustrates how to measure the smallest distance between two meshes:

```cpp
#include "geom.h"

int main(int argc, char* argv[])
{
    // Create mesh 1 (containing a single triangle, for simplicity):
    std::vector<simReal> vertices1{0.0,0.0,0.0,
                                   0.5,0.5,0.0,
                                   0.5,0.0,0.5};
    std::vector<int> indices1{0,1,2};
    CObbStruct* mesh1=geom_createMesh(&vertices1[0],vertices1.size(),&indices1[0],indices1.size());

    // Create mesh 2 (containing a single triangle, for simplicity):
    std::vector<simReal> vertices2{0.5,0.0,0.0,
                                   0.0,0.5,0.5,
                                   0.0,0.0,0.5};
    std::vector<int> indices2{0,1,2};
    CObbStruct* mesh2=geom_createMesh(&vertices2[0],vertices2.size(),&indices2[0],indices2.size());

    // now move and rotate the two meshes and compute their minimum distance:
    simReal t=0.0;
    while (true)
    {
        t+=0.001;
        CPose mesh1Transformation;
        mesh1Transformation.X=C3Vector(0.5*cos(0.1*t),0.0,0.0); // sinusoidal x-axis movement
        mesh1Transformation.Q.setIdentity();
        CPose mesh2Transformation;
        mesh2Transformation.X=C3Vector(0.0,0.4*cos(0.2*t),0.3*cos(0.1*t)); // sinusoidal y- and z-axis movement
        C3Vector eulerAngles(0.0,0.0,t*1.2); // rotation around vertical axis
        mesh2Transformation.Q.setEulerAngles(eulerAngles);

        // compute the distance:
        simReal dist=REAL_MAX;
        geom_getMeshMeshDistanceIfSmaller(mesh1,mesh1Transformation,mesh2,mesh2Transformation,dist);

        printf("mesh-mesh minimum distance: %f\n",dist);
    }
    return(0);
}
```
