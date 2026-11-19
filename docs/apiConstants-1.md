# regular API constants

## <a id="generalObjectTypes"></a>General object types

- `sim.objecttype_sceneobject`
- `sim.objecttype_collection`
- `sim.objecttype_mesh`
- `sim.objecttype_texture`
- See also the
- function

## <a id="sceneObjectTypes"></a>Scene object types

- `sim.sceneobject_shape`
- `sim.sceneobject_joint`
- `sim.sceneobject_graph`
- `sim.sceneobject_camera`
- `sim.sceneobject_light`
- `sim.sceneobject_dummy`
- `sim.sceneobject_proximitysensor`
- `sim.sceneobject_octree`
- `sim.sceneobject_pointcloud`
- `sim.sceneobject_visionsensor`
- `sim.sceneobject_forcesensor`
- `sim.sceneobject_script`
- See also the
- and
- functions

## <a id="sceneObjectSubTypes"></a>Scene object sub-types

- `sim.light_omnidirectional`
- `sim.light_spot`
- `sim.light_directional`
- `sim.joint_revolute`
- `sim.joint_prismatic`
- `sim.joint_spherical`
- `sim.shape_simple`
- `sim.shape_compound`
- `sim.proximitysensor_ray`
- `sim.proximitysensor_pyramid`
- `sim.proximitysensor_cylinder`
- `sim.proximitysensor_disc`
- `sim.proximitysensor_cone`

## <a id="simulatorMessages"></a>Simulator messages

- The following messages can be queried from a script, by calling the [sim.getSimulatorMessage](sim/simGetSimulatorMessage.htm) function:
- `sim.message_model_loaded`
- `sim.message_scene_loaded`
- `sim.message_keypress`
  auxData[0]=key, auxData[1]=ctrl and shift key state
- The following messages can be queried from the CoppeliaSim client application (and only from the client application!), by calling the [simGetSimulatorMessage](sim/simGetSimulatorMessage.htm) function:
- `sim_message_simulation_start_resume_request`
  The user wishes to start/resume a simulation. See also the [simStartSimulation](sim/simStartSimulation.htm) function
- `sim_message_simulation_pause_request`
  The user wishes to pause a simulation. See also the [simPauseSimulation](sim/simPauseSimulation.htm) function
- `sim_message_simulation_stop_request`
  The user wishes to stop a simulation. See also the [simStopSimulation](sim/simStopSimulation.htm) function
- The following messages are dispatched to the [plugins](plugins.md) (refer to the plugin [simMsg entry point](plugins.md)):
- `sim_message_eventcallback_instancepass`
  Called once every main client application loop pass. auxData[0] contains event flags of events that happened since last time. If you react to some of the event flags below, make sure you do not react to their equivalent event callback message (e.g. sim_message_eventcallback_sceneloaded is similar to the bit3 set below)
- bit0 set: object(s) erased
  bit1 set: object(s) created
- bit2 set: model loaded
  bit3 set: scene loaded
- bit4 set: undo called
  bit5 set: redo called
- bit6 set: scene switched (react to this message in a similar way as you would react to a full scene content change)
  bit7 set: edit mode active. This is not an event flag, but a state flag
- bit8 set: object(s) scaled
  bit9 set: selection state changed. (different objects are selected now)
- bit10 set: key pressed
  bit11 set: simulation started
- bit12 set: simulation ended
- `sim_message_eventcallback_instanceswitch`
  scene was switched (react to this message in a similar way as you would react to a full scene content change)
- auxData[0]: do not use
  auxData[1]=current scene unique ID
- auxData[2]=previous scene unique ID
- `sim_message_eventcallback_instanceabouttoswitch`
  we are about to switch to a different scene
- auxData[0]: do not use
  auxData[1]=next scene unique ID
- auxData[2]=current scene unique ID
- `sim_message_eventcallback_scriptstateabouttobedestroyed`
  The specified script state is about to be destroyed
- auxData[0]: script handle
  auxData[1]: script UID
- `sim_message_eventcallback_scriptabouttobedestroyed`
  The specified script is about to be destroyed
- auxData[0]: script handle
  auxData[1]: script UID
- sim_message_eventcallback_menuitemselected (called from the UI thread)
  auxData[0]=handle of the item
