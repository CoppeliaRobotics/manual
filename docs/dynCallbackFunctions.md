# Dynamics callback functions

Scripts can include a dynamics callback function, which is one of many [system callback functions](callbackFunctions.md#systemCallbacks). When present, then the physics engine calls the callback function with appropriate arguments, before and after each dynamics simulation step. The dynamics callback function might be called quite often, normally 10\*2 times per simulation step. For that reason, keep things simple, to avoid slowing down the simulation.

The following represents a simple dynamics callback function:

```lua
import 'sim-2'

function sysCall_dyn(inData)
    -- This function gets called often, so it might slow down the simulation
    --     (this is called twice at each dynamic simulation step, by default 20x more often than a simulation script)
    -- We have:
    -- inData.passCnt : the current dynamics calculation pass. 1-10 by default. See next item for details.
    -- inData.totalPasses : the number of dynamics calculation passes for each "regular" simulation pass.
    --                      10 by default (i.e. 10*5ms=50ms which is the default simulation time step)
    -- inData.dt : the step size used for the dynamics calculations (by default 5ms)
    -- inData.afterStep : false when called before, and true after a dynamics step was computed.

    local txt = string.format(" the %ith dynamics calculation step (out of %i steps)", inData.passCnt, inData.totalPasses)
    if inData.afterStep then
        txt = "After"..txt
    else
        txt = "Before"..txt
    end
    print(txt)
end
```
