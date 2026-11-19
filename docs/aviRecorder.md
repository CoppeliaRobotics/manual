# Video exporter

The video recorder from previous CoppeliaSim versions is not supported anymore. You can however get a similar functionality via a third-party tool, or by actively acquiring frames ([camera:getImage](sim/camera_getImage.htm)) and saving them to disk ([app:saveImage](sim/app_saveImage.htm)), and later assembling them into a video sequence via e.g. [ffmpeg](https://ffmpeg.org/).

Frame acquisition:

```lua
--lua

function sysCall_init()
    sim = require('sim-2')
    camera = sim.self:getObject('..')
    resolution = {640, 480}
    path = 'c:/images'
    filePrefix = 'frame_'
    ext = 'png'
    nb = 0
end

function sysCall_sensing()
    local img = camera:getImage({resolution = resolution})
    local fn = path .. '/' .. filePrefix .. string.format('%04d', nb) .. '.' .. ext
    sim.app:saveImage(img, resolution, fn)
    nb = nb + 1
end
```

ffmpeg installation:

```
Windows:
$ choco install ffmpeg

Linux:
$ sudo apt install ffmpeg

Mac:
$ brew install ffmpeg
```

Video sequence creation (as H.265 with a framerate of 30 f/s):

```
ffmpeg -framerate 30 -i frame_%04d.png -c:v libx265 -pix_fmt yuv420p -crf 18 out.mp4
```
