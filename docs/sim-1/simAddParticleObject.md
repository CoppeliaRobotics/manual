# sim.addParticleObject

Adds a particle object that will be simulated and displayed in the scene. Particle objects are containers that hold several items (particles) of a given type. This can be used for several different applications (e.g. simulation of air/water jets)

## Synopsis

```lua
int particleObjectHandle = sim.addParticleObject(int objectType, float size, float density,
                                                 float[] parameters, float lifeTime,
                                                 int maxItemCount, float[3] color = nil)
```

```python
int particleObjectHandle = sim.addParticleObject(int objectType, float size, float density,
                                                 list parameters, float lifeTime, int maxItemCount,
                                                 list color = None)
```

## Parameters

- **objectType**: a [particle object type combined with attributes](../apiConstants-1.md#particleObjects)
- **size**: diameter of the particles (spheres)
- **density**: density of the particles
- **parameters**: an array of values, allowing to specify additional parameters. Can be None/nil. Values come in pair (an integer indicating what parameter, and a float indicating the parameter value. Following indicates the parameters:

    - 0: Bullet friction coefficient (default: 0.0)
    - 1: Bullet restitution coefficient (default: 0.0)
    - 2: ODE friction coefficient (default: 0.0)
    - 3: ODE soft ERP value (default: 0.2)
    - 4: ODE soft CFM values (default: 0.0)
    - 5: Bullet, ODE, Newton and Vortex linear drag parameter (default: 0.0). Adds a force opposite to the particle velocity (f=v*parameter)
    - 6: Bullet, ODE, Newton and Vortex quadratic drag parameter (default: 0.0). Adds a force opposite to the particle velocity (f=v*v*parameter)
    - 7: Bullet, ODE, Newton and Vortex linear drag parameter in air (z&gt;0) if sim.particle_water was specified (default: 0.0). Adds a force opposite to the particle velocity (f=v*parameter)
    - 8: Bullet, ODE, Newton and Vortex quadratic drag parameter in air (z&gt;0) if sim.particle_water was specified (default: 0.0). Adds a force opposite to the particle velocity (f=v*v*parameter)
    - 9: Vortex friction (default: 0.0)
    - 10: Vortex restitution (default: 0.0)
    - 11: Vortex restitution threshold (default: 0.001)
    - 12: Vortex compliance (default: 0.0)
    - 13: Vortex damping (default: 0.0)
    - 14: Vortex adhesive force (default: 0.0)
    - 15: Newton static friction (default: 0.0)
    - 16: Newton kinetic friction (default: 0.0)
    - 17: Newton restitution (default: 0.0)
    - If a parameter is not set, then its default value is used
- **lifeTime**: simulation time after which the particles are destroyed. Set to 0.0 for an unlimited lifetime.
- **maxItemCount**: the maximum number of particles that this object can hold
- **color**: default ambient/diffuse color (pointer to 3 rgb values). Can be None/nil

## Return values

- handle of the particle object

## See also

- [sim.addParticleObjectItem](simAddParticleObjectItem.md)
- [sim.removeParticleObject](simRemoveParticleObject.md)
