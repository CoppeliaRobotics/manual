# Data visualization/output

Data can be visualized or output/logged in various ways:

- [Web-browser based front-end](externalFrontEnd.md)
- Visualizing data in [graphs](graphs.md)
- Displaying data in [custom user interfaces](customUIPlugin.md)
- <a id="augmentingScene"></a>[Augmenting the scene with visual items](markers.md)
- Logging data to the status bar via the simple *print* command
- Logging data to the status bar and/or terminal via [`sim.app:logInfo`](sim-2/app_logInfo.md), [`sim.app:logWarn`](sim-2/app_logWarn.md) and [`sim.app:logError`](sim-2/app_logError.md)
- [Logging data to a file](#loggingToFile)
- [Printing text in a console](#auxConsoles)
- [Text editing](#textEditors)

The following example illustrates how to display a joint angle in a simple custom user interface:

```python
import sim
import simUI
import math
from types import SimpleNamespace
state = SimpleNamespace()

def sysCall_init():
    state.joint = sim.self.getObject('/Joint')
    xml = """
        <ui title="Example" closeable="false" layout="form">
            <label text="joint angle:" />
            <label id="1" text="-" />
        </ui>
    """
    state.ui = simUI.create(xml)

def sysCall_sensing():
    v = 180 * state.joint.joint.position / math.pi
    simUI.setLabelText(state.ui, "1", '{:.3f}'.format(v))

def sysCall_cleanup():
    simUI.destroy(state.ui)
```

```lua
import 'sim-2'
import 'simUI'

function sysCall_init()
    joint = sim.self:getObject('/Joint')
    local xml =[[<ui title="Example" closeable="false" layout="form">
        <label text="joint angle:" />
        <label id="1" text="-" />
        </ui>]]
    ui = simUI.create(xml)
end

function sysCall_sensing()
    local v = 180 * joint.joint.position / math.pi
    simUI.setLabelText(ui, 1, string.format('%.3f', v))
end

function sysCall_cleanup()
    simUI.destroy(ui)
end
```

More complex items, such as random meshes can be created on the fly via [`sim.scene:loadModel`](sim-2/scene_loadModel.md), [`sim.scene:createObject`](sim-2/scene_createObject.md) and/or [`sim.scene:duplicateObjects`](sim-2/scene_duplicateObjects.md). To avoid overloading the scene with too many additional objects, make sure to group shapes with [`sim.scene:groupShapes`](sim-2/scene_groupShapes.md) or [`sim.scene:mergeShapes`](sim-2/scene_mergeShapes.md). For example:

```lua
import 'sim-2'

function sysCall_init()
    local individualShapes = {}
    for i = 0, 359, 1 do
        local shape = sim.scene:createObject({type = 'shape',
                      ['color.diffuse'] = Color('red'),
                      cylinder = {radius = 0.0025, length = 0.02}})
        local coord = {math.cos(i * math.pi / 180),
                       math.sin(i * math.pi / 180), 0.01}
        shape.worldPosition = coord
        individualShapes[i + 1] = shape
    end
    -- Merge the shapes:
    local masterShape = sim.scene:mergeShapes(individualShapes)
    -- Make it invisible to collision detection, sensors, etc.:
    masterShape.collidable = false
    masterShape.measurable = false
    masterShape.detectable = false
end
```

## <a id="loggingToFile"></a>Logging data to a file

The following example illustrates how to log a joint angle to a file:

```python
import sim
import math
from types import SimpleNamespace
state = SimpleNamespace()

def sysCall_init():
    state.joint = sim.self.getObject('/Joint')
    state.file = open('jointAngles.txt', 'w+')
    state.file.write('Joint angles for each simulation step:\n\n')

def sysCall_sensing():
    v = 180 * state.joint.joint.position / math.pi
    state.file.write('time: {:.3f} [s]'.format(sim.scene.simulation.time + sim.scene.simulation.timeStep))
    state.file.write(', joint angle: {:.1f} [deg]\n'.format(v))

def sysCall_cleanup():
    state.file.close()
```

```lua
import 'sim-2'

function sysCall_init()
    joint = sim.self:getObject('/Joint')
    file = io.open('jointAngles.txt', 'w+')
    file:write('Joint angles for each simulation step:\n\n')
end

function sysCall_sensing()
    local v = 180 * joint.joint.position / math.pi
    file:write(string.format('time: %.3f [s]', sim.scene.simulation.time + sim.scene.simulation.timeStep))
    file:write(string.format(', joint angle: %.1f [deg]\n', v))
end

function sysCall_cleanup()
    file:close()
end
```

## <a id="auxConsoles"></a>Printing text in a console

The following example illustrates how to create an auxiliary console, and print text into it:

```lua
import 'sim-2'

function sysCall_init()
    console = sim.app:createObject({type = 'console'})
end

function sysCall_sensing()
    if console:isValid() then
        console:print('sim. time: ' .. sim.scene.simulation.time .. '\n')
    end
end

function sysCall_cleanup()
    if console:isValid() then
        console:remove()
    end
end
```

## <a id="textEditors"></a>Text editing

The following example illustrates how to edit text in an editor:

```lua
import 'sim-2'

function sysCall_init()
    editor = sim.app:createObject({type = 'textEditor'})
end

function sysCall_cleanup()
    if editor:isValid() then
        print(editor.text)
        editor:remove()
    end
end
```
