# Common types

The following types are commonly used in and around CoppeliaSim:

## <a id="bool"></a>bool

```python
True or False
```

```lua
true or false
```

## <a id="int"></a>int

```python
e.g. 1
```

```lua
e.g. 1
```

## <a id="float"></a>float

```python
e.g. 1.23
```

```lua
e.g. 1.23
```

## <a id="string"></a>string

```python
a str, e.g. 'hello'
```

```lua
e.g. 'hello'
```

## <a id="buffer"></a><a id="bufferArray"></a>buffer

```python
a bytes item, e.g. b'hello\0world'
```

```lua
e.g. tobuffer('hello\0world')
```

## <a id="handle"></a>sim.Object

```python
e.g. sim.Object(1), or 1
```

```lua
e.g. sim.Object(1), or 1
```

## <a id="luaObject"></a>Lua object

```python
a Lua object item
```

```lua
a Lua object item
```

## <a id="function"></a><a id="functionArray"></a>func

```python
function or reference to a function
```

```lua
function or reference to a function
```

## <a id="color"></a><a id="colorArray"></a>color

```python
a tuple of 4 floats, e.g. (255, 255, 255, 128)
```

```lua
e.g. Color('red') or Color('#ffffff80') or {255, 255, 255, 128}
```

## <a id="enum"></a><a id="enumArray"></a>enum

```python
an int, e.g. 0
```

```lua
e.g. 0 or sim.app.getEnumInfo('physicsEngine')['bullet']
```

## <a id="any"></a><a id="anyArray"></a>any

```python
any type
```

```lua
any type
```

## <a id="map"></a>map

```python
a dict, e.g. {'John': 1, 'Bella': 2}
```

```lua
e.g. {'John' = 1, 'Bella' = sim.Object(2)}
```

## <a id="vector"></a><a id="vectorArray"></a>vector

```python
e.g. np.array([[1.0], [2.0]]), dtype=float)
```

```lua
e.g. simEigen.Vector({1.0, 2.0}) or {1.0, 2.0}
```

## <a id="vector3"></a><a id="vector3Array"></a>vector3

```python
e.g. np.array([[1.0], [2.0], [3.0]]), dtype=float)
```

```lua
e.g. simEigen.Vector({1.0, 2.0, 3.0}) or {1.0, 2.0, 3.0}
```

## <a id="quaternion"></a><a id="quaternionArray"></a>quaternion

```python
e.g. np.array([0.0, 0.0, 0.0, 1.0]), dtype=float)
```

```lua
e.g. simEigen.Quaternion({0.0, 0.0, 0.0, 1.0}) or {0.0, 0.0, 0.0, 1.0}
```

## <a id="pose"></a><a id="poseArray"></a>pose

```python
e.g. np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]), dtype=float)
```

```lua
e.g. simEigen.Pose({0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0}) or {0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0}
```

## <a id="matrix"></a><a id="matrixArray"></a>matrix

```python
e.g. np.array([[1.0, 2.0], [3.0, 4.0]]), dtype=float)
```

```lua
e.g. simEigen(2, 2, {1.0, 2.0, 3.0, 4.0}) or {{1.0, 2.0}, {3.0, 4.0}} or sometimes {1.0, 2.0, 3.0, 4.0}
```

## <a id="boolArray"></a>bool[]

```python
e.g. np.array([True, False], dtype=bool)
```

```lua
e.g. {true, false}
```

## <a id="intArray"></a>int[]

```python
e.g. np.array([1, 2], dtype=int)
```

```lua
e.g. {1, 2}
```

## <a id="floatArray"></a>float[]

```python
e.g. np.array([1.23, 2.34], dtype=float)
```

```lua
e.g. {1.23, 2.34}
```

## <a id="stringArray"></a>string[]

```python
e.g. ['hello', 'world']
```

```lua
e.g. {'hello', 'world'}
```

## <a id="handleArray"></a>sim.Object[]

```python
e.g. [sim.Object(1), sim.Object(2)] or [1, 2]
```

```lua
e.g. sim.ObjectArray({1, 2}) or {sim.Object(1), sim.Object(2)}
```

## <a id="luaObjectArray"></a>Lua object array

```python
a list of Lua object items
```

```lua
table of Lua object items
```

## <a id="mapArray"></a>map[]

```python
a list of dict items, e.g. [{'John': 1, 'Bella': 2}, {'output': 'hello'}]
```

```lua
e.g. {{'John' = 1, 'Bella' = sim.Object(2)}, {'output' = 'hello'}}
```
