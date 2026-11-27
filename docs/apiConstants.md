# regular API constants ([sim-2](apisOverview.md))

This page lists all constants/enums related to the regular API, version 2 (version 1 can be found [here](apiConstants-1.md)).

- [Lua constants](#lua)
- [C constants](#c)

## <a id="lua"></a>Lua constants

### <a id="singletons"></a>Singletons

- `sim.app`
- `sim.scene`
- `sim.self`

### <a id="appFlavor"></a>App flavor

- `sim.appFlavor.edu`
- `sim.appFlavor.pro`
- `sim.appFlavor.lite`

### <a id="forceSensorFilter"></a>Force sensor filter type

- `sim.forceSensorFilter.average`
- `sim.forceSensorFilter.median`

### <a id="handle"></a>Special argument values

- `sim.handle.all`
- `sim.handle.app`
- `sim.handle.scene`
- `sim.handle.self`

### <a id="headlessMode"></a>Headless mode

- `sim.headlessMode.disabled`
- `sim.headlessMode.emulated`
- `sim.headlessMode.enabled`

### <a id="jointMode"></a>Joint modes

- `sim.jointMode.kinematic`
- `sim.jointMode.dependent`
- `sim.jointMode.dynamic`

### <a id="jointDynamicsCtrlMode"></a>Dynamic joint control modes

- `sim.jointDynamicsCtrlMode.free`
- `sim.jointDynamicsCtrlMode.force`
- `sim.jointDynamicsCtrlMode.velocity`
- `sim.jointDynamicsCtrlMode.position`
- `sim.jointDynamicsCtrlMode.spring`
- `sim.jointDynamicsCtrlMode.custom`

### <a id="physicsEngine"></a>Physics engine

- `sim.physicsEngine.bullet`
- `sim.physicsEngine.ode`
- `sim.physicsEngine.newton`
- `sim.physicsEngine.vortex`
- `sim.physicsEngine.mujoco`

### <a id="platform"></a>Platform

- `sim.platform.linux`
- `sim.platform.macos`
- `sim.platform.windows`

### <a id="primitiveType"></a>Primitive shape types

- `sim.primitiveType.none`
- `sim.primitiveType.plane`
- `sim.primitiveType.disc`
- `sim.primitiveType.cuboid`
- `sim.primitiveType.spheroid`
- `sim.primitiveType.cylinder`
- `sim.primitiveType.cone`
- `sim.primitiveType.capsule`
- `sim.primitiveType.heightfield`

### <a id="renderMode"></a>Render modes

- `sim.renderMode.openGl`
- `sim.renderMode.colorCoded`
- `sim.renderMode.openGl3`
- `sim.renderMode.openGl3ColorCoded`
- `sim.renderMode.povray`

### <a id="scriptExecOrder"></a>Script execution priority

- `sim.scriptExecOrder.first`
- `sim.scriptExecOrder.normal`
- `sim.scriptExecOrder.last`

### <a id="simulationState"></a>Simulation state

- `sim.simulationState.stopped`
- `sim.simulationState.paused`
- `sim.simulationState.running`
- `sim.simulationState.lastbeforestop`

### <a id="scriptState"></a>Script state

- `sim.scriptState.unloaded`
- `sim.scriptState.initialized`
- `sim.scriptState.ended`
- `sim.scriptState.suspended`

### <a id="stringType"></a>String types

- `sim.stringType.binary`
- `sim.stringType.buffer`
- `sim.stringType.text`

### <a id="textureApplyMode"></a>Texture apply mode

- `sim.textureApplyMode.add`
- `sim.textureApplyMode.decal`
- `sim.textureApplyMode.modulate`

### <a id="verbosity"></a>Verbosity

- `sim.verbosity.none`
- `sim.verbosity.errors`
- `sim.verbosity.warnings`
- `sim.verbosity.loadinfos`
- `sim.verbosity.dflt`
- `sim.verbosity.infos`
- `sim.verbosity.questions`
- `sim.verbosity.scriptErrors`
- `sim.verbosity.scriptWarnings`
- `sim.verbosity.scriptInfos`
- `sim.verbosity.useGlobal`
- `sim.verbosity.debug`
- `sim.verbosity.traceLua`
- `sim.verbosity.traceAll`

### <a id="jointType"></a>Joint types

- `sim.jointType.revolute`
- `sim.jointType.prismatic`
- `sim.jointType.spherical`

### <a id="dummyType"></a>Dummy types

- `sim.dummyType.neutral`
- `sim.dummyType.assembly`
- `sim.dummyType.dynLoopClosure`
- `sim.dummyType.dynTendon`

### <a id="proximitySensorType"></a>Proximity sensor types

- `sim.proximitySensorType.cone`
- `sim.proximitySensorType.cylinder`
- `sim.proximitySensorType.disc`
- `sim.proximitySensorType.pyramid`
- `sim.proximitySensorType.ray`

### <a id="shapeType"></a>Shape types

- `sim.shapeType.simple`
- `sim.shapeType.compound`

### <a id="lightType"></a>Light types

- `sim.lightType.directional`
- `sim.lightType.omnidirectional`
- `sim.lightType.spot`

### <a id="propertyType"></a>Property types

- `sim.propertyType.null`
- `sim.propertyType.boolean`
- `sim.propertyType.int32`
- `sim.propertyType.int64`
- `sim.propertyType.real`
- `sim.propertyType.string`
- `sim.propertyType.buffer`
- `sim.propertyType.handle`
- `sim.propertyType.vector3`
- `sim.propertyType.quaternion`
- `sim.propertyType.pose`
- `sim.propertyType.matrix`
- `sim.propertyType.color`
- `sim.propertyType.method`
- `sim.propertyType.int32Array`
- `sim.propertyType.int64Array`
- `sim.propertyType.realArray`
- `sim.propertyType.handleArray`
- `sim.propertyType.stringArray`
- `sim.propertyType.array`
- `sim.propertyType.table`
- `sim.propertyType.map`
- `sim.propertyType.group`
- `sim.propertyType.enumeration`

### <a id="propertyFlags"></a>Property flags

- `sim.propertyInfoFlags.notWritable`
- `sim.propertyInfoFlags.notReadable`
- `sim.propertyInfoFlags.removable`
- `sim.propertyInfoFlags.modelHashExclude`
- `sim.propertyInfoFlags.deprecated`
- `sim.propertyInfoFlags.silent`
- `sim.propertyInfoFlags.constant`
- `sim.propertyInfoFlags.largeData`
- `sim.propertyInfoFlags.retMethodsOnly`

### <a id="ruckig"></a><a id="RMLFunctions"></a><a id="ruckigFunctions"></a>Ruckig Online Trajectory Generator constants

- `sim.ruckig.phaseSync`
- `sim.ruckig.timeSync`
- `sim.ruckig.noSync`

### <a id="markerType"></a>Marker types

- `sim.markerType.cubes`
- `sim.markerType.custom`
- `sim.markerType.cylinders`
- `sim.markerType.discs`
- `sim.markerType.lines`
- `sim.markerType.points`
- `sim.markerType.spheres`
- `sim.markerType.squares`
- `sim.markerType.triangles`

### <a id="markerOptions"></a>Marker options

- `sim.markerOptions.local`
- `sim.markerOptions.cyclic`
- `sim.markerOptions.overlay`
- `sim.markerOptions.notShaded`
- `sim.markerOptions.tube`
- `sim.markerOptions.axis`

### <a id="materialComponent"></a>Material component

- `sim.materialComponent.diffuse`
- `sim.materialComponent.lightDiffuse`
- `sim.materialComponent.specular`
- `sim.materialComponent.emission`

### <a id="bulletSolverType"></a>Bullet solver types

- `sim.bulletConstrSolverType.sequentialImpulse`
- `sim.bulletConstrSolverType.nncg`
- `sim.bulletConstrSolverType.dantzig`
- `sim.bulletConstrSolverType.projectedGaussSeidel`

### <a id="vortexBodyFrictionModel"></a>Vortex friction models

- `sim.vortexBodyFrictionModel.box`
- `sim.vortexBodyFrictionModel.scaledBox`
- `sim.vortexBodyFrictionModel.propLow`
- `sim.vortexBodyFrictionModel.propHigh`
- `sim.vortexBodyFrictionModel.scaledBoxFast`
- `sim.vortexBodyFrictionModel.neutral`
- `sim.vortexBodyFrictionModel.none`

## <a id="c"></a>C / C++ constants

### <a id="generalObjectTypes"></a>General object types

- `sim_objecttype_app`
- `sim_objecttype_scene`
- `sim_objecttype_sceneobject`
- `sim_objecttype_collection`
- `sim_objecttype_script`
- `sim_objecttype_mesh`
- `sim_objecttype_customobject`
- `sim_objecttype_interfacestack`
- `sim_objecttype_texture`

### <a id="sceneObjectTypes"></a>Scene object types

- `sim_sceneobject_shape`
- `sim_sceneobject_joint`
- `sim_sceneobject_graph`
- `sim_sceneobject_camera`
- `sim_sceneobject_light`
- `sim_sceneobject_dummy`
- `sim_sceneobject_proximitysensor`
- `sim_sceneobject_octree`
- `sim_sceneobject_pointcloud`
- `sim_sceneobject_visionsensor`
- `sim_sceneobject_forcesensor`
- `sim_sceneobject_scriptObject`
- `sim_sceneobject_marker`
- `sim_sceneobject_customSceneObject`

### <a id="sceneObjectSubTypes"></a>Scene object sub-types

- `sim_light_omnidirectional`
- `sim_light_spot`
- `sim_light_directional`
- `sim_joint_revolute`
- `sim_joint_prismatic`
- `sim_joint_spherical`
- `sim_shape_simple`
- `sim_shape_compound`
- `sim_proximitysensor_ray`
- `sim_proximitysensor_pyramid`
- `sim_proximitysensor_cylinder`
- `sim_proximitysensor_disc`
- `sim_proximitysensor_cone`

### <a id="simulatorMessages"></a>Simulator messages (messages dispatched to plugins)

- `sim_message_eventcallback_instancepass`
  Called once every main client application loop pass. auxData[0] contains event flags of events that happened since last time. If you react to some of the event flags below, make sure you do not react to their equivalent event callback message (e.g. sim_message_eventcallback_sceneloaded is similar to the bit3 set below).
  - bit0 set: object(s) erased
  - bit1 set: object(s) created
  - bit2 set: model loaded
  - bit3 set: scene loaded
  - bit4 set: undo called
  - bit5 set: redo called
  - bit6 set: scene switched (react to this message in a similar way as you would react to a full scene content change)
  - bit7 set: edit mode active. This is not an event flag, but a state flag
  - bit8 set: object(s) scaled
  - bit9 set: selection state changed. (different objects are selected now)
  - bit10 set: key pressed
  - bit11 set: simulation started
  - bit12 set: simulation ended
- `sim_message_eventcallback_instanceswitch`
  Scene was switched (react to this message in a similar way as you would react to a full scene content change)
  - auxData[0]: do not use
  - auxData[1]=current scene unique ID
  - auxData[2]=previous scene unique ID
- `sim_message_eventcallback_instanceabouttoswitch`
  We are about to switch to a different scene
  - auxData[0]: do not use
  - auxData[1]=next scene unique ID
  - auxData[2]=current scene unique ID
- `sim_message_eventcallback_scriptstateabouttobedestroyed`
  The specified script state is about to be destroyed
  - auxData[0]: script handle
  - auxData[1]: script UID
- `sim_message_eventcallback_scriptabouttobedestroyed`
  The specified script is about to be destroyed
  - auxData[0]: script handle
  - auxData[1]: script UID
- `sim_message_eventcallback_menuitemselected`
  Called from the UI thread
  - auxData[0]=handle of the item
  - auxData[1]=state of the item
- `sim_message_eventcallback_scenesave`
  About to save a scene
- `sim_message_eventcallback_modelsave`
  About to save a model (current selection will be saved)
- `sim_message_eventcallback_abouttoundo`
  The undo button was hit and a previous state is about to be restored
- `sim_message_eventcallback_undoperformed`
  The undo button was hit and a previous state was restored
- `sim_message_eventcallback_abouttoredo`
  The redo button was hit and a future state is about to be restored
- `sim_message_eventcallback_redoperformed`
  The redo button was hit and a future state was restored
- `sim_message_eventcallback_simulationabouttostart`
  Simulation will start
- `sim_message_eventcallback_simulationabouttoend`
  Simulation will end
- `sim_message_eventcallback_simulationended`
  Simulation has ended
- `sim_message_eventcallback_simulationinit`
  Called just before/after the main script's corresponding init section.
  - auxData[0]: 0 if called before, 1 if called after
- `sim_message_eventcallback_simulationactuation`
  Called just before/after the main script's corresponding actuation section.
  - auxData[0]: 0 if called before, 1 if called after
  - auxData[1]: simulation time in ms
- `sim_message_eventcallback_simulationsensing`
  Called just before/after the main script's corresponding sensing section.
  - auxData[0]: 0 if called before, 1 if called after
  - auxData[1]: simulation time in ms
- `sim_message_eventcallback_simulationcleanup`
  Called just before/after the main script's corresponding cleanup section.
  - auxData[0]: 0 if called before, 1 if called after
- `sim_message_eventcallback_keypress`
  Called from the UI thread
  - auxData[0]=key
  - auxData[1]=ctrl and shift key state
- `sim_message_eventcallback_refreshdialogs`
  Called from the UI thread, just before dialogs are refreshed in CoppeliaSim
  - auxData[0]=refresh degree (0=light, 1=medium, 2=full)
- `sim_message_eventcallback_sceneloaded`
  Called after a scene was loaded
- `sim_message_eventcallback_modelloaded`
  Called after a model was loaded
- `sim_message_eventcallback_mainscriptabouttobecalled`
  Called just before the main script is called. A plugin can write a value different from -1 into auxData[0] to temporarily halt simulation progress (e.g. stepping mode)
- `sim_message_eventcallback_moduleentry`
  Called when a custom menu item is selected. auxData[0]=item handle.
- `sim_message_eventcallback_events`
  Called to dispatch events. auxPointer is a const unsigned char\*, holding the CBOR-coded events. auxData[0] indicates the number of events

### <a id="specialHandleFlags"></a>Special handle flags

- `sim_handleflag_assembly`
- `sim_handleflag_model`
- `sim_handleflag_rawvalue`
- `sim_handleflag_togglevisibility`
- `sim_handleflag_greyscale`
- `sim_handleflag_depthbuffermeters`
- `sim_handleflag_depthbuffer`
- `sim_handleflag_abscoords`
- `sim_handleflag_codedstring`
- `sim_handleflag_keeporiginal`
- `sim_handleflag_camera`
- `sim_handleflag_axis`
- `sim_handleflag_silenterror`
- `sim_handleflag_resetforce`
- `sim_handleflag_resettorque`
- `sim_handleflag_absolutecoords`
- `sim_handleflag_relativecoords`
- `sim_handleflag_wxyzquat`
- `sim_handleflag_reljointbaseframe`
- `sim_handleflag_addmultiple`

### <a id="verbosity-2"></a>Verbosity

- `sim_verbosity_useglobal`
- `sim_verbosity_none`
- `sim_verbosity_errors`
- `sim_verbosity_warnings`
- `sim_verbosity_loadinfos`
- `sim_verbosity_questions`
- `sim_verbosity_scripterrors`
- `sim_verbosity_scriptwarnings`
- `sim_verbosity_scriptinfos`
- `sim_verbosity_infos`
- `sim_verbosity_debug`
- `sim_verbosity_trace`
- `sim_verbosity_tracelua`
- `sim_verbosity_traceall`
- `sim_verbosity_default`

### <a id="startupOptions"></a>Bit-coded start-up options

- `sim_gui_menubar`
- `sim_gui_popups`
- `sim_gui_toolbar1`
- `sim_gui_toolbar2`
- `sim_gui_hierarchy`
- `sim_gui_infobar`
- `sim_gui_statusbar`
- `sim_gui_scripteditor`
- `sim_gui_scriptsimulationparameters`
- `sim_gui_dialogs`
- `sim_gui_browser`
- `sim_gui_all`
- `sim_gui_headless` (overrides all other GUI flags)

### <a id="scriptType"></a>Script types

- `sim_scripttype_main`
- `sim_scripttype_simulation`
- `sim_scripttype_addon`
- `sim_scripttype_customization`
- `sim_scripttype_sandbox`
- `sim_scripttype_passive`

### <a id="colorComponents"></a>Color components

- `sim_colorcomponent_ambient_diffuse` (only for objects)
- `sim_colorcomponent_diffuse` (only for lights)
- `sim_colorcomponent_specular`
- `sim_colorcomponent_emission` (only for objects)
- `sim_colorcomponent_transparency` (only for objects)
- `sim_colorcomponent_auxiliary` (only for objects)

### <a id="volumeTypes"></a>Proximity sensor volume types

- `sim_volume_pyramid`
- `sim_volume_cylinder`
- `sim_volume_disc`
- `sim_volume_cone`
- `sim_volume_ray`
- `sim_volume_randomizedray`

### <a id="stringTypes"></a>String types

- `sim_string_text`
- `sim_string_binary`
- `sim_string_buffer`

### <a id="stackItemTypes"></a>Stack item types

- `sim_stackitem_null`
- `sim_stackitem_bool`
- `sim_stackitem_integer`
- `sim_stackitem_double`
- `sim_stackitem_string`
- `sim_stackitem_matrix`
- `sim_stackitem_table`
- `sim_stackitem_func`
- `sim_stackitem_userdat`
- `sim_stackitem_thread`
- `sim_stackitem_lightuserdat`

### <a id="stackTableInfo"></a>Stack table info

- `sim_stack_table_circular_ref`
- `sim_stack_table_not_table`
- `sim_stack_table_map`
- `sim_stack_table_empty`

### Simulation status

- `sim_simulation_stopped`
- `sim_simulation_paused`
- `sim_simulation_running`
- `sim_simulation_lastbeforestop`

### Property types

- `sim_propertytype_null`
- `sim_propertytype_bool`
- `sim_propertytype_int`
- `sim_propertytype_long`
- `sim_propertytype_float`
- `sim_propertytype_string`
- `sim_propertytype_buffer`
- `sim_propertytype_vector3`
- `sim_propertytype_quaternion`
- `sim_propertytype_pose`
- `sim_propertytype_matrix`
- `sim_propertytype_color`
- `sim_propertytype_intarray2`
- `sim_propertytype_intarray`
- `sim_propertytype_floatarray`
- `sim_propertytype_table`
- `sim_propertytype_array`
- `sim_propertytype_map`
- `sim_propertytype_handle`
- `sim_propertytype_handlearray`
- `sim_propertytype_stringarray`
- `sim_propertytype_group`
- `sim_propertytype_enum`
- `sim_propertytype_object`
- `sim_propertytype_objectarray`
- `sim_propertytype_objectmap`

### Property flags

- `sim_propertyinfo_notwritable`
- `sim_propertyinfo_notreadable`
- `sim_propertyinfo_removable`
- `sim_propertyinfo_modelhashexclude`
- `sim_propertyinfo_deprecated`
- `sim_propertyinfo_silent`
- `sim_propertyinfo_constant`
- `sim_propertyinfo_largedata`

### Script execution priority

- `sim_scriptexecorder_first`
- `sim_scriptexecorder_normal`
- `sim_scriptexecorder_last`

### Special argument values

- `sim_handle_absolute`
- `sim_handle_all`
- `sim_handle_all_except_explicit`
- `sim_handle_self`
- `sim_handle_main_script`
- `sim_handle_tree`
- `sim_handle_chain`
- `sim_handle_single`
- `sim_handle_default`
- `sim_handle_all_except_self`
- `sim_handle_parent`
- `sim_handle_scene`
- `sim_handle_app`
- `sim_handle_appstorage`
- `sim_handle_inverse`

### Joint modes

- `sim_jointmode_kinematic`
- `sim_jointmode_dependent`
- `sim_jointmode_dynamic`

### Dynamic joint control modes

- `sim_jointdynctrl_free`
- `sim_jointdynctrl_force`
- `sim_jointdynctrl_velocity`
- `sim_jointdynctrl_position`
- `sim_jointdynctrl_spring`
- `sim_jointdynctrl_callback`

### Primitive shape types

- `sim_primitiveshape_none`
- `sim_primitiveshape_plane`
- `sim_primitiveshape_disc`
- `sim_primitiveshape_cuboid`
- `sim_primitiveshape_spheroid`
- `sim_primitiveshape_cylinder`
- `sim_primitiveshape_cone`
- `sim_primitiveshape_capsule`
- `sim_primitiveshape_heightfield`

### Dummy types

- `sim_dummytype_default`
- `sim_dummytype_assembly`
- `sim_dummytype_dynloopclosure`
- `sim_dummytype_dyntendon`

### Physics engine types

- `sim_physics_bullet`
- `sim_physics_ode`
- `sim_physics_newton`
- `sim_physics_vortex`
- `sim_physics_mujoco`

## <a id="navigationModes"></a>Mouse navigation and selection modes

- `sim_navigation_passive`
- `simnavigation_camerashift`
- `sim_navigation_camerarotate`
- `sim_navigation_camerazoom`
- `sim_navigation_cameratilt`
- `sim_navigation_cameraangle`
- `sim_navigation_objectshift`
- `sim_navigation_objectrotate`

  Bit-combine the following values and add them to one of the above values for a valid navigation mode:
  - `sim_navigation_clickselection`
  - `sim_navigation_ctrlselection`
  - `sim_navigation_shiftselection`
  - `sim_navigation_camerazoomwheel`
  - `sim_navigation_camerarotatemiddlebutton`

## <a id="moduleInfos"></a><a id="pluginInfos"></a>Plugin infos

- `sim_plugininfo_extversionstr`
- `sim_plugininfo_builddatestr`
- `sim_plugininfo_extversionint`
- `sim_plugininfo_verbosity` See the various [verbosity levels](#verbosity-2)
- `sim_plugininfo_statusbarverbosity` See the various [verbosity levels](#verbosity-2)

## <a id="streamTransformations"></a>Graph stream transformations

- `sim_stream_transf_raw`
- `sim_stream_transf_derivative`
- `sim_stream_transf_integral`
- `sim_stream_transf_cumulative`

## <a id="textureMappingModes"></a>Texture mapping modes

- `sim_texturemap_plane`
- `sim_texturemap_cylinder`
- `sim_texturemap_sphere`
- `sim_texturemap_cube`
