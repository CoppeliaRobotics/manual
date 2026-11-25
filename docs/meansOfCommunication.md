# Messaging, interfaces and connectivity

There are several ways to exchange messages or data within CoppeliaSim, and also between CoppeliaSim and an external application, another computer or machine:

You can send or receive data via:

- <a id="signals"></a>[Signals](properties.md#signals)
- <a id="customData"></a><a id="customDataBlocks"></a>[Custom data](properties.md#customData)
- [Calling plugin functions](#pluginFunctions)
- [Calling script functions](#simCallScriptFunction)
- [Remote API](remoteApiOverview.md)
- [Broadcasting a message](#simBroadcastMsg)
- [Events](#events)
- [ROS](rosInterfaces.md)
- [ZeroMQ](#zmq)
- [WebSocket](#ws)
- [Sockets](#sockets)
- [Other](#other)

## <a id="callingPluginFunctions"></a><a id="pluginFunctions"></a>Calling plugin functions

[Scripts](scripts.md) can call specific [plugin](plugins.md) functions, referred to as callback functions. To do so, a plugin must first register its callback functions via [`simRegisterScriptCallbackFunction`](sim-2/simRegisterScriptCallbackFunction_cpp.md). This is a convenient mechanism to extend CoppeliaSim's functionality, but can also be used for complex data exchange between scripts and plugins. The following illustrates a very simple plugin function and its registration:

```cpp
void myCallbackFunc(SScriptCallBack* p)
{
    int stack = p -> stackID;
    CStackArray inArguments;
    inArguments.buildFromStack(stack);

    if ( (inArguments.getSize() > 0) && inArguments.isString(0) )
    {
        std::string tmp("we received a string: ");
        tmp += inArguments.getString(0);
        simAddLog("ABC", sim_verbosity_msgs,tmp.c_str());

        CStackArray outArguments;
        outArguments.pushString("Hello to you too!");
        outArguments.buildOntoStack(stack);
    }
    else
        simSetLastError(nullptr, "Not enough arguments or wrong arguments.");
}

// Somewhere in the plugin's initialization code:
simRegisterScriptCallbackFunction("func", nullptr, myCallbackFunc);
```

## <a id="simCallScriptFunction"></a><a id="simCallScriptFunctionEx"></a>Calling script functions

A [script](scripts.md) function can be called from within the same script, and also:

- From other scripts: refer to [`script:callFunction`](sim-2/script_callFunction.md), [`script:getFunctions`](sim-2/script_getFunctions.md) or [`script:executeString`](sim-2/script_executeString.md).
- From a plugin: refer to [`simCallScriptFunctionEx`](sim-2/simCallScriptFunctionEx_cpp.md).
- From a [ROS](rosInterfaces.md) client, via a callback mechanism.
- From a [remote API](remoteApiOverview.md) client.

The called script function can perform various tasks, then return some data to the caller. However, it is important not to perform lengthy tasks within the called function, as everything comes to a halt during that time. Lengthy tasks should instead be triggered only via [`script:callFunction`](sim-2/script_callFunction.md), then processed within a sysCall_thread [system callback](callbackFunctions.md) section.

## <a id="simBroadcastMsg"></a>Broadcasting messages

A [script](scripts.md) or a [remote API](remoteApiOverview.md) client can broadcast a message to all scripts at once via [`script:broadcast`](sim-2/script_broadcast.md). For instance, the following constantly broadcasts a message to all scripts, while printing other broadcast messages:

```lua
import 'sim-2'

function sysCall_init()
end

function sysCall_sensing()
    local message = {id = 'greetingMessage', data = {msg = 'Hello!'}}
    sim.self:broadcast(message)
end

function sysCall_msg(msg, origin)
    print("Received following: ", msg)
    print("From script: ", origin)
end
```

## <a id="events"></a>Events

A [script](scripts.md) or a [plugin](plugins.md) can receive notifications for everything that happens in CoppeliaSim itself, e.g. when an object is created, modified or removed, or when an internal state changes. A script can use the sysCall_event [callback function](callbackFunctions.md) to that end, coupled with some filtering for the sake of efficiency. For instance, the following script tracks pose changes of any scene object, and changes in scene object selection:

```lua
import 'sim-2'
cbor = require 'sim.cbor'

function sysCall_init()
    local filters = {}
    filters['sceneObject'] = {'pose'}
    filters[sim.scene] = {'selection'}
    sim.self:setEventFilters(filters)
end

function sysCall_event(events)
    local ev = cbor.decode(events)
    print(ev)
end
```

See also the event viewer add-on located at [Modules > Developer tools > Event viewer] and the property explorer add-on located at [Modules > Developer tools > Property explorer].

## <a id="zmq"></a>ZeroMQ

The [ZeroMQ library](http://api.zeromq.org/), wrapped inside the [ZMQ plugin](https://github.com/CoppeliaRobotics/simZMQ), offers several [API functions related to ZeroMQ messaging](simZMQ/simZMQ.md). When using Python, you are of course also free to use the pyzmq package for ZeroMQ functionality. The following illustrates a simple requester:

```lua
import 'sim-2'
import 'simZMQ'

function sysCall_thread()
    print('Connecting to responder server...')
    context = simZMQ.ctx_new()
    requester = simZMQ.socket(context, simZMQ.REQ)
    simZMQ.connect(requester, 'tcp://localhost:5555')

    for request_nbr = 0, 10 do
        print('-----------------------------------------')
        local data = 'Hello ' .. request_nbr
        printf('[requester] Sending "%s"...', data)
        simZMQ.send(requester, data, 0)
        local rc, data = simZMQ.recv(requester, 0)
        printf('[requester] Received "%s"', data)
    end
end

function sysCall_cleanup()
    simZMQ.close(requester)
    simZMQ.ctx_term(context)
end
```

The following would be the corresponding responder:

```lua
import 'sim-2'
import 'simZMQ'

function sysCall_thread()
    context = simZMQ.ctx_new()
    responder = simZMQ.socket(context, simZMQ.REP)
    local rc = simZMQ.bind(responder, 'tcp://*:5555')
    if rc ~= 0 then
        error('failed bind')
    end

    while true do
        local rc, data = simZMQ.recv(responder, 0)
        printf('[responder] Received "%s"', data)
        data = 'World'
        printf('[responder] Sending "%s"...', data)
        simZMQ.send(responder, data, 0)
    end
end

function sysCall_cleanup()
    simZMQ.close(responder)
    simZMQ.ctx_term(context)
end
```

## <a id="ws"></a>WebSocket

The [WebSocket plugin](https://github.com/CoppeliaRobotics/simWS) offers several [API functions that allow you to interact with a web browser](simWS/simWS.md). When using Python, you are of course also free to use a Python-specific WebSocket package. The following is a simple echo server:

```lua
import 'sim-2'
import 'simWS'

function onMessage(server, connection, data)
    simWS.send(server, connection, data)
end

function sysCall_init()
    server = simWS.start(9000)
    simWS.setMessageHandler(server, 'onMessage')
end
```

The following is a simple broadcaster:

```lua
import 'sim-2'
import 'simWS'

function onOpen(server, connection)
    clients[server] = clients[server] or {}
    clients[server][connection] = 1
end

function onClose(server, connection)
    clients[server][connection] = nil
end

function broadcast(server, data)
    for connection, _ in pairs(clients[server] or {}) do
        simWS.send(server, connection, data)
    end
end

function sysCall_init()
    clients = {}
    server = simWS.start(9000)
    simWS.setOpenHandler(server, 'onOpen')
    simWS.setCloseHandler(server, 'onClose')
end
```

## <a id="sockets"></a>Sockets

CoppeliaSim ships with the [LuaSocket](http://w3.impa.br/~diego/software/luasocket/home.html) extension library for Lua, while several packages are available for Python. The following illustrates how to fetch a web page:

```python
import sim

import requests
response = requests.get('http://www.google.com')
page = response.text
```

```lua
import 'sim-2'

http = require('socket.http')
page = http.request('http://www.google.com')
```

## <a id="other"></a>Other

Many other means of communication can be directly supported from within a script, via a Lua extension library or via a Python package. Indirectly, by going through a [plugin](plugins.md), there are even more possibilities, since a plugin can virtually link to any type of C/C++ communication library.
