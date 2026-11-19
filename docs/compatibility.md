# Forward/backward compatibility

CoppeliaSim is developed by a small team, and as such, we embrace an agile development methodology, which means a more frequent update cycle and rapid deployment of fixes. This approach may lead to occasional issues, but allows for swift resolution and the introduction of new features. User feedback and bug reports are crucial to this process and are an important way of identifying and addressing problems.

## <a id="scriptObjects"></a>Introduction of [script objects](newScriptObjects.md) in CoppeliaSim V4.7

### Forward compatibility

Associated scripts remain operational. It is however recommended to [convert them to script objects](newScriptObjects.md#conversion). Automatic conversion is not perfect, and several manual adjustments might have to be done, additionally.

### Backward compatibility

Scenes and models containing script objects can be converted back to scenes and models containing only associated scripts, by setting the [user settings](commandLine.md#settingsFile) parameter *scriptConversion* to -1. The related script code is however not touched by this conversion, and manual adjustments will have to be done.

## <a id="buffers"></a>Introduction of [buffers](buffers.md) in CoppeliaSim V4.7

### Forward compatibility

There are potentially two problematic situations with existing code:

- Code that relies on the usage of the *type*-function will break with buffers, e.g.:
- Most API methods/properties that clearly return binary data (e.g. [visionSensor.image](sim/property_visionSensor_image.htm)) now return the data as a buffer. Comparing that buffer with a string always resolves to *false*, e.g.:
- In sim-1, sim.packTable now returns a buffer of different length from previous CoppeliaSim versions (text/strings and buffers are now differentiated and this is reflected in the packed data), e.g.:

Workarounds:

- Converting a buffer to string via *tostring*, before handing it to a code base that is not aware of buffers, is the best way to avoid potential problems
- Where a buffer is compared to a string (and vice-versa), convert one or the other via *tostring* or *tobuffer*, otherwise the comparison always resolves to *false*

### Backward compatibility

*isbuffer* and *tobuffer* are not recognized functions. Workaround:

- Add following functions to *lua/base.lua* (alternatively to *lua/sim.lua*, or to a specific script code):