- auxData[1]=state of the item
- `sim_message_eventcallback_scenesave`
  about to save a scene
- `sim_message_eventcallback_modelsave`
  about to save a model (current selection will be saved)
- `sim_message_eventcallback_abouttoundo`
  the undo button was hit and a previous state is about to be restored
- `sim_message_eventcallback_undoperformed`
  the undo button was hit and a previous state was restored
- `sim_message_eventcallback_abouttoredo`
  the redo button was hit and a future state is about to be restored
- `sim_message_eventcallback_redoperformed`
  the redo button was hit and a future state was restored
- `sim_message_eventcallback_simulationabouttostart`
  simulation will start
- `sim_message_eventcallback_simulationabouttoend`
  simulation will end
- `sim_message_eventcallback_simulationended`
  simulation has ended
- `sim_message_eventcallback_simulationinit`
  Called just before/after the main script's corresponding init section.
- auxData[0]: 0 if called before, 1 if called after
- `sim_message_eventcallback_simulationactuation`
  Called just before/after the main script's corresponding actuation section.
- auxData[0]: 0 if called before, 1 if called after
  auxData[1]: simulation time in ms
- `sim_message_eventcallback_simulationsensing`
  Called just before/after the main script's corresponding sensing section.
- auxData[0]: 0 if called before, 1 if called after
  auxData[1]: simulation time in ms
- `sim_message_eventcallback_simulationcleanup`
  Called just before/after the main script's corresponding cleanup section.
- auxData[0]: 0 if called before, 1 if called after
- sim_message_eventcallback_keypress (called from the UI thread)
  auxData[0]=key, auxData[1]=ctrl and shift key state
- sim_message_eventcallback_refreshdialogs (called from the UI thread)
  called just before dialogs are refreshed in CoppeliaSim.
- auxData[0]=refresh degree (0=light, 1=medium, 2=full)
- `sim_message_eventcallback_sceneloaded`
  called after a scene was loaded
- `sim_message_eventcallback_modelloaded`
  called after a model was loaded
- `sim_message_eventcallback_mainscriptabouttobecalled`
  Called just before the main script is called. A plugin can write a value different from -1 into auxData[0] to temporarily halt simulation progress (e.g. stepping mode)
- `sim_message_eventcallback_moduleentry`
  Called when a custom menu item is selected. auxData[0]=item handle.
- `sim_message_eventcallback_events`
  Called to dispatch events. auxPointer is a const unsigned char\*, holding the CBOR-coded events. auxData[0] indicates the number of events

## <a id="customLuaCommandArgumentTypes"></a>Script - plugin data types

- `sim_script_arg_null`
  can be combined with sim_script_arg_table
- `sim_script_arg_bool`
  can be combined with sim_script_arg_table
- `sim_script_arg_int32`
  can be combined with sim_script_arg_table
- `sim_script_arg_float`
  can be combined with sim_script_arg_table
- `sim_script_arg_double`
  can be combined with sim_script_arg_table
- `sim_script_arg_string`
  can be combined with sim_script_arg_table
- `sim_script_arg_charbuff`
  CANNOT be combined with sim_script_arg_table
- `sim_script_arg_invalid`
- `sim_script_arg_table`
- See also the
- function.

## <a id="renderingAttributes"></a>Rendering attributes

- `sim.displayattribute_renderpass`
- `sim.displayattribute_depthpass`
- `sim.displayattribute_pickpass`
- `sim.displayattribute_selected`
- `sim.displayattribute_groupselection`
- `sim.displayattribute_mainselection`
- `sim.displayattribute_forcewireframe`
- `sim.displayattribute_forbidwireframe`
- `sim.displayattribute_forbidedges`
- `sim.displayattribute_originalcolors`
- `sim.displayattribute_ignorelayer`
- `sim.displayattribute_forvisionsensor`
- `sim.displayattribute_trianglewireframe`
- `sim.displayattribute_simplifyasboundingbox`
- `sim.displayattribute_thickedges`
- `sim.displayattribute_dynamiccontentonly`
- `sim.displayattribute_useauxcomponent`
- `sim.displayattribute_ignorerenderableflag`
- `sim.displayattribute_noopenglcallbacks`
- `sim.displayattribute_nopointclouds`
- `sim.displayattribute_nodrawingobjects`
- `sim.displayattribute_noparticles`
- `sim.displayattribute_colorcodedtriangles`

