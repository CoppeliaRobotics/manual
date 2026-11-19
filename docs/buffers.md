# Buffers

A Lua string does not differentiate between text and binary data, which is fine as long as we stay in Lua world. This however poses various problems when Lua-generated data is read/received via a programming language that makes the distinction between those two types of data (e.g. Python). Assigning specific types by relying on some heuristics (and/or function calltip inspection) works up to a certain degree, but does not cover all cases (e.g. is an empty string intended as empty text or empty binary data?).

For the above reasons, buffers have been introduced in CoppeliaSim V4.7 to be able (if desired) to clearly identify buffers, i.e. binary data (versus Lua strings). This is done with the newly introduced *tobuffer* function:

```lua
local buffer = tobuffer('Hello') -- represents binary data
```

Buffers are implemented via a specific metatable, and identify as *table*, with the *type* function. One should use *isbuffer* to make the distinction between buffer and non-buffer:

```lua
isbuffer(tobuffer('Hello')) --> returns true
isbuffer('Hello') --> returns false
isbuffer('\0\0\0') --> returns false
```

The same operations on/with Lua strings are also supported with buffers (but most return a Lua string, not a buffer), e.g.:

```lua
#tobuffer('Hello') --> returns 5
local buffer = tobuffer('Hello') .. tobuffer(' World!') --> buffer is buffer 'Hello World!'
buffer:str() --> returns string 'Hello World!'
buffer:gsub('World', 'Planet') --> returns string 'Hello Planet!'
string.gsub(buffer, 'World', 'Planet') --> returns string 'Hello Planet!'
```

Mixed operations are also supported, e.g.:

```lua
tobuffer('Hello') .. ' World!' --> returns buffer 'Hello World!'
'Hello' .. tobuffer(' World!') --> returns buffer 'Hello World!'
```

Beware that comparison between a string and a buffer always resolves to **false**. Remember that buffers identify as table when evaluated with the type function. This can lead to [potential compatibility issues](compatibility.md#buffers).
