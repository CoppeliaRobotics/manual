# sim.getExtensionString

Retrieves a string that describes additional environment or object properties, mainly used by extension plugins.

## Synopsis

```lua
string theString = sim.getExtensionString(int objectHandle, int index, string key = nil)
```

```python
string theString = sim.getExtensionString(int objectHandle, int index, string key = None)
```

## Parameters

- **objectHandle**: handle of an object, or -1 if you wish to retrieve the extension string of the environment
- **index**: keep to -1, unless the object is a shape, and you wish to retrieve the extension string of a shape component (since a shape can be a compound of several other shapes)
- **key**: optional key indicating what value to retrieve. If None/nil is specified, then the whole extension string is returned. Keys should have the form of *key@parentKey@...@parentKey*. To retrieve the *shadow enabled* value of extension string "povray{ shadow {true} fadeXDist {0.00}}", specify following key: *shadow@povray*. The key is case sensitive.

## Return values

- **theString**: the desired string