## <a id="simulationStatus"></a>Simulation status

- `sim.simulation_stopped`
- `sim.simulation_paused`
- `sim.simulation_advancing_running`
- `sim.simulation_advancing_lastbeforestop`
- See also the
- function

## <a id="scriptTypes"></a>Script types

- `sim.scripttype_main`
- `sim.scripttype_simulation`
- `sim.scripttype_addon`
- `sim.scripttype_customization`
- `sim.scripttype_sandbox`
- `sim.scripttype_passive`
- See also

## <a id="propertyTypes"></a>Property types

- `sim.propertytype_null`
- `sim.propertytype_bool`
- `sim.propertytype_int`
- `sim.propertytype_long`
- `sim.propertytype_float`
- `sim.propertytype_string`
- `sim.propertytype_buffer`
- `sim.propertytype_vector2`
- `sim.propertytype_vector3`
- `sim.propertytype_quaternion`
- `sim.propertytype_pose`
- `sim.propertytype_matrix`
- `sim.propertytype_matrix3x3`
- `sim.propertytype_matrix4x4`
- `sim.propertytype_color`
- `sim.propertytype_intarray2`
- `sim.propertytype_intarray`
- `sim.propertytype_floatarray`
- `sim.propertytype_table`
- `sim.propertytype_array`
- `sim.propertytype_map`
- See also

## <a id="propertyFlags"></a>Property flags

- `sim.propertyinfo_notwritable`
- `sim.propertyinfo_notreadable`
- `sim.propertyinfo_removable`
- `sim.propertyinfo_modelhashexclude`
- `sim.propertyinfo_deprecated`
- `sim.propertyinfo_largedata`
- See also

## <a id="scriptExecutionOrder"></a>Script execution priority

- `sim.scriptexecorder_first`
- `sim.scriptexecorder_normal`
- `sim.scriptexecorder_last`
- See also

## <a id="specialArgumentValues"></a>Special argument values

- `sim.handle_absolute`
- `sim.handle_all`
- `sim.handle_all_except_explicit`
- `sim.handle_self`
- `sim.handle_main_script`
- `sim.handle_tree`
- `sim.handle_chain`
- `sim.handle_single`
- `sim.handle_default`
- `sim.handle_all_except_self`
- `sim.handle_parent`
- `sim.handle_scene`
- `sim.handle_app`
- `sim.handle_appstorage`
- `sim.handle_inverse`

## <a id="specialHandleFlags"></a>Special handle flags

- `sim.handleflag_assembly`
- `sim.handleflag_model`
- `sim.handleflag_rawvalue`
- `sim.handleflag_togglevisibility`
- `sim.handleflag_greyscale`
- `sim.handleflag_depthbuffermeters`
- `sim.handleflag_depthbuffer`
- `sim.handleflag_abscoords`
- `sim.handleflag_codedstring`
- `sim.handleflag_keeporiginal`
- `sim.handleflag_camera`
- `sim.handleflag_axis`
- `sim.handleflag_silenterror`
- `sim.handleflag_resetforce`
- `sim.handleflag_resettorque`
- `sim.handleflag_absolutecoords`
- `sim.handleflag_relativecoords`
- `sim.handleflag_wxyzquat`
- `sim.handleflag_reljointbaseframe`
- `sim.handleflag_addmultiple`

## <a id="genericDialogStyles"></a>Generic dialog styles

- `sim.dlgstyle_message`
- `sim.dlgstyle_input`
- `sim.dlgstyle_ok`
- `sim.dlgstyle_ok_cancel`
- `sim.dlgstyle_yes_no`

## <a id="genericDialogReturnValues"></a>Generic dialog return values

- `sim.dlgret_still_open`
- `sim.dlgret_ok`
- `sim.dlgret_cancel`
- `sim.dlgret_yes`
- `sim.dlgret_no`

## <a id="customDrawingObjects"></a>Custom drawing objects

- Drawing object type (combine with drawing object attributes):
- `sim.drawing_points`
  items are pixel-sized points (3 values per item (x;y;z))
