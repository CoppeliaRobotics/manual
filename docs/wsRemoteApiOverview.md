# WebSocket remote API

The WebSocket remote API is one of [several ways an application can connect with CoppeliaSim](meansOfCommunication.md).

The WebSocket remote API allows you to control a simulation (or the simulator itself) from an external JavaScript application or remote client/server, via WebSocket. It offers all API functions also available via a CoppeliaSim script in [sim-1](apiFunctions-1.md): this includes all [regular API functions](apiFunctions.md) (i.e. sim.\* -type functions), but also all API functions provided by [plugins](plugins.md) (e.g. simOMPL.\*, simUI.\*, simIK.\*). The WebSocket remote API represents a very thin wrapper around the mentioned API functions, and can be used in a very similar way as from within a CoppeliaSim script.

The WebSocket remote API functions are interacting with CoppeliaSim via WebSocket and its [interface plugin](simWS/simWS.htm) to CoppeliaSim and the WS remote API [add-on](addOns.md). All this happens in a hidden fashion to the user. The remote API can let one or several external applications interact with CoppeliaSim in a [stepping](simulation.md#stepped) (i.e. *synchronized* with each simulation step) or non-stepping way (i.e. the normal operation mode), and even remote control of the simulator is supported (e.g. remotely loading a scene, starting, pausing or stopping a simulation for instance).

Here a very simple WebSocket remote API example:

```javascript
const log = (what) => $('#log').append(`${what}\n`);
(async () => {
    var client = new RemoteAPIClient('localhost', 23050, 'json');
    log('Connecting...');
    await client.websocket.open();
    log('Getting proxy object "sim"...');
    var sim = await client.require('sim');
    log('Calling sim.getObject("/Floor")...');
    var [h] = await sim.getObject('/Floor');
    log(`Result: ${h}`);
})();
```

See programming/wsRemoteApi folder or [its related repository](https://github.com/CoppeliaRobotics/wsRemoteApi) for examples.
