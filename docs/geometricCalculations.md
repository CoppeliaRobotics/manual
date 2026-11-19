# Geometry / Mesh Calculations

CoppeliaSim handles major geometric calculations via the [Coppelia Geometric Routines](coppeliaGeometricRoutines.md), which is a collection of C++ functions that can be embedded into stand-alone applications. Those routines are wrapped in the [geometric plugin](geometricPlugin.md) for CoppeliaSim, which is in charge of handling:

- [Collision detection](collisionDetection.md)
- [Distance calculation](distanceCalculation.md)
- [Proximity sensor](proximitySensors.md) simulation

Other geometry / mesh functionality is supported via dedicated plugins:

- [simConvex](simConvex/simConvex.htm), offers e.g. [convex hull](convexHull.md) and [convex decomposition](convexDecomposition.md) operations
- [simOpenMesh](simOpenMesh/simOpenMesh.htm), offers e.g. mesh decimation operations
- [simIGL](simIGL/simIGL.htm), offers boolean and other operations