- `sim.drawing_lines`
  items are pixel-sized lines (6 values per item (x0;y0;z0;x1;y1;z1))
- `sim.drawing_linestrip`
  items are pixel-sized lines (3 values per line strip corner or end-point)
- `sim.drawing_triangles`
  items are triangles (9 values per item (x0;y0;z0;x1;y1;z1;x2;y2;z2))
- `sim.drawing_trianglepts`
  items are "triangle points" (7 values per item (x;y;z;Qx;Qy;Qz;Qw) (Q=quaternion))
- `sim.drawing_quadpts`
  items are "rectangle points" (7 values per item (x;y;z;Qx;Qy;Qz;Qw) (Q=quaternion))
- `sim.drawing_discpts`
  items are "disc points" (7 values per item (x;y;z;Qx;Qy;Qz;Qw) (Q=quaternion))
- `sim.drawing_cubepts`
  items are "cube points" (7 values per item (x;y;z;Qx;Qy;Qz;Qw) (Q=quaternion))
- `sim.drawing_spherepts`
  items are "sphere points" (3 values per item (x;y;z))
- Drawing object attributes:
- `sim.drawing_cyclic`
  if the drawing object is full, then the first items are overwritten
- `sim.drawing_local`
  coordinate data has to be specified locally, if the drawing object is attached to an object
- `sim.drawing_painttag`
  will be rendered by vision sensors too
- `sim.drawing_overlay`
  will be rendered on top of scene objects
- See also the
- function.

## <a id="particleObjects"></a>Particle objects

- Particle object type (combine with particle object attributes). Each item (particle) requires 6 values: pt1x, pt1y, pt1z, pt2x, pt2y, pt2z (Pt1 is the start position, pt2-pt1 is the initial velocity vector)
- `sim.particle_points1`
  items are displayed as 1 pixel-sized point (internally handled as a perfect sphere)
- `sim.particle_points2`
  items are displayed as 2 pixel-sized points (internally handled as a perfect sphere)
- `sim.particle_points4`
  items are displayed as 4 pixel-sized points (internally handled as a perfect sphere)
- `sim.particle_roughspheres`
  items are displayed as rough spheres (internally handled as a perfect sphere)
- `sim.particle_spheres`
  items are displayed as spheres
- Particle object attributes:
- `sim.particle_respondable1to4`
  the particles are respondable against shapes that have at least one bit 1-4 activated in the global respondable mask
- `sim.particle_respondable5to8`
  the particles are respondable against shapes that have at least one bit 5-8 activated in the global respondable mask
- `sim.particle_particlerespondable`
  the particles are respondable against each other
- `sim.particle_ignoresgravity`
  the particles ignore the effect of gravity
- `sim.particle_invisible`
  the particles are invisible
- `sim.particle_painttag`
  the particles are visible when seen from vision sensors. sim.particle_invisible must not be set
- `sim.particle_cyclic`
  if the max particle count was reached, then the first particles are overwritten
- `sim.particle_water`
  particles are water particles (no weight in the water (i.e. when z&lt;0)). In addition to that, particles can have drag coefficients for the water and the air. Not compatible with sim.particle_ignoresgravity
- See also the
- function.

## <a id="verbosity"></a>Verbosity

