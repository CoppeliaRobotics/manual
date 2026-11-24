# simCheckDistance

Checks the minimum distance between two entities. The measurable flags of the entities are overridden if the entities are objects. If the entities are both the same collection (i.e. with the same collection handle), then same objects will not be checked against themselve

## Synopsis

```cpp
int simCheckDistance(int entity1Handle, int entity2Handle, double threshold, double* distanceData)
```

## Parameters

- **entity1Handle**: handle of entity 1 (can be an object handle or a collection handle)
- **entity2Handle**: handle of entity 2 (can be an object handle or a collection handle), or sim.handle_all to check entity1 against all other measurable objects
- **threshold**: if distance is bigger than the threshold, the distance is not calculated and return value is 0. If threshold is 0 or negative, then no threshold is used.
- **distanceData**: distanceData[0]-distanceData[5] represents the distance segment, distanceData[6] is the distance between the entities. This data is valid only if return value is 1

## Return values

- 0 or 1 if operation was successful (1 if distance is smaller than threshold), -1 otherwise
