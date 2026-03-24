function sysCall_init()
    sim = require 'sim-2'
    json = require 'dkjson'
    cbor = require 'simCBOR'
    lfsx = require 'lfsx'

    infos = {}
    superclass = {sceneObject = 'object'}
    flags = {'readable', 'writable', 'removable', 'silent', 'deprecated', 'constant'}
    typemap = table.invert(table.filter(sim, {matchKeyPrefix = 'propertytype_', stripKeyPrefix = true}))

    addOnDir = lfsx.dirname(sim.self.addOnPath)

    allHandles = {
        sim.app,
        sim.scene,
        sim.app:createObject{objectType = 'collection'},
        sim.scene.mainScript,
        sim.scene:createObject{objectType = 'drawingObject'},
        sim.scene:createObject{objectType = 'dummy'},
        sim.scene:createObject{objectType = 'joint'},
        sim.scene:createObject{objectType = 'camera'},
        sim.scene:createObject{objectType = 'marker'},
        sim.scene:createObject{objectType = 'shape', mesh = {}},
        sim.scene:createObject{objectType = 'script'},
        sim.scene:createObject{objectType = 'forceSensor'},
        sim.scene:loadModel(lfsx.pathjoin(addOnDir, 'graph.simmodel.xml')), --sim.scene:createObject{objectType = 'graph'},
        sim.scene:createObject{objectType = 'light'},
        sim.scene:createObject{objectType = 'ocTree'},
        sim.scene:createObject{objectType = 'pointCloud'},
        sim.scene:createObject{objectType = 'proximitySensor'},
        sim.scene:createObject{objectType = 'visionSensor'},
        sim.scene:loadModel(lfsx.pathjoin(addOnDir, 'shape.simmodel.xml')).meshes[1], --sim.scene:createObject{objectType = 'shape', mesh = {texture = {resolution = {2, 2}, image = string.rep('\x00', 3 * 4), rgba = false}}}.meshes[1],
    }

    local foundInconsistentFlags = false
    for _, h in ipairs(allHandles) do
        local objectType = h.objectType
        local objectMetaInfo = json.decode(h.objectMetaInfo)
        superclass[objectType] = objectMetaInfo.superclass
        local ok, err = pcall(function()
            info = sim.getPropertiesInfos(h, {excludeFlags = 0})
        end)
        if not ok then
            error(string.format('target %d: %s', h.handle, err))
        end
        infos[objectType] = infos[objectType] or {}
        for pname, pinfo in pairs(info) do
            local pclass = pinfo.class or objectType
            local fullk = pclass .. '.' .. pname
            pinfo.type = typemap[pinfo.type]
            pinfo.flags.large = nil
            pinfo.flags.value = nil
            if pclass == 'app' and string.startswith(pname, 'namedParam.') then goto continue end
            if string.startswith(pname, 'customData.') then goto continue end
            if string.startswith(pname, 'signal.') then goto continue end
            if string.startswith(pname, 'refs.') then goto continue end
            if string.startswith(pname, 'origRefs.') then goto continue end
            infos[pclass] = infos[pclass] or {}
            if infos[pclass][pname] then
                if not table.eq(pinfo, infos[pclass][pname]) then
                    printf('inconsistent property info for %s.%s', pclass, pname)
                    print(infos[pclass][pname])
                    print(pinfo)
                    foundInconsistentFlags = true
                end
            else
                infos[pclass][pname] = pinfo
            end
            ::continue::
        end
    end
    assert(not foundInconsistentFlags, 'found inconsistent flags')

    -- XXX: drawing objects currently do not have any exposed property
    infos.drawingObject.cyclic = {type = 'bool'}
    infos.drawingObject.maxCnt = {type = 'int'}
    infos.drawingObject.overlay = {type = 'bool'}
    infos.drawingObject.parentUid = {type = 'long'}
    infos.drawingObject.size = {type = 'float'}
    infos.drawingObject.type = {type = 'string'}
    infos.drawingObject.points = {type = 'floatarray'}
    infos.drawingObject.quaternions = {type = 'floatarray'}
    infos.drawingObject.colors = {type = 'floatarray'}
    infos.drawingObject.appendPoints = {type = 'floatarray'}
    infos.drawingObject.appendQuaternions = {type = 'floatarray'}
    infos.drawingObject.appendColors = {type = 'floatarray'}

    -- XXX: temporary
    infos.joint.dynCtrlMode.enum = 'jointDynCtrlMode'
    infos.scene.simulationState.enum = 'simulationState'

    outputFile = {xml = sim.app.namedParam.output_xml}
    output = {}
    output.xml = {tag = 'object-classes', attrs = {}, children = {}}
    clss = table.keys(infos)
    table.sort(clss)
    for _, cls in ipairs(clss) do
        clsinfo = infos[cls]
        local clsnode = {tag = 'object-class', attrs = {name = cls, superclass = superclass[cls]}, children = {}}
        table.insert(output.xml.children, clsnode)
        ks = table.keys(clsinfo)
        table.sort(ks)
        for _, k in ipairs(ks) do
            info = clsinfo[k]
            local propnode = {tag = 'property', attrs = {name = k, type = info.type}, children = {}}
            flgs = {}
            local flgs_def = {
                readable = true,
                writable = true,
                removable = false,
                deprecated = false,
                silent = false,
                constant = false,
            }
            for flg, v in pairs(info.flags or {}) do
                if v ~= flgs_def[flg] then
                    table.insert(flgs, '"' .. flg .. '": ' .. (v and 'true' or 'false'))
                    propnode.attrs[flg] = (v and 'true' or 'false')
                end
            end
            if (infos[cls][k].handleType or '') ~= '' then
                propnode.attrs['handle-type'] = infos[cls][k].handleType
            end
            if (infos[cls][k].label or '') ~= '' then
                propnode.attrs.label = infos[cls][k].label
            end
            propnode.attrs.enum = infos[cls][k].enum
            propnode.attrs['deprecated-by'] = infos[cls][k]['deprecated-by']
            if (infos[cls][k].description or '') ~= '' then
                table.insert(propnode.children, {tag = 'description', attrs = {}, children = {infos[cls][k].description}})
            end
            table.insert(clsnode.children, propnode)
        end
    end
    output.xml = string.renderxml(output.xml, {'name', 'type', 'readable', 'writable', 'removable', 'silent'})
    for ext, fileName in pairs(outputFile) do
        local file = io.open(fileName, 'w')
        if file then
            file:write(output[ext])
            file:close()
        else
            print('Error: Could not open output file ' .. fileName)
        end
    end

    sim.app:quit()
end
