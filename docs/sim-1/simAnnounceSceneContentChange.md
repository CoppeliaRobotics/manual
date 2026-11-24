# sim.announceSceneContentChange

Announces a change in the scene. This is required for the undo/redo function to operate properly when performing changes via the API. Only call this function directly after a change was made through a dialog element (e.g. a checkbox was checked/unchecked) and that change was reported to the scene. What this call will do is following: the whole scene will be serialized (saved) to memory as a "scene image" and compared to a previously memorized "scene image". If both images are same, then the last image is discarded, otherwise only the changes between the two images are memorized. A call to this function has no effect (and doesn't generate any error) when called during simulation or when in edit mode.

## Synopsis

```lua
int result = sim.announceSceneContentChange()
```

```python
int result = sim.announceSceneContentChange()
```

## Parameters

No parameters.

## Return values

- **result**: 0 if nothing was memorized, or 1 if changes were memorized.
