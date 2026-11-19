# The sandboxes

The sandboxes are instances of the [script type](mainObjectTypes.md#script), itself of type *sandbox*. A sandbox is quite similar to an [add-on](addOns.md): it is automatically loaded at program start-up, and allows CoppeliaSim's functionality to be extended by user-written functionality. In addition to that, the sandboxes are extensively used in CoppeliaSim's commander plugin (read-eval-print loop), that adds a text input to the CoppeliaSim status bar, allowing entering and executing code on the fly, like in a terminal.

Sandboxes are persistent across all opened scenes, and are effectively running in the background. For that reason, they should only execute minimalistic code every time called, since the whole application would otherwise slow down. Sandboxes are called via [system callback functions](callbackFunctions.md#systemCallbacks), and follow a precise [execution order](scriptExecution.md) in relation to other script types.

There is a Lua and a Python sandbox. Refer also to [app.sandboxLua](sim/property_app_sandboxLua.htm) and [app.sandboxPython](sim/property_app_sandboxPython.htm).
