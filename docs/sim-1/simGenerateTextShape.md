# sim.generateTextShape

Generates a 3D text model.

## Synopsis

```lua
int modelHandle = sim.generateTextShape(string txt, float[3] color = {1, 1, 1}, float height = 0.1,
                                        bool centered = false, string alphabetLocation = nil)
```

```python
int modelHandle = sim.generateTextShape(string txt, list color = [1, 1, 1], float height = 0.1,
                                        bool centered = False, string alphabetLocation = None)
```

## Parameters

- **txt**: the text string
- **color**: the text color. Optional
- **height**: the height of the text. Optional
- **centered**: whether the text should be centered. Optional
- **alphabetLocation**: the path to an alphabet model. Optional

## Return values

- **modelHandle**: handle of the generated model
