dofile('wb_usr.lua')
json = require "dkjson"

function conv(x)
    local anchors={}
    local pp = '../en'
    local f = io.open(pp..'/'..x.link, "r")
    if f then
        local c = f:read("*all")
        f:close()
        for w in string.gmatch(c, '<a name="(%w+)"') do
            table.insert(anchors,w)
        end
    end
    local r={file=x.link, title=x.name.en, anchors=anchors, children={}}
    if x.folder ~= nil then
        for i=1,#x.folder do
            table.insert(r.children, conv(x.folder[i]))
        end
    end
    return r
end

--print(wb_usr.tree, #wb_usr.tree)
---[[
local c = json.encode(conv(wb_usr.tree))
local file = io.open('manual.json', 'w')
file:write(c)
file:close()
--]]
print('Done!')