# sim.createScript

Creates a [script object](../scriptObjects.md).

## Synopsis

```lua
int scriptHandle = sim.createScript(int scriptType, string scriptText, int options = 0
                                    string lang = 'lua')
```

```python
int scriptHandle = sim.createScript(int scriptType, string scriptText, int options = 0
                                    string lang = 'lua')
```

## Parameters

- **scriptType**: the [script type](../apiConstants-1.md#scriptTypes). Only simulation-, customization- or passive scripts are allowed
- **scriptText**: the content of the script
- **options**: bit-coded options:

    - bit 0 set (1): script is initially disabled
- **lang**: language. A value different 'lua' or 'python' disables the script

## Return values

- **scriptHandle**: handle of the script object
