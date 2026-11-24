# sim.createPath

Creates a [path](../paths.md).

## Synopsis

```lua
int pathHandle = sim.createPath(float[] ctrlPts, int options = 0, int subdiv = 100,
                                float smoothness = 1.0, int orientationMode = 0,
                                float[3] upVector = {0, 0, 1})
```

```python
int pathHandle = sim.createPath(list ctrlPts, int options = 0, int subdiv = 100,
                                float smoothness = 1.0, int orientationMode = 0,
                                list upVector = [0, 0, 1])
```

## Parameters

- **ctrlPts**: control points, specified in row-major order, with *[x y z qx qy qz qw]* values for each path point
- **options**: bit-coded:

    - bit0 set (1): path is hidden during simulation
    - bit1 set (2): path is closed
    - bit2 set (4): generates an extruded shape
    - bit3 set (8): show individual path points
    - bit4 set (16): the path points' orientation is computed according to the orientationMode below
- **subdiv**: number of individual path points
- **smoothness**: value between 0.0 (linear interpolation) and 1.0 (100% Bezier interpolation)
- **orientationMode**: value specifiying how the individual path points are oriented along the path, if bit16 of options is set: 0: x along path, y is up, 1: x along path, z is up, 2: y along path, x is up, 3: y along path, z is up, 4: z along path, x is up, 5: z along path, y is up
- **upVector**: up vector, used for generating an extruded shape and for computing individual path point orientations

## Return values

- **pathHandle**: handle of the created path object