- `sim.verbosity_useglobal`
  Use global verbosity (can be used to reset a plugin's verbosity to the global verbosity again)
- `sim.verbosity_none`
  No verbosity
- `sim.verbosity_errors`
  System and plugin error messages
- `sim.verbosity_warnings`
  System and plugin warning messages
- `sim.verbosity_loadinfos`
  Messages related to CoppeliaSim start-up and shut-down. Default console verbosity.
- `sim.verbosity_questions`
  Messages related to question dialogs.
- `sim.verbosity_scripterrors`
  Script error messages
- `sim.verbosity_scriptwarnings`
  Script warning messages
- `sim.verbosity_scriptinfos`
  Information messages mainly related to scripts. Default status bar verbosity.
- `sim.verbosity_infos`
  General information messages
- `sim.verbosity_debug`
  Debug messages
- `sim.verbosity_trace`
  Plugin trace messages
- `sim.verbosity_tracelua`
  Script calls to API functions
- `sim.verbosity_traceall`
  Full verbosity
- `sim.verbosity_default`
  Default verbosity (normally sim.verbosity_loadinfos)
- See also

## <a id="moduleInfos"></a><a id="pluginInfos"></a>Plugin infos

- `sim.plugininfo_extversionstr`
  Extended version string
- `sim.plugininfo_builddatestr`
  Build date string
- `sim.plugininfo_extversionint`
  Extended version integer
- `sim.plugininfo_verbosity`
  Console verbosity. See the various [verbosity levels](#verbosity)
- `sim.plugininfo_statusbarverbosity`
  Status bar verbosity. See the various [verbosity levels](#verbosity)
- See also
- and
- .

## <a id="navigationModes"></a>Mouse navigation and selection modes

- `sim.navigation_passive`
- `sim.navigation_camerashift`
- `sim.navigation_camerarotate`
- `sim.navigation_camerazoom`
- `sim.navigation_cameratilt`
- `sim.navigation_cameraangle`
- `sim.navigation_objectshift`
- `sim.navigation_objectrotate`
- Bit-combine the following values and add them to one of the above values for a valid navigation mode:
- `sim.navigation_clickselection`
- `sim.navigation_ctrlselection`
- `sim.navigation_shiftselection`
- `sim.navigation_camerazoomwheel`
- `sim.navigation_camerarotatemiddlebutton`
- See also the
- and
- functions.

## <a id="startupOptions"></a>Bit-coded start-up options

- sim_gui_menubar (1)
- sim_gui_popups (2)
- sim_gui_toolbar1 (4)
- sim_gui_toolbar2 (8)
- sim_gui_hierarchy (16)
- sim_gui_infobar (32)
- sim_gui_statusbar (64)
- sim_gui_scripteditor (128)
- sim_gui_scriptsimulationparameters (256)
- sim_gui_dialogs (512)
- sim_gui_browser (1024)
- sim_gui_all (0x0ffff)
- sim_gui_headless (will override all other GUI flags) (65536)

## <a id="jointModes"></a>Joint modes

- `sim.jointmode_kinematic`
- `sim.jointmode_dependent`
- `sim.jointmode_dynamic`
- See also the
- function.

## <a id="ctrlModes"></a>Dynamic joint control modes

- `sim.jointdynctrl_free`
- `sim.jointdynctrl_force`
- `sim.jointdynctrl_velocity`
- `sim.jointdynctrl_position`
- `sim.jointdynctrl_spring`
- `sim.jointdynctrl_callback`
- See also

## <a id="RMLFunctions"></a><a id="ruckigFunctions"></a>Ruckig Online Trajectory Generator constants

- Select exactly one of the following:
  sim.ruckig_phasesync (default)
- `sim.ruckig_timesync`
  sim.ruckig_nosync

## <a id="pureTypes"></a><a id="purePrimitiveTypes"></a><a id="primitiveTypes"></a>Primitive shape types

- `sim.primitiveshape_none`
- `sim.primitiveshape_plane`
- `sim.primitiveshape_disc`
- `sim.primitiveshape_cuboid`
- `sim.primitiveshape_spheroid`
- `sim.primitiveshape_cylinder`
- `sim.primitiveshape_cone`
- `sim.primitiveshape_capsule`
- `sim.primitiveshape_heightfield`
- See also the
- and
- functions.

## <a id="dummyTypes"></a><a id="dummyLinkTypes"></a>Dummy types

- `sim.dummytype_default`
- `sim.dummytype_assembly`
- `sim.dummytype_dynloopclosure`
- `sim.dummytype_dyntendon`

## <a id="physicsEngineTypes"></a>Physics engine types

- [sim.physics_bullet](dynamicsModule.md#bullet)
- [sim.physics_ode](dynamicsModule.md#ode)
- [sim.physics_newton](dynamicsModule.md#newton)
- [sim.physics_vortex](dynamicsModule.md#vortex)
- [sim.physics_mujoco](dynamicsModule.md#mujoco)

## <a id="textureMappingModes"></a>Texture mapping modes

- `sim.texturemap_plane`
- `sim.texturemap_cylinder`
- `sim.texturemap_sphere`
- `sim.texturemap_cube`
- See also the
- function.

## <a id="colorComponents"></a>Color components

- `sim.colorcomponent_ambient_diffuse (only for objects)`
- `sim.colorcomponent_diffuse (only for lights)`
- `sim.colorcomponent_specular`
- `sim.colorcomponent_emission (only for objects)`
- `sim.colorcomponent_transparency (only for objects)`
- `sim.colorcomponent_auxiliary (only for objects)`
- See also the
- function.

## <a id="volumeTypes"></a>Proximity sensor volume types

- `sim.volume_pyramid`
- `sim.volume_cylinder`
- `sim.volume_disc`
- `sim.volume_cone`
- `sim.volume_ray`
- `sim.volume_randomizedray`

## <a id="bufferTypes"></a>Buffer types with allowed transformations

- `sim.buffer_uint8`
  with sim.buffer_uint8,sim.buffer_uint8rgb,sim.buffer_base64 (multiplier and offset are ignored),sim.buffer_split (multiplier is ignored, offset is the split size)
- `sim.buffer_uint8rgb`
  with sim.buffer_uint8rgb,sim.buffer_uint8bgr,sim.buffer_uint8
- `sim.buffer_uint8bgr`
  with sim.buffer_uint8bgr,sim.buffer_uint8rgb,sim.buffer_uint8
- `sim.buffer_uint8rgba`
  with sim.buffer_uint8rgba,sim.buffer_uint8rgb
- `sim.buffer_uint8argb`
  with sim.buffer_uint8argb,sim.buffer_uint8rgb
- `sim.buffer_float`
  with sim.buffer_uint8, sim.buffer_int8, sim.buffer_uint16, sim.buffer_int16, sim.buffer_uint32,
- sim.buffer_int32,sim.buffer_float,sim.buffer_double,sim.buffer_uint8rgb
- `sim.buffer_double`
  with sim.buffer_uint8, sim.buffer_int8, sim.buffer_uint16, sim.buffer_int16, sim.buffer_uint32,
- sim.buffer_int32,sim.buffer_float,sim.buffer_double,sim.buffer_uint8rgb
- `sim.buffer_base64 (multiplier and offset are ignored)`
  with sim.buffer_uint8
- See also the
- function.

## <a id="imageCombination"></a>Image combination operations

- `sim.imgcomb_vertical: vertical concatenation`
- `sim.imgcomb_horizontal: horizontal concatenation`
- See also the
- function.

## <a id="streamTransformations"></a>Graph stream transformations

- `sim.stream_transf_raw`
- `sim.stream_transf_derivative`
- `sim.stream_transf_integral`
- `sim.stream_transf_cumulative`
- See also the
- function.

## <a id="stringTypes"></a>String types

- `sim_string_text`
- `sim_string_binary`
- `sim_string_buffer`

## <a id="stackItemTypes"></a>Stack item types

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

## <a id="stackTableInfo"></a>Stack table info

- `sim_stack_table_circular_ref`
- `sim_stack_table_not_table`
- `sim_stack_table_map`
- `sim_stack_table_empty`

## <a id="bulletSolverTypes"></a>Bullet solver types

- `sim.bullet_constraintsolvertype_sequentialimpulse`
- `sim.bullet_constraintsolvertype_nncg`
- `sim.bullet_constraintsolvertype_dantzig`
- `sim.bullet_constraintsolvertype_projectedgaussseidel`
- See also

## <a id="vortexFrictionModels"></a>Vortex friction models

- `sim.vortex_bodyfrictionmodel_box`
- `sim.vortex_bodyfrictionmodel_scaledbox`
- `sim.vortex_bodyfrictionmodel_proplow`
- `sim.vortex_bodyfrictionmodel_prophigh`
- `sim.vortex_bodyfrictionmodel_scaledboxfast`
- `sim.vortex_bodyfrictionmodel_neutral`
- `sim.vortex_bodyfrictionmodel_none`
- See also

## <a id="sceneObjectProperties"></a><a id="engineParameters"></a><a id="arrayParameters"></a><a id="stringParameters"></a><a id="sceneObjectSpecialProperties"></a><a id="floatingParameters"></a><a id="uinteger64Parameters"></a><a id="modelProperties"></a><a id="booleanParameters"></a><a id="integerParameters"></a>Various

See: [properties](properties.md)
