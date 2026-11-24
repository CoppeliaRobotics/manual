# simCheckCollision

Checks whether two entities are colliding. The collidable flags of the entities are overridden if the entities are objects. If the entities are both the same collection (i.e. with the same collection handle), then same objects will not be checked against themselve

## Synopsis

```cpp
int simCheckCollision(int entity1Handle, int entity2Handle)
```

## Parameters

- **entity1Handle**: handle of entity 1 (can be an object handle or a collection handle)
- **entity2Handle**: handle of entity 2 (can be an object handle or a collection handle), or sim.handle_all to check entity1 against all other collidable objects

## Return values

- -1 in case of an error, 0 or 1 to indicate a collision state
