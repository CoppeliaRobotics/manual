# simGenerateShapefromPath

Generates an extrusion shape from a path

## Synopsis

```cpp
int simGenerateShapeFromPath(const double* path, int pathSize, const double* section,
                             int sectionSize, int options, const double* upVector, double reserved)
```

## Parameters

- **path**: path, specified in row-major order, with [x y z qx qy qz qw] values for each path point. The orientation parts for each path point are ignored if the two first bits of **options** are zero.
- **pathSize**: size/length of the path pointer
- **section**: extrusion profile, with x/y pairs, e.g. [x1 y1 x2 y2 ... xn yn]. If the first and last pair overlap, the section is closed
- **sectionSize**: size/length of the section pointer
- **options**: bit-coded:

    - bit0-bit1: 0 = upVector is **upVector**, 1 = upVector is the x-axis of the path point frame, 2 = upVector is the y-axis of the path point frame, 3 = upVector is the z-axis of the path point frame
    - bit2 set (4): the path is closed
- **upVector**: vector that identifies the up-side of the extrusion shape. Can be nullptr if the two first bits of **options** are non-zero.

## Return values

- **shapeHandle**: the handle of the generated shape

## See also

- [path related functions](../apiFunctions-1.md#paths)
