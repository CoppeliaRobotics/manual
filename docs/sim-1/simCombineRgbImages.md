# sim.combineRgbImages

Combines two RGB images

## Synopsis

```lua
buffer outImg = sim.combineRgbImages(buffer img1, int[2] img1Res, buffer img2, int[2] img2Res,
                                     int operation)
```

```python
bytes outImg = sim.combineRgbImages(bytes img1, list img1Res, bytes img2, list img2Res,
                                    int operation)
```

## Parameters

- **img1**: input image 1, as succession of rgb values.
- **img1Res**: x/y resolution of image 1.
- **img2**: input image 2, as succession of rgb values.
- **img2Res**: x/y resolution of image 2.
- **operation**: [operation](../apiConstants-1.md#imageCombination) to be performed with the two input images.

## Return values

- output image as succession of rgb values.

## See also

- [sim.transformImage](simTransformImage.md)
