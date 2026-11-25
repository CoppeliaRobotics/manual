# CoppeliaSim API framework

Within CoppeliaSim, you can distinguish between two groups of functions, methods and properties:

- The regular API is made available by CoppeliaSim itself, and represents the core functionality:
  - [sim-1](apiFunctions-1.md) (version 1, function-based)
  - [sim-2](apiFunctions.md) (version 2. The Lua API is OOP-based, the C/C++ API is centered around property/stack functions, and [simCallMethod](sim-2/simCallMethod_cpp.md) mainly)
- The other API items are mainly functions made available by specific [plugins](plugins.md). Each plugin groups its functionality under a unique namespace, e.g. [simOMPL](simOMPL/simOMPL.md), [simUI](simUI/simUI.md). The documentation for those functions can be found in the [functionality section](functionality.md).

From an external application, there are [many different API mechanisms available to communicate and interact with CoppeliaSim](meansOfCommunication.md).
