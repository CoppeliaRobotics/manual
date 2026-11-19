# Data manipulation/transformation

Data in CoppeliaSim can be transformed in various ways:

- [Data packing/unpacking](#packing)
- [Linear algebra functionality](#algebra)
- [Image processing](syntheticVision.md)
- [Path data transformation](apiFunctions.md#paths)
- [sim.transformBuffer](sim/simTransformBuffer.htm)
- Other [matrix/transformation related functions](apiFunctions.md#coordinatesAndTransformations)

<a id="packing"></a>The following example illustrates how to pack/unpack data. Other functions can be found here:

```python
#python
# using sim-2

# Refer to the various Python packages, e.g.:
import struct
import base64
import cbor2 as cbor

# One can also use some built-in functions:
base64Buffer = sim.app:transformBuffer(binaryPackedData, 'uint8', 'base64')
originalBuffer = sim.app:transformBuffer(base64Buffer, 'base64', 'uint8')

# Packing/unpacking random data, in CoppeliaSim format:
data = [1, 'hello', {'value': 'world'}, [1, [2, 3]]]
binaryPackedData = sim.app:pack(data)
data = sim.app:unpack(binaryPackedData)
```

```lua
--lua
sim = require('sim-2')

-- Packing/unpacking specific type of data:
local data = {1, 2, 3}
local binaryPackedData = sim.app:packArray(data, {type = 'double'}) -- binary packing
data = sim.unpackArray(binaryPackedData, {type = 'double'}) -- binary unpacking

base16 = require('base16')
local base16PackedData = base16.encode(binaryPackedData) -- base16 encoding
binaryPackedData = base16.decode(base16PackedData) -- base16 decoding

base64 = require('base64')
local base64PackedData = base64.encode(binaryPackedData) -- base64 encoding
binaryPackedData = base64.decode(base64PackedData) -- base64 decoding

local base64Buffer = sim.app:transformBuffer(binaryPackedData, 'uint8', 'base64')
local originalBuffer = sim.app:transformBuffer(base64Buffer, 'base64', 'uint8')

-- Packing/unpacking random data:
local data = {1, 'hello', {value = 'world'}, {1, {2, 3}}}
local binaryPackedData = sim.app:pack(data) -- binary packing
data = sim.app:unpack(binaryPackedData) -- binary unpacking

cbor = require('org.conman.cbor')
local cborPackedData = cbor.encode(data) -- cbor encoding
data = cbor.decode(cborPackedData) -- cbor decoding
```

<a id="algebra"></a>The following example illustrates usage of linear algebra functionality:

```python
#python

# Refer to the numpy package for instance:
import numpy
```

```lua
--lua
sim = require('sim-2')
import('simEigen', '*')

-- Get the absolute poses of an object and its parent:
local absObj = object.worldPose
local absParentObj = object.parent.worldPose

-- Compute the relative pose of the object:
local relObj = absParentObj:inv() * absObj

-- Get the relative pose of the object directly:
local relObj2 = object:getPose({relativeToObject = object.parent})

-- Check that both poses are same:
print( (relObj:totransform() - relObj2:totransform()):abs():maxcoeff() )
```

For the full linear algebra functionality, refer to the [simEigen plugin](simEigen/simEigen.htm).
