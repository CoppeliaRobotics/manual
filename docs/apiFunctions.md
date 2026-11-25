# Regular API reference ([sim-2](apisOverview.md))

This page lists all methods, properties and functions related to the regular API.  
Unless explicitly stated otherwise, all values passed to or returned from the regular API use SI units: meters, kilograms, seconds, and **radians**, or combinations thereof:

- [Methods and properties](#methodsAndProperties)
- [Functions (C/C++)](#functions)

---

<a id="methodsAndProperties"></a>Methods and properties are organized into the following categories:

- [object](#methodsAndProperties_object)
- [app](#methodsAndProperties_app)
- [scene](#methodsAndProperties_scene)
- [collection](#methodsAndProperties_collection)
- [customObject](#methodsAndProperties_customObject)
- [script](#methodsAndProperties_script)
- [mesh](#methodsAndProperties_mesh)
- [textureData](#methodsAndProperties_textureData)
- [sceneObject](#methodsAndProperties_sceneObject)
- [shape](#methodsAndProperties_shape)
- [joint](#methodsAndProperties_joint)
- [dummy](#methodsAndProperties_dummy)
- [marker](#methodsAndProperties_marker)
- [scriptObject](#methodsAndProperties_scriptObject)
- [camera](#methodsAndProperties_camera)
- [light](#methodsAndProperties_light)
- [graph](#methodsAndProperties_graph)
- [proximitySensor](#methodsAndProperties_proximitySensor)
- [visionSensor](#methodsAndProperties_visionSensor)
- [forceSensor](#methodsAndProperties_forceSensor)
- [pointCloud](#methodsAndProperties_pointCloud)
- [ocTree](#methodsAndProperties_ocTree)
- [customSceneObject](#methodsAndProperties_customSceneObject)
- [Path](#methodsAndProperties_Path)
- [File operations](#methodsAndProperties_file)
- [General functionality handling](#methodsAndProperties_main)
- [Dynamics](#methodsAndProperties_dynamics)
- [Properties](#methodsAndProperties_property)
- [Collision detection](#methodsAndProperties_collision)
- [Distance calculation](#methodsAndProperties_distance)
- [Rendering](#methodsAndProperties_rendering)
- [Customization](#methodsAndProperties_customization)
- [Models](#methodsAndProperties_model)
- [Selection](#methodsAndProperties_selection)
- [Object creation](#methodsAndProperties_creation)
- [Script related](#methodsAndProperties_scriptRelated)
- [Simulation](#methodsAndProperties_simulation)
- [Threads](#methodsAndProperties_thread)
- [Blocking methods](#methodsAndProperties_blocking)
- [Coordinates and transformations](#methodsAndProperties_transformation)
- [Scene hierarchy](#methodsAndProperties_hierarchy)
- [Messaging](#methodsAndProperties_messaging)
- [console](#methodsAndProperties_console)
- [textEditor](#methodsAndProperties_textEditor)
- [Import/export](#methodsAndProperties_importExport)
- [Motion functionality](#methodsAndProperties_Motion)
- [MoveToConfig](#methodsAndProperties_MoveToConfig)
- [MoveToPose](#methodsAndProperties_MoveToPose)
- [TimeOptimalTrajectory](#methodsAndProperties_TimeOptimalTrajectory)
- [RuckigPosition](#methodsAndProperties_RuckigPosition)
- [RuckigVelocity](#methodsAndProperties_RuckigVelocity)
- [Packing/unpacking](#methodsAndProperties_packing)
- [IK](#methodsAndProperties_IK)
- [IKObject](#methodsAndProperties_IKObject)
- [IKjoint](#methodsAndProperties_IKJoint)
- [IKGroup](#methodsAndProperties_IKGroup)
- [IKElement](#methodsAndProperties_IKElement)
- [Other](#methodsAndProperties_other)
- [drawingObject (deprecated, see marker instead)](#methodsAndProperties_drawingObject)

---

<a id="functions"></a>C-functions are organized into the following categories:

- [Main](#functions_c_main)
- [Properties](#functions_c_property)
- [Stack](#functions_c_stack)
- [Auxiliary functions](#functions_c_aux)

Keep in mind that **all** methods can also be called from C/C++ via the [`simCallMethod`](sim/simCallMethod_cpp.htm) function.

---

## <a id="methodsAndProperties_object"></a>object (methods & properties)

- [`object:getBoolProperty`](sim-2/object_getBoolProperty.htm) — Fetches a boolean property
- [`object:getBufferProperty`](sim-2/object_getBufferProperty.htm) — Fetches a buffer property
- [`object:getColorProperty`](sim-2/object_getColorProperty.htm) — Fetches a color property
- [`object:getEnumProperty`](sim-2/object_getEnumProperty.htm) — Fetches an enum property
- [`object:getFloatArrayProperty`](sim-2/object_getFloatArrayProperty.htm) — Fetches a float array property
- [`object:getFloatProperty`](sim-2/object_getFloatProperty.htm) — Fetches a float property
- [`object:getHandleArrayProperty`](sim-2/object_getHandleArrayProperty.htm) — Fetches a handle array property
- [`object:getHandleProperty`](sim-2/object_getHandleProperty.htm) — Fetches a handle property
- [`object:getIntArrayProperty`](sim-2/object_getIntArrayProperty.htm) — Fetches an int array property
- [`object:getIntProperty`](sim-2/object_getIntProperty.htm) — Fetches an int32 property
- [`object:getLongProperty`](sim-2/object_getLongProperty.htm) — Fetches an int64 property
- [`object:getMatrixProperty`](sim-2/object_getMatrixProperty.htm) — Fetches a matrix property
- [`object:getMethodProperty`](sim-2/object_getMethodProperty.htm) — Fetches a method property
- [`object:getPoseProperty`](sim-2/object_getPoseProperty.htm) — Fetches a pose property
- [`object:getProperties`](sim-2/object_getProperties.htm) — Fetches all properties of a target
- [`object:getPropertiesInfos`](sim-2/object_getPropertiesInfos.htm) — Fetches all property infos of a target
- [`object:getProperty`](sim-2/object_getProperty.htm) — Convenience function to fetch a property
- [`object:getPropertyInfo`](sim-2/object_getPropertyInfo.htm) — Fetches information about a property
- [`object:getPropertyInfos`](sim-2/object_getPropertyInfos.htm) — Fetches an extended set of property infos
- [`object:getPropertyName`](sim-2/object_getPropertyName.htm) — Fetches a property name by index
- [`object:getPropertyTypeString`](sim-2/object_getPropertyTypeString.htm) — Gets string for a property type
- [`object:getQuaternionProperty`](sim-2/object_getQuaternionProperty.htm) — Fetches a quaternion property
- [`object:getStringArrayProperty`](sim-2/object_getStringArrayProperty.htm) — Fetches a text array property
- [`object:getStringProperty`](sim-2/object_getStringProperty.htm) — Fetches a string property
- [`object:getTableProperty`](sim-2/object_getTableProperty.htm) — Fetches a table property
- [`object:getVector3Property`](sim-2/object_getVector3Property.htm) — Fetches a vector3 property
- [`object:isValid`](sim-2/object_isValid.htm) — Checks if the object is valid
- [`object:removeProperty`](sim-2/object_removeProperty.htm) — Removes a removable property
- [`object:setBoolProperty`](sim-2/object_setBoolProperty.htm) — Sets a boolean property
- [`object:setBufferProperty`](sim-2/object_setBufferProperty.htm) — Sets a buffer property
- [`object:setColorProperty`](sim-2/object_setColorProperty.htm) — Sets a color property
- [`object:setEnumProperty`](sim-2/object_setEnumProperty.htm) — Sets an enum property
- [`object:setFloatArrayProperty`](sim-2/object_setFloatArrayProperty.htm) — Sets a float array property
- [`object:setFloatProperty`](sim-2/object_setFloatProperty.htm) — Sets a float property
- [`object:setHandleArrayProperty`](sim-2/object_setHandleArrayProperty.htm) — Sets a handle array property
- [`object:setHandleProperty`](sim-2/object_setHandleProperty.htm) — Sets a handle property
- [`object:setIntArrayProperty`](sim-2/object_setIntArrayProperty.htm) — Sets an int array property
- [`object:setIntProperty`](sim-2/object_setIntProperty.htm) — Sets an int32 property
- [`object:setLongProperty`](sim-2/object_setLongProperty.htm) — Sets an int64 property
- [`object:setMatrixProperty`](sim-2/object_setMatrixProperty.htm) — Sets a matrix property
- [`object:setMethodProperty`](sim-2/object_setMethodProperty.htm) — Sets a method property
- [`object:setPoseProperty`](sim-2/object_setPoseProperty.htm) — Sets a pose property
- [`object:setProperties`](sim-2/object_setProperties.htm) — Sets several properties at once
- [`object:setProperty`](sim-2/object_setProperty.htm) — Convenience function to set a property
- [`object:setPropertyInfo`](sim-2/object_setPropertyInfo.htm) — Sets information about a property
- [`object:setQuaternionProperty`](sim-2/object_setQuaternionProperty.htm) — Sets a quaternion property
- [`object:setStringArrayProperty`](sim-2/object_setStringArrayProperty.htm) — Sets a text array property
- [`object:setStringProperty`](sim-2/object_setStringProperty.htm) — Sets a string property
- [`object:setTableProperty`](sim-2/object_setTableProperty.htm) — Sets a table property
- [`object:setVector3Property`](sim-2/object_setVector3Property.htm) — Sets a vector3 property
- [`object.handle`](sim-2/property_object_handle.htm) — Handle
- [`object.metaInfo.isClass`](sim-2/property_object_metaInfo_isClass.htm) — Class flag
- [`object.metaInfo.isSceneObject`](sim-2/property_object_metaInfo_isSceneObject.htm) — Scene object flag
- [`object.metaInfo.namespaces`](sim-2/property_object_metaInfo_namespaces.htm) — Object namespaces
- [`object.metaInfo.superClass`](sim-2/property_object_metaInfo_superClass.htm) — Object superclass
- [`object.type`](sim-2/property_object_type.htm) — Object type

## <a id="methodsAndProperties_app"></a>app (methods & properties)

- [`app:createCustomObjectClass`](sim-2/app_createCustomObjectClass.htm) — Creates a custom object class
- [`app:createObject`](sim-2/app_createObject.htm) — Creates various objects (collections, scripts, sensors, etc.)
- [`app:deserialize`](sim-2/app_deserialize.htm) — Deserializes a buffer using CBOR format
- [`app:fastIdleLoop`](sim-2/app_fastIdleLoop.htm) — Speeds up the idle loop for reactivity
- [`app:getEnumInfo`](sim-2/app_getEnumInfo.htm) — Returns information about an enum
- [`app:getGenesisEvents`](sim-2/app_getGenesisEvents.htm) — Retrieves events to reconstruct the app's state
- [`app:getObjects`](sim-2/app_getObjects.htm) — Retrieves objects of a certain type
- [`app:getPluginInfo`](sim-2/app_getPluginInfo.htm) — Returns information about a loaded plugin
- [`app:handleAddOns`](sim-2/app_handleAddOns.htm) — Calls a system callback in add-ons
- [`app:handleMessagePump`](sim-2/app_handleMessagePump.htm) — Handles the message pump explicitly
- [`app:handleSandboxes`](sim-2/app_handleSandboxes.htm) — Calls a system callback in the sandbox
- [`app:loadImage`](sim-2/app_loadImage.htm) — Loads an image from file
- [`app:loadImageFromBuffer`](sim-2/app_loadImageFromBuffer.htm) — Loads an image from memory
- [`app:loadModelInfo`](sim-2/app_loadModelInfo.htm) — Loads a model thumbnail
- [`app:loadModelInfoFromBuffer`](sim-2/app_loadModelInfoFromBuffer.htm) — Loads a model thumbnail from buffer
- [`app:loadScene`](sim-2/app_loadScene.htm) — Loads a scene from file
- [`app:loadSceneFromBuffer`](sim-2/app_loadSceneFromBuffer.htm) — Loads a scene from buffer
- [`app:logError`](sim-2/app_logError.htm) — Outputs an error message in the status bar
- [`app:logInfo`](sim-2/app_logInfo.htm) — Outputs an information message in the status bar
- [`app:logWarn`](sim-2/app_logWarn.htm) — Outputs a warning message in the status bar
- [`app:openFile`](sim-2/app_openFile.htm) — Opens a file in a subprocess
- [`app:pack`](sim-2/app_pack.htm) — Packs data using CoppeliaSim format
- [`app:packArray`](sim-2/app_packArray.htm) — Packs an array of numbers as little-endian
- [`app:pushEvent`](sim-2/app_pushEvent.htm) — Pushes a user event for asynchronous reception
- [`app:quit`](sim-2/app_quit.htm) — Triggers a quit signal for the application
- [`app:removeObjects`](sim-2/app_removeObjects.htm) — Removes one or several objects
- [`app:saveImage`](sim-2/app_saveImage.htm) — Saves an image to file
- [`app:saveImageToBuffer`](sim-2/app_saveImageToBuffer.htm) — Saves an image to a buffer
- [`app:serialize`](sim-2/app_serialize.htm) — Serializes data using CBOR format
- [`app:setPluginInfo`](sim-2/app_setPluginInfo.htm) — Modifies information of a loaded plugin
- [`app:systemLock`](sim-2/app_systemLock.htm) — Acquires/releases a system-wide semaphore
- [`app:test`](sim-2/app_test.htm) — Test method
- [`app:transformBuffer`](sim-2/app_transformBuffer.htm) — Modifies a buffer (format, scale, offset)
- [`app:transformImage`](sim-2/app_transformImage.htm) — Transforms an image (scaling, flipping)
- [`app:unpack`](sim-2/app_unpack.htm) — Unpacks data using CoppeliaSim format
- [`app:unpackArray`](sim-2/app_unpackArray.htm) — Unpacks a buffer into an array of numbers
- [`app.addOns`](sim-2/property_app_addOns.htm) — Add-ons
- [`app.args`](sim-2/property_app_args.htm) — App args
- [`app.auxAddOn1`](sim-2/property_app_auxAddOn1.htm) — Aux. add-on 1
- [`app.auxAddOn2`](sim-2/property_app_auxAddOn2.htm) — Aux. add-on 2
- [`app.browserEnabled`](sim-2/property_app_browserEnabled.htm) — Browser enabled
- [`app.canSave`](sim-2/property_app_canSave.htm) — Can save
- [`app.consoleVerbosity`](sim-2/property_app_consoleVerbosity.htm) — Console verbosity
- [`app.consoleVerbosityStr`](sim-2/property_app_consoleVerbosityStr.htm) — Console verbosity string
- [`app.current`](sim-2/property_app_current.htm) — Current
- [`app.customClasses`](sim-2/property_app_customClasses.htm) — Custom classes
- [`app.customObjects`](sim-2/property_app_customObjects.htm) — Custom objects
- [`app.customSceneObjectClasses`](sim-2/property_app_customSceneObjectClasses.htm) — Custom scene object classes
- [`app.defaultPython`](sim-2/property_app_defaultPython.htm) — Default Python
- [`app.defaultRotationStepSize`](sim-2/property_app_defaultRotationStepSize.htm) — Rotation step size
- [`app.defaultTranslationStepSize`](sim-2/property_app_defaultTranslationStepSize.htm) — Translation step size
- [`app.dialogVerbosity`](sim-2/property_app_dialogVerbosity.htm) — Dialog verbosity
- [`app.dialogVerbosityStr`](sim-2/property_app_dialogVerbosityStr.htm) — Dialog verbosity string
- [`app.displayEnabled`](sim-2/property_app_displayEnabled.htm) — Display enabled
- [`app.dongleId`](sim-2/property_app_dongleId.htm)
- [`app.dongleSerial`](sim-2/property_app_dongleSerial.htm)
- [`app.enumTypes`](sim-2/property_app_enumTypes.htm) — Enum types
- [`app.execUnsafe`](sim-2/property_app_execUnsafe.htm) — Execute unsafe
- [`app.execUnsafeExt`](sim-2/property_app_execUnsafeExt.htm) — Execute unsafe extended
- [`app.flavor`](sim-2/property_app_flavor.htm) — Flavor
- [`app.headlessMode`](sim-2/property_app_headlessMode.htm) — Headless mode
- [`app.hierarchyEnabled`](sim-2/property_app_hierarchyEnabled.htm) — Hierarchy enabled
- [`app.idleFps`](sim-2/property_app_idleFps.htm) — Idle FPS
- [`app.legacyMachineId`](sim-2/property_app_legacyMachineId.htm) — Legacy machine ID
- [`app.machineId`](sim-2/property_app_machineId.htm) — Machine ID
- [`app.machineId0`](sim-2/property_app_machineId0.htm)
- [`app.machineId1`](sim-2/property_app_machineId1.htm)
- [`app.machineId2`](sim-2/property_app_machineId2.htm)
- [`app.machineId3`](sim-2/property_app_machineId3.htm)
- [`app.machineIdX`](sim-2/property_app_machineIdX.htm)
- [`app.machineSerial`](sim-2/property_app_machineSerial.htm)
- [`app.machineSerialND`](sim-2/property_app_machineSerialND.htm)
- [`app.notifyDeprecated`](sim-2/property_app_notifyDeprecated.htm) — Notify deprecated
- [`app.paths.addOns`](sim-2/property_app_paths_addOns.htm) — Add-on path
- [`app.paths.app`](sim-2/property_app_paths_app.htm) — Application path
- [`app.paths.importExport`](sim-2/property_app_paths_importExport.htm) — Import/export path
- [`app.paths.lua`](sim-2/property_app_paths_lua.htm) — Lua path
- [`app.paths.models`](sim-2/property_app_paths_models.htm) — Model path
- [`app.paths.mujoco`](sim-2/property_app_paths_mujoco.htm) — MuJoCo path
- [`app.paths.python`](sim-2/property_app_paths_python.htm) — Python path
- [`app.paths.resources`](sim-2/property_app_paths_resources.htm) — Resource path
- [`app.paths.sceneTemp`](sim-2/property_app_paths_sceneTemp.htm) — Scene temporary path
- [`app.paths.scenes`](sim-2/property_app_paths_scenes.htm) — Scene path
- [`app.paths.settings`](sim-2/property_app_paths_settings.htm) — Settings path
- [`app.paths.system`](sim-2/property_app_paths_system.htm) — System path
- [`app.paths.temp`](sim-2/property_app_paths_temp.htm) — Temporary path
- [`app.pid`](sim-2/property_app_pid.htm) — PID
- [`app.platform`](sim-2/property_app_platform.htm) — OS type
- [`app.pluginNames`](sim-2/property_app_pluginNames.htm) — Plugins
- [`app.processCnt`](sim-2/property_app_processCnt.htm) — Processes
- [`app.processId`](sim-2/property_app_processId.htm) — Process
- [`app.productVersion`](sim-2/property_app_productVersion.htm) — Product string
- [`app.productVersionNb`](sim-2/property_app_productVersionNb.htm) — Product
- [`app.protocolVersion`](sim-2/property_app_protocolVersion.htm) — Protocol
- [`app.qtVersion`](sim-2/property_app_qtVersion.htm) — Qt
- [`app.randomFloat`](sim-2/property_app_randomFloat.htm) — Random number
- [`app.randomQuaternion`](sim-2/property_app_randomQuaternion.htm) — Random quaternion
- [`app.randomString`](sim-2/property_app_randomString.htm) — Random string
- [`app.sandboxLua`](sim-2/property_app_sandboxLua.htm) — Lua sandbox
- [`app.sandboxPython`](sim-2/property_app_sandboxPython.htm) — Python sandbox
- [`app.sessionId`](sim-2/property_app_sessionId.htm) — Session ID
- [`app.startupCode`](sim-2/property_app_startupCode.htm) — Start-up code
- [`app.statusbarVerbosity`](sim-2/property_app_statusbarVerbosity.htm) — Statusbar verbosity
- [`app.statusbarVerbosityStr`](sim-2/property_app_statusbarVerbosityStr.htm) — Statusbar verbosity string
- [`app.systemTime`](sim-2/property_app_systemTime.htm) — System time

## <a id="methodsAndProperties_scene"></a>[scene](scenes.md) (methods & properties)

- [`scene:announceChange`](sim-2/scene_announceChange.htm) — Announces a change in the scene for undo/redo
- [`scene:copyObjects`](sim-2/scene_copyObjects.htm) — Copies selected objects
- [`scene:createObject`](sim-2/scene_createObject.htm) — Creates various objects (collections, scripts, sensors, etc.)
- [`scene:cutObjects`](sim-2/scene_cutObjects.htm) — Cuts selected objects
- [`scene:duplicateObjects`](sim-2/scene_duplicateObjects.htm) — Duplicates scene objects
- [`scene:getDescendants`](sim-2/scene_getDescendants.htm) — Retrieves scene objects up to a specific depth
- [`scene:getObject`](sim-2/scene_getObject.htm) — Retrieves an object by its path and name
- [`scene:getObjectFromUid`](sim-2/scene_getObjectFromUid.htm) — Retrieves an object by its unique identifier
- [`scene:getObjects`](sim-2/scene_getObjects.htm) — Retrieves objects of a certain type
- [`scene:groupShapes`](sim-2/scene_groupShapes.htm) — Groups shapes into a compound shape
- [`scene:handleCustomizationScripts`](sim-2/scene_handleCustomizationScripts.htm) — Calls a system callback in customization scripts
- [`scene:handleSimulationScripts`](sim-2/scene_handleSimulationScripts.htm) — Calls a system callback in simulation scripts
- [`scene:loadModel`](sim-2/scene_loadModel.htm) — Loads a previously saved model
- [`scene:loadModelFromBuffer`](sim-2/scene_loadModelFromBuffer.htm) — Loads a model from buffer
- [`scene:mergeShapes`](sim-2/scene_mergeShapes.htm) — Merges several shapes
- [`scene:pasteObjects`](sim-2/scene_pasteObjects.htm) — Pastes objects
- [`scene:remove`](sim-2/scene_remove.htm) — Closes the scene
- [`scene:removeObjects`](sim-2/scene_removeObjects.htm) — Removes one or several objects
- [`scene:save`](sim-2/scene_save.htm) — Saves the scene to file
- [`scene:saveToBuffer`](sim-2/scene_saveToBuffer.htm) — Serializes the scene to a buffer
- [`scene:stepKinematicJoints`](sim-2/scene_stepKinematicJoints.htm) — Steps all kinematic mode joints
- [`scene.dynamics:getContacts`](sim-2/scene_dynamics_getContacts.htm) — Retrieves contact information from the dynamics world
- [`scene.dynamics:step`](sim-2/scene_dynamics_step.htm) — Steps the dynamics engine
- [`scene.simulation:pause`](sim-2/scene_simulation_pause.htm) — Requests a simulation pause
- [`scene.simulation:start`](sim-2/scene_simulation_start.htm) — Requests a simulation start or resume
- [`scene.simulation:stop`](sim-2/scene_simulation_stop.htm) — Requests a simulation stop
- [`scene.acknowledgment`](sim-2/property_scene_acknowledgment.htm) — Acknowledgment
- [`scene.ambientLight`](sim-2/property_scene_ambientLight.htm) — Ambient light
- [`scene.collections`](sim-2/property_scene_collections.htm) — Collections
- [`scene.customObjects`](sim-2/property_scene_customObjects.htm) — Custom objects
- [`scene.drawingObjects`](sim-2/property_scene_drawingObjects.htm) — Drawing objects
- [`scene.dynamics.bullet.collisionMarginScaling`](sim-2/property_scene_dynamics_bullet_collisionMarginScaling.htm)
- [`scene.dynamics.bullet.computeInertias`](sim-2/property_scene_dynamics_bullet_computeInertias.htm)
- [`scene.dynamics.bullet.internalScalingFull`](sim-2/property_scene_dynamics_bullet_internalScalingFull.htm)
- [`scene.dynamics.bullet.internalScalingValue`](sim-2/property_scene_dynamics_bullet_internalScalingValue.htm)
- [`scene.dynamics.bullet.iterations`](sim-2/property_scene_dynamics_bullet_iterations.htm)
- [`scene.dynamics.bullet.solver`](sim-2/property_scene_dynamics_bullet_solver.htm)
- [`scene.dynamics.enabled`](sim-2/property_scene_dynamics_enabled.htm) — Dynamics enabled
- [`scene.dynamics.engine`](sim-2/property_scene_dynamics_engine.htm) — Dynamics engine
- [`scene.dynamics.engineProperties`](sim-2/property_scene_dynamics_engineProperties.htm) — Engine properties
- [`scene.dynamics.engineVersion`](sim-2/property_scene_dynamics_engineVersion.htm) — Dynamics engine version
- [`scene.dynamics.gravity`](sim-2/property_scene_dynamics_gravity.htm) — Gravity
- [`scene.dynamics.mujoco.actuationEnable`](sim-2/property_scene_dynamics_mujoco_actuationEnable.htm)
- [`scene.dynamics.mujoco.alignfree`](sim-2/property_scene_dynamics_mujoco_alignfree.htm)
- [`scene.dynamics.mujoco.autoresetEnable`](sim-2/property_scene_dynamics_mujoco_autoresetEnable.htm)
- [`scene.dynamics.mujoco.balanceInertias`](sim-2/property_scene_dynamics_mujoco_balanceInertias.htm)
- [`scene.dynamics.mujoco.boundInertia`](sim-2/property_scene_dynamics_mujoco_boundInertia.htm)
- [`scene.dynamics.mujoco.boundMass`](sim-2/property_scene_dynamics_mujoco_boundMass.htm)
- [`scene.dynamics.mujoco.ccd_iterations`](sim-2/property_scene_dynamics_mujoco_ccd_iterations.htm)
- [`scene.dynamics.mujoco.ccd_tolerance`](sim-2/property_scene_dynamics_mujoco_ccd_tolerance.htm)
- [`scene.dynamics.mujoco.computeInertias`](sim-2/property_scene_dynamics_mujoco_computeInertias.htm)
- [`scene.dynamics.mujoco.cone`](sim-2/property_scene_dynamics_mujoco_cone.htm)
- [`scene.dynamics.mujoco.contactEnable`](sim-2/property_scene_dynamics_mujoco_contactEnable.htm)
- [`scene.dynamics.mujoco.contactParamsMargin`](sim-2/property_scene_dynamics_mujoco_contactParamsMargin.htm)
- [`scene.dynamics.mujoco.contactParamsOverride`](sim-2/property_scene_dynamics_mujoco_contactParamsOverride.htm)
- [`scene.dynamics.mujoco.contactParamsSolimp`](sim-2/property_scene_dynamics_mujoco_contactParamsSolimp.htm)
- [`scene.dynamics.mujoco.contactParamsSolref`](sim-2/property_scene_dynamics_mujoco_contactParamsSolref.htm)
- [`scene.dynamics.mujoco.density`](sim-2/property_scene_dynamics_mujoco_density.htm)
- [`scene.dynamics.mujoco.energyEnable`](sim-2/property_scene_dynamics_mujoco_energyEnable.htm)
- [`scene.dynamics.mujoco.equalityEnable`](sim-2/property_scene_dynamics_mujoco_equalityEnable.htm)
- [`scene.dynamics.mujoco.eulerdampEnable`](sim-2/property_scene_dynamics_mujoco_eulerdampEnable.htm)
- [`scene.dynamics.mujoco.frictionlossEnable`](sim-2/property_scene_dynamics_mujoco_frictionlossEnable.htm)
- [`scene.dynamics.mujoco.gravityEnable`](sim-2/property_scene_dynamics_mujoco_gravityEnable.htm)
- [`scene.dynamics.mujoco.impratio`](sim-2/property_scene_dynamics_mujoco_impratio.htm)
- [`scene.dynamics.mujoco.integrator`](sim-2/property_scene_dynamics_mujoco_integrator.htm)
- [`scene.dynamics.mujoco.invdiscreteEnable`](sim-2/property_scene_dynamics_mujoco_invdiscreteEnable.htm)
- [`scene.dynamics.mujoco.iterations`](sim-2/property_scene_dynamics_mujoco_iterations.htm)
- [`scene.dynamics.mujoco.jacobian`](sim-2/property_scene_dynamics_mujoco_jacobian.htm)
- [`scene.dynamics.mujoco.kinematicBodiesInertia`](sim-2/property_scene_dynamics_mujoco_kinematicBodiesInertia.htm)
- [`scene.dynamics.mujoco.kinematicBodiesMass`](sim-2/property_scene_dynamics_mujoco_kinematicBodiesMass.htm)
- [`scene.dynamics.mujoco.kinematicBodiesOverrideFlags`](sim-2/property_scene_dynamics_mujoco_kinematicBodiesOverrideFlags.htm)
- [`scene.dynamics.mujoco.kinematicWeldSolimp`](sim-2/property_scene_dynamics_mujoco_kinematicWeldSolimp.htm)
- [`scene.dynamics.mujoco.kinematicWeldSolref`](sim-2/property_scene_dynamics_mujoco_kinematicWeldSolref.htm)
- [`scene.dynamics.mujoco.kinematicWeldTorquescale`](sim-2/property_scene_dynamics_mujoco_kinematicWeldTorquescale.htm)
- [`scene.dynamics.mujoco.limitEnable`](sim-2/property_scene_dynamics_mujoco_limitEnable.htm)
- [`scene.dynamics.mujoco.ls_iterations`](sim-2/property_scene_dynamics_mujoco_ls_iterations.htm)
- [`scene.dynamics.mujoco.ls_tolerance`](sim-2/property_scene_dynamics_mujoco_ls_tolerance.htm)
- [`scene.dynamics.mujoco.mbmemory`](sim-2/property_scene_dynamics_mujoco_mbmemory.htm)
- [`scene.dynamics.mujoco.midphaseEnable`](sim-2/property_scene_dynamics_mujoco_midphaseEnable.htm)
- [`scene.dynamics.mujoco.multiccd`](sim-2/property_scene_dynamics_mujoco_multiccd.htm)
- [`scene.dynamics.mujoco.multithreaded`](sim-2/property_scene_dynamics_mujoco_multithreaded.htm)
- [`scene.dynamics.mujoco.nativeccdEnable`](sim-2/property_scene_dynamics_mujoco_nativeccdEnable.htm)
- [`scene.dynamics.mujoco.nconmax`](sim-2/property_scene_dynamics_mujoco_nconmax.htm)
- [`scene.dynamics.mujoco.njmax`](sim-2/property_scene_dynamics_mujoco_njmax.htm)
- [`scene.dynamics.mujoco.noslip_iterations`](sim-2/property_scene_dynamics_mujoco_noslip_iterations.htm)
- [`scene.dynamics.mujoco.noslip_tolerance`](sim-2/property_scene_dynamics_mujoco_noslip_tolerance.htm)
- [`scene.dynamics.mujoco.nstack`](sim-2/property_scene_dynamics_mujoco_nstack.htm)
- [`scene.dynamics.mujoco.passiveEnable`](sim-2/property_scene_dynamics_mujoco_passiveEnable.htm)
- [`scene.dynamics.mujoco.rebuildTrigger`](sim-2/property_scene_dynamics_mujoco_rebuildTrigger.htm)
- [`scene.dynamics.mujoco.refsafeEnable`](sim-2/property_scene_dynamics_mujoco_refsafeEnable.htm)
- [`scene.dynamics.mujoco.sdf_initpoints`](sim-2/property_scene_dynamics_mujoco_sdf_initpoints.htm)
- [`scene.dynamics.mujoco.sdf_iterations`](sim-2/property_scene_dynamics_mujoco_sdf_iterations.htm)
- [`scene.dynamics.mujoco.sensorEnable`](sim-2/property_scene_dynamics_mujoco_sensorEnable.htm)
- [`scene.dynamics.mujoco.solver`](sim-2/property_scene_dynamics_mujoco_solver.htm)
- [`scene.dynamics.mujoco.tolerance`](sim-2/property_scene_dynamics_mujoco_tolerance.htm)
- [`scene.dynamics.mujoco.viscosity`](sim-2/property_scene_dynamics_mujoco_viscosity.htm)
- [`scene.dynamics.mujoco.warmstartEnable`](sim-2/property_scene_dynamics_mujoco_warmstartEnable.htm)
- [`scene.dynamics.mujoco.wind`](sim-2/property_scene_dynamics_mujoco_wind.htm)
- [`scene.dynamics.newton.computeInertias`](sim-2/property_scene_dynamics_newton_computeInertias.htm)
- [`scene.dynamics.newton.contactMergeTolerance`](sim-2/property_scene_dynamics_newton_contactMergeTolerance.htm)
- [`scene.dynamics.newton.exactSolver`](sim-2/property_scene_dynamics_newton_exactSolver.htm)
- [`scene.dynamics.newton.highJointAccuracy`](sim-2/property_scene_dynamics_newton_highJointAccuracy.htm)
- [`scene.dynamics.newton.iterations`](sim-2/property_scene_dynamics_newton_iterations.htm)
- [`scene.dynamics.newton.multithreading`](sim-2/property_scene_dynamics_newton_multithreading.htm)
- [`scene.dynamics.ode.computeInertias`](sim-2/property_scene_dynamics_ode_computeInertias.htm)
- [`scene.dynamics.ode.globalCfm`](sim-2/property_scene_dynamics_ode_globalCfm.htm)
- [`scene.dynamics.ode.globalErp`](sim-2/property_scene_dynamics_ode_globalErp.htm)
- [`scene.dynamics.ode.internalScalingFull`](sim-2/property_scene_dynamics_ode_internalScalingFull.htm)
- [`scene.dynamics.ode.internalScalingValue`](sim-2/property_scene_dynamics_ode_internalScalingValue.htm)
- [`scene.dynamics.ode.quickStepEnabled`](sim-2/property_scene_dynamics_ode_quickStepEnabled.htm)
- [`scene.dynamics.ode.quickStepIterations`](sim-2/property_scene_dynamics_ode_quickStepIterations.htm)
- [`scene.dynamics.showContactPoints`](sim-2/property_scene_dynamics_showContactPoints.htm) — Show contact points
- [`scene.dynamics.stepSize`](sim-2/property_scene_dynamics_stepSize.htm) — Dynamics dt
- [`scene.dynamics.vortex.autoSleep`](sim-2/property_scene_dynamics_vortex_autoSleep.htm)
- [`scene.dynamics.vortex.computeInertias`](sim-2/property_scene_dynamics_vortex_computeInertias.htm)
- [`scene.dynamics.vortex.constraintsAngularCompliance`](sim-2/property_scene_dynamics_vortex_constraintsAngularCompliance.htm)
- [`scene.dynamics.vortex.constraintsAngularDamping`](sim-2/property_scene_dynamics_vortex_constraintsAngularDamping.htm)
- [`scene.dynamics.vortex.constraintsAngularKineticLoss`](sim-2/property_scene_dynamics_vortex_constraintsAngularKineticLoss.htm)
- [`scene.dynamics.vortex.constraintsLinearCompliance`](sim-2/property_scene_dynamics_vortex_constraintsLinearCompliance.htm)
- [`scene.dynamics.vortex.constraintsLinearDamping`](sim-2/property_scene_dynamics_vortex_constraintsLinearDamping.htm)
- [`scene.dynamics.vortex.constraintsLinearKineticLoss`](sim-2/property_scene_dynamics_vortex_constraintsLinearKineticLoss.htm)
- [`scene.dynamics.vortex.contactTolerance`](sim-2/property_scene_dynamics_vortex_contactTolerance.htm)
- [`scene.dynamics.vortex.multithreading`](sim-2/property_scene_dynamics_vortex_multithreading.htm)
- [`scene.finalSaveRequest`](sim-2/property_scene_finalSaveRequest.htm) — Final save
- [`scene.hierarchyChangeCounter`](sim-2/property_scene_hierarchyChangeCounter.htm) — Hierarchy change counter
- [`scene.locked`](sim-2/property_scene_locked.htm) — Scene is locked
- [`scene.mainScript`](sim-2/property_scene_mainScript.htm) — Main script
- [`scene.objectCreationCounter`](sim-2/property_scene_objectCreationCounter.htm) — Object creation counter
- [`scene.objectDestructionCounter`](sim-2/property_scene_objectDestructionCounter.htm) — Object destruction counter
- [`scene.objects`](sim-2/property_scene_objects.htm) — Objects
- [`scene.orphans`](sim-2/property_scene_orphans.htm) — Orphan objects
- [`scene.path`](sim-2/property_scene_path.htm) — Scene path
- [`scene.saveCalculationStructs`](sim-2/property_scene_saveCalculationStructs.htm) — Save calculation structures
- [`scene.selection`](sim-2/property_scene_selection.htm) — Selected objects
- [`scene.simulation.pauseAtError`](sim-2/property_scene_simulation_pauseAtError.htm) — Pause simulation on script error
- [`scene.simulation.pauseAtTime`](sim-2/property_scene_simulation_pauseAtTime.htm) — Pause simulation at time
- [`scene.simulation.realtime`](sim-2/property_scene_simulation_realtime.htm) — Real-time simulation
- [`scene.simulation.realtimeModifier`](sim-2/property_scene_simulation_realtimeModifier.htm) — Real-time modifier
- [`scene.simulation.removeNewObjects`](sim-2/property_scene_simulation_removeNewObjects.htm) — Remove new objects
- [`scene.simulation.speedModifier`](sim-2/property_scene_simulation_speedModifier.htm) — Speed modifier
- [`scene.simulation.state`](sim-2/property_scene_simulation_state.htm) — Simulation state
- [`scene.simulation.stepCount`](sim-2/property_scene_simulation_stepCount.htm) — Simulation steps
- [`scene.simulation.stepsPerRendering`](sim-2/property_scene_simulation_stepsPerRendering.htm) — Steps per frame
- [`scene.simulation.time`](sim-2/property_scene_simulation_time.htm) — Simulation time
- [`scene.simulation.timeStep`](sim-2/property_scene_simulation_timeStep.htm) — Simulation dt
- [`scene.simulation.timeToPause`](sim-2/property_scene_simulation_timeToPause.htm) — Simulation pause time
- [`scene.textures`](sim-2/property_scene_textures.htm) — Textures
- [`scene.uid`](sim-2/property_scene_uid.htm) — Scene UID
- [`scene.uidString`](sim-2/property_scene_uidString.htm) — Scene UID string
- [`scene.visibilityLayers`](sim-2/property_scene_visibilityLayers.htm) — Visibility layers

## <a id="methodsAndProperties_collection"></a><a id="methodsAndProperties_collections"></a>[collection](collections.md) (methods & properties)

- [`collection:addItem`](sim-2/collection_addItem.htm) — Adds one or several items to the collection
- [`collection:changeColor`](sim-2/collection_changeColor.htm) — Changes the color of all shapes in the collection
- [`collection:checkCollision`](sim-2/collection_checkCollision.htm) — Checks collision with another entity
- [`collection:checkDistance`](sim-2/collection_checkDistance.htm) — Checks minimum distance with another entity
- [`collection:remove`](sim-2/collection_remove.htm) — Removes the collection
- [`collection:removeItem`](sim-2/collection_removeItem.htm) — Removes one or several items from the collection
- [`collection:restoreColor`](sim-2/collection_restoreColor.htm) — Restores the color of shapes in the collection
- [`app:createObject`](sim-2/app_createObject.htm) — Creates various objects (collections, scripts, sensors, etc.)
- [`app:removeObjects`](sim-2/app_removeObjects.htm) — Removes one or several objects
- [`scene:createObject`](sim-2/scene_createObject.htm) — Creates various objects (collections, scripts, sensors, etc.)
- [`scene:removeObjects`](sim-2/scene_removeObjects.htm) — Removes one or several objects
- [`collection.objects`](sim-2/property_collection_objects.htm) — Children
- [`sceneObject.collectionSelfCollisionIndicator`](sim-2/property_sceneObject_collectionSelfCollisionIndicator.htm) — Collection self-collision indicator

## <a id="methodsAndProperties_customObject"></a>[customObject](customObjects.htm) (methods & properties)

- [`customObject:makeObject`](sim-2/customObject_makeObject.htm) — Instantiates a custom object from a class
- [`customObject:remove`](sim-2/customObject_remove.htm) — Removes the custom scene object

## <a id="methodsAndProperties_script"></a>[script](scripts.md) (methods & properties)

- [`script:broadcast`](sim-2/script_broadcast.htm) — Broadcasts a message to all other scripts
- [`script:callFunction`](sim-2/script_callFunction.htm) — Calls a function
- [`script:callMethod`](sim-2/script_callMethod.htm) — Calls a method
- [`script:cancelScheduledExecution`](sim-2/script_cancelScheduledExecution.htm) — Cancels a scheduled function execution
- [`script:executeString`](sim-2/script_executeString.htm) — Executes code from a string
- [`script:getFunctions`](sim-2/script_getFunctions.htm) — Retrieves callable functions of the script
- [`script:getObject`](sim-2/script_getObject.htm) — Retrieves an object by its path and name
- [`script:getStackTraceback`](sim-2/script_getStackTraceback.htm) — Retrieves and clears the last stack traceback
- [`script:getStepping`](sim-2/script_getStepping.htm) — Informs whether the stepping operation mode is enabled
- [`script:init`](sim-2/script_init.htm) — Initializes/reinitializes the script
- [`script:lock`](sim-2/script_lock.htm) — Acquires/releases a script lock to forbid yielding
- [`script:registerFunctionHook`](sim-2/script_registerFunctionHook.htm) — Registers a function hook for callbacks
- [`script:remove`](sim-2/script_remove.htm) — Removes the script
- [`script:removeFunctionHook`](sim-2/script_removeFunctionHook.htm) — Removes a function hook
- [`script:reset`](sim-2/script_reset.htm) — Resets/ends the script
- [`script:resume`](sim-2/script_resume.htm) — Resumes the suspended script
- [`script:scheduleExecution`](sim-2/script_scheduleExecution.htm) — Schedules a function for execution after a delay
- [`script:setEventFilters`](sim-2/script_setEventFilters.htm) — Specifies filters for the sysCall_event callback
- [`script:setModuleEntry`](sim-2/script_setModuleEntry.htm) — Creates/modifies/destroys module menu entries
- [`script:setStepping`](sim-2/script_setStepping.htm) — Enables/disables stepping operation mode
- [`script:step`](sim-2/script_step.htm) — Triggers the next simulation step
- [`script:suspend`](sim-2/script_suspend.htm) — Suspends the script
- [`script:throttle`](sim-2/script_throttle.htm) — Limits the rate of a function call
- [`script:wait`](sim-2/script_wait.htm) — Waits for a certain amount of time
- [`script:yield`](sim-2/script_yield.htm) — Identical to step()
- [`app:createObject`](sim-2/app_createObject.htm) — Creates various objects (collections, scripts, sensors, etc.)
- [`app:handleAddOns`](sim-2/app_handleAddOns.htm) — Calls a system callback in add-ons
- [`app:handleSandboxes`](sim-2/app_handleSandboxes.htm) — Calls a system callback in the sandbox
- [`app:removeObjects`](sim-2/app_removeObjects.htm) — Removes one or several objects
- [`scene:createObject`](sim-2/scene_createObject.htm) — Creates various objects (collections, scripts, sensors, etc.)
- [`scene:removeObjects`](sim-2/scene_removeObjects.htm) — Removes one or several objects
- [`app.sandboxLua`](sim-2/property_app_sandboxLua.htm) — Lua sandbox
- [`app.sandboxPython`](sim-2/property_app_sandboxPython.htm) — Python sandbox
- [`scene.mainScript`](sim-2/property_scene_mainScript.htm) — Main script
- [`script.addOnMenuPath`](sim-2/property_script_addOnMenuPath.htm) — Add-on menu path
- [`script.addOnPath`](sim-2/property_script_addOnPath.htm) — Add-on path
- [`script.autoYieldDelay`](sim-2/property_script_autoYieldDelay.htm) — Automatic yield delay
- [`script.code`](sim-2/property_script_code.htm) — Code
- [`script.enabled`](sim-2/property_script_enabled.htm) — Enabled
- [`script.execPriority`](sim-2/property_script_execPriority.htm) — Execution priority
- [`script.executionDepth`](sim-2/property_script_executionDepth.htm) — Execution depth
- [`script.language`](sim-2/property_script_language.htm) — Language
- [`script.restartOnError`](sim-2/property_script_restartOnError.htm) — Restart
- [`script.script.type`](sim-2/property_script_script_type.htm) — Type
- [`script.scriptName`](sim-2/property_script_scriptName.htm) — Name
- [`script.state`](sim-2/property_script_state.htm) — State
- [`scriptObject.script`](sim-2/property_scriptObject_script.htm) — Script

## <a id="methodsAndProperties_mesh"></a>[mesh](geometryDialog.md) (methods & properties)

- [`mesh:setTexture`](sim-2/mesh_setTexture.htm) — Sets a texture
- [`mesh.color.diffuse`](sim-2/property_mesh_color_diffuse.htm) — Diffuse color
- [`mesh.color.emission`](sim-2/property_mesh_color_emission.htm) — Emission color
- [`mesh.color.specular`](sim-2/property_mesh_color_specular.htm) — Specular color
- [`mesh.color.transparency`](sim-2/property_mesh_color_transparency.htm) — Transparency
- [`mesh.colorName`](sim-2/property_mesh_colorName.htm) — Color name
- [`mesh.convex`](sim-2/property_mesh_convex.htm) — Convex
- [`mesh.culling`](sim-2/property_mesh_culling.htm) — Backface culling
- [`mesh.indices`](sim-2/property_mesh_indices.htm) — Indices
- [`mesh.normals`](sim-2/property_mesh_normals.htm) — Normals
- [`mesh.primitive`](sim-2/property_mesh_primitive.htm) — Primitive type
- [`mesh.shadingAngle`](sim-2/property_mesh_shadingAngle.htm) — Shading angle
- [`mesh.shape`](sim-2/property_mesh_shape.htm) — Shape
- [`mesh.shapeUid`](sim-2/property_mesh_shapeUid.htm) — Shape UID
- [`mesh.showEdges`](sim-2/property_mesh_showEdges.htm) — Visible edges
- [`mesh.texture.applyMode`](sim-2/property_mesh_texture_applyMode.htm) — Texture apply mode
- [`mesh.texture.interpolate`](sim-2/property_mesh_texture_interpolate.htm) — Interpolate texture
- [`mesh.texture.repeatU`](sim-2/property_mesh_texture_repeatU.htm) — Texture repeat U
- [`mesh.texture.repeatV`](sim-2/property_mesh_texture_repeatV.htm) — Texture repeat V
- [`mesh.texture.textureData`](sim-2/property_mesh_texture_textureData.htm) — Texture
- [`mesh.textureCoordinates`](sim-2/property_mesh_textureCoordinates.htm) — Texture coordinates
- [`mesh.vertices`](sim-2/property_mesh_vertices.htm) — Vertices
- [`mesh.wireframe`](sim-2/property_mesh_wireframe.htm) — Wireframe

## <a id="methodsAndProperties_textureData"></a><a id="methodsAndProperties_textures"></a>[textureData](textureDialog.md) (methods & properties)

- [`app:loadImage`](sim-2/app_loadImage.htm) — Loads an image from file
- [`app:loadImageFromBuffer`](sim-2/app_loadImageFromBuffer.htm) — Loads an image from memory
- [`app:saveImage`](sim-2/app_saveImage.htm) — Saves an image to file
- [`app:saveImageToBuffer`](sim-2/app_saveImageToBuffer.htm) — Saves an image to a buffer
- [`app:transformBuffer`](sim-2/app_transformBuffer.htm) — Modifies a buffer (format, scale, offset)
- [`app:transformImage`](sim-2/app_transformImage.htm) — Transforms an image (scaling, flipping)
- [`mesh:setTexture`](sim-2/mesh_setTexture.htm) — Sets a texture
- [`textureData:getData`](sim-2/textureData_getData.htm) — Reads a portion of the texture
- [`textureData:remove`](sim-2/textureData_remove.htm) — Removes the texture
- [`textureData:setData`](sim-2/textureData_setData.htm) — Overwrites a portion of the texture
- [`mesh.texture.applyMode`](sim-2/property_mesh_texture_applyMode.htm) — Texture apply mode
- [`mesh.texture.interpolate`](sim-2/property_mesh_texture_interpolate.htm) — Interpolate texture
- [`mesh.texture.repeatU`](sim-2/property_mesh_texture_repeatU.htm) — Texture repeat U
- [`mesh.texture.repeatV`](sim-2/property_mesh_texture_repeatV.htm) — Texture repeat V
- [`mesh.texture.textureData`](sim-2/property_mesh_texture_textureData.htm) — Texture
- [`mesh.textureCoordinates`](sim-2/property_mesh_textureCoordinates.htm) — Texture coordinates
- [`scene.textures`](sim-2/property_scene_textures.htm) — Textures
- [`textureData.image`](sim-2/property_textureData_image.htm) — Image
- [`textureData.resolution`](sim-2/property_textureData_resolution.htm) — Resolution

## <a id="methodsAndProperties_sceneObject"></a><a id="methodsAndProperties_sceneObjectFunctionality"></a>[sceneObject](objects.md) (methods & properties)

- [`app:removeObjects`](sim-2/app_removeObjects.htm) — Removes one or several objects
- [`scene:copyObjects`](sim-2/scene_copyObjects.htm) — Copies selected objects
- [`scene:cutObjects`](sim-2/scene_cutObjects.htm) — Cuts selected objects
- [`scene:duplicateObjects`](sim-2/scene_duplicateObjects.htm) — Duplicates scene objects
- [`scene:pasteObjects`](sim-2/scene_pasteObjects.htm) — Pastes objects
- [`scene:removeObjects`](sim-2/scene_removeObjects.htm) — Removes one or several objects
- [`sceneObject:changeColor`](sim-2/sceneObject_changeColor.htm) — Changes the color of the object (if shape)
- [`sceneObject:checkCollision`](sim-2/sceneObject_checkCollision.htm) — Checks collision with another entity
- [`sceneObject:checkDistance`](sim-2/sceneObject_checkDistance.htm) — Checks minimum distance with another entity
- [`sceneObject:dynamicReset`](sim-2/sceneObject_dynamicReset.htm) — Dynamically resets the object in the physics engine
- [`sceneObject:getAncestors`](sim-2/sceneObject_getAncestors.htm) — Retrieves ancestor scene objects
- [`sceneObject:getDescendants`](sim-2/sceneObject_getDescendants.htm) — Retrieves descendant scene objects
- [`sceneObject:getName`](sim-2/sceneObject_getName.htm) — Retrieves the name or path of the object
- [`sceneObject:getObject`](sim-2/sceneObject_getObject.htm) — Retrieves an object by its path and name
- [`sceneObject:getPose`](sim-2/sceneObject_getPose.htm) — Retrieves the pose of the scene object
- [`sceneObject:getPosition`](sim-2/sceneObject_getPosition.htm) — Retrieves the position of the scene object
- [`sceneObject:getQuaternion`](sim-2/sceneObject_getQuaternion.htm) — Retrieves the quaternion of the scene object
- [`sceneObject:makeClass`](sim-2/sceneObject_makeClass.htm) — Creates a class from this object
- [`sceneObject:makeObject`](sim-2/sceneObject_makeObject.htm) — Instantiates a customized scene object from a class
- [`sceneObject:remove`](sim-2/sceneObject_remove.htm) — Removes the object from the scene
- [`sceneObject:removeModel`](sim-2/sceneObject_removeModel.htm) — Removes the model from the scene
- [`sceneObject:restoreColor`](sim-2/sceneObject_restoreColor.htm) — Restores the object's color (if shape)
- [`sceneObject:saveModel`](sim-2/sceneObject_saveModel.htm) — Saves this model to a file
- [`sceneObject:saveModelToBuffer`](sim-2/sceneObject_saveModelToBuffer.htm) — Serializes this model to a buffer
- [`sceneObject:scale`](sim-2/sceneObject_scale.htm) — Scales the object non-isometrically
- [`sceneObject:scaleTree`](sim-2/sceneObject_scaleTree.htm) — Scales the object tree isometrically
- [`sceneObject:setParent`](sim-2/sceneObject_setParent.htm) — Sets the object's parent
- [`sceneObject:setPose`](sim-2/sceneObject_setPose.htm) — Sets the pose of the scene object
- [`sceneObject:setPosition`](sim-2/sceneObject_setPosition.htm) — Sets the position of the scene object
- [`sceneObject:setQuaternion`](sim-2/sceneObject_setQuaternion.htm) — Sets the quaternion of the scene object
- [`sceneObject.angularVelocity`](sim-2/property_sceneObject_angularVelocity.htm) — Angular velocity
- [`sceneObject.bbPose`](sim-2/property_sceneObject_bbPose.htm) — Bounding box pose
- [`sceneObject.cannotDelete`](sim-2/property_sceneObject_cannotDelete.htm) — Cannot delete
- [`sceneObject.cannotDeleteInSim`](sim-2/property_sceneObject_cannotDeleteInSim.htm) — Cannot delete during simulation
- [`sceneObject.childOrder`](sim-2/property_sceneObject_childOrder.htm) — Child order
- [`sceneObject.children`](sim-2/property_sceneObject_children.htm) — Children
- [`sceneObject.collapsed`](sim-2/property_sceneObject_collapsed.htm) — Collapsed hierarchy
- [`sceneObject.collectionSelfCollisionIndicator`](sim-2/property_sceneObject_collectionSelfCollisionIndicator.htm) — Collection self-collision indicator
- [`sceneObject.collidable`](sim-2/property_sceneObject_collidable.htm) — Collidable
- [`sceneObject.depthInvisible`](sim-2/property_sceneObject_depthInvisible.htm) — Depth pass invisible
- [`sceneObject.detectable`](sim-2/property_sceneObject_detectable.htm) — Detectable
- [`sceneObject.dimension`](sim-2/property_sceneObject_dimension.htm) — Bounding box size
- [`sceneObject.dna`](sim-2/property_sceneObject_dna.htm) — DNA
- [`sceneObject.dynamicFlag`](sim-2/property_sceneObject_dynamicFlag.htm) — Dynamic flag
- [`sceneObject.dynamicIcon`](sim-2/property_sceneObject_dynamicIcon.htm) — Dynamic icon
- [`sceneObject.dynamicallyEnabled`](sim-2/property_sceneObject_dynamicallyEnabled.htm) — Dynamically enabled
- [`sceneObject.eulerAngles`](sim-2/property_sceneObject_eulerAngles.htm) — Euler angles
- [`sceneObject.hideFromModelBB`](sim-2/property_sceneObject_hideFromModelBB.htm) — Hide from model bounding box
- [`sceneObject.hierarchyColor`](sim-2/property_sceneObject_hierarchyColor.htm) — Hierarchy color
- [`sceneObject.ignoreViewFitting`](sim-2/property_sceneObject_ignoreViewFitting.htm) — Ignore view fitting
- [`sceneObject.layer`](sim-2/property_sceneObject_layer.htm) — Visibility layer
- [`sceneObject.linearVelocity`](sim-2/property_sceneObject_linearVelocity.htm) — Linear velocity
- [`sceneObject.measurable`](sim-2/property_sceneObject_measurable.htm) — Measurable
- [`sceneObject.model.bbPos`](sim-2/property_sceneObject_model_bbPos.htm) — Model bounding box position
- [`sceneObject.model.bbSize`](sim-2/property_sceneObject_model_bbSize.htm) — Model bounding box size
- [`sceneObject.model.notCollidable`](sim-2/property_sceneObject_model_notCollidable.htm) — Model not collidable
- [`sceneObject.model.notDetectable`](sim-2/property_sceneObject_model_notDetectable.htm) — Model not detectable
- [`sceneObject.model.notDynamic`](sim-2/property_sceneObject_model_notDynamic.htm) — Model not dynamic
- [`sceneObject.model.notInParentBB`](sim-2/property_sceneObject_model_notInParentBB.htm) — Model invisible to other models' bounding boxes
- [`sceneObject.model.notMeasurable`](sim-2/property_sceneObject_model_notMeasurable.htm) — Model not measurable
- [`sceneObject.model.notRespondable`](sim-2/property_sceneObject_model_notRespondable.htm) — Model not respondable
- [`sceneObject.model.notVisible`](sim-2/property_sceneObject_model_notVisible.htm) — Model not visible
- [`sceneObject.model.propertyFlags`](sim-2/property_sceneObject_model_propertyFlags.htm) — Model flags
- [`sceneObject.model.scriptsNotActive`](sim-2/property_sceneObject_model_scriptsNotActive.htm) — Model scripts inactive
- [`sceneObject.modelAcknowledgment`](sim-2/property_sceneObject_modelAcknowledgment.htm) — Acknowledgment
- [`sceneObject.modelBase`](sim-2/property_sceneObject_modelBase.htm) — Model base
- [`sceneObject.modelHash`](sim-2/property_sceneObject_modelHash.htm) — Model hash
- [`sceneObject.modelInvisible`](sim-2/property_sceneObject_modelInvisible.htm) — Inherited model invisibility
- [`sceneObject.mov.altRot`](sim-2/property_sceneObject_mov_altRot.htm) — Alternate rotation axes enabled
- [`sceneObject.mov.altTransl`](sim-2/property_sceneObject_mov_altTransl.htm) — Alternate translation axes enabled
- [`sceneObject.mov.optionsFlags`](sim-2/property_sceneObject_mov_optionsFlags.htm) — Movement flags
- [`sceneObject.mov.prefRotX`](sim-2/property_sceneObject_mov_prefRotX.htm) — Preferred X-axis rotation
- [`sceneObject.mov.prefRotY`](sim-2/property_sceneObject_mov_prefRotY.htm) — Preferred Y-axis rotation
- [`sceneObject.mov.prefRotZ`](sim-2/property_sceneObject_mov_prefRotZ.htm) — Preferred Z-axis rotation
- [`sceneObject.mov.prefTranslX`](sim-2/property_sceneObject_mov_prefTranslX.htm) — Preferred X-translation
- [`sceneObject.mov.prefTranslY`](sim-2/property_sceneObject_mov_prefTranslY.htm) — Preferred Y-translation
- [`sceneObject.mov.prefTranslZ`](sim-2/property_sceneObject_mov_prefTranslZ.htm) — Preferred Z-translation
- [`sceneObject.mov.preferredAxesFlags`](sim-2/property_sceneObject_mov_preferredAxesFlags.htm) — Preferred axes
- [`sceneObject.mov.relativity`](sim-2/property_sceneObject_mov_relativity.htm) — Movement relativity
- [`sceneObject.mov.rotInSim`](sim-2/property_sceneObject_mov_rotInSim.htm) — Rotation enabled during simulation
- [`sceneObject.mov.rotNoSim`](sim-2/property_sceneObject_mov_rotNoSim.htm) — Rotation enabled
- [`sceneObject.mov.stepSize`](sim-2/property_sceneObject_mov_stepSize.htm) — Movement step sizes
- [`sceneObject.mov.translInSim`](sim-2/property_sceneObject_mov_translInSim.htm) — Translation enabled during simulation
- [`sceneObject.mov.translNoSim`](sim-2/property_sceneObject_mov_translNoSim.htm) — Translation enabled
- [`sceneObject.name`](sim-2/property_sceneObject_name.htm) — Name
- [`sceneObject.objectPropertyFlags`](sim-2/property_sceneObject_objectPropertyFlags.htm) — Object flags
- [`sceneObject.parent`](sim-2/property_sceneObject_parent.htm) — Parent
- [`sceneObject.parentUid`](sim-2/property_sceneObject_parentUid.htm) — Parent UID
- [`sceneObject.persistentUid`](sim-2/property_sceneObject_persistentUid.htm) — Persistent UID
- [`sceneObject.pose`](sim-2/property_sceneObject_pose.htm) — Pose
- [`sceneObject.position`](sim-2/property_sceneObject_position.htm) — Position
- [`sceneObject.quaternion`](sim-2/property_sceneObject_quaternion.htm) — Quaternion
- [`sceneObject.selectInvisible`](sim-2/property_sceneObject_selectInvisible.htm) — Select invisible
- [`sceneObject.selectModel`](sim-2/property_sceneObject_selectModel.htm) — Select model instead
- [`sceneObject.selectable`](sim-2/property_sceneObject_selectable.htm) — Selectable
- [`sceneObject.selected`](sim-2/property_sceneObject_selected.htm) — Selected
- [`sceneObject.tree`](sim-2/property_sceneObject_tree.htm) — Object tree
- [`sceneObject.uid`](sim-2/property_sceneObject_uid.htm) — Object UID
- [`sceneObject.visible`](sim-2/property_sceneObject_visible.htm) — Visible
- [`sceneObject.worldEulerAngles`](sim-2/property_sceneObject_worldEulerAngles.htm) — Euler angles
- [`sceneObject.worldPose`](sim-2/property_sceneObject_worldPose.htm) — Pose
- [`sceneObject.worldPosition`](sim-2/property_sceneObject_worldPosition.htm) — Position
- [`sceneObject.worldQuaternion`](sim-2/property_sceneObject_worldQuaternion.htm) — Quaternion

## <a id="methodsAndProperties_shape"></a><a id="methodsAndProperties_shapeObject"></a>[shape](shapes.md) (methods & properties)

- [`shape:alignBoundingBox`](sim-2/shape_alignBoundingBox.htm) — Reorients the shape's bounding box
- [`shape:divide`](sim-2/shape_divide.htm) — Divides a simple shape into separate ones
- [`shape:getAppearance`](sim-2/shape_getAppearance.htm) — Fetches the shape's main appearance properties
- [`shape:relocateFrame`](sim-2/shape_relocateFrame.htm) — Repositions/reorients the shape's reference frame
- [`shape:setAppearance`](sim-2/shape_setAppearance.htm) — Sets the shape's main appearance properties
- [`shape:ungroup`](sim-2/shape_ungroup.htm) — Ungroups a compound shape
- [`app:createObject`](sim-2/app_createObject.htm) — Creates various objects (collections, scripts, sensors, etc.)
- [`collection:changeColor`](sim-2/collection_changeColor.htm) — Changes the color of all shapes in the collection
- [`collection:restoreColor`](sim-2/collection_restoreColor.htm) — Restores the color of shapes in the collection
- [`mesh:setTexture`](sim-2/mesh_setTexture.htm) — Sets a texture
- [`ocTree:addFromObjects`](sim-2/ocTree_addFromObjects.htm) — Adds voxels from scene objects
- [`ocTree:subtractFromObjects`](sim-2/ocTree_subtractFromObjects.htm) — Subtracts voxels using scene objects
- [`pointCloud:addFromObjects`](sim-2/pointCloud_addFromObjects.htm) — Adds points from scene objects
- [`pointCloud:subtractFromObjects`](sim-2/pointCloud_subtractFromObjects.htm) — Subtracts points using scene objects
- [`scene:createObject`](sim-2/scene_createObject.htm) — Creates various objects (collections, scripts, sensors, etc.)
- [`scene:groupShapes`](sim-2/scene_groupShapes.htm) — Groups shapes into a compound shape
- [`scene:mergeShapes`](sim-2/scene_mergeShapes.htm) — Merges several shapes
- [`sceneObject:changeColor`](sim-2/sceneObject_changeColor.htm) — Changes the color of the object (if shape)
- [`sceneObject:restoreColor`](sim-2/sceneObject_restoreColor.htm) — Restores the object's color (if shape)
- [`shape.dynamics:addForce`](sim-2/shape_dynamics_addForce.htm) — Applies a force to the dynamically enabled shape
- [`shape.dynamics:addTorque`](sim-2/shape_dynamics_addTorque.htm) — Applies a torque to the dynamically enabled shape
- [`shape.dynamics:computeInertia`](sim-2/shape_dynamics_computeInertia.htm) — Computes and applies mass/inertia properties
- [`shape.dynamics:getContacts`](sim-2/shape_dynamics_getContacts.htm) — Retrieves the shape's contact information
- [`shape.dynamics:getInertia`](sim-2/shape_dynamics_getInertia.htm) — Retrieves the shape's inertia information
- [`shape.dynamics:setInertia`](sim-2/shape_dynamics_setInertia.htm) — Applies a new inertia matrix
- [`textureData:getData`](sim-2/textureData_getData.htm) — Reads a portion of the texture
- [`textureData:setData`](sim-2/textureData_setData.htm) — Overwrites a portion of the texture
- [`scene.saveCalculationStructs`](sim-2/property_scene_saveCalculationStructs.htm) — Save calculation structures
- [`shape.applyColor.diffuse`](sim-2/property_shape_applyColor_diffuse.htm) — Apply diffuse color
- [`shape.applyColor.emission`](sim-2/property_shape_applyColor_emission.htm) — Apply emission color
- [`shape.applyColor.specular`](sim-2/property_shape_applyColor_specular.htm) — Apply specular color
- [`shape.applyColor.transparency`](sim-2/property_shape_applyColor_transparency.htm) — Apply transparency
- [`shape.applyCulling`](sim-2/property_shape_applyCulling.htm) — Apply culling
- [`shape.applyShadingAngle`](sim-2/property_shape_applyShadingAngle.htm) — Apply shading
- [`shape.applyShowEdges`](sim-2/property_shape_applyShowEdges.htm) — Apply edges
- [`shape.compound`](sim-2/property_shape_compound.htm) — Compound
- [`shape.compoundColors.diffuse`](sim-2/property_shape_compoundColors_diffuse.htm) — Diffuse color data
- [`shape.compoundColors.emission`](sim-2/property_shape_compoundColors_emission.htm) — Emission color data
- [`shape.compoundColors.specular`](sim-2/property_shape_compoundColors_specular.htm) — Specular color data
- [`shape.compoundColors.transparency`](sim-2/property_shape_compoundColors_transparency.htm) — Transparency data
- [`shape.compoundCullings`](sim-2/property_shape_compoundCullings.htm) — Culling data
- [`shape.compoundEdges`](sim-2/property_shape_compoundEdges.htm) — Edge visibility data
- [`shape.compoundShadingAngles`](sim-2/property_shape_compoundShadingAngles.htm) — Shading angle data
- [`shape.compoundWireframe`](sim-2/property_shape_compoundWireframe.htm) — Wireframe data
- [`shape.convex`](sim-2/property_shape_convex.htm) — Convex
- [`shape.dynamics.angularVelocity`](sim-2/property_shape_dynamics_angularVelocity.htm) — Rotational velocity
- [`shape.dynamics.bullet.angularDamping`](sim-2/property_shape_dynamics_bullet_angularDamping.htm)
- [`shape.dynamics.bullet.autoShrinkConvexMeshes`](sim-2/property_shape_dynamics_bullet_autoShrinkConvexMeshes.htm)
- [`shape.dynamics.bullet.customCollisionMarginConvexEnabled`](sim-2/property_shape_dynamics_bullet_customCollisionMarginConvexEnabled.htm)
- [`shape.dynamics.bullet.customCollisionMarginConvexValue`](sim-2/property_shape_dynamics_bullet_customCollisionMarginConvexValue.htm)
- [`shape.dynamics.bullet.customCollisionMarginEnabled`](sim-2/property_shape_dynamics_bullet_customCollisionMarginEnabled.htm)
- [`shape.dynamics.bullet.customCollisionMarginValue`](sim-2/property_shape_dynamics_bullet_customCollisionMarginValue.htm)
- [`shape.dynamics.bullet.friction`](sim-2/property_shape_dynamics_bullet_friction.htm)
- [`shape.dynamics.bullet.frictionOld`](sim-2/property_shape_dynamics_bullet_frictionOld.htm)
- [`shape.dynamics.bullet.linearDamping`](sim-2/property_shape_dynamics_bullet_linearDamping.htm)
- [`shape.dynamics.bullet.restitution`](sim-2/property_shape_dynamics_bullet_restitution.htm)
- [`shape.dynamics.bullet.stickyContact`](sim-2/property_shape_dynamics_bullet_stickyContact.htm)
- [`shape.dynamics.centerOfMass`](sim-2/property_shape_dynamics_centerOfMass.htm) — Center of mass
- [`shape.dynamics.dynamic`](sim-2/property_shape_dynamics_dynamic.htm) — Dynamic
- [`shape.dynamics.engineProperties`](sim-2/property_shape_dynamics_engineProperties.htm) — Engine properties
- [`shape.dynamics.inertiaMatrix`](sim-2/property_shape_dynamics_inertiaMatrix.htm) — Inertia matrix
- [`shape.dynamics.initAngularVelocity`](sim-2/property_shape_dynamics_initAngularVelocity.htm) — Initial rotational velocity
- [`shape.dynamics.initLinearVelocity`](sim-2/property_shape_dynamics_initLinearVelocity.htm) — Initial linear velocity
- [`shape.dynamics.kinematic`](sim-2/property_shape_dynamics_kinematic.htm) — Kinematic
- [`shape.dynamics.linearVelocity`](sim-2/property_shape_dynamics_linearVelocity.htm) — Linear velocity
- [`shape.dynamics.mass`](sim-2/property_shape_dynamics_mass.htm) — Mass
- [`shape.dynamics.mujoco.adhesion`](sim-2/property_shape_dynamics_mujoco_adhesion.htm)
- [`shape.dynamics.mujoco.adhesionctrl`](sim-2/property_shape_dynamics_mujoco_adhesionctrl.htm)
- [`shape.dynamics.mujoco.adhesionctrlrange`](sim-2/property_shape_dynamics_mujoco_adhesionctrlrange.htm)
- [`shape.dynamics.mujoco.adhesionforcelimited`](sim-2/property_shape_dynamics_mujoco_adhesionforcelimited.htm)
- [`shape.dynamics.mujoco.adhesionforcerange`](sim-2/property_shape_dynamics_mujoco_adhesionforcerange.htm)
- [`shape.dynamics.mujoco.adhesiongain`](sim-2/property_shape_dynamics_mujoco_adhesiongain.htm)
- [`shape.dynamics.mujoco.condim`](sim-2/property_shape_dynamics_mujoco_condim.htm)
- [`shape.dynamics.mujoco.friction`](sim-2/property_shape_dynamics_mujoco_friction.htm)
- [`shape.dynamics.mujoco.gap`](sim-2/property_shape_dynamics_mujoco_gap.htm)
- [`shape.dynamics.mujoco.gravcomp`](sim-2/property_shape_dynamics_mujoco_gravcomp.htm)
- [`shape.dynamics.mujoco.margin`](sim-2/property_shape_dynamics_mujoco_margin.htm)
- [`shape.dynamics.mujoco.priority`](sim-2/property_shape_dynamics_mujoco_priority.htm)
- [`shape.dynamics.mujoco.solimp`](sim-2/property_shape_dynamics_mujoco_solimp.htm)
- [`shape.dynamics.mujoco.solmix`](sim-2/property_shape_dynamics_mujoco_solmix.htm)
- [`shape.dynamics.mujoco.solref`](sim-2/property_shape_dynamics_mujoco_solref.htm)
- [`shape.dynamics.newton.angularDrag`](sim-2/property_shape_dynamics_newton_angularDrag.htm)
- [`shape.dynamics.newton.fastMoving`](sim-2/property_shape_dynamics_newton_fastMoving.htm)
- [`shape.dynamics.newton.kineticFriction`](sim-2/property_shape_dynamics_newton_kineticFriction.htm)
- [`shape.dynamics.newton.linearDrag`](sim-2/property_shape_dynamics_newton_linearDrag.htm)
- [`shape.dynamics.newton.restitution`](sim-2/property_shape_dynamics_newton_restitution.htm)
- [`shape.dynamics.newton.staticFriction`](sim-2/property_shape_dynamics_newton_staticFriction.htm)
- [`shape.dynamics.ode.angularDamping`](sim-2/property_shape_dynamics_ode_angularDamping.htm)
- [`shape.dynamics.ode.friction`](sim-2/property_shape_dynamics_ode_friction.htm)
- [`shape.dynamics.ode.linearDamping`](sim-2/property_shape_dynamics_ode_linearDamping.htm)
- [`shape.dynamics.ode.maxContacts`](sim-2/property_shape_dynamics_ode_maxContacts.htm)
- [`shape.dynamics.ode.softCfm`](sim-2/property_shape_dynamics_ode_softCfm.htm)
- [`shape.dynamics.ode.softErp`](sim-2/property_shape_dynamics_ode_softErp.htm)
- [`shape.dynamics.pmi`](sim-2/property_shape_dynamics_pmi.htm) — Principal moment of inertia
- [`shape.dynamics.pmiQuaternion`](sim-2/property_shape_dynamics_pmiQuaternion.htm) — Quaternion of the principal moment of inertia
- [`shape.dynamics.respondable`](sim-2/property_shape_dynamics_respondable.htm) — Respondable
- [`shape.dynamics.respondableMask`](sim-2/property_shape_dynamics_respondableMask.htm) — Respondable mask
- [`shape.dynamics.setToDynamicWithParent`](sim-2/property_shape_dynamics_setToDynamicWithParent.htm) — Set to dynamic if gets parent
- [`shape.dynamics.startInSleepMode`](sim-2/property_shape_dynamics_startInSleepMode.htm) — Start in sleep mode
- [`shape.dynamics.vortex.adhesiveForce`](sim-2/property_shape_dynamics_vortex_adhesiveForce.htm)
- [`shape.dynamics.vortex.angularNormalAxisFollowPrimaryAxis`](sim-2/property_shape_dynamics_vortex_angularNormalAxisFollowPrimaryAxis.htm)
- [`shape.dynamics.vortex.angularNormalAxisFrictionModel`](sim-2/property_shape_dynamics_vortex_angularNormalAxisFrictionModel.htm)
- [`shape.dynamics.vortex.angularNormalAxisFrictionValue`](sim-2/property_shape_dynamics_vortex_angularNormalAxisFrictionValue.htm)
- [`shape.dynamics.vortex.angularNormalAxisSlide`](sim-2/property_shape_dynamics_vortex_angularNormalAxisSlide.htm)
- [`shape.dynamics.vortex.angularNormalAxisSlip`](sim-2/property_shape_dynamics_vortex_angularNormalAxisSlip.htm)
- [`shape.dynamics.vortex.angularNormalAxisStaticFrictionScale`](sim-2/property_shape_dynamics_vortex_angularNormalAxisStaticFrictionScale.htm)
- [`shape.dynamics.vortex.angularPrimaryAxisFrictionModel`](sim-2/property_shape_dynamics_vortex_angularPrimaryAxisFrictionModel.htm)
- [`shape.dynamics.vortex.angularPrimaryAxisFrictionValue`](sim-2/property_shape_dynamics_vortex_angularPrimaryAxisFrictionValue.htm)
- [`shape.dynamics.vortex.angularPrimaryAxisSlide`](sim-2/property_shape_dynamics_vortex_angularPrimaryAxisSlide.htm)
- [`shape.dynamics.vortex.angularPrimaryAxisSlip`](sim-2/property_shape_dynamics_vortex_angularPrimaryAxisSlip.htm)
- [`shape.dynamics.vortex.angularPrimaryAxisStaticFrictionScale`](sim-2/property_shape_dynamics_vortex_angularPrimaryAxisStaticFrictionScale.htm)
- [`shape.dynamics.vortex.angularSecondaryAxisFollowPrimaryAxis`](sim-2/property_shape_dynamics_vortex_angularSecondaryAxisFollowPrimaryAxis.htm)
- [`shape.dynamics.vortex.angularSecondaryAxisFrictionModel`](sim-2/property_shape_dynamics_vortex_angularSecondaryAxisFrictionModel.htm)
- [`shape.dynamics.vortex.angularSecondaryAxisFrictionValue`](sim-2/property_shape_dynamics_vortex_angularSecondaryAxisFrictionValue.htm)
- [`shape.dynamics.vortex.angularSecondaryAxisSlide`](sim-2/property_shape_dynamics_vortex_angularSecondaryAxisSlide.htm)
- [`shape.dynamics.vortex.angularSecondaryAxisSlip`](sim-2/property_shape_dynamics_vortex_angularSecondaryAxisSlip.htm)
- [`shape.dynamics.vortex.angularSecondaryAxisStaticFrictionScale`](sim-2/property_shape_dynamics_vortex_angularSecondaryAxisStaticFrictionScale.htm)
- [`shape.dynamics.vortex.angularVelDamping`](sim-2/property_shape_dynamics_vortex_angularVelDamping.htm)
- [`shape.dynamics.vortex.autoAngularDampingEnabled`](sim-2/property_shape_dynamics_vortex_autoAngularDampingEnabled.htm)
- [`shape.dynamics.vortex.autoAngularDampingTensionRatio`](sim-2/property_shape_dynamics_vortex_autoAngularDampingTensionRatio.htm)
- [`shape.dynamics.vortex.autoSleepThresholdAngularAccel`](sim-2/property_shape_dynamics_vortex_autoSleepThresholdAngularAccel.htm)
- [`shape.dynamics.vortex.autoSleepThresholdAngularSpeed`](sim-2/property_shape_dynamics_vortex_autoSleepThresholdAngularSpeed.htm)
- [`shape.dynamics.vortex.autoSleepThresholdLinearAccel`](sim-2/property_shape_dynamics_vortex_autoSleepThresholdLinearAccel.htm)
- [`shape.dynamics.vortex.autoSleepThresholdLinearSpeed`](sim-2/property_shape_dynamics_vortex_autoSleepThresholdLinearSpeed.htm)
- [`shape.dynamics.vortex.autoSleepThresholdSteps`](sim-2/property_shape_dynamics_vortex_autoSleepThresholdSteps.htm)
- [`shape.dynamics.vortex.autoSlip`](sim-2/property_shape_dynamics_vortex_autoSlip.htm)
- [`shape.dynamics.vortex.compliance`](sim-2/property_shape_dynamics_vortex_compliance.htm)
- [`shape.dynamics.vortex.convexAsRandom`](sim-2/property_shape_dynamics_vortex_convexAsRandom.htm)
- [`shape.dynamics.vortex.damping`](sim-2/property_shape_dynamics_vortex_damping.htm)
- [`shape.dynamics.vortex.fastMoving`](sim-2/property_shape_dynamics_vortex_fastMoving.htm)
- [`shape.dynamics.vortex.linearPrimaryAxisFrictionModel`](sim-2/property_shape_dynamics_vortex_linearPrimaryAxisFrictionModel.htm)
- [`shape.dynamics.vortex.linearPrimaryAxisFrictionValue`](sim-2/property_shape_dynamics_vortex_linearPrimaryAxisFrictionValue.htm)
- [`shape.dynamics.vortex.linearPrimaryAxisSlide`](sim-2/property_shape_dynamics_vortex_linearPrimaryAxisSlide.htm)
- [`shape.dynamics.vortex.linearPrimaryAxisSlip`](sim-2/property_shape_dynamics_vortex_linearPrimaryAxisSlip.htm)
- [`shape.dynamics.vortex.linearPrimaryAxisStaticFrictionScale`](sim-2/property_shape_dynamics_vortex_linearPrimaryAxisStaticFrictionScale.htm)
- [`shape.dynamics.vortex.linearPrimaryValue`](sim-2/property_shape_dynamics_vortex_linearPrimaryValue.htm)
- [`shape.dynamics.vortex.linearSecondaryAxisFollowPrimaryAxis`](sim-2/property_shape_dynamics_vortex_linearSecondaryAxisFollowPrimaryAxis.htm)
- [`shape.dynamics.vortex.linearSecondaryAxisFrictionModel`](sim-2/property_shape_dynamics_vortex_linearSecondaryAxisFrictionModel.htm)
- [`shape.dynamics.vortex.linearSecondaryAxisFrictionValue`](sim-2/property_shape_dynamics_vortex_linearSecondaryAxisFrictionValue.htm)
- [`shape.dynamics.vortex.linearSecondaryAxisSlide`](sim-2/property_shape_dynamics_vortex_linearSecondaryAxisSlide.htm)
- [`shape.dynamics.vortex.linearSecondaryAxisSlip`](sim-2/property_shape_dynamics_vortex_linearSecondaryAxisSlip.htm)
- [`shape.dynamics.vortex.linearSecondaryAxisStaticFrictionScale`](sim-2/property_shape_dynamics_vortex_linearSecondaryAxisStaticFrictionScale.htm)
- [`shape.dynamics.vortex.linearVelDamping`](sim-2/property_shape_dynamics_vortex_linearVelDamping.htm)
- [`shape.dynamics.vortex.materialUniqueId`](sim-2/property_shape_dynamics_vortex_materialUniqueId.htm)
- [`shape.dynamics.vortex.primitiveAsConvex`](sim-2/property_shape_dynamics_vortex_primitiveAsConvex.htm)
- [`shape.dynamics.vortex.randomAsTerrain`](sim-2/property_shape_dynamics_vortex_randomAsTerrain.htm)
- [`shape.dynamics.vortex.restitution`](sim-2/property_shape_dynamics_vortex_restitution.htm)
- [`shape.dynamics.vortex.restitutionThreshold`](sim-2/property_shape_dynamics_vortex_restitutionThreshold.htm)
- [`shape.dynamics.vortex.skinThickness`](sim-2/property_shape_dynamics_vortex_skinThickness.htm)
- [`shape.flipFaces`](sim-2/property_shape_flipFaces.htm) — Flip faces
- [`shape.meshes`](sim-2/property_shape_meshes.htm) — Meshes
- [`shape.primitive`](sim-2/property_shape_primitive.htm) — Primitive

## <a id="methodsAndProperties_joint"></a><a id="methodsAndProperties_jointObject"></a>[joint](joints.md) (methods & properties)

- [`joint:setTargetPosition`](sim-2/joint_setTargetPosition.htm) — Sets the joint's desired linear/angular position
- [`joint:setTargetVelocity`](sim-2/joint_setTargetVelocity.htm) — Sets the joint's desired linear/angular velocity
- [`app:createObject`](sim-2/app_createObject.htm) — Creates various objects (collections, scripts, sensors, etc.)
- [`scene:createObject`](sim-2/scene_createObject.htm) — Creates various objects (collections, scripts, sensors, etc.)
- [`joint.bounds`](sim-2/property_joint_bounds.htm) — Bounds
- [`joint.color.diffuse`](sim-2/property_joint_color_diffuse.htm) — Diffuse color
- [`joint.color.emission`](sim-2/property_joint_color_emission.htm) — Emission color
- [`joint.color.specular`](sim-2/property_joint_color_specular.htm) — Specular color
- [`joint.configuration`](sim-2/property_joint_configuration.htm) — Configuration
- [`joint.cyclic`](sim-2/property_joint_cyclic.htm) — Cyclic
- [`joint.dependencyMaster`](sim-2/property_joint_dependencyMaster.htm) — Dependency master
- [`joint.dependencyParams`](sim-2/property_joint_dependencyParams.htm) — Dependency parameters
- [`joint.diameter`](sim-2/property_joint_diameter.htm) — Diameter
- [`joint.dynamics.averageForce`](sim-2/property_joint_dynamics_averageForce.htm) — Average force
- [`joint.dynamics.bullet.normalCfm`](sim-2/property_joint_dynamics_bullet_normalCfm.htm)
- [`joint.dynamics.bullet.posPid`](sim-2/property_joint_dynamics_bullet_posPid.htm)
- [`joint.dynamics.bullet.stopCfm`](sim-2/property_joint_dynamics_bullet_stopCfm.htm)
- [`joint.dynamics.bullet.stopErp`](sim-2/property_joint_dynamics_bullet_stopErp.htm)
- [`joint.dynamics.ctrlMode`](sim-2/property_joint_dynamics_ctrlMode.htm) — Control mode
- [`joint.dynamics.engineProperties`](sim-2/property_joint_dynamics_engineProperties.htm) — Engine properties
- [`joint.dynamics.force`](sim-2/property_joint_dynamics_force.htm) — Force
- [`joint.dynamics.mujoco.armature`](sim-2/property_joint_dynamics_mujoco_armature.htm)
- [`joint.dynamics.mujoco.dependencyPolyCoeff`](sim-2/property_joint_dynamics_mujoco_dependencyPolyCoeff.htm)
- [`joint.dynamics.mujoco.frictionLoss`](sim-2/property_joint_dynamics_mujoco_frictionLoss.htm)
- [`joint.dynamics.mujoco.frictionSolimp`](sim-2/property_joint_dynamics_mujoco_frictionSolimp.htm)
- [`joint.dynamics.mujoco.frictionSolref`](sim-2/property_joint_dynamics_mujoco_frictionSolref.htm)
- [`joint.dynamics.mujoco.limitsSolimp`](sim-2/property_joint_dynamics_mujoco_limitsSolimp.htm)
- [`joint.dynamics.mujoco.limitsSolref`](sim-2/property_joint_dynamics_mujoco_limitsSolref.htm)
- [`joint.dynamics.mujoco.margin`](sim-2/property_joint_dynamics_mujoco_margin.htm)
- [`joint.dynamics.mujoco.posPid`](sim-2/property_joint_dynamics_mujoco_posPid.htm)
- [`joint.dynamics.mujoco.springDamping`](sim-2/property_joint_dynamics_mujoco_springDamping.htm)
- [`joint.dynamics.mujoco.springRef`](sim-2/property_joint_dynamics_mujoco_springRef.htm)
- [`joint.dynamics.mujoco.springSpringDamper`](sim-2/property_joint_dynamics_mujoco_springSpringDamper.htm)
- [`joint.dynamics.mujoco.springStiffness`](sim-2/property_joint_dynamics_mujoco_springStiffness.htm)
- [`joint.dynamics.newton.posPid`](sim-2/property_joint_dynamics_newton_posPid.htm)
- [`joint.dynamics.ode.bounce`](sim-2/property_joint_dynamics_ode_bounce.htm)
- [`joint.dynamics.ode.fudge`](sim-2/property_joint_dynamics_ode_fudge.htm)
- [`joint.dynamics.ode.normalCfm`](sim-2/property_joint_dynamics_ode_normalCfm.htm)
- [`joint.dynamics.ode.posPid`](sim-2/property_joint_dynamics_ode_posPid.htm)
- [`joint.dynamics.ode.stopCfm`](sim-2/property_joint_dynamics_ode_stopCfm.htm)
- [`joint.dynamics.ode.stopErp`](sim-2/property_joint_dynamics_ode_stopErp.htm)
- [`joint.dynamics.smoothMotionProfile`](sim-2/property_joint_dynamics_smoothMotionProfile.htm) — Smooth dynamics motion profile
- [`joint.dynamics.springDamper`](sim-2/property_joint_dynamics_springDamper.htm) — Spring damper parameters
- [`joint.dynamics.targetForce`](sim-2/property_joint_dynamics_targetForce.htm) — Target force
- [`joint.dynamics.vortex.axisFrictionEnabled`](sim-2/property_joint_dynamics_vortex_axisFrictionEnabled.htm)
- [`joint.dynamics.vortex.axisFrictionLoss`](sim-2/property_joint_dynamics_vortex_axisFrictionLoss.htm)
- [`joint.dynamics.vortex.axisFrictionMaxForce`](sim-2/property_joint_dynamics_vortex_axisFrictionMaxForce.htm)
- [`joint.dynamics.vortex.axisFrictionProportional`](sim-2/property_joint_dynamics_vortex_axisFrictionProportional.htm)
- [`joint.dynamics.vortex.axisFrictionValue`](sim-2/property_joint_dynamics_vortex_axisFrictionValue.htm)
- [`joint.dynamics.vortex.axisLimitsLowerDamping`](sim-2/property_joint_dynamics_vortex_axisLimitsLowerDamping.htm)
- [`joint.dynamics.vortex.axisLimitsLowerMaxForce`](sim-2/property_joint_dynamics_vortex_axisLimitsLowerMaxForce.htm)
- [`joint.dynamics.vortex.axisLimitsLowerRestitution`](sim-2/property_joint_dynamics_vortex_axisLimitsLowerRestitution.htm)
- [`joint.dynamics.vortex.axisLimitsLowerStiffness`](sim-2/property_joint_dynamics_vortex_axisLimitsLowerStiffness.htm)
- [`joint.dynamics.vortex.axisLimitsUpperDamping`](sim-2/property_joint_dynamics_vortex_axisLimitsUpperDamping.htm)
- [`joint.dynamics.vortex.axisLimitsUpperMaxForce`](sim-2/property_joint_dynamics_vortex_axisLimitsUpperMaxForce.htm)
- [`joint.dynamics.vortex.axisLimitsUpperRestitution`](sim-2/property_joint_dynamics_vortex_axisLimitsUpperRestitution.htm)
- [`joint.dynamics.vortex.axisLimitsUpperStiffness`](sim-2/property_joint_dynamics_vortex_axisLimitsUpperStiffness.htm)
- [`joint.dynamics.vortex.frictionEnabledBits`](sim-2/property_joint_dynamics_vortex_frictionEnabledBits.htm)
- [`joint.dynamics.vortex.frictionProportionalBits`](sim-2/property_joint_dynamics_vortex_frictionProportionalBits.htm)
- [`joint.dynamics.vortex.posPid`](sim-2/property_joint_dynamics_vortex_posPid.htm)
- [`joint.dynamics.vortex.relaxationEnabledBits`](sim-2/property_joint_dynamics_vortex_relaxationEnabledBits.htm)
- [`joint.dynamics.vortex.xAxisOrientFrictionCoeff`](sim-2/property_joint_dynamics_vortex_xAxisOrientFrictionCoeff.htm)
- [`joint.dynamics.vortex.xAxisOrientFrictionLoss`](sim-2/property_joint_dynamics_vortex_xAxisOrientFrictionLoss.htm)
- [`joint.dynamics.vortex.xAxisOrientFrictionMaxTorque`](sim-2/property_joint_dynamics_vortex_xAxisOrientFrictionMaxTorque.htm)
- [`joint.dynamics.vortex.xAxisOrientRelaxationDamping`](sim-2/property_joint_dynamics_vortex_xAxisOrientRelaxationDamping.htm)
- [`joint.dynamics.vortex.xAxisOrientRelaxationLoss`](sim-2/property_joint_dynamics_vortex_xAxisOrientRelaxationLoss.htm)
- [`joint.dynamics.vortex.xAxisOrientRelaxationStiffness`](sim-2/property_joint_dynamics_vortex_xAxisOrientRelaxationStiffness.htm)
- [`joint.dynamics.vortex.xAxisPosFrictionCoeff`](sim-2/property_joint_dynamics_vortex_xAxisPosFrictionCoeff.htm)
- [`joint.dynamics.vortex.xAxisPosFrictionLoss`](sim-2/property_joint_dynamics_vortex_xAxisPosFrictionLoss.htm)
- [`joint.dynamics.vortex.xAxisPosFrictionMaxForce`](sim-2/property_joint_dynamics_vortex_xAxisPosFrictionMaxForce.htm)
- [`joint.dynamics.vortex.xAxisPosRelaxationDamping`](sim-2/property_joint_dynamics_vortex_xAxisPosRelaxationDamping.htm)
- [`joint.dynamics.vortex.xAxisPosRelaxationLoss`](sim-2/property_joint_dynamics_vortex_xAxisPosRelaxationLoss.htm)
- [`joint.dynamics.vortex.xAxisPosRelaxationStiffness`](sim-2/property_joint_dynamics_vortex_xAxisPosRelaxationStiffness.htm)
- [`joint.dynamics.vortex.yAxisOrientFrictionCoeff`](sim-2/property_joint_dynamics_vortex_yAxisOrientFrictionCoeff.htm)
- [`joint.dynamics.vortex.yAxisOrientFrictionLoss`](sim-2/property_joint_dynamics_vortex_yAxisOrientFrictionLoss.htm)
- [`joint.dynamics.vortex.yAxisOrientFrictionMaxTorque`](sim-2/property_joint_dynamics_vortex_yAxisOrientFrictionMaxTorque.htm)
- [`joint.dynamics.vortex.yAxisOrientRelaxationDamping`](sim-2/property_joint_dynamics_vortex_yAxisOrientRelaxationDamping.htm)
- [`joint.dynamics.vortex.yAxisOrientRelaxationLoss`](sim-2/property_joint_dynamics_vortex_yAxisOrientRelaxationLoss.htm)
- [`joint.dynamics.vortex.yAxisOrientRelaxationStiffness`](sim-2/property_joint_dynamics_vortex_yAxisOrientRelaxationStiffness.htm)
- [`joint.dynamics.vortex.yAxisPosFrictionCoeff`](sim-2/property_joint_dynamics_vortex_yAxisPosFrictionCoeff.htm)
- [`joint.dynamics.vortex.yAxisPosFrictionLoss`](sim-2/property_joint_dynamics_vortex_yAxisPosFrictionLoss.htm)
- [`joint.dynamics.vortex.yAxisPosFrictionMaxForce`](sim-2/property_joint_dynamics_vortex_yAxisPosFrictionMaxForce.htm)
- [`joint.dynamics.vortex.yAxisPosRelaxationDamping`](sim-2/property_joint_dynamics_vortex_yAxisPosRelaxationDamping.htm)
- [`joint.dynamics.vortex.yAxisPosRelaxationLoss`](sim-2/property_joint_dynamics_vortex_yAxisPosRelaxationLoss.htm)
- [`joint.dynamics.vortex.yAxisPosRelaxationStiffness`](sim-2/property_joint_dynamics_vortex_yAxisPosRelaxationStiffness.htm)
- [`joint.dynamics.vortex.zAxisOrientFrictionCoeff`](sim-2/property_joint_dynamics_vortex_zAxisOrientFrictionCoeff.htm)
- [`joint.dynamics.vortex.zAxisOrientFrictionLoss`](sim-2/property_joint_dynamics_vortex_zAxisOrientFrictionLoss.htm)
- [`joint.dynamics.vortex.zAxisOrientFrictionMaxTorque`](sim-2/property_joint_dynamics_vortex_zAxisOrientFrictionMaxTorque.htm)
- [`joint.dynamics.vortex.zAxisOrientRelaxationDamping`](sim-2/property_joint_dynamics_vortex_zAxisOrientRelaxationDamping.htm)
- [`joint.dynamics.vortex.zAxisOrientRelaxationLoss`](sim-2/property_joint_dynamics_vortex_zAxisOrientRelaxationLoss.htm)
- [`joint.dynamics.vortex.zAxisOrientRelaxationStiffness`](sim-2/property_joint_dynamics_vortex_zAxisOrientRelaxationStiffness.htm)
- [`joint.dynamics.vortex.zAxisPosFrictionCoeff`](sim-2/property_joint_dynamics_vortex_zAxisPosFrictionCoeff.htm)
- [`joint.dynamics.vortex.zAxisPosFrictionLoss`](sim-2/property_joint_dynamics_vortex_zAxisPosFrictionLoss.htm)
- [`joint.dynamics.vortex.zAxisPosFrictionMaxForce`](sim-2/property_joint_dynamics_vortex_zAxisPosFrictionMaxForce.htm)
- [`joint.dynamics.vortex.zAxisPosRelaxationDamping`](sim-2/property_joint_dynamics_vortex_zAxisPosRelaxationDamping.htm)
- [`joint.dynamics.vortex.zAxisPosRelaxationLoss`](sim-2/property_joint_dynamics_vortex_zAxisPosRelaxationLoss.htm)
- [`joint.dynamics.vortex.zAxisPosRelaxationStiffness`](sim-2/property_joint_dynamics_vortex_zAxisPosRelaxationStiffness.htm)
- [`joint.enforceBounds`](sim-2/property_joint_enforceBounds.htm) — Enforce bounds
- [`joint.intrinsicError`](sim-2/property_joint_intrinsicError.htm) — Intrinsic error
- [`joint.intrinsicPose`](sim-2/property_joint_intrinsicPose.htm) — Intrinsic pose
- [`joint.joint.position`](sim-2/property_joint_joint_position.htm) — Position
- [`joint.joint.quaternion`](sim-2/property_joint_joint_quaternion.htm) — Spherical joint quaternion
- [`joint.joint.type`](sim-2/property_joint_joint_type.htm) — Type
- [`joint.length`](sim-2/property_joint_length.htm) — Length
- [`joint.maxVelAccelJerk`](sim-2/property_joint_maxVelAccelJerk.htm) — Maximum velocity, acceleration and jerk
- [`joint.mode`](sim-2/property_joint_mode.htm) — Mode
- [`joint.screwLead`](sim-2/property_joint_screwLead.htm) — Screw lead
- [`joint.targetPosition`](sim-2/property_joint_targetPosition.htm) — Target position
- [`joint.targetVelocity`](sim-2/property_joint_targetVelocity.htm) — Target velocity
- [`joint.velocity`](sim-2/property_joint_velocity.htm) — Velocity

## <a id="methodsAndProperties_dummy"></a><a id="methodsAndProperties_dummyObject"></a>[dummy](dummies.md) (methods & properties)

- [`app:createObject`](sim-2/app_createObject.htm) — Creates various objects (collections, scripts, sensors, etc.)
- [`ocTree:addFromObjects`](sim-2/ocTree_addFromObjects.htm) — Adds voxels from scene objects
- [`ocTree:subtractFromObjects`](sim-2/ocTree_subtractFromObjects.htm) — Subtracts voxels using scene objects
- [`pointCloud:addFromObjects`](sim-2/pointCloud_addFromObjects.htm) — Adds points from scene objects
- [`pointCloud:subtractFromObjects`](sim-2/pointCloud_subtractFromObjects.htm) — Subtracts points using scene objects
- [`scene:createObject`](sim-2/scene_createObject.htm) — Creates various objects (collections, scripts, sensors, etc.)
- [`dummy.assemblyTag`](sim-2/property_dummy_assemblyTag.htm) — Assembly tag
- [`dummy.color.diffuse`](sim-2/property_dummy_color_diffuse.htm) — Diffuse color
- [`dummy.color.emission`](sim-2/property_dummy_color_emission.htm) — Emission color
- [`dummy.color.specular`](sim-2/property_dummy_color_specular.htm) — Specular color
- [`dummy.dummy.type`](sim-2/property_dummy_dummy_type.htm) — Type
- [`dummy.dynamics.engineProperties`](sim-2/property_dummy_dynamics_engineProperties.htm) — Engine properties
- [`dummy.dynamics.mujoco.jointProxyHandle`](sim-2/property_dummy_dynamics_mujoco_jointProxyHandle.htm) — Joint proxy
- [`dummy.dynamics.mujoco.limitsEnabled`](sim-2/property_dummy_dynamics_mujoco_limitsEnabled.htm)
- [`dummy.dynamics.mujoco.limitsRange`](sim-2/property_dummy_dynamics_mujoco_limitsRange.htm)
- [`dummy.dynamics.mujoco.limitsSolimp`](sim-2/property_dummy_dynamics_mujoco_limitsSolimp.htm)
- [`dummy.dynamics.mujoco.limitsSolref`](sim-2/property_dummy_dynamics_mujoco_limitsSolref.htm)
- [`dummy.dynamics.mujoco.margin`](sim-2/property_dummy_dynamics_mujoco_margin.htm)
- [`dummy.dynamics.mujoco.overlapConstrSolimp`](sim-2/property_dummy_dynamics_mujoco_overlapConstrSolimp.htm)
- [`dummy.dynamics.mujoco.overlapConstrSolref`](sim-2/property_dummy_dynamics_mujoco_overlapConstrSolref.htm)
- [`dummy.dynamics.mujoco.overlapConstrTorquescale`](sim-2/property_dummy_dynamics_mujoco_overlapConstrTorquescale.htm)
- [`dummy.dynamics.mujoco.springDamping`](sim-2/property_dummy_dynamics_mujoco_springDamping.htm)
- [`dummy.dynamics.mujoco.springLength`](sim-2/property_dummy_dynamics_mujoco_springLength.htm)
- [`dummy.dynamics.mujoco.springStiffness`](sim-2/property_dummy_dynamics_mujoco_springStiffness.htm)
- [`dummy.linkedDummy`](sim-2/property_dummy_linkedDummy.htm) — Linked dummy
- [`dummy.size`](sim-2/property_dummy_size.htm) — Size

## <a id="methodsAndProperties_marker"></a>[marker](markers.md) (methods & properties)

- [`marker:addItems`](sim-2/marker_addItems.htm) — Adds items to a marker
- [`marker:addPackedItems`](sim-2/marker_addPackedItems.htm) — Adds packed items to a marker
- [`marker:clearItems`](sim-2/marker_clearItems.htm) — Clears a marker
- [`marker:removeItems`](sim-2/marker_removeItems.htm) — Removes specific items from a marker
- [`app:createObject`](sim-2/app_createObject.htm) — Creates various objects (collections, scripts, sensors, etc.)
- [`scene:createObject`](sim-2/scene_createObject.htm) — Creates various objects (collections, scripts, sensors, etc.)
- [`marker.colors`](sim-2/property_marker_colors.htm) — Colors
- [`marker.cyclic`](sim-2/property_marker_cyclic.htm) — Cyclic
- [`marker.defaultItemSize`](sim-2/property_marker_defaultItemSize.htm) — Default size
- [`marker.indices`](sim-2/property_marker_indices.htm) — Indices
- [`marker.local`](sim-2/property_marker_local.htm) — Local
- [`marker.marker.type`](sim-2/property_marker_marker_type.htm) — Type
- [`marker.normals`](sim-2/property_marker_normals.htm) — Normals
- [`marker.overlay`](sim-2/property_marker_overlay.htm) — Overlay
- [`marker.packedPoints`](sim-2/property_marker_packedPoints.htm) — Packed points
- [`marker.packedQuaternions`](sim-2/property_marker_packedQuaternions.htm) — Packed quaternions
- [`marker.packedSizes`](sim-2/property_marker_packedSizes.htm) — Packed sizes
- [`marker.points`](sim-2/property_marker_points.htm) — Points
- [`marker.quaternions`](sim-2/property_marker_quaternions.htm) — Quaternions
- [`marker.sizes`](sim-2/property_marker_sizes.htm) — Sizes
- [`marker.vertices`](sim-2/property_marker_vertices.htm) — Vertices

## <a id="methodsAndProperties_scriptObject"></a><a id="methodsAndProperties_scriptObject"></a>  
[scriptObject](scriptObjects.md) (methods & properties)

- [`app:createObject`](sim-2/app_createObject.htm) — Creates various objects (collections, scripts, sensors, etc.)
- [`scene:createObject`](sim-2/scene_createObject.htm) — Creates various objects (collections, scripts, sensors, etc.)
- [`script:callFunction`](sim-2/script_callFunction.htm) — Calls a function
- [`script:callMethod`](sim-2/script_callMethod.htm) — Calls a method
- [`script:executeString`](sim-2/script_executeString.htm) — Executes code from a string
- [`script:getFunctions`](sim-2/script_getFunctions.htm) — Retrieves callable functions of the script
- [`script:getStackTraceback`](sim-2/script_getStackTraceback.htm) — Retrieves and clears the last stack traceback
- [`script:init`](sim-2/script_init.htm) — Initializes/reinitializes the script
- [`script:reset`](sim-2/script_reset.htm) — Resets/ends the script
- [`script:resume`](sim-2/script_resume.htm) — Resumes the suspended script
- [`script:suspend`](sim-2/script_suspend.htm) — Suspends the script
- [`sceneObject.model.scriptsNotActive`](sim-2/property_sceneObject_model_scriptsNotActive.htm) — Model scripts inactive
- [`scriptObject.color.diffuse`](sim-2/property_scriptObject_color_diffuse.htm) — Diffuse color
- [`scriptObject.color.emission`](sim-2/property_scriptObject_color_emission.htm) — Emission color
- [`scriptObject.color.specular`](sim-2/property_scriptObject_color_specular.htm) — Specular color
- [`scriptObject.resetAfterSimError`](sim-2/property_scriptObject_resetAfterSimError.htm) — Reset after simulation error
- [`scriptObject.script`](sim-2/property_scriptObject_script.htm) — Script
- [`scriptObject.scriptObject.type`](sim-2/property_scriptObject_scriptObject_type.htm) — Type
- [`scriptObject.size`](sim-2/property_scriptObject_size.htm) — Size

## <a id="methodsAndProperties_camera"></a><a id="methodsAndProperties_cameraObject"></a>[camera](cameras.md) (methods & properties)

- [`camera:getImage`](sim-2/camera_getImage.htm) — Returns an image as seen by the camera
- [`app:createObject`](sim-2/app_createObject.htm) — Creates various objects (collections, scripts, sensors, etc.)
- [`scene:createObject`](sim-2/scene_createObject.htm) — Creates various objects (collections, scripts, sensors, etc.)
- [`camera.clippingPlanes`](sim-2/property_camera_clippingPlanes.htm) — Clipping planes
- [`camera.color.diffuse`](sim-2/property_camera_color_diffuse.htm) — Diffuse color
- [`camera.color.emission`](sim-2/property_camera_color_emission.htm) — Emission color
- [`camera.color.specular`](sim-2/property_camera_color_specular.htm) — Specular color
- [`camera.frustumCornerFar`](sim-2/property_camera_frustumCornerFar.htm) — Far corner of view frustum
- [`camera.frustumCornerNear`](sim-2/property_camera_frustumCornerNear.htm) — Near corner of view frustum
- [`camera.parentAsManipulationProxy`](sim-2/property_camera_parentAsManipulationProxy.htm) — Parent as proxy
- [`camera.perspective`](sim-2/property_camera_perspective.htm) — Perspective
- [`camera.resolution`](sim-2/property_camera_resolution.htm) — Resolution
- [`camera.rotationEnabled`](sim-2/property_camera_rotationEnabled.htm) — Rotation enabled
- [`camera.showFrustum`](sim-2/property_camera_showFrustum.htm) — Show view frustum
- [`camera.size`](sim-2/property_camera_size.htm) — Size
- [`camera.trackedObject`](sim-2/property_camera_trackedObject.htm) — Tracked object
- [`camera.translationEnabled`](sim-2/property_camera_translationEnabled.htm) — Translation enabled
- [`camera.viewAngle`](sim-2/property_camera_viewAngle.htm) — View angle
- [`camera.viewSize`](sim-2/property_camera_viewSize.htm) — View size

## <a id="methodsAndProperties_light"></a><a id="methodsAndProperties_lightObject"></a>[light](lights.md) (methods & properties)

- [`app:createObject`](sim-2/app_createObject.htm) — Creates various objects (collections, scripts, sensors, etc.)
- [`scene:createObject`](sim-2/scene_createObject.htm) — Creates various objects (collections, scripts, sensors, etc.)
- [`light.attenuationFactors`](sim-2/property_light_attenuationFactors.htm) — Attenuation factors
- [`light.color.diffuse`](sim-2/property_light_color_diffuse.htm) — Diffuse color
- [`light.color.emission`](sim-2/property_light_color_emission.htm) — Emission color
- [`light.color.specular`](sim-2/property_light_color_specular.htm) — Specular color
- [`light.enabled`](sim-2/property_light_enabled.htm) — Enabled
- [`light.light.type`](sim-2/property_light_light_type.htm) — Type
- [`light.lightColor.diffuse`](sim-2/property_light_lightColor_diffuse.htm) — Diffuse color
- [`light.lightColor.emission`](sim-2/property_light_lightColor_emission.htm) — Emission color
- [`light.lightColor.specular`](sim-2/property_light_lightColor_specular.htm) — Specular color
- [`light.povray.castShadows`](sim-2/property_light_povray_castShadows.htm) — POV-Ray: Cast shadows
- [`light.size`](sim-2/property_light_size.htm) — Size
- [`light.spotCutoffAngle`](sim-2/property_light_spotCutoffAngle.htm) — Cutoff angle
- [`light.spotExponent`](sim-2/property_light_spotExponent.htm) — Spot exponent

## <a id="methodsAndProperties_graph"></a><a id="methodsAndProperties_graphs"></a>[graph](graphs.md) (methods & properties)

- [`graph:addCurve`](sim-2/graph_addCurve.htm) — Adds or updates a graph curve
- [`graph:addSignal`](sim-2/graph_addSignal.htm) — Adds or updates a graph signal
- [`graph:removeTrace`](sim-2/graph_removeTrace.htm) — Removes a signal or curve
- [`graph:reset`](sim-2/graph_reset.htm) — Resets the graph, clearing all signals
- [`graph:setSignalPoint`](sim-2/graph_setSignalPoint.htm) — Sets the next signal value to record
- [`graph:snapshotTrace`](sim-2/graph_snapshotTrace.htm) — Duplicates and freezes a graph trace
- [`graph:step`](sim-2/graph_step.htm) — Records signal values for the current time
- [`app:createObject`](sim-2/app_createObject.htm) — Creates various objects (collections, scripts, sensors, etc.)
- [`scene:createObject`](sim-2/scene_createObject.htm) — Creates various objects (collections, scripts, sensors, etc.)
- [`graph.backgroundColor`](sim-2/property_graph_backgroundColor.htm) — Background color
- [`graph.bufferSize`](sim-2/property_graph_bufferSize.htm) — Buffer size
- [`graph.color.diffuse`](sim-2/property_graph_color_diffuse.htm) — Diffuse color
- [`graph.color.emission`](sim-2/property_graph_color_emission.htm) — Emission color
- [`graph.color.specular`](sim-2/property_graph_color_specular.htm) — Specular color
- [`graph.cyclic`](sim-2/property_graph_cyclic.htm) — Cyclic
- [`graph.foregroundColor`](sim-2/property_graph_foregroundColor.htm) — Foreground color
- [`graph.size`](sim-2/property_graph_size.htm) — Size

## <a id="methodsAndProperties_proximitySensor"></a>[proximitySensor](proximitySensors.md) (methods & properties)

- [`app:createObject`](sim-2/app_createObject.htm) — Creates various objects (collections, scripts, sensors, etc.)
- [`proximitySensor:checkSensor`](sim-2/proximitySensor_checkSensor.htm) — Checks sensor detection silently
- [`proximitySensor:handleSensor`](sim-2/proximitySensor_handleSensor.htm) — Handles the sensor with visual feedback
- [`proximitySensor:resetSensor`](sim-2/proximitySensor_resetSensor.htm) — Clears the sensor's detection state
- [`scene:createObject`](sim-2/scene_createObject.htm) — Creates various objects (collections, scripts, sensors, etc.)
- [`proximitySensor.angleThreshold`](sim-2/property_proximitySensor_angleThreshold.htm) — Angle threshold
- [`proximitySensor.backFaceDetection`](sim-2/property_proximitySensor_backFaceDetection.htm) — Back face detection
- [`proximitySensor.closeThreshold`](sim-2/property_proximitySensor_closeThreshold.htm) — Close threshold
- [`proximitySensor.color.diffuse`](sim-2/property_proximitySensor_color_diffuse.htm) — Diffuse color
- [`proximitySensor.color.emission`](sim-2/property_proximitySensor_color_emission.htm) — Emission color
- [`proximitySensor.color.specular`](sim-2/property_proximitySensor_color_specular.htm) — Specular color
- [`proximitySensor.detectedDistance`](sim-2/property_proximitySensor_detectedDistance.htm) — Detected distance
- [`proximitySensor.detectedNormal`](sim-2/property_proximitySensor_detectedNormal.htm) — Detected normal
- [`proximitySensor.detectedObject`](sim-2/property_proximitySensor_detectedObject.htm) — Detected object
- [`proximitySensor.detectedPoint`](sim-2/property_proximitySensor_detectedPoint.htm) — Detected point
- [`proximitySensor.exactMode`](sim-2/property_proximitySensor_exactMode.htm) — Exact mode
- [`proximitySensor.explicitHandling`](sim-2/property_proximitySensor_explicitHandling.htm) — Explicit handling
- [`proximitySensor.frontFaceDetection`](sim-2/property_proximitySensor_frontFaceDetection.htm) — Front face detection
- [`proximitySensor.pointSize`](sim-2/property_proximitySensor_pointSize.htm) — Sensor point size
- [`proximitySensor.proximitySensor.type`](sim-2/property_proximitySensor_proximitySensor_type.htm) — Type
- [`proximitySensor.randomizedDetection`](sim-2/property_proximitySensor_randomizedDetection.htm) — Randomized detection
- [`proximitySensor.rayColor.diffuse`](sim-2/property_proximitySensor_rayColor_diffuse.htm) — Diffuse color
- [`proximitySensor.rayColor.emission`](sim-2/property_proximitySensor_rayColor_emission.htm) — Emission color
- [`proximitySensor.rayColor.specular`](sim-2/property_proximitySensor_rayColor_specular.htm) — Specular color
- [`proximitySensor.showVolume`](sim-2/property_proximitySensor_showVolume.htm) — Show volume
- [`proximitySensor.volume.angle`](sim-2/property_proximitySensor_volume_angle.htm) — Angles
- [`proximitySensor.volume.closeEdges`](sim-2/property_proximitySensor_volume_closeEdges.htm) — Volume close edges
- [`proximitySensor.volume.edges`](sim-2/property_proximitySensor_volume_edges.htm) — Volume edges
- [`proximitySensor.volume.faces`](sim-2/property_proximitySensor_volume_faces.htm) — Faces
- [`proximitySensor.volume.offset`](sim-2/property_proximitySensor_volume_offset.htm) — Offset
- [`proximitySensor.volume.radius`](sim-2/property_proximitySensor_volume_radius.htm) — Radius
- [`proximitySensor.volume.range`](sim-2/property_proximitySensor_volume_range.htm) — Range
- [`proximitySensor.volume.subdivisions`](sim-2/property_proximitySensor_volume_subdivisions.htm) — Subdivisions
- [`proximitySensor.volume.xSize`](sim-2/property_proximitySensor_volume_xSize.htm) — X-sizes
- [`proximitySensor.volume.ySize`](sim-2/property_proximitySensor_volume_ySize.htm) — Y-sizes
- [`sceneObject.detectable`](sim-2/property_sceneObject_detectable.htm) — Detectable
- [`sceneObject.model.notDetectable`](sim-2/property_sceneObject_model_notDetectable.htm) — Model not detectable

## <a id="methodsAndProperties_visionSensor"></a>[visionSensor](visionSensors.md) (methods & properties)

- [`app:createObject`](sim-2/app_createObject.htm) — Creates various objects (collections, scripts, sensors, etc.)
- [`scene:createObject`](sim-2/scene_createObject.htm) — Creates various objects (collections, scripts, sensors, etc.)
- [`visionSensor:checkSensor`](sim-2/visionSensor_checkSensor.htm) — Checks vision sensor detection silently
- [`visionSensor:getDepth`](sim-2/visionSensor_getDepth.htm) — Reads the vision sensor's depth buffer
- [`visionSensor:getImage`](sim-2/visionSensor_getImage.htm) — Reads the vision sensor's image
- [`visionSensor:handleSensor`](sim-2/visionSensor_handleSensor.htm) — Handles the vision sensor (sensing, image processing)
- [`visionSensor:resetSensor`](sim-2/visionSensor_resetSensor.htm) — Clears the vision sensor's detection state
- [`visionSensor:setImage`](sim-2/visionSensor_setImage.htm) — Writes an image to the vision sensor
- [`visionSensor.backgroundColor`](sim-2/property_visionSensor_backgroundColor.htm) — Background color
- [`visionSensor.backgroundColorFromEnvironment`](sim-2/property_visionSensor_backgroundColorFromEnvironment.htm) — Background color from environment
- [`visionSensor.clippingPlanes`](sim-2/property_visionSensor_clippingPlanes.htm) — Clipping planes
- [`visionSensor.color.diffuse`](sim-2/property_visionSensor_color_diffuse.htm) — Diffuse color
- [`visionSensor.color.emission`](sim-2/property_visionSensor_color_emission.htm) — Emission color
- [`visionSensor.color.specular`](sim-2/property_visionSensor_color_specular.htm) — Specular color
- [`visionSensor.depth`](sim-2/property_visionSensor_depth.htm) — Depth buffer
- [`visionSensor.emitDepthChangedEvent`](sim-2/property_visionSensor_emitDepthChangedEvent.htm) — Emit depth change event
- [`visionSensor.emitImageChangedEvent`](sim-2/property_visionSensor_emitImageChangedEvent.htm) — Emit image change event
- [`visionSensor.explicitHandling`](sim-2/property_visionSensor_explicitHandling.htm) — Explicit handling
- [`visionSensor.frustumCornerFar`](sim-2/property_visionSensor_frustumCornerFar.htm) — Far corner of view frustum
- [`visionSensor.frustumCornerNear`](sim-2/property_visionSensor_frustumCornerNear.htm) — Near corner of view frustum
- [`visionSensor.ignoreDepthInfo`](sim-2/property_visionSensor_ignoreDepthInfo.htm) — Ignore depth buffer
- [`visionSensor.ignoreImageInfo`](sim-2/property_visionSensor_ignoreImageInfo.htm) — Ignore RGB buffer
- [`visionSensor.image`](sim-2/property_visionSensor_image.htm) — RGB buffer
- [`visionSensor.omitPacket1`](sim-2/property_visionSensor_omitPacket1.htm) — Packet 1 is blank
- [`visionSensor.packedDepth`](sim-2/property_visionSensor_packedDepth.htm) — Packed depth buffer
- [`visionSensor.packet1`](sim-2/property_visionSensor_packet1.htm) — Data packet 1
- [`visionSensor.packet2`](sim-2/property_visionSensor_packet2.htm) — Data packet 2
- [`visionSensor.perspective`](sim-2/property_visionSensor_perspective.htm) — Perspective
- [`visionSensor.povray.aperture`](sim-2/property_visionSensor_povray_aperture.htm) — POV-Ray: aperture
- [`visionSensor.povray.blurDistance`](sim-2/property_visionSensor_povray_blurDistance.htm) — POV-Ray: blur distance
- [`visionSensor.povray.blurSamples`](sim-2/property_visionSensor_povray_blurSamples.htm) — POV-Ray: blur samples
- [`visionSensor.povray.focalBlur`](sim-2/property_visionSensor_povray_focalBlur.htm) — POV-Ray: focal blur
- [`visionSensor.renderMode`](sim-2/property_visionSensor_renderMode.htm) — Render mode
- [`visionSensor.resolution`](sim-2/property_visionSensor_resolution.htm) — Resolution
- [`visionSensor.showFrustum`](sim-2/property_visionSensor_showFrustum.htm) — Show view frustum
- [`visionSensor.size`](sim-2/property_visionSensor_size.htm) — Size
- [`visionSensor.triggerState`](sim-2/property_visionSensor_triggerState.htm) — Trigger state
- [`visionSensor.useExtImage`](sim-2/property_visionSensor_useExtImage.htm) — External input
- [`visionSensor.viewAngle`](sim-2/property_visionSensor_viewAngle.htm) — View angle
- [`visionSensor.viewSize`](sim-2/property_visionSensor_viewSize.htm) — View size

## <a id="methodsAndProperties_forceSensor"></a>[forceSensor](forceSensors.md) (methods & properties)

- [`app:createObject`](sim-2/app_createObject.htm) — Creates various objects (collections, scripts, sensors, etc.)
- [`scene:createObject`](sim-2/scene_createObject.htm) — Creates various objects (collections, scripts, sensors, etc.)
- [`forceSensor.color.diffuse`](sim-2/property_forceSensor_color_diffuse.htm) — Diffuse color
- [`forceSensor.color.emission`](sim-2/property_forceSensor_color_emission.htm) — Emission color
- [`forceSensor.color.specular`](sim-2/property_forceSensor_color_specular.htm) — Specular color
- [`forceSensor.dynamics.consecutiveViolationsToTrigger`](sim-2/property_forceSensor_dynamics_consecutiveViolationsToTrigger.htm) — Consecutive violations to trigger
- [`forceSensor.dynamics.filter`](sim-2/property_forceSensor_dynamics_filter.htm) — Filter
- [`forceSensor.dynamics.filterSampleSize`](sim-2/property_forceSensor_dynamics_filterSampleSize.htm) — Filter sample size
- [`forceSensor.dynamics.filteredForce`](sim-2/property_forceSensor_dynamics_filteredForce.htm) — Filtered force
- [`forceSensor.dynamics.filteredTorque`](sim-2/property_forceSensor_dynamics_filteredTorque.htm) — Filtered torque
- [`forceSensor.dynamics.force`](sim-2/property_forceSensor_dynamics_force.htm) — Force
- [`forceSensor.dynamics.forceThreshold`](sim-2/property_forceSensor_dynamics_forceThreshold.htm) — Force threshold
- [`forceSensor.dynamics.forceThresholdEnabled`](sim-2/property_forceSensor_dynamics_forceThresholdEnabled.htm) — Force threshold enabled
- [`forceSensor.dynamics.torque`](sim-2/property_forceSensor_dynamics_torque.htm) — Torque
- [`forceSensor.dynamics.torqueThreshold`](sim-2/property_forceSensor_dynamics_torqueThreshold.htm) — Torque threshold
- [`forceSensor.dynamics.torqueThresholdEnabled`](sim-2/property_forceSensor_dynamics_torqueThresholdEnabled.htm) — Torque threshold enabled
- [`forceSensor.intrinsicError`](sim-2/property_forceSensor_intrinsicError.htm) — Intrinsic error
- [`forceSensor.size`](sim-2/property_forceSensor_size.htm) — Size

## <a id="methodsAndProperties_pointCloud"></a>[pointCloud](pointClouds.md) (methods & properties)

- [`app:createObject`](sim-2/app_createObject.htm) — Creates various objects (collections, scripts, sensors, etc.)
- [`ocTree:addFromObjects`](sim-2/ocTree_addFromObjects.htm) — Adds voxels from scene objects
- [`ocTree:subtractFromObjects`](sim-2/ocTree_subtractFromObjects.htm) — Subtracts voxels using scene objects
- [`pointCloud:addFromObjects`](sim-2/pointCloud_addFromObjects.htm) — Adds points from scene objects
- [`pointCloud:addPackedPoints`](sim-2/pointCloud_addPackedPoints.htm) — Inserts points from a packed buffer
- [`pointCloud:addPoints`](sim-2/pointCloud_addPoints.htm) — Inserts points
- [`pointCloud:clear`](sim-2/pointCloud_clear.htm) — Removes all points
- [`pointCloud:intersectPackedPoints`](sim-2/pointCloud_intersectPackedPoints.htm) — Keeps only points intersecting with provided packed points
- [`pointCloud:intersectPoints`](sim-2/pointCloud_intersectPoints.htm) — Keeps only points intersecting with provided points
- [`pointCloud:subtractFromObjects`](sim-2/pointCloud_subtractFromObjects.htm) — Subtracts points using scene objects
- [`pointCloud:subtractPackedPoints`](sim-2/pointCloud_subtractPackedPoints.htm) — Removes points from a packed buffer
- [`pointCloud:subtractPoints`](sim-2/pointCloud_subtractPoints.htm) — Removes points
- [`scene:createObject`](sim-2/scene_createObject.htm) — Creates various objects (collections, scripts, sensors, etc.)
- [`pointCloud.cellSize`](sim-2/property_pointCloud_cellSize.htm) — Cell size
- [`pointCloud.color.diffuse`](sim-2/property_pointCloud_color_diffuse.htm) — Diffuse color
- [`pointCloud.color.emission`](sim-2/property_pointCloud_color_emission.htm) — Emission color
- [`pointCloud.color.specular`](sim-2/property_pointCloud_color_specular.htm) — Specular color
- [`pointCloud.colors`](sim-2/property_pointCloud_colors.htm) — Colors
- [`pointCloud.maxPointsInCell`](sim-2/property_pointCloud_maxPointsInCell.htm) — Max. points in cell
- [`pointCloud.octreeStruct`](sim-2/property_pointCloud_octreeStruct.htm) — OC-Tree structure Enabled
- [`pointCloud.packedPoints`](sim-2/property_pointCloud_packedPoints.htm) — Packed points
- [`pointCloud.pointDisplayFraction`](sim-2/property_pointCloud_pointDisplayFraction.htm) — Display fraction
- [`pointCloud.pointSize`](sim-2/property_pointCloud_pointSize.htm) — Point size
- [`pointCloud.points`](sim-2/property_pointCloud_points.htm) — Points
- [`pointCloud.randomColors`](sim-2/property_pointCloud_randomColors.htm) — Random point colors

## <a id="methodsAndProperties_ocTree"></a><a id="methodsAndProperties_octree"></a>[ocTree](octrees.md) (methods & properties)

- [`app:createObject`](sim-2/app_createObject.htm) — Creates various objects (collections, scripts, sensors, etc.)
- [`ocTree:addFromObjects`](sim-2/ocTree_addFromObjects.htm) — Adds voxels from scene objects
- [`ocTree:addPackedVoxels`](sim-2/ocTree_addPackedVoxels.htm) — Inserts voxels from a packed buffer
- [`ocTree:addVoxels`](sim-2/ocTree_addVoxels.htm) — Inserts voxels
- [`ocTree:checkPackedPoints`](sim-2/ocTree_checkPackedPoints.htm) — Checks if packed points collide with voxels
- [`ocTree:checkPoints`](sim-2/ocTree_checkPoints.htm) — Checks if points collide with the voxels
- [`ocTree:clear`](sim-2/ocTree_clear.htm) — Removes all voxels
- [`ocTree:subtractFromObjects`](sim-2/ocTree_subtractFromObjects.htm) — Subtracts voxels using scene objects
- [`ocTree:subtractPackedVoxels`](sim-2/ocTree_subtractPackedVoxels.htm) — Removes voxels from a packed buffer
- [`ocTree:subtractVoxels`](sim-2/ocTree_subtractVoxels.htm) — Removes voxels
- [`pointCloud:addFromObjects`](sim-2/pointCloud_addFromObjects.htm) — Adds points from scene objects
- [`pointCloud:subtractFromObjects`](sim-2/pointCloud_subtractFromObjects.htm) — Subtracts points using scene objects
- [`scene:createObject`](sim-2/scene_createObject.htm) — Creates various objects (collections, scripts, sensors, etc.)
- [`ocTree.color.diffuse`](sim-2/property_ocTree_color_diffuse.htm) — Diffuse color
- [`ocTree.color.emission`](sim-2/property_ocTree_color_emission.htm) — Emission color
- [`ocTree.color.specular`](sim-2/property_ocTree_color_specular.htm) — Specular color
- [`ocTree.colors`](sim-2/property_ocTree_colors.htm) — Voxel colors
- [`ocTree.packedPoints`](sim-2/property_ocTree_packedPoints.htm) — Packed voxels
- [`ocTree.points`](sim-2/property_ocTree_points.htm) — Voxels
- [`ocTree.randomColors`](sim-2/property_ocTree_randomColors.htm) — Random voxel colors
- [`ocTree.showPoints`](sim-2/property_ocTree_showPoints.htm) — Show points instead of voxels
- [`ocTree.voxelSize`](sim-2/property_ocTree_voxelSize.htm) — Voxel size

## <a id="methodsAndProperties_customSceneObject"></a>[customSceneObject](customSceneObjects.htm) (methods & properties)

- [`app:createObject`](sim-2/app_createObject.htm) — Creates various objects (collections, scripts, sensors, etc.)
- [`scene:createObject`](sim-2/scene_createObject.htm) — Creates various objects (collections, scripts, sensors, etc.)

## <a id="methodsAndProperties_Path"></a><a id="methodsAndProperties_paths"></a>[Path](paths.md) (methods & properties)

- [`Path:appendFromJoints`](sim-2/Path_appendFromJoints.htm) — Appends a point from the joints' current configuration
- [`Path:appendFromObject`](sim-2/Path_appendFromObject.htm) — Appends a point from the object's current pose
- [`Path:appendPoints`](sim-2/Path_appendPoints.htm) — Appends path control points
- [`Path:clearPoints`](sim-2/Path_clearPoints.htm) — Clears all path control points
- [`Path:closest`](sim-2/Path_closest.htm) — Returns the closest point on the path
- [`Path:configs`](sim-2/Path_configs.htm) — Returns equivalent configurations for a given one
- [`Path:createMarkers`](sim-2/Path_createMarkers.htm) — Creates markers for path visualization
- [`Path:createShape`](sim-2/Path_createShape.htm) — Creates an extrusion shape from the path
- [`Path:data`](sim-2/Path_data.htm) — Returns path information
- [`Path:distance`](sim-2/Path_distance.htm) — Returns distance between two points
- [`Path:fromBuffer`](sim-2/Path_fromBuffer.htm) — Creates a path from serialized data
- [`Path:fromJoints`](sim-2/Path_fromJoints.htm) — Creates an empty path from joints
- [`Path:fromObject`](sim-2/Path_fromObject.htm) — Creates an empty path from an object's pose
- [`Path:getPoint`](sim-2/Path_getPoint.htm) — Returns a point on the path at a specific distance
- [`Path:interpolate`](sim-2/Path_interpolate.htm) — Returns linear interpolation between two points
- [`Path:new`](sim-2/Path_new.htm) — Creates a path
- [`Path:removeMarkers`](sim-2/Path_removeMarkers.htm) — Removes path visualization markers
- [`Path:setPoints`](sim-2/Path_setPoints.htm) — Sets the path control points
- [`Path:toBuffer`](sim-2/Path_toBuffer.htm) — Returns serialized path data
- [`app:createObject`](sim-2/app_createObject.htm) — Creates various objects (collections, scripts, sensors, etc.)
- [`scene:createObject`](sim-2/scene_createObject.htm) — Creates various objects (collections, scripts, sensors, etc.)

## <a id="methodsAndProperties_file"></a><a id="methodsAndProperties_fileOperations"></a>File operations (methods & properties)

- [`app:loadModelInfo`](sim-2/app_loadModelInfo.htm) — Loads a model thumbnail
- [`app:loadModelInfoFromBuffer`](sim-2/app_loadModelInfoFromBuffer.htm) — Loads a model thumbnail from buffer
- [`app:loadScene`](sim-2/app_loadScene.htm) — Loads a scene from file
- [`app:loadSceneFromBuffer`](sim-2/app_loadSceneFromBuffer.htm) — Loads a scene from buffer
- [`scene:loadModel`](sim-2/scene_loadModel.htm) — Loads a previously saved model
- [`scene:loadModelFromBuffer`](sim-2/scene_loadModelFromBuffer.htm) — Loads a model from buffer
- [`scene:remove`](sim-2/scene_remove.htm) — Closes the scene
- [`scene:save`](sim-2/scene_save.htm) — Saves the scene to file
- [`scene:saveToBuffer`](sim-2/scene_saveToBuffer.htm) — Serializes the scene to a buffer
- [`sceneObject:saveModel`](sim-2/sceneObject_saveModel.htm) — Saves this model to a file
- [`sceneObject:saveModelToBuffer`](sim-2/sceneObject_saveModelToBuffer.htm) — Serializes this model to a buffer
- [`scene.finalSaveRequest`](sim-2/property_scene_finalSaveRequest.htm) — Final save
- [`scene.locked`](sim-2/property_scene_locked.htm) — Scene is locked
- [`scene.saveCalculationStructs`](sim-2/property_scene_saveCalculationStructs.htm) — Save calculation structures

## <a id="methodsAndProperties_main"></a><a id="methodsAndProperties_mainFunctionalityHandling"></a>General functionality handling (methods & properties)

- [`scene:getObject`](sim-2/scene_getObject.htm) — Retrieves an object by its path and name
- [`scene:getObjectFromUid`](sim-2/scene_getObjectFromUid.htm) — Retrieves an object by its unique identifier
- [`sceneObject:getObject`](sim-2/sceneObject_getObject.htm) — Retrieves an object by its path and name
- [`script:getObject`](sim-2/script_getObject.htm) — Retrieves an object by its path and name

## <a id="methodsAndProperties_dynamics"></a><a id="methodsAndProperties_dynamicsFunctionality"></a>[Dynamics](dynamicsModule.md) (methods & properties)

- [`joint:setTargetPosition`](sim-2/joint_setTargetPosition.htm) — Sets the joint's desired linear/angular position
- [`joint:setTargetVelocity`](sim-2/joint_setTargetVelocity.htm) — Sets the joint's desired linear/angular velocity
- [`scene.dynamics:getContacts`](sim-2/scene_dynamics_getContacts.htm) — Retrieves contact information from the dynamics world
- [`scene.dynamics:step`](sim-2/scene_dynamics_step.htm) — Steps the dynamics engine
- [`sceneObject:dynamicReset`](sim-2/sceneObject_dynamicReset.htm) — Dynamically resets the object in the physics engine
- [`shape.dynamics:addForce`](sim-2/shape_dynamics_addForce.htm) — Applies a force to the dynamically enabled shape
- [`shape.dynamics:addTorque`](sim-2/shape_dynamics_addTorque.htm) — Applies a torque to the dynamically enabled shape
- [`shape.dynamics:computeInertia`](sim-2/shape_dynamics_computeInertia.htm) — Computes and applies mass/inertia properties
- [`shape.dynamics:getContacts`](sim-2/shape_dynamics_getContacts.htm) — Retrieves the shape's contact information
- [`shape.dynamics:getInertia`](sim-2/shape_dynamics_getInertia.htm) — Retrieves the shape's inertia information
- [`shape.dynamics:setInertia`](sim-2/shape_dynamics_setInertia.htm) — Applies a new inertia matrix
- [`app.paths.mujoco`](sim-2/property_app_paths_mujoco.htm) — MuJoCo path
- [`dummy.dynamics.engineProperties`](sim-2/property_dummy_dynamics_engineProperties.htm) — Engine properties
- [`dummy.dynamics.mujoco.jointProxyHandle`](sim-2/property_dummy_dynamics_mujoco_jointProxyHandle.htm) — Joint proxy
- [`dummy.dynamics.mujoco.limitsEnabled`](sim-2/property_dummy_dynamics_mujoco_limitsEnabled.htm)
- [`dummy.dynamics.mujoco.limitsRange`](sim-2/property_dummy_dynamics_mujoco_limitsRange.htm)
- [`dummy.dynamics.mujoco.limitsSolimp`](sim-2/property_dummy_dynamics_mujoco_limitsSolimp.htm)
- [`dummy.dynamics.mujoco.limitsSolref`](sim-2/property_dummy_dynamics_mujoco_limitsSolref.htm)
- [`dummy.dynamics.mujoco.margin`](sim-2/property_dummy_dynamics_mujoco_margin.htm)
- [`dummy.dynamics.mujoco.overlapConstrSolimp`](sim-2/property_dummy_dynamics_mujoco_overlapConstrSolimp.htm)
- [`dummy.dynamics.mujoco.overlapConstrSolref`](sim-2/property_dummy_dynamics_mujoco_overlapConstrSolref.htm)
- [`dummy.dynamics.mujoco.overlapConstrTorquescale`](sim-2/property_dummy_dynamics_mujoco_overlapConstrTorquescale.htm)
- [`dummy.dynamics.mujoco.springDamping`](sim-2/property_dummy_dynamics_mujoco_springDamping.htm)
- [`dummy.dynamics.mujoco.springLength`](sim-2/property_dummy_dynamics_mujoco_springLength.htm)
- [`dummy.dynamics.mujoco.springStiffness`](sim-2/property_dummy_dynamics_mujoco_springStiffness.htm)
- [`forceSensor.dynamics.filter`](sim-2/property_forceSensor_dynamics_filter.htm) — Filter
- [`forceSensor.dynamics.filterSampleSize`](sim-2/property_forceSensor_dynamics_filterSampleSize.htm) — Filter sample size
- [`forceSensor.dynamics.filteredForce`](sim-2/property_forceSensor_dynamics_filteredForce.htm) — Filtered force
- [`forceSensor.dynamics.filteredTorque`](sim-2/property_forceSensor_dynamics_filteredTorque.htm) — Filtered torque
- [`forceSensor.dynamics.force`](sim-2/property_forceSensor_dynamics_force.htm) — Force
- [`forceSensor.dynamics.forceThreshold`](sim-2/property_forceSensor_dynamics_forceThreshold.htm) — Force threshold
- [`forceSensor.dynamics.forceThresholdEnabled`](sim-2/property_forceSensor_dynamics_forceThresholdEnabled.htm) — Force threshold enabled
- [`forceSensor.dynamics.torque`](sim-2/property_forceSensor_dynamics_torque.htm) — Torque
- [`forceSensor.dynamics.torqueThreshold`](sim-2/property_forceSensor_dynamics_torqueThreshold.htm) — Torque threshold
- [`forceSensor.dynamics.torqueThresholdEnabled`](sim-2/property_forceSensor_dynamics_torqueThresholdEnabled.htm) — Torque threshold enabled
- [`forceSensor.intrinsicError`](sim-2/property_forceSensor_intrinsicError.htm) — Intrinsic error
- [`joint.dynamics.averageForce`](sim-2/property_joint_dynamics_averageForce.htm) — Average force
- [`joint.dynamics.bullet.normalCfm`](sim-2/property_joint_dynamics_bullet_normalCfm.htm)
- [`joint.dynamics.bullet.posPid`](sim-2/property_joint_dynamics_bullet_posPid.htm)
- [`joint.dynamics.bullet.stopCfm`](sim-2/property_joint_dynamics_bullet_stopCfm.htm)
- [`joint.dynamics.bullet.stopErp`](sim-2/property_joint_dynamics_bullet_stopErp.htm)
- [`joint.dynamics.ctrlMode`](sim-2/property_joint_dynamics_ctrlMode.htm) — Control mode
- [`joint.dynamics.engineProperties`](sim-2/property_joint_dynamics_engineProperties.htm) — Engine properties
- [`joint.dynamics.force`](sim-2/property_joint_dynamics_force.htm) — Force
- [`joint.dynamics.mujoco.armature`](sim-2/property_joint_dynamics_mujoco_armature.htm)
- [`joint.dynamics.mujoco.dependencyPolyCoeff`](sim-2/property_joint_dynamics_mujoco_dependencyPolyCoeff.htm)
- [`joint.dynamics.mujoco.frictionLoss`](sim-2/property_joint_dynamics_mujoco_frictionLoss.htm)
- [`joint.dynamics.mujoco.frictionSolimp`](sim-2/property_joint_dynamics_mujoco_frictionSolimp.htm)
- [`joint.dynamics.mujoco.frictionSolref`](sim-2/property_joint_dynamics_mujoco_frictionSolref.htm)
- [`joint.dynamics.mujoco.limitsSolimp`](sim-2/property_joint_dynamics_mujoco_limitsSolimp.htm)
- [`joint.dynamics.mujoco.limitsSolref`](sim-2/property_joint_dynamics_mujoco_limitsSolref.htm)
- [`joint.dynamics.mujoco.margin`](sim-2/property_joint_dynamics_mujoco_margin.htm)
- [`joint.dynamics.mujoco.posPid`](sim-2/property_joint_dynamics_mujoco_posPid.htm)
- [`joint.dynamics.mujoco.springDamping`](sim-2/property_joint_dynamics_mujoco_springDamping.htm)
- [`joint.dynamics.mujoco.springRef`](sim-2/property_joint_dynamics_mujoco_springRef.htm)
- [`joint.dynamics.mujoco.springSpringDamper`](sim-2/property_joint_dynamics_mujoco_springSpringDamper.htm)
- [`joint.dynamics.mujoco.springStiffness`](sim-2/property_joint_dynamics_mujoco_springStiffness.htm)
- [`joint.dynamics.newton.posPid`](sim-2/property_joint_dynamics_newton_posPid.htm)
- [`joint.dynamics.ode.bounce`](sim-2/property_joint_dynamics_ode_bounce.htm)
- [`joint.dynamics.ode.fudge`](sim-2/property_joint_dynamics_ode_fudge.htm)
- [`joint.dynamics.ode.normalCfm`](sim-2/property_joint_dynamics_ode_normalCfm.htm)
- [`joint.dynamics.ode.posPid`](sim-2/property_joint_dynamics_ode_posPid.htm)
- [`joint.dynamics.ode.stopCfm`](sim-2/property_joint_dynamics_ode_stopCfm.htm)
- [`joint.dynamics.ode.stopErp`](sim-2/property_joint_dynamics_ode_stopErp.htm)
- [`joint.dynamics.smoothMotionProfile`](sim-2/property_joint_dynamics_smoothMotionProfile.htm) — Smooth dynamics motion profile
- [`joint.dynamics.springDamper`](sim-2/property_joint_dynamics_springDamper.htm) — Spring damper parameters
- [`joint.dynamics.targetForce`](sim-2/property_joint_dynamics_targetForce.htm) — Target force
- [`joint.dynamics.vortex.axisFrictionEnabled`](sim-2/property_joint_dynamics_vortex_axisFrictionEnabled.htm)
- [`joint.dynamics.vortex.axisFrictionLoss`](sim-2/property_joint_dynamics_vortex_axisFrictionLoss.htm)
- [`joint.dynamics.vortex.axisFrictionMaxForce`](sim-2/property_joint_dynamics_vortex_axisFrictionMaxForce.htm)
- [`joint.dynamics.vortex.axisFrictionProportional`](sim-2/property_joint_dynamics_vortex_axisFrictionProportional.htm)
- [`joint.dynamics.vortex.axisFrictionValue`](sim-2/property_joint_dynamics_vortex_axisFrictionValue.htm)
- [`joint.dynamics.vortex.axisLimitsLowerDamping`](sim-2/property_joint_dynamics_vortex_axisLimitsLowerDamping.htm)
- [`joint.dynamics.vortex.axisLimitsLowerMaxForce`](sim-2/property_joint_dynamics_vortex_axisLimitsLowerMaxForce.htm)
- [`joint.dynamics.vortex.axisLimitsLowerRestitution`](sim-2/property_joint_dynamics_vortex_axisLimitsLowerRestitution.htm)
- [`joint.dynamics.vortex.axisLimitsLowerStiffness`](sim-2/property_joint_dynamics_vortex_axisLimitsLowerStiffness.htm)
- [`joint.dynamics.vortex.axisLimitsUpperDamping`](sim-2/property_joint_dynamics_vortex_axisLimitsUpperDamping.htm)
- [`joint.dynamics.vortex.axisLimitsUpperMaxForce`](sim-2/property_joint_dynamics_vortex_axisLimitsUpperMaxForce.htm)
- [`joint.dynamics.vortex.axisLimitsUpperRestitution`](sim-2/property_joint_dynamics_vortex_axisLimitsUpperRestitution.htm)
- [`joint.dynamics.vortex.axisLimitsUpperStiffness`](sim-2/property_joint_dynamics_vortex_axisLimitsUpperStiffness.htm)
- [`joint.dynamics.vortex.frictionEnabledBits`](sim-2/property_joint_dynamics_vortex_frictionEnabledBits.htm)
- [`joint.dynamics.vortex.frictionProportionalBits`](sim-2/property_joint_dynamics_vortex_frictionProportionalBits.htm)
- [`joint.dynamics.vortex.posPid`](sim-2/property_joint_dynamics_vortex_posPid.htm)
- [`joint.dynamics.vortex.relaxationEnabledBits`](sim-2/property_joint_dynamics_vortex_relaxationEnabledBits.htm)
- [`joint.dynamics.vortex.xAxisOrientFrictionCoeff`](sim-2/property_joint_dynamics_vortex_xAxisOrientFrictionCoeff.htm)
- [`joint.dynamics.vortex.xAxisOrientFrictionLoss`](sim-2/property_joint_dynamics_vortex_xAxisOrientFrictionLoss.htm)
- [`joint.dynamics.vortex.xAxisOrientFrictionMaxTorque`](sim-2/property_joint_dynamics_vortex_xAxisOrientFrictionMaxTorque.htm)
- [`joint.dynamics.vortex.xAxisOrientRelaxationDamping`](sim-2/property_joint_dynamics_vortex_xAxisOrientRelaxationDamping.htm)
- [`joint.dynamics.vortex.xAxisOrientRelaxationLoss`](sim-2/property_joint_dynamics_vortex_xAxisOrientRelaxationLoss.htm)
- [`joint.dynamics.vortex.xAxisOrientRelaxationStiffness`](sim-2/property_joint_dynamics_vortex_xAxisOrientRelaxationStiffness.htm)
- [`joint.dynamics.vortex.xAxisPosFrictionCoeff`](sim-2/property_joint_dynamics_vortex_xAxisPosFrictionCoeff.htm)
- [`joint.dynamics.vortex.xAxisPosFrictionLoss`](sim-2/property_joint_dynamics_vortex_xAxisPosFrictionLoss.htm)
- [`joint.dynamics.vortex.xAxisPosFrictionMaxForce`](sim-2/property_joint_dynamics_vortex_xAxisPosFrictionMaxForce.htm)
- [`joint.dynamics.vortex.xAxisPosRelaxationDamping`](sim-2/property_joint_dynamics_vortex_xAxisPosRelaxationDamping.htm)
- [`joint.dynamics.vortex.xAxisPosRelaxationLoss`](sim-2/property_joint_dynamics_vortex_xAxisPosRelaxationLoss.htm)
- [`joint.dynamics.vortex.xAxisPosRelaxationStiffness`](sim-2/property_joint_dynamics_vortex_xAxisPosRelaxationStiffness.htm)
- [`joint.dynamics.vortex.yAxisOrientFrictionCoeff`](sim-2/property_joint_dynamics_vortex_yAxisOrientFrictionCoeff.htm)
- [`joint.dynamics.vortex.yAxisOrientFrictionLoss`](sim-2/property_joint_dynamics_vortex_yAxisOrientFrictionLoss.htm)
- [`joint.dynamics.vortex.yAxisOrientFrictionMaxTorque`](sim-2/property_joint_dynamics_vortex_yAxisOrientFrictionMaxTorque.htm)
- [`joint.dynamics.vortex.yAxisOrientRelaxationDamping`](sim-2/property_joint_dynamics_vortex_yAxisOrientRelaxationDamping.htm)
- [`joint.dynamics.vortex.yAxisOrientRelaxationLoss`](sim-2/property_joint_dynamics_vortex_yAxisOrientRelaxationLoss.htm)
- [`joint.dynamics.vortex.yAxisOrientRelaxationStiffness`](sim-2/property_joint_dynamics_vortex_yAxisOrientRelaxationStiffness.htm)
- [`joint.dynamics.vortex.yAxisPosFrictionCoeff`](sim-2/property_joint_dynamics_vortex_yAxisPosFrictionCoeff.htm)
- [`joint.dynamics.vortex.yAxisPosFrictionLoss`](sim-2/property_joint_dynamics_vortex_yAxisPosFrictionLoss.htm)
- [`joint.dynamics.vortex.yAxisPosFrictionMaxForce`](sim-2/property_joint_dynamics_vortex_yAxisPosFrictionMaxForce.htm)
- [`joint.dynamics.vortex.yAxisPosRelaxationDamping`](sim-2/property_joint_dynamics_vortex_yAxisPosRelaxationDamping.htm)
- [`joint.dynamics.vortex.yAxisPosRelaxationLoss`](sim-2/property_joint_dynamics_vortex_yAxisPosRelaxationLoss.htm)
- [`joint.dynamics.vortex.yAxisPosRelaxationStiffness`](sim-2/property_joint_dynamics_vortex_yAxisPosRelaxationStiffness.htm)
- [`joint.dynamics.vortex.zAxisOrientFrictionCoeff`](sim-2/property_joint_dynamics_vortex_zAxisOrientFrictionCoeff.htm)
- [`joint.dynamics.vortex.zAxisOrientFrictionLoss`](sim-2/property_joint_dynamics_vortex_zAxisOrientFrictionLoss.htm)
- [`joint.dynamics.vortex.zAxisOrientFrictionMaxTorque`](sim-2/property_joint_dynamics_vortex_zAxisOrientFrictionMaxTorque.htm)
- [`joint.dynamics.vortex.zAxisOrientRelaxationDamping`](sim-2/property_joint_dynamics_vortex_zAxisOrientRelaxationDamping.htm)
- [`joint.dynamics.vortex.zAxisOrientRelaxationLoss`](sim-2/property_joint_dynamics_vortex_zAxisOrientRelaxationLoss.htm)
- [`joint.dynamics.vortex.zAxisOrientRelaxationStiffness`](sim-2/property_joint_dynamics_vortex_zAxisOrientRelaxationStiffness.htm)
- [`joint.dynamics.vortex.zAxisPosFrictionCoeff`](sim-2/property_joint_dynamics_vortex_zAxisPosFrictionCoeff.htm)
- [`joint.dynamics.vortex.zAxisPosFrictionLoss`](sim-2/property_joint_dynamics_vortex_zAxisPosFrictionLoss.htm)
- [`joint.dynamics.vortex.zAxisPosFrictionMaxForce`](sim-2/property_joint_dynamics_vortex_zAxisPosFrictionMaxForce.htm)
- [`joint.dynamics.vortex.zAxisPosRelaxationDamping`](sim-2/property_joint_dynamics_vortex_zAxisPosRelaxationDamping.htm)
- [`joint.dynamics.vortex.zAxisPosRelaxationLoss`](sim-2/property_joint_dynamics_vortex_zAxisPosRelaxationLoss.htm)
- [`joint.dynamics.vortex.zAxisPosRelaxationStiffness`](sim-2/property_joint_dynamics_vortex_zAxisPosRelaxationStiffness.htm)
- [`joint.enforceBounds`](sim-2/property_joint_enforceBounds.htm) — Enforce bounds
- [`joint.intrinsicError`](sim-2/property_joint_intrinsicError.htm) — Intrinsic error
- [`joint.targetPosition`](sim-2/property_joint_targetPosition.htm) — Target position
- [`joint.targetVelocity`](sim-2/property_joint_targetVelocity.htm) — Target velocity
- [`joint.velocity`](sim-2/property_joint_velocity.htm) — Velocity
- [`scene.dynamics.bullet.collisionMarginScaling`](sim-2/property_scene_dynamics_bullet_collisionMarginScaling.htm)
- [`scene.dynamics.bullet.computeInertias`](sim-2/property_scene_dynamics_bullet_computeInertias.htm)
- [`scene.dynamics.bullet.internalScalingFull`](sim-2/property_scene_dynamics_bullet_internalScalingFull.htm)
- [`scene.dynamics.bullet.internalScalingValue`](sim-2/property_scene_dynamics_bullet_internalScalingValue.htm)
- [`scene.dynamics.bullet.iterations`](sim-2/property_scene_dynamics_bullet_iterations.htm)
- [`scene.dynamics.bullet.solver`](sim-2/property_scene_dynamics_bullet_solver.htm)
- [`scene.dynamics.enabled`](sim-2/property_scene_dynamics_enabled.htm) — Dynamics enabled
- [`scene.dynamics.engine`](sim-2/property_scene_dynamics_engine.htm) — Dynamics engine
- [`scene.dynamics.engineProperties`](sim-2/property_scene_dynamics_engineProperties.htm) — Engine properties
- [`scene.dynamics.engineVersion`](sim-2/property_scene_dynamics_engineVersion.htm) — Dynamics engine version
- [`scene.dynamics.gravity`](sim-2/property_scene_dynamics_gravity.htm) — Gravity
- [`scene.dynamics.mujoco.actuationEnable`](sim-2/property_scene_dynamics_mujoco_actuationEnable.htm)
- [`scene.dynamics.mujoco.alignfree`](sim-2/property_scene_dynamics_mujoco_alignfree.htm)
- [`scene.dynamics.mujoco.autoresetEnable`](sim-2/property_scene_dynamics_mujoco_autoresetEnable.htm)
- [`scene.dynamics.mujoco.balanceInertias`](sim-2/property_scene_dynamics_mujoco_balanceInertias.htm)
- [`scene.dynamics.mujoco.boundInertia`](sim-2/property_scene_dynamics_mujoco_boundInertia.htm)
- [`scene.dynamics.mujoco.boundMass`](sim-2/property_scene_dynamics_mujoco_boundMass.htm)
- [`scene.dynamics.mujoco.ccd_iterations`](sim-2/property_scene_dynamics_mujoco_ccd_iterations.htm)
- [`scene.dynamics.mujoco.ccd_tolerance`](sim-2/property_scene_dynamics_mujoco_ccd_tolerance.htm)
- [`scene.dynamics.mujoco.computeInertias`](sim-2/property_scene_dynamics_mujoco_computeInertias.htm)
- [`scene.dynamics.mujoco.cone`](sim-2/property_scene_dynamics_mujoco_cone.htm)
- [`scene.dynamics.mujoco.contactEnable`](sim-2/property_scene_dynamics_mujoco_contactEnable.htm)
- [`scene.dynamics.mujoco.contactParamsMargin`](sim-2/property_scene_dynamics_mujoco_contactParamsMargin.htm)
- [`scene.dynamics.mujoco.contactParamsOverride`](sim-2/property_scene_dynamics_mujoco_contactParamsOverride.htm)
- [`scene.dynamics.mujoco.contactParamsSolimp`](sim-2/property_scene_dynamics_mujoco_contactParamsSolimp.htm)
- [`scene.dynamics.mujoco.contactParamsSolref`](sim-2/property_scene_dynamics_mujoco_contactParamsSolref.htm)
- [`scene.dynamics.mujoco.density`](sim-2/property_scene_dynamics_mujoco_density.htm)
- [`scene.dynamics.mujoco.energyEnable`](sim-2/property_scene_dynamics_mujoco_energyEnable.htm)
- [`scene.dynamics.mujoco.equalityEnable`](sim-2/property_scene_dynamics_mujoco_equalityEnable.htm)
- [`scene.dynamics.mujoco.eulerdampEnable`](sim-2/property_scene_dynamics_mujoco_eulerdampEnable.htm)
- [`scene.dynamics.mujoco.frictionlossEnable`](sim-2/property_scene_dynamics_mujoco_frictionlossEnable.htm)
- [`scene.dynamics.mujoco.gravityEnable`](sim-2/property_scene_dynamics_mujoco_gravityEnable.htm)
- [`scene.dynamics.mujoco.impratio`](sim-2/property_scene_dynamics_mujoco_impratio.htm)
- [`scene.dynamics.mujoco.integrator`](sim-2/property_scene_dynamics_mujoco_integrator.htm)
- [`scene.dynamics.mujoco.invdiscreteEnable`](sim-2/property_scene_dynamics_mujoco_invdiscreteEnable.htm)
- [`scene.dynamics.mujoco.iterations`](sim-2/property_scene_dynamics_mujoco_iterations.htm)
- [`scene.dynamics.mujoco.jacobian`](sim-2/property_scene_dynamics_mujoco_jacobian.htm)
- [`scene.dynamics.mujoco.kinematicBodiesInertia`](sim-2/property_scene_dynamics_mujoco_kinematicBodiesInertia.htm)
- [`scene.dynamics.mujoco.kinematicBodiesMass`](sim-2/property_scene_dynamics_mujoco_kinematicBodiesMass.htm)
- [`scene.dynamics.mujoco.kinematicBodiesOverrideFlags`](sim-2/property_scene_dynamics_mujoco_kinematicBodiesOverrideFlags.htm)
- [`scene.dynamics.mujoco.kinematicWeldSolimp`](sim-2/property_scene_dynamics_mujoco_kinematicWeldSolimp.htm)
- [`scene.dynamics.mujoco.kinematicWeldSolref`](sim-2/property_scene_dynamics_mujoco_kinematicWeldSolref.htm)
- [`scene.dynamics.mujoco.kinematicWeldTorquescale`](sim-2/property_scene_dynamics_mujoco_kinematicWeldTorquescale.htm)
- [`scene.dynamics.mujoco.limitEnable`](sim-2/property_scene_dynamics_mujoco_limitEnable.htm)
- [`scene.dynamics.mujoco.ls_iterations`](sim-2/property_scene_dynamics_mujoco_ls_iterations.htm)
- [`scene.dynamics.mujoco.ls_tolerance`](sim-2/property_scene_dynamics_mujoco_ls_tolerance.htm)
- [`scene.dynamics.mujoco.mbmemory`](sim-2/property_scene_dynamics_mujoco_mbmemory.htm)
- [`scene.dynamics.mujoco.midphaseEnable`](sim-2/property_scene_dynamics_mujoco_midphaseEnable.htm)
- [`scene.dynamics.mujoco.multiccd`](sim-2/property_scene_dynamics_mujoco_multiccd.htm)
- [`scene.dynamics.mujoco.multithreaded`](sim-2/property_scene_dynamics_mujoco_multithreaded.htm)
- [`scene.dynamics.mujoco.nativeccdEnable`](sim-2/property_scene_dynamics_mujoco_nativeccdEnable.htm)
- [`scene.dynamics.mujoco.nconmax`](sim-2/property_scene_dynamics_mujoco_nconmax.htm)
- [`scene.dynamics.mujoco.njmax`](sim-2/property_scene_dynamics_mujoco_njmax.htm)
- [`scene.dynamics.mujoco.noslip_iterations`](sim-2/property_scene_dynamics_mujoco_noslip_iterations.htm)
- [`scene.dynamics.mujoco.noslip_tolerance`](sim-2/property_scene_dynamics_mujoco_noslip_tolerance.htm)
- [`scene.dynamics.mujoco.nstack`](sim-2/property_scene_dynamics_mujoco_nstack.htm)
- [`scene.dynamics.mujoco.passiveEnable`](sim-2/property_scene_dynamics_mujoco_passiveEnable.htm)
- [`scene.dynamics.mujoco.rebuildTrigger`](sim-2/property_scene_dynamics_mujoco_rebuildTrigger.htm)
- [`scene.dynamics.mujoco.refsafeEnable`](sim-2/property_scene_dynamics_mujoco_refsafeEnable.htm)
- [`scene.dynamics.mujoco.sdf_initpoints`](sim-2/property_scene_dynamics_mujoco_sdf_initpoints.htm)
- [`scene.dynamics.mujoco.sdf_iterations`](sim-2/property_scene_dynamics_mujoco_sdf_iterations.htm)
- [`scene.dynamics.mujoco.sensorEnable`](sim-2/property_scene_dynamics_mujoco_sensorEnable.htm)
- [`scene.dynamics.mujoco.solver`](sim-2/property_scene_dynamics_mujoco_solver.htm)
- [`scene.dynamics.mujoco.tolerance`](sim-2/property_scene_dynamics_mujoco_tolerance.htm)
- [`scene.dynamics.mujoco.viscosity`](sim-2/property_scene_dynamics_mujoco_viscosity.htm)
- [`scene.dynamics.mujoco.warmstartEnable`](sim-2/property_scene_dynamics_mujoco_warmstartEnable.htm)
- [`scene.dynamics.mujoco.wind`](sim-2/property_scene_dynamics_mujoco_wind.htm)
- [`scene.dynamics.newton.computeInertias`](sim-2/property_scene_dynamics_newton_computeInertias.htm)
- [`scene.dynamics.newton.contactMergeTolerance`](sim-2/property_scene_dynamics_newton_contactMergeTolerance.htm)
- [`scene.dynamics.newton.exactSolver`](sim-2/property_scene_dynamics_newton_exactSolver.htm)
- [`scene.dynamics.newton.highJointAccuracy`](sim-2/property_scene_dynamics_newton_highJointAccuracy.htm)
- [`scene.dynamics.newton.iterations`](sim-2/property_scene_dynamics_newton_iterations.htm)
- [`scene.dynamics.newton.multithreading`](sim-2/property_scene_dynamics_newton_multithreading.htm)
- [`scene.dynamics.ode.computeInertias`](sim-2/property_scene_dynamics_ode_computeInertias.htm)
- [`scene.dynamics.ode.globalCfm`](sim-2/property_scene_dynamics_ode_globalCfm.htm)
- [`scene.dynamics.ode.globalErp`](sim-2/property_scene_dynamics_ode_globalErp.htm)
- [`scene.dynamics.ode.internalScalingFull`](sim-2/property_scene_dynamics_ode_internalScalingFull.htm)
- [`scene.dynamics.ode.internalScalingValue`](sim-2/property_scene_dynamics_ode_internalScalingValue.htm)
- [`scene.dynamics.ode.quickStepEnabled`](sim-2/property_scene_dynamics_ode_quickStepEnabled.htm)
- [`scene.dynamics.ode.quickStepIterations`](sim-2/property_scene_dynamics_ode_quickStepIterations.htm)
- [`scene.dynamics.showContactPoints`](sim-2/property_scene_dynamics_showContactPoints.htm) — Show contact points
- [`scene.dynamics.stepSize`](sim-2/property_scene_dynamics_stepSize.htm) — Dynamics dt
- [`scene.dynamics.vortex.autoSleep`](sim-2/property_scene_dynamics_vortex_autoSleep.htm)
- [`scene.dynamics.vortex.computeInertias`](sim-2/property_scene_dynamics_vortex_computeInertias.htm)
- [`scene.dynamics.vortex.constraintsAngularCompliance`](sim-2/property_scene_dynamics_vortex_constraintsAngularCompliance.htm)
- [`scene.dynamics.vortex.constraintsAngularDamping`](sim-2/property_scene_dynamics_vortex_constraintsAngularDamping.htm)
- [`scene.dynamics.vortex.constraintsAngularKineticLoss`](sim-2/property_scene_dynamics_vortex_constraintsAngularKineticLoss.htm)
- [`scene.dynamics.vortex.constraintsLinearCompliance`](sim-2/property_scene_dynamics_vortex_constraintsLinearCompliance.htm)
- [`scene.dynamics.vortex.constraintsLinearDamping`](sim-2/property_scene_dynamics_vortex_constraintsLinearDamping.htm)
- [`scene.dynamics.vortex.constraintsLinearKineticLoss`](sim-2/property_scene_dynamics_vortex_constraintsLinearKineticLoss.htm)
- [`scene.dynamics.vortex.contactTolerance`](sim-2/property_scene_dynamics_vortex_contactTolerance.htm)
- [`scene.dynamics.vortex.multithreading`](sim-2/property_scene_dynamics_vortex_multithreading.htm)
- [`sceneObject.dynamicFlag`](sim-2/property_sceneObject_dynamicFlag.htm) — Dynamic flag
- [`sceneObject.dynamicIcon`](sim-2/property_sceneObject_dynamicIcon.htm) — Dynamic icon
- [`sceneObject.dynamicallyEnabled`](sim-2/property_sceneObject_dynamicallyEnabled.htm) — Dynamically enabled
- [`sceneObject.model.notDynamic`](sim-2/property_sceneObject_model_notDynamic.htm) — Model not dynamic
- [`sceneObject.model.notRespondable`](sim-2/property_sceneObject_model_notRespondable.htm) — Model not respondable
- [`shape.convex`](sim-2/property_shape_convex.htm) — Convex
- [`shape.dynamics.angularVelocity`](sim-2/property_shape_dynamics_angularVelocity.htm) — Rotational velocity
- [`shape.dynamics.bullet.angularDamping`](sim-2/property_shape_dynamics_bullet_angularDamping.htm)
- [`shape.dynamics.bullet.autoShrinkConvexMeshes`](sim-2/property_shape_dynamics_bullet_autoShrinkConvexMeshes.htm)
- [`shape.dynamics.bullet.customCollisionMarginConvexEnabled`](sim-2/property_shape_dynamics_bullet_customCollisionMarginConvexEnabled.htm)
- [`shape.dynamics.bullet.customCollisionMarginConvexValue`](sim-2/property_shape_dynamics_bullet_customCollisionMarginConvexValue.htm)
- [`shape.dynamics.bullet.customCollisionMarginEnabled`](sim-2/property_shape_dynamics_bullet_customCollisionMarginEnabled.htm)
- [`shape.dynamics.bullet.customCollisionMarginValue`](sim-2/property_shape_dynamics_bullet_customCollisionMarginValue.htm)
- [`shape.dynamics.bullet.friction`](sim-2/property_shape_dynamics_bullet_friction.htm)
- [`shape.dynamics.bullet.frictionOld`](sim-2/property_shape_dynamics_bullet_frictionOld.htm)
- [`shape.dynamics.bullet.linearDamping`](sim-2/property_shape_dynamics_bullet_linearDamping.htm)
- [`shape.dynamics.bullet.restitution`](sim-2/property_shape_dynamics_bullet_restitution.htm)
- [`shape.dynamics.bullet.stickyContact`](sim-2/property_shape_dynamics_bullet_stickyContact.htm)
- [`shape.dynamics.centerOfMass`](sim-2/property_shape_dynamics_centerOfMass.htm) — Center of mass
- [`shape.dynamics.dynamic`](sim-2/property_shape_dynamics_dynamic.htm) — Dynamic
- [`shape.dynamics.engineProperties`](sim-2/property_shape_dynamics_engineProperties.htm) — Engine properties
- [`shape.dynamics.inertiaMatrix`](sim-2/property_shape_dynamics_inertiaMatrix.htm) — Inertia matrix
- [`shape.dynamics.initAngularVelocity`](sim-2/property_shape_dynamics_initAngularVelocity.htm) — Initial rotational velocity
- [`shape.dynamics.initLinearVelocity`](sim-2/property_shape_dynamics_initLinearVelocity.htm) — Initial linear velocity
- [`shape.dynamics.kinematic`](sim-2/property_shape_dynamics_kinematic.htm) — Kinematic
- [`shape.dynamics.linearVelocity`](sim-2/property_shape_dynamics_linearVelocity.htm) — Linear velocity
- [`shape.dynamics.mass`](sim-2/property_shape_dynamics_mass.htm) — Mass
- [`shape.dynamics.mujoco.adhesion`](sim-2/property_shape_dynamics_mujoco_adhesion.htm)
- [`shape.dynamics.mujoco.adhesionctrl`](sim-2/property_shape_dynamics_mujoco_adhesionctrl.htm)
- [`shape.dynamics.mujoco.adhesionctrlrange`](sim-2/property_shape_dynamics_mujoco_adhesionctrlrange.htm)
- [`shape.dynamics.mujoco.adhesionforcelimited`](sim-2/property_shape_dynamics_mujoco_adhesionforcelimited.htm)
- [`shape.dynamics.mujoco.adhesionforcerange`](sim-2/property_shape_dynamics_mujoco_adhesionforcerange.htm)
- [`shape.dynamics.mujoco.adhesiongain`](sim-2/property_shape_dynamics_mujoco_adhesiongain.htm)
- [`shape.dynamics.mujoco.condim`](sim-2/property_shape_dynamics_mujoco_condim.htm)
- [`shape.dynamics.mujoco.friction`](sim-2/property_shape_dynamics_mujoco_friction.htm)
- [`shape.dynamics.mujoco.gap`](sim-2/property_shape_dynamics_mujoco_gap.htm)
- [`shape.dynamics.mujoco.gravcomp`](sim-2/property_shape_dynamics_mujoco_gravcomp.htm)
- [`shape.dynamics.mujoco.margin`](sim-2/property_shape_dynamics_mujoco_margin.htm)
- [`shape.dynamics.mujoco.priority`](sim-2/property_shape_dynamics_mujoco_priority.htm)
- [`shape.dynamics.mujoco.solimp`](sim-2/property_shape_dynamics_mujoco_solimp.htm)
- [`shape.dynamics.mujoco.solmix`](sim-2/property_shape_dynamics_mujoco_solmix.htm)
- [`shape.dynamics.mujoco.solref`](sim-2/property_shape_dynamics_mujoco_solref.htm)
- [`shape.dynamics.newton.angularDrag`](sim-2/property_shape_dynamics_newton_angularDrag.htm)
- [`shape.dynamics.newton.fastMoving`](sim-2/property_shape_dynamics_newton_fastMoving.htm)
- [`shape.dynamics.newton.kineticFriction`](sim-2/property_shape_dynamics_newton_kineticFriction.htm)
- [`shape.dynamics.newton.linearDrag`](sim-2/property_shape_dynamics_newton_linearDrag.htm)
- [`shape.dynamics.newton.restitution`](sim-2/property_shape_dynamics_newton_restitution.htm)
- [`shape.dynamics.newton.staticFriction`](sim-2/property_shape_dynamics_newton_staticFriction.htm)
- [`shape.dynamics.ode.angularDamping`](sim-2/property_shape_dynamics_ode_angularDamping.htm)
- [`shape.dynamics.ode.friction`](sim-2/property_shape_dynamics_ode_friction.htm)
- [`shape.dynamics.ode.linearDamping`](sim-2/property_shape_dynamics_ode_linearDamping.htm)
- [`shape.dynamics.ode.maxContacts`](sim-2/property_shape_dynamics_ode_maxContacts.htm)
- [`shape.dynamics.ode.softCfm`](sim-2/property_shape_dynamics_ode_softCfm.htm)
- [`shape.dynamics.ode.softErp`](sim-2/property_shape_dynamics_ode_softErp.htm)
- [`shape.dynamics.pmi`](sim-2/property_shape_dynamics_pmi.htm) — Principal moment of inertia
- [`shape.dynamics.pmiQuaternion`](sim-2/property_shape_dynamics_pmiQuaternion.htm) — Quaternion of the principal moment of inertia
- [`shape.dynamics.respondable`](sim-2/property_shape_dynamics_respondable.htm) — Respondable
- [`shape.dynamics.respondableMask`](sim-2/property_shape_dynamics_respondableMask.htm) — Respondable mask
- [`shape.dynamics.setToDynamicWithParent`](sim-2/property_shape_dynamics_setToDynamicWithParent.htm) — Set to dynamic if gets parent
- [`shape.dynamics.startInSleepMode`](sim-2/property_shape_dynamics_startInSleepMode.htm) — Start in sleep mode
- [`shape.dynamics.vortex.adhesiveForce`](sim-2/property_shape_dynamics_vortex_adhesiveForce.htm)
- [`shape.dynamics.vortex.angularNormalAxisFollowPrimaryAxis`](sim-2/property_shape_dynamics_vortex_angularNormalAxisFollowPrimaryAxis.htm)
- [`shape.dynamics.vortex.angularNormalAxisFrictionModel`](sim-2/property_shape_dynamics_vortex_angularNormalAxisFrictionModel.htm)
- [`shape.dynamics.vortex.angularNormalAxisFrictionValue`](sim-2/property_shape_dynamics_vortex_angularNormalAxisFrictionValue.htm)
- [`shape.dynamics.vortex.angularNormalAxisSlide`](sim-2/property_shape_dynamics_vortex_angularNormalAxisSlide.htm)
- [`shape.dynamics.vortex.angularNormalAxisSlip`](sim-2/property_shape_dynamics_vortex_angularNormalAxisSlip.htm)
- [`shape.dynamics.vortex.angularNormalAxisStaticFrictionScale`](sim-2/property_shape_dynamics_vortex_angularNormalAxisStaticFrictionScale.htm)
- [`shape.dynamics.vortex.angularPrimaryAxisFrictionModel`](sim-2/property_shape_dynamics_vortex_angularPrimaryAxisFrictionModel.htm)
- [`shape.dynamics.vortex.angularPrimaryAxisFrictionValue`](sim-2/property_shape_dynamics_vortex_angularPrimaryAxisFrictionValue.htm)
- [`shape.dynamics.vortex.angularPrimaryAxisSlide`](sim-2/property_shape_dynamics_vortex_angularPrimaryAxisSlide.htm)
- [`shape.dynamics.vortex.angularPrimaryAxisSlip`](sim-2/property_shape_dynamics_vortex_angularPrimaryAxisSlip.htm)
- [`shape.dynamics.vortex.angularPrimaryAxisStaticFrictionScale`](sim-2/property_shape_dynamics_vortex_angularPrimaryAxisStaticFrictionScale.htm)
- [`shape.dynamics.vortex.angularSecondaryAxisFollowPrimaryAxis`](sim-2/property_shape_dynamics_vortex_angularSecondaryAxisFollowPrimaryAxis.htm)
- [`shape.dynamics.vortex.angularSecondaryAxisFrictionModel`](sim-2/property_shape_dynamics_vortex_angularSecondaryAxisFrictionModel.htm)
- [`shape.dynamics.vortex.angularSecondaryAxisFrictionValue`](sim-2/property_shape_dynamics_vortex_angularSecondaryAxisFrictionValue.htm)
- [`shape.dynamics.vortex.angularSecondaryAxisSlide`](sim-2/property_shape_dynamics_vortex_angularSecondaryAxisSlide.htm)
- [`shape.dynamics.vortex.angularSecondaryAxisSlip`](sim-2/property_shape_dynamics_vortex_angularSecondaryAxisSlip.htm)
- [`shape.dynamics.vortex.angularSecondaryAxisStaticFrictionScale`](sim-2/property_shape_dynamics_vortex_angularSecondaryAxisStaticFrictionScale.htm)
- [`shape.dynamics.vortex.angularVelDamping`](sim-2/property_shape_dynamics_vortex_angularVelDamping.htm)
- [`shape.dynamics.vortex.autoAngularDampingEnabled`](sim-2/property_shape_dynamics_vortex_autoAngularDampingEnabled.htm)
- [`shape.dynamics.vortex.autoAngularDampingTensionRatio`](sim-2/property_shape_dynamics_vortex_autoAngularDampingTensionRatio.htm)
- [`shape.dynamics.vortex.autoSleepThresholdAngularAccel`](sim-2/property_shape_dynamics_vortex_autoSleepThresholdAngularAccel.htm)
- [`shape.dynamics.vortex.autoSleepThresholdAngularSpeed`](sim-2/property_shape_dynamics_vortex_autoSleepThresholdAngularSpeed.htm)
- [`shape.dynamics.vortex.autoSleepThresholdLinearAccel`](sim-2/property_shape_dynamics_vortex_autoSleepThresholdLinearAccel.htm)
- [`shape.dynamics.vortex.autoSleepThresholdLinearSpeed`](sim-2/property_shape_dynamics_vortex_autoSleepThresholdLinearSpeed.htm)
- [`shape.dynamics.vortex.autoSleepThresholdSteps`](sim-2/property_shape_dynamics_vortex_autoSleepThresholdSteps.htm)
- [`shape.dynamics.vortex.autoSlip`](sim-2/property_shape_dynamics_vortex_autoSlip.htm)
- [`shape.dynamics.vortex.compliance`](sim-2/property_shape_dynamics_vortex_compliance.htm)
- [`shape.dynamics.vortex.convexAsRandom`](sim-2/property_shape_dynamics_vortex_convexAsRandom.htm)
- [`shape.dynamics.vortex.damping`](sim-2/property_shape_dynamics_vortex_damping.htm)
- [`shape.dynamics.vortex.fastMoving`](sim-2/property_shape_dynamics_vortex_fastMoving.htm)
- [`shape.dynamics.vortex.linearPrimaryAxisFrictionModel`](sim-2/property_shape_dynamics_vortex_linearPrimaryAxisFrictionModel.htm)
- [`shape.dynamics.vortex.linearPrimaryAxisFrictionValue`](sim-2/property_shape_dynamics_vortex_linearPrimaryAxisFrictionValue.htm)
- [`shape.dynamics.vortex.linearPrimaryAxisSlide`](sim-2/property_shape_dynamics_vortex_linearPrimaryAxisSlide.htm)
- [`shape.dynamics.vortex.linearPrimaryAxisSlip`](sim-2/property_shape_dynamics_vortex_linearPrimaryAxisSlip.htm)
- [`shape.dynamics.vortex.linearPrimaryAxisStaticFrictionScale`](sim-2/property_shape_dynamics_vortex_linearPrimaryAxisStaticFrictionScale.htm)
- [`shape.dynamics.vortex.linearPrimaryValue`](sim-2/property_shape_dynamics_vortex_linearPrimaryValue.htm)
- [`shape.dynamics.vortex.linearSecondaryAxisFollowPrimaryAxis`](sim-2/property_shape_dynamics_vortex_linearSecondaryAxisFollowPrimaryAxis.htm)
- [`shape.dynamics.vortex.linearSecondaryAxisFrictionModel`](sim-2/property_shape_dynamics_vortex_linearSecondaryAxisFrictionModel.htm)
- [`shape.dynamics.vortex.linearSecondaryAxisFrictionValue`](sim-2/property_shape_dynamics_vortex_linearSecondaryAxisFrictionValue.htm)
- [`shape.dynamics.vortex.linearSecondaryAxisSlide`](sim-2/property_shape_dynamics_vortex_linearSecondaryAxisSlide.htm)
- [`shape.dynamics.vortex.linearSecondaryAxisSlip`](sim-2/property_shape_dynamics_vortex_linearSecondaryAxisSlip.htm)
- [`shape.dynamics.vortex.linearSecondaryAxisStaticFrictionScale`](sim-2/property_shape_dynamics_vortex_linearSecondaryAxisStaticFrictionScale.htm)
- [`shape.dynamics.vortex.linearVelDamping`](sim-2/property_shape_dynamics_vortex_linearVelDamping.htm)
- [`shape.dynamics.vortex.materialUniqueId`](sim-2/property_shape_dynamics_vortex_materialUniqueId.htm)
- [`shape.dynamics.vortex.primitiveAsConvex`](sim-2/property_shape_dynamics_vortex_primitiveAsConvex.htm)
- [`shape.dynamics.vortex.randomAsTerrain`](sim-2/property_shape_dynamics_vortex_randomAsTerrain.htm)
- [`shape.dynamics.vortex.restitution`](sim-2/property_shape_dynamics_vortex_restitution.htm)
- [`shape.dynamics.vortex.restitutionThreshold`](sim-2/property_shape_dynamics_vortex_restitutionThreshold.htm)
- [`shape.dynamics.vortex.skinThickness`](sim-2/property_shape_dynamics_vortex_skinThickness.htm)
- [`shape.primitive`](sim-2/property_shape_primitive.htm) — Primitive

## <a id="methodsAndProperties_property"></a><a id="methodsAndProperties_properties"></a><a id="methodsAndProperties_scriptParameters"></a>[Properties](properties.md) (methods & properties)

- [`object:getBoolProperty`](sim-2/object_getBoolProperty.htm) — Fetches a boolean property
- [`object:getBufferProperty`](sim-2/object_getBufferProperty.htm) — Fetches a buffer property
- [`object:getColorProperty`](sim-2/object_getColorProperty.htm) — Fetches a color property
- [`object:getEnumProperty`](sim-2/object_getEnumProperty.htm) — Fetches an enum property
- [`object:getFloatArrayProperty`](sim-2/object_getFloatArrayProperty.htm) — Fetches a float array property
- [`object:getFloatProperty`](sim-2/object_getFloatProperty.htm) — Fetches a float property
- [`object:getHandleArrayProperty`](sim-2/object_getHandleArrayProperty.htm) — Fetches a handle array property
- [`object:getHandleProperty`](sim-2/object_getHandleProperty.htm) — Fetches a handle property
- [`object:getIntArrayProperty`](sim-2/object_getIntArrayProperty.htm) — Fetches an int array property
- [`object:getIntProperty`](sim-2/object_getIntProperty.htm) — Fetches an int32 property
- [`object:getLongProperty`](sim-2/object_getLongProperty.htm) — Fetches an int64 property
- [`object:getMatrixProperty`](sim-2/object_getMatrixProperty.htm) — Fetches a matrix property
- [`object:getMethodProperty`](sim-2/object_getMethodProperty.htm) — Fetches a method property
- [`object:getPoseProperty`](sim-2/object_getPoseProperty.htm) — Fetches a pose property
- [`object:getProperties`](sim-2/object_getProperties.htm) — Fetches all properties of a target
- [`object:getPropertiesInfos`](sim-2/object_getPropertiesInfos.htm) — Fetches all property infos of a target
- [`object:getProperty`](sim-2/object_getProperty.htm) — Convenience function to fetch a property
- [`object:getPropertyInfo`](sim-2/object_getPropertyInfo.htm) — Fetches information about a property
- [`object:getPropertyInfos`](sim-2/object_getPropertyInfos.htm) — Fetches an extended set of property infos
- [`object:getPropertyName`](sim-2/object_getPropertyName.htm) — Fetches a property name by index
- [`object:getPropertyTypeString`](sim-2/object_getPropertyTypeString.htm) — Gets string for a property type
- [`object:getQuaternionProperty`](sim-2/object_getQuaternionProperty.htm) — Fetches a quaternion property
- [`object:getStringArrayProperty`](sim-2/object_getStringArrayProperty.htm) — Fetches a text array property
- [`object:getStringProperty`](sim-2/object_getStringProperty.htm) — Fetches a string property
- [`object:getTableProperty`](sim-2/object_getTableProperty.htm) — Fetches a table property
- [`object:getVector3Property`](sim-2/object_getVector3Property.htm) — Fetches a vector3 property
- [`object:removeProperty`](sim-2/object_removeProperty.htm) — Removes a removable property
- [`object:setBoolProperty`](sim-2/object_setBoolProperty.htm) — Sets a boolean property
- [`object:setBufferProperty`](sim-2/object_setBufferProperty.htm) — Sets a buffer property
- [`object:setColorProperty`](sim-2/object_setColorProperty.htm) — Sets a color property
- [`object:setEnumProperty`](sim-2/object_setEnumProperty.htm) — Sets an enum property
- [`object:setFloatArrayProperty`](sim-2/object_setFloatArrayProperty.htm) — Sets a float array property
- [`object:setFloatProperty`](sim-2/object_setFloatProperty.htm) — Sets a float property
- [`object:setHandleArrayProperty`](sim-2/object_setHandleArrayProperty.htm) — Sets a handle array property
- [`object:setHandleProperty`](sim-2/object_setHandleProperty.htm) — Sets a handle property
- [`object:setIntArrayProperty`](sim-2/object_setIntArrayProperty.htm) — Sets an int array property
- [`object:setIntProperty`](sim-2/object_setIntProperty.htm) — Sets an int32 property
- [`object:setLongProperty`](sim-2/object_setLongProperty.htm) — Sets an int64 property
- [`object:setMatrixProperty`](sim-2/object_setMatrixProperty.htm) — Sets a matrix property
- [`object:setMethodProperty`](sim-2/object_setMethodProperty.htm) — Sets a method property
- [`object:setPoseProperty`](sim-2/object_setPoseProperty.htm) — Sets a pose property
- [`object:setProperties`](sim-2/object_setProperties.htm) — Sets several properties at once
- [`object:setProperty`](sim-2/object_setProperty.htm) — Convenience function to set a property
- [`object:setPropertyInfo`](sim-2/object_setPropertyInfo.htm) — Sets information about a property
- [`object:setQuaternionProperty`](sim-2/object_setQuaternionProperty.htm) — Sets a quaternion property
- [`object:setStringArrayProperty`](sim-2/object_setStringArrayProperty.htm) — Sets a text array property
- [`object:setStringProperty`](sim-2/object_setStringProperty.htm) — Sets a string property
- [`object:setTableProperty`](sim-2/object_setTableProperty.htm) — Sets a table property
- [`object:setVector3Property`](sim-2/object_setVector3Property.htm) — Sets a vector3 property

## <a id="methodsAndProperties_collision"></a><a id="methodsAndProperties_collisionDetection"></a>[Collision detection](collisionDetection.md) (methods & properties)

- [`collection:checkCollision`](sim-2/collection_checkCollision.htm) — Checks collision with another entity
- [`ocTree:checkPackedPoints`](sim-2/ocTree_checkPackedPoints.htm) — Checks if packed points collide with voxels
- [`ocTree:checkPoints`](sim-2/ocTree_checkPoints.htm) — Checks if points collide with the voxels
- [`sceneObject:checkCollision`](sim-2/sceneObject_checkCollision.htm) — Checks collision with another entity
- [`sceneObject.collectionSelfCollisionIndicator`](sim-2/property_sceneObject_collectionSelfCollisionIndicator.htm) — Collection self-collision indicator
- [`sceneObject.collidable`](sim-2/property_sceneObject_collidable.htm) — Collidable
- [`sceneObject.model.notCollidable`](sim-2/property_sceneObject_model_notCollidable.htm) — Model not collidable

## <a id="methodsAndProperties_distance"></a><a id="methodsAndProperties_distanceCalculation"></a>[Distance calculation](distanceCalculation.md) (methods & properties)

- [`collection:checkDistance`](sim-2/collection_checkDistance.htm) — Checks minimum distance with another entity
- [`sceneObject:checkDistance`](sim-2/sceneObject_checkDistance.htm) — Checks minimum distance with another entity
- [`proximitySensor.detectedDistance`](sim-2/property_proximitySensor_detectedDistance.htm) — Detected distance
- [`sceneObject.measurable`](sim-2/property_sceneObject_measurable.htm) — Measurable
- [`sceneObject.model.notMeasurable`](sim-2/property_sceneObject_model_notMeasurable.htm) — Model not measurable

## <a id="methodsAndProperties_rendering"></a>[Rendering](dataVisualizationAndOutput.md) (methods & properties)

- [`collection:changeColor`](sim-2/collection_changeColor.htm) — Changes the color of all shapes in the collection
- [`collection:restoreColor`](sim-2/collection_restoreColor.htm) — Restores the color of shapes in the collection
- [`marker:addItems`](sim-2/marker_addItems.htm) — Adds items to a marker
- [`marker:addPackedItems`](sim-2/marker_addPackedItems.htm) — Adds packed items to a marker
- [`marker:clearItems`](sim-2/marker_clearItems.htm) — Clears a marker
- [`marker:removeItems`](sim-2/marker_removeItems.htm) — Removes specific items from a marker
- [`sceneObject:changeColor`](sim-2/sceneObject_changeColor.htm) — Changes the color of the object (if shape)
- [`sceneObject:restoreColor`](sim-2/sceneObject_restoreColor.htm) — Restores the object's color (if shape)
- [`shape:getAppearance`](sim-2/shape_getAppearance.htm) — Fetches the shape's main appearance properties
- [`shape:setAppearance`](sim-2/shape_setAppearance.htm) — Sets the shape's main appearance properties
- [`app.displayEnabled`](sim-2/property_app_displayEnabled.htm) — Display enabled
- [`app.headlessMode`](sim-2/property_app_headlessMode.htm) — Headless mode
- [`camera.clippingPlanes`](sim-2/property_camera_clippingPlanes.htm) — Clipping planes
- [`camera.color.diffuse`](sim-2/property_camera_color_diffuse.htm) — Diffuse color
- [`camera.color.emission`](sim-2/property_camera_color_emission.htm) — Emission color
- [`camera.color.specular`](sim-2/property_camera_color_specular.htm) — Specular color
- [`camera.frustumCornerFar`](sim-2/property_camera_frustumCornerFar.htm) — Far corner of view frustum
- [`camera.frustumCornerNear`](sim-2/property_camera_frustumCornerNear.htm) — Near corner of view frustum
- [`camera.perspective`](sim-2/property_camera_perspective.htm) — Perspective
- [`camera.resolution`](sim-2/property_camera_resolution.htm) — Resolution
- [`camera.showFrustum`](sim-2/property_camera_showFrustum.htm) — Show view frustum
- [`camera.size`](sim-2/property_camera_size.htm) — Size
- [`camera.viewAngle`](sim-2/property_camera_viewAngle.htm) — View angle
- [`camera.viewSize`](sim-2/property_camera_viewSize.htm) — View size
- [`console.hiddenInSimulation`](sim-2/property_console_hiddenInSimulation.htm) — Hides during simulation
- [`console.visible`](sim-2/property_console_visible.htm) — Visible
- [`dummy.color.diffuse`](sim-2/property_dummy_color_diffuse.htm) — Diffuse color
- [`dummy.color.emission`](sim-2/property_dummy_color_emission.htm) — Emission color
- [`dummy.color.specular`](sim-2/property_dummy_color_specular.htm) — Specular color
- [`dummy.size`](sim-2/property_dummy_size.htm) — Size
- [`forceSensor.color.diffuse`](sim-2/property_forceSensor_color_diffuse.htm) — Diffuse color
- [`forceSensor.color.emission`](sim-2/property_forceSensor_color_emission.htm) — Emission color
- [`forceSensor.color.specular`](sim-2/property_forceSensor_color_specular.htm) — Specular color
- [`forceSensor.size`](sim-2/property_forceSensor_size.htm) — Size
- [`graph.backgroundColor`](sim-2/property_graph_backgroundColor.htm) — Background color
- [`graph.color.diffuse`](sim-2/property_graph_color_diffuse.htm) — Diffuse color
- [`graph.color.emission`](sim-2/property_graph_color_emission.htm) — Emission color
- [`graph.color.specular`](sim-2/property_graph_color_specular.htm) — Specular color
- [`graph.foregroundColor`](sim-2/property_graph_foregroundColor.htm) — Foreground color
- [`graph.size`](sim-2/property_graph_size.htm) — Size
- [`joint.color.diffuse`](sim-2/property_joint_color_diffuse.htm) — Diffuse color
- [`joint.color.emission`](sim-2/property_joint_color_emission.htm) — Emission color
- [`joint.color.specular`](sim-2/property_joint_color_specular.htm) — Specular color
- [`joint.length`](sim-2/property_joint_length.htm) — Length
- [`light.attenuationFactors`](sim-2/property_light_attenuationFactors.htm) — Attenuation factors
- [`light.color.diffuse`](sim-2/property_light_color_diffuse.htm) — Diffuse color
- [`light.color.emission`](sim-2/property_light_color_emission.htm) — Emission color
- [`light.color.specular`](sim-2/property_light_color_specular.htm) — Specular color
- [`light.enabled`](sim-2/property_light_enabled.htm) — Enabled
- [`light.light.type`](sim-2/property_light_light_type.htm) — Type
- [`light.lightColor.diffuse`](sim-2/property_light_lightColor_diffuse.htm) — Diffuse color
- [`light.lightColor.emission`](sim-2/property_light_lightColor_emission.htm) — Emission color
- [`light.lightColor.specular`](sim-2/property_light_lightColor_specular.htm) — Specular color
- [`light.povray.castShadows`](sim-2/property_light_povray_castShadows.htm) — POV-Ray: Cast shadows
- [`light.size`](sim-2/property_light_size.htm) — Size
- [`light.spotCutoffAngle`](sim-2/property_light_spotCutoffAngle.htm) — Cutoff angle
- [`light.spotExponent`](sim-2/property_light_spotExponent.htm) — Spot exponent
- [`marker.colors`](sim-2/property_marker_colors.htm) — Colors
- [`marker.defaultItemSize`](sim-2/property_marker_defaultItemSize.htm) — Default size
- [`marker.indices`](sim-2/property_marker_indices.htm) — Indices
- [`marker.local`](sim-2/property_marker_local.htm) — Local
- [`marker.marker.type`](sim-2/property_marker_marker_type.htm) — Type
- [`marker.normals`](sim-2/property_marker_normals.htm) — Normals
- [`marker.overlay`](sim-2/property_marker_overlay.htm) — Overlay
- [`marker.packedPoints`](sim-2/property_marker_packedPoints.htm) — Packed points
- [`marker.packedQuaternions`](sim-2/property_marker_packedQuaternions.htm) — Packed quaternions
- [`marker.packedSizes`](sim-2/property_marker_packedSizes.htm) — Packed sizes
- [`marker.points`](sim-2/property_marker_points.htm) — Points
- [`marker.quaternions`](sim-2/property_marker_quaternions.htm) — Quaternions
- [`marker.sizes`](sim-2/property_marker_sizes.htm) — Sizes
- [`marker.vertices`](sim-2/property_marker_vertices.htm) — Vertices
- [`mesh.color.diffuse`](sim-2/property_mesh_color_diffuse.htm) — Diffuse color
- [`mesh.color.emission`](sim-2/property_mesh_color_emission.htm) — Emission color
- [`mesh.color.specular`](sim-2/property_mesh_color_specular.htm) — Specular color
- [`mesh.color.transparency`](sim-2/property_mesh_color_transparency.htm) — Transparency
- [`mesh.colorName`](sim-2/property_mesh_colorName.htm) — Color name
- [`mesh.culling`](sim-2/property_mesh_culling.htm) — Backface culling
- [`mesh.indices`](sim-2/property_mesh_indices.htm) — Indices
- [`mesh.normals`](sim-2/property_mesh_normals.htm) — Normals
- [`mesh.primitive`](sim-2/property_mesh_primitive.htm) — Primitive type
- [`mesh.shadingAngle`](sim-2/property_mesh_shadingAngle.htm) — Shading angle
- [`mesh.showEdges`](sim-2/property_mesh_showEdges.htm) — Visible edges
- [`mesh.texture.applyMode`](sim-2/property_mesh_texture_applyMode.htm) — Texture apply mode
- [`mesh.texture.interpolate`](sim-2/property_mesh_texture_interpolate.htm) — Interpolate texture
- [`mesh.texture.repeatU`](sim-2/property_mesh_texture_repeatU.htm) — Texture repeat U
- [`mesh.texture.repeatV`](sim-2/property_mesh_texture_repeatV.htm) — Texture repeat V
- [`mesh.textureCoordinates`](sim-2/property_mesh_textureCoordinates.htm) — Texture coordinates
- [`mesh.vertices`](sim-2/property_mesh_vertices.htm) — Vertices
- [`mesh.wireframe`](sim-2/property_mesh_wireframe.htm) — Wireframe
- [`ocTree.color.diffuse`](sim-2/property_ocTree_color_diffuse.htm) — Diffuse color
- [`ocTree.color.emission`](sim-2/property_ocTree_color_emission.htm) — Emission color
- [`ocTree.color.specular`](sim-2/property_ocTree_color_specular.htm) — Specular color
- [`ocTree.colors`](sim-2/property_ocTree_colors.htm) — Voxel colors
- [`ocTree.packedPoints`](sim-2/property_ocTree_packedPoints.htm) — Packed voxels
- [`ocTree.points`](sim-2/property_ocTree_points.htm) — Voxels
- [`ocTree.randomColors`](sim-2/property_ocTree_randomColors.htm) — Random voxel colors
- [`ocTree.showPoints`](sim-2/property_ocTree_showPoints.htm) — Show points instead of voxels
- [`ocTree.voxelSize`](sim-2/property_ocTree_voxelSize.htm) — Voxel size
- [`pointCloud.cellSize`](sim-2/property_pointCloud_cellSize.htm) — Cell size
- [`pointCloud.color.diffuse`](sim-2/property_pointCloud_color_diffuse.htm) — Diffuse color
- [`pointCloud.color.emission`](sim-2/property_pointCloud_color_emission.htm) — Emission color
- [`pointCloud.color.specular`](sim-2/property_pointCloud_color_specular.htm) — Specular color
- [`pointCloud.colors`](sim-2/property_pointCloud_colors.htm) — Colors
- [`pointCloud.maxPointsInCell`](sim-2/property_pointCloud_maxPointsInCell.htm) — Max. points in cell
- [`pointCloud.packedPoints`](sim-2/property_pointCloud_packedPoints.htm) — Packed points
- [`pointCloud.pointDisplayFraction`](sim-2/property_pointCloud_pointDisplayFraction.htm) — Display fraction
- [`pointCloud.pointSize`](sim-2/property_pointCloud_pointSize.htm) — Point size
- [`pointCloud.points`](sim-2/property_pointCloud_points.htm) — Points
- [`pointCloud.randomColors`](sim-2/property_pointCloud_randomColors.htm) — Random point colors
- [`proximitySensor.color.diffuse`](sim-2/property_proximitySensor_color_diffuse.htm) — Diffuse color
- [`proximitySensor.color.emission`](sim-2/property_proximitySensor_color_emission.htm) — Emission color
- [`proximitySensor.color.specular`](sim-2/property_proximitySensor_color_specular.htm) — Specular color
- [`proximitySensor.pointSize`](sim-2/property_proximitySensor_pointSize.htm) — Sensor point size
- [`proximitySensor.rayColor.diffuse`](sim-2/property_proximitySensor_rayColor_diffuse.htm) — Diffuse color
- [`proximitySensor.rayColor.emission`](sim-2/property_proximitySensor_rayColor_emission.htm) — Emission color
- [`proximitySensor.rayColor.specular`](sim-2/property_proximitySensor_rayColor_specular.htm) — Specular color
- [`proximitySensor.showVolume`](sim-2/property_proximitySensor_showVolume.htm) — Show volume
- [`scene.ambientLight`](sim-2/property_scene_ambientLight.htm) — Ambient light
- [`scene.drawingObjects`](sim-2/property_scene_drawingObjects.htm) — Drawing objects
- [`scene.dynamics.showContactPoints`](sim-2/property_scene_dynamics_showContactPoints.htm) — Show contact points
- [`scene.visibilityLayers`](sim-2/property_scene_visibilityLayers.htm) — Visibility layers
- [`sceneObject.depthInvisible`](sim-2/property_sceneObject_depthInvisible.htm) — Depth pass invisible
- [`sceneObject.hideFromModelBB`](sim-2/property_sceneObject_hideFromModelBB.htm) — Hide from model bounding box
- [`sceneObject.layer`](sim-2/property_sceneObject_layer.htm) — Visibility layer
- [`sceneObject.model.notInParentBB`](sim-2/property_sceneObject_model_notInParentBB.htm) — Model invisible to other models' bounding boxes
- [`sceneObject.model.notVisible`](sim-2/property_sceneObject_model_notVisible.htm) — Model not visible
- [`sceneObject.visible`](sim-2/property_sceneObject_visible.htm) — Visible
- [`scriptObject.color.diffuse`](sim-2/property_scriptObject_color_diffuse.htm) — Diffuse color
- [`scriptObject.color.emission`](sim-2/property_scriptObject_color_emission.htm) — Emission color
- [`scriptObject.color.specular`](sim-2/property_scriptObject_color_specular.htm) — Specular color
- [`scriptObject.size`](sim-2/property_scriptObject_size.htm) — Size
- [`shape.applyColor.diffuse`](sim-2/property_shape_applyColor_diffuse.htm) — Apply diffuse color
- [`shape.applyColor.emission`](sim-2/property_shape_applyColor_emission.htm) — Apply emission color
- [`shape.applyColor.specular`](sim-2/property_shape_applyColor_specular.htm) — Apply specular color
- [`shape.applyColor.transparency`](sim-2/property_shape_applyColor_transparency.htm) — Apply transparency
- [`shape.applyCulling`](sim-2/property_shape_applyCulling.htm) — Apply culling
- [`shape.applyShadingAngle`](sim-2/property_shape_applyShadingAngle.htm) — Apply shading
- [`shape.applyShowEdges`](sim-2/property_shape_applyShowEdges.htm) — Apply edges
- [`shape.compoundColors.diffuse`](sim-2/property_shape_compoundColors_diffuse.htm) — Diffuse color data
- [`shape.compoundColors.emission`](sim-2/property_shape_compoundColors_emission.htm) — Emission color data
- [`shape.compoundColors.specular`](sim-2/property_shape_compoundColors_specular.htm) — Specular color data
- [`shape.compoundColors.transparency`](sim-2/property_shape_compoundColors_transparency.htm) — Transparency data
- [`shape.compoundCullings`](sim-2/property_shape_compoundCullings.htm) — Culling data
- [`shape.compoundEdges`](sim-2/property_shape_compoundEdges.htm) — Edge visibility data
- [`shape.compoundShadingAngles`](sim-2/property_shape_compoundShadingAngles.htm) — Shading angle data
- [`shape.compoundWireframe`](sim-2/property_shape_compoundWireframe.htm) — Wireframe data
- [`shape.flipFaces`](sim-2/property_shape_flipFaces.htm) — Flip faces
- [`shape.meshes`](sim-2/property_shape_meshes.htm) — Meshes
- [`textEditor.hiddenInSimulation`](sim-2/property_textEditor_hiddenInSimulation.htm) — Hides during simulation
- [`textEditor.visible`](sim-2/property_textEditor_visible.htm) — Visible
- [`textureData.image`](sim-2/property_textureData_image.htm) — Image
- [`textureData.resolution`](sim-2/property_textureData_resolution.htm) — Resolution
- [`visionSensor.backgroundColor`](sim-2/property_visionSensor_backgroundColor.htm) — Background color
- [`visionSensor.backgroundColorFromEnvironment`](sim-2/property_visionSensor_backgroundColorFromEnvironment.htm) — Background color from environment
- [`visionSensor.clippingPlanes`](sim-2/property_visionSensor_clippingPlanes.htm) — Clipping planes
- [`visionSensor.color.diffuse`](sim-2/property_visionSensor_color_diffuse.htm) — Diffuse color
- [`visionSensor.color.emission`](sim-2/property_visionSensor_color_emission.htm) — Emission color
- [`visionSensor.color.specular`](sim-2/property_visionSensor_color_specular.htm) — Specular color
- [`visionSensor.depth`](sim-2/property_visionSensor_depth.htm) — Depth buffer
- [`visionSensor.frustumCornerFar`](sim-2/property_visionSensor_frustumCornerFar.htm) — Far corner of view frustum
- [`visionSensor.frustumCornerNear`](sim-2/property_visionSensor_frustumCornerNear.htm) — Near corner of view frustum
- [`visionSensor.image`](sim-2/property_visionSensor_image.htm) — RGB buffer
- [`visionSensor.perspective`](sim-2/property_visionSensor_perspective.htm) — Perspective
- [`visionSensor.povray.aperture`](sim-2/property_visionSensor_povray_aperture.htm) — POV-Ray: aperture
- [`visionSensor.povray.blurDistance`](sim-2/property_visionSensor_povray_blurDistance.htm) — POV-Ray: blur distance
- [`visionSensor.povray.blurSamples`](sim-2/property_visionSensor_povray_blurSamples.htm) — POV-Ray: blur samples
- [`visionSensor.povray.focalBlur`](sim-2/property_visionSensor_povray_focalBlur.htm) — POV-Ray: focal blur
- [`visionSensor.renderMode`](sim-2/property_visionSensor_renderMode.htm) — Render mode
- [`visionSensor.resolution`](sim-2/property_visionSensor_resolution.htm) — Resolution
- [`visionSensor.showFrustum`](sim-2/property_visionSensor_showFrustum.htm) — Show view frustum
- [`visionSensor.size`](sim-2/property_visionSensor_size.htm) — Size
- [`visionSensor.viewAngle`](sim-2/property_visionSensor_viewAngle.htm) — View angle
- [`visionSensor.viewSize`](sim-2/property_visionSensor_viewSize.htm) — View size

## <a id="methodsAndProperties_customization"></a><a id="methodsAndProperties_customizingLuaFunctions"></a><a id="methodsAndProperties_customScriptFunctions"></a>Customization (methods & properties)

- [`app:createCustomObjectClass`](sim-2/app_createCustomObjectClass.htm) — Creates a custom object class
- [`customObject:makeObject`](sim-2/customObject_makeObject.htm) — Instantiates a custom object from a class
- [`sceneObject:makeClass`](sim-2/sceneObject_makeClass.htm) — Creates a class from this object
- [`sceneObject:makeObject`](sim-2/sceneObject_makeObject.htm) — Instantiates a customized scene object from a class
- [`app.addOns`](sim-2/property_app_addOns.htm) — Add-ons
- [`app.auxAddOn1`](sim-2/property_app_auxAddOn1.htm) — Aux. add-on 1
- [`app.auxAddOn2`](sim-2/property_app_auxAddOn2.htm) — Aux. add-on 2
- [`app.customClasses`](sim-2/property_app_customClasses.htm) — Custom classes
- [`app.customObjects`](sim-2/property_app_customObjects.htm) — Custom objects
- [`app.customSceneObjectClasses`](sim-2/property_app_customSceneObjectClasses.htm) — Custom scene object classes
- [`app.paths.addOns`](sim-2/property_app_paths_addOns.htm) — Add-on path
- [`app.paths.settings`](sim-2/property_app_paths_settings.htm) — Settings path
- [`app.pluginNames`](sim-2/property_app_pluginNames.htm) — Plugins
- [`camera.rotationEnabled`](sim-2/property_camera_rotationEnabled.htm) — Rotation enabled
- [`camera.translationEnabled`](sim-2/property_camera_translationEnabled.htm) — Translation enabled
- [`dummy.assemblyTag`](sim-2/property_dummy_assemblyTag.htm) — Assembly tag
- [`scene.customObjects`](sim-2/property_scene_customObjects.htm) — Custom objects
- [`sceneObject.cannotDelete`](sim-2/property_sceneObject_cannotDelete.htm) — Cannot delete
- [`sceneObject.cannotDeleteInSim`](sim-2/property_sceneObject_cannotDeleteInSim.htm) — Cannot delete during simulation
- [`sceneObject.hierarchyColor`](sim-2/property_sceneObject_hierarchyColor.htm) — Hierarchy color

## <a id="methodsAndProperties_model"></a><a id="methodsAndProperties_modelFunctionality"></a>[Models](models.md) (methods & properties)

- [`app:loadModelInfo`](sim-2/app_loadModelInfo.htm) — Loads a model thumbnail
- [`app:loadModelInfoFromBuffer`](sim-2/app_loadModelInfoFromBuffer.htm) — Loads a model thumbnail from buffer
- [`scene:copyObjects`](sim-2/scene_copyObjects.htm) — Copies selected objects
- [`scene:cutObjects`](sim-2/scene_cutObjects.htm) — Cuts selected objects
- [`scene:loadModel`](sim-2/scene_loadModel.htm) — Loads a previously saved model
- [`scene:loadModelFromBuffer`](sim-2/scene_loadModelFromBuffer.htm) — Loads a model from buffer
- [`scene:pasteObjects`](sim-2/scene_pasteObjects.htm) — Pastes objects
- [`sceneObject:saveModel`](sim-2/sceneObject_saveModel.htm) — Saves this model to a file
- [`sceneObject:saveModelToBuffer`](sim-2/sceneObject_saveModelToBuffer.htm) — Serializes this model to a buffer
- [`app.paths.models`](sim-2/property_app_paths_models.htm) — Model path
- [`scene.collections`](sim-2/property_scene_collections.htm) — Collections
- [`sceneObject.childOrder`](sim-2/property_sceneObject_childOrder.htm) — Child order
- [`sceneObject.children`](sim-2/property_sceneObject_children.htm) — Children
- [`sceneObject.collapsed`](sim-2/property_sceneObject_collapsed.htm) — Collapsed hierarchy
- [`sceneObject.hideFromModelBB`](sim-2/property_sceneObject_hideFromModelBB.htm) — Hide from model bounding box
- [`sceneObject.model.bbPos`](sim-2/property_sceneObject_model_bbPos.htm) — Model bounding box position
- [`sceneObject.model.bbSize`](sim-2/property_sceneObject_model_bbSize.htm) — Model bounding box size
- [`sceneObject.model.notCollidable`](sim-2/property_sceneObject_model_notCollidable.htm) — Model not collidable
- [`sceneObject.model.notDetectable`](sim-2/property_sceneObject_model_notDetectable.htm) — Model not detectable
- [`sceneObject.model.notDynamic`](sim-2/property_sceneObject_model_notDynamic.htm) — Model not dynamic
- [`sceneObject.model.notInParentBB`](sim-2/property_sceneObject_model_notInParentBB.htm) — Model invisible to other models' bounding boxes
- [`sceneObject.model.notMeasurable`](sim-2/property_sceneObject_model_notMeasurable.htm) — Model not measurable
- [`sceneObject.model.notRespondable`](sim-2/property_sceneObject_model_notRespondable.htm) — Model not respondable
- [`sceneObject.model.notVisible`](sim-2/property_sceneObject_model_notVisible.htm) — Model not visible
- [`sceneObject.model.propertyFlags`](sim-2/property_sceneObject_model_propertyFlags.htm) — Model flags
- [`sceneObject.model.scriptsNotActive`](sim-2/property_sceneObject_model_scriptsNotActive.htm) — Model scripts inactive
- [`sceneObject.modelAcknowledgment`](sim-2/property_sceneObject_modelAcknowledgment.htm) — Acknowledgment
- [`sceneObject.modelBase`](sim-2/property_sceneObject_modelBase.htm) — Model base
- [`sceneObject.modelHash`](sim-2/property_sceneObject_modelHash.htm) — Model hash
- [`sceneObject.modelInvisible`](sim-2/property_sceneObject_modelInvisible.htm) — Inherited model invisibility
- [`sceneObject.parent`](sim-2/property_sceneObject_parent.htm) — Parent
- [`sceneObject.parentUid`](sim-2/property_sceneObject_parentUid.htm) — Parent UID
- [`sceneObject.persistentUid`](sim-2/property_sceneObject_persistentUid.htm) — Persistent UID
- [`sceneObject.selectModel`](sim-2/property_sceneObject_selectModel.htm) — Select model instead
- [`sceneObject.tree`](sim-2/property_sceneObject_tree.htm) — Object tree

## <a id="methodsAndProperties_selection"></a><a id="methodsAndProperties_sceneObjectSelectionFunctionality"></a>Selection (methods & properties)

- [`app.current`](sim-2/property_app_current.htm) — Current
- [`scene.selection`](sim-2/property_scene_selection.htm) — Selected objects
- [`sceneObject.selectInvisible`](sim-2/property_sceneObject_selectInvisible.htm) — Select invisible
- [`sceneObject.selectModel`](sim-2/property_sceneObject_selectModel.htm) — Select model instead
- [`sceneObject.selectable`](sim-2/property_sceneObject_selectable.htm) — Selectable
- [`sceneObject.selected`](sim-2/property_sceneObject_selected.htm) — Selected

## <a id="methodsAndProperties_creation"></a><a id="methodsAndProperties_sceneObjectCreationFunctionality"></a>Object creation (methods & properties)

- [`app:createCustomObjectClass`](sim-2/app_createCustomObjectClass.htm) — Creates a custom object class
- [`app:createObject`](sim-2/app_createObject.htm) — Creates various objects (collections, scripts, sensors, etc.)
- [`app:removeObjects`](sim-2/app_removeObjects.htm) — Removes one or several objects
- [`collection:remove`](sim-2/collection_remove.htm) — Removes the collection
- [`console:remove`](sim-2/console_remove.htm) — Removes the console
- [`customObject:makeObject`](sim-2/customObject_makeObject.htm) — Instantiates a custom object from a class
- [`customObject:remove`](sim-2/customObject_remove.htm) — Removes the custom scene object
- [`scene:createObject`](sim-2/scene_createObject.htm) — Creates various objects (collections, scripts, sensors, etc.)
- [`scene:pasteObjects`](sim-2/scene_pasteObjects.htm) — Pastes objects
- [`scene:removeObjects`](sim-2/scene_removeObjects.htm) — Removes one or several objects
- [`sceneObject:remove`](sim-2/sceneObject_remove.htm) — Removes the object from the scene
- [`sceneObject:removeModel`](sim-2/sceneObject_removeModel.htm) — Removes the model from the scene
- [`script:remove`](sim-2/script_remove.htm) — Removes the script
- [`textEditor:remove`](sim-2/textEditor_remove.htm) — Removes the text editor
- [`textureData:remove`](sim-2/textureData_remove.htm) — Removes the texture
- [`object.type`](sim-2/property_object_type.htm) — Object type
- [`scene.objectCreationCounter`](sim-2/property_scene_objectCreationCounter.htm) — Object creation counter
- [`scene.objectDestructionCounter`](sim-2/property_scene_objectDestructionCounter.htm) — Object destruction counter
- [`scene.objects`](sim-2/property_scene_objects.htm) — Objects
- [`scene.orphans`](sim-2/property_scene_orphans.htm) — Orphan objects
- [`scene.simulation.removeNewObjects`](sim-2/property_scene_simulation_removeNewObjects.htm) — Remove new objects

## <a id="methodsAndProperties_scriptRelated"></a>[Script related](scripts.md) (methods & properties)

- [`app:handleAddOns`](sim-2/app_handleAddOns.htm) — Calls a system callback in add-ons
- [`app:handleSandboxes`](sim-2/app_handleSandboxes.htm) — Calls a system callback in the sandbox
- [`scene:handleCustomizationScripts`](sim-2/scene_handleCustomizationScripts.htm) — Calls a system callback in customization scripts
- [`scene:handleSimulationScripts`](sim-2/scene_handleSimulationScripts.htm) — Calls a system callback in simulation scripts
- [`script:broadcast`](sim-2/script_broadcast.htm) — Broadcasts a message to all other scripts
- [`script:callFunction`](sim-2/script_callFunction.htm) — Calls a function
- [`script:callMethod`](sim-2/script_callMethod.htm) — Calls a method
- [`script:cancelScheduledExecution`](sim-2/script_cancelScheduledExecution.htm) — Cancels a scheduled function execution
- [`script:executeString`](sim-2/script_executeString.htm) — Executes code from a string
- [`script:getFunctions`](sim-2/script_getFunctions.htm) — Retrieves callable functions of the script
- [`script:getStackTraceback`](sim-2/script_getStackTraceback.htm) — Retrieves and clears the last stack traceback
- [`script:getStepping`](sim-2/script_getStepping.htm) — Informs whether the stepping operation mode is enabled
- [`script:init`](sim-2/script_init.htm) — Initializes/reinitializes the script
- [`script:lock`](sim-2/script_lock.htm) — Acquires/releases a script lock to forbid yielding
- [`script:registerFunctionHook`](sim-2/script_registerFunctionHook.htm) — Registers a function hook for callbacks
- [`script:removeFunctionHook`](sim-2/script_removeFunctionHook.htm) — Removes a function hook
- [`script:reset`](sim-2/script_reset.htm) — Resets/ends the script
- [`script:resume`](sim-2/script_resume.htm) — Resumes the suspended script
- [`script:scheduleExecution`](sim-2/script_scheduleExecution.htm) — Schedules a function for execution after a delay
- [`script:setEventFilters`](sim-2/script_setEventFilters.htm) — Specifies filters for the sysCall_event callback
- [`script:setStepping`](sim-2/script_setStepping.htm) — Enables/disables stepping operation mode
- [`script:step`](sim-2/script_step.htm) — Triggers the next simulation step
- [`script:suspend`](sim-2/script_suspend.htm) — Suspends the script
- [`script:throttle`](sim-2/script_throttle.htm) — Limits the rate of a function call
- [`script:yield`](sim-2/script_yield.htm) — Identical to step()
- [`app.defaultPython`](sim-2/property_app_defaultPython.htm) — Default Python
- [`app.execUnsafe`](sim-2/property_app_execUnsafe.htm) — Execute unsafe
- [`app.execUnsafeExt`](sim-2/property_app_execUnsafeExt.htm) — Execute unsafe extended
- [`app.paths.lua`](sim-2/property_app_paths_lua.htm) — Lua path
- [`app.paths.python`](sim-2/property_app_paths_python.htm) — Python path
- [`app.sandboxLua`](sim-2/property_app_sandboxLua.htm) — Lua sandbox
- [`app.sandboxPython`](sim-2/property_app_sandboxPython.htm) — Python sandbox
- [`app.startupCode`](sim-2/property_app_startupCode.htm) — Start-up code
- [`proximitySensor.explicitHandling`](sim-2/property_proximitySensor_explicitHandling.htm) — Explicit handling
- [`scene.mainScript`](sim-2/property_scene_mainScript.htm) — Main script
- [`sceneObject.model.scriptsNotActive`](sim-2/property_sceneObject_model_scriptsNotActive.htm) — Model scripts inactive
- [`script.addOnMenuPath`](sim-2/property_script_addOnMenuPath.htm) — Add-on menu path
- [`script.addOnPath`](sim-2/property_script_addOnPath.htm) — Add-on path
- [`script.autoYieldDelay`](sim-2/property_script_autoYieldDelay.htm) — Automatic yield delay
- [`script.code`](sim-2/property_script_code.htm) — Code
- [`script.enabled`](sim-2/property_script_enabled.htm) — Enabled
- [`script.execPriority`](sim-2/property_script_execPriority.htm) — Execution priority
- [`script.executionDepth`](sim-2/property_script_executionDepth.htm) — Execution depth
- [`script.language`](sim-2/property_script_language.htm) — Language
- [`script.restartOnError`](sim-2/property_script_restartOnError.htm) — Restart
- [`script.script.type`](sim-2/property_script_script_type.htm) — Type
- [`script.scriptName`](sim-2/property_script_scriptName.htm) — Name
- [`script.state`](sim-2/property_script_state.htm) — State
- [`visionSensor.explicitHandling`](sim-2/property_visionSensor_explicitHandling.htm) — Explicit handling

## <a id="methodsAndProperties_simulation"></a><a id="methodsAndProperties_SimulationFunctionality"></a>[Simulation](simulation.md) (methods & properties)

- [`scene.simulation:pause`](sim-2/scene_simulation_pause.htm) — Requests a simulation pause
- [`scene.simulation:start`](sim-2/scene_simulation_start.htm) — Requests a simulation start or resume
- [`scene.simulation:stop`](sim-2/scene_simulation_stop.htm) — Requests a simulation stop
- [`app.paths.mujoco`](sim-2/property_app_paths_mujoco.htm) — MuJoCo path
- [`scene.dynamics.stepSize`](sim-2/property_scene_dynamics_stepSize.htm) — Dynamics dt
- [`scene.simulation.pauseAtError`](sim-2/property_scene_simulation_pauseAtError.htm) — Pause simulation on script error
- [`scene.simulation.pauseAtTime`](sim-2/property_scene_simulation_pauseAtTime.htm) — Pause simulation at time
- [`scene.simulation.realtime`](sim-2/property_scene_simulation_realtime.htm) — Real-time simulation
- [`scene.simulation.realtimeModifier`](sim-2/property_scene_simulation_realtimeModifier.htm) — Real-time modifier
- [`scene.simulation.removeNewObjects`](sim-2/property_scene_simulation_removeNewObjects.htm) — Remove new objects
- [`scene.simulation.speedModifier`](sim-2/property_scene_simulation_speedModifier.htm) — Speed modifier
- [`scene.simulation.state`](sim-2/property_scene_simulation_state.htm) — Simulation state
- [`scene.simulation.stepCount`](sim-2/property_scene_simulation_stepCount.htm) — Simulation steps
- [`scene.simulation.stepsPerRendering`](sim-2/property_scene_simulation_stepsPerRendering.htm) — Steps per frame
- [`scene.simulation.time`](sim-2/property_scene_simulation_time.htm) — Simulation time
- [`scene.simulation.timeStep`](sim-2/property_scene_simulation_timeStep.htm) — Simulation dt
- [`scene.simulation.timeToPause`](sim-2/property_scene_simulation_timeToPause.htm) — Simulation pause time
- [`scriptObject.resetAfterSimError`](sim-2/property_scriptObject_resetAfterSimError.htm) — Reset after simulation error

## <a id="methodsAndProperties_thread"></a><a id="methodsAndProperties_threads"></a><a id="methodsAndProperties_threadRelatedFunctionality"></a>[Threads](threadedAndNonThreadedCode.md) (methods & properties)

- [`app:handleMessagePump`](sim-2/app_handleMessagePump.htm) — Handles the message pump explicitly
- [`script:getStepping`](sim-2/script_getStepping.htm) — Informs whether the stepping operation mode is enabled
- [`script:lock`](sim-2/script_lock.htm) — Acquires/releases a script lock to forbid yielding
- [`script:setStepping`](sim-2/script_setStepping.htm) — Enables/disables stepping operation mode
- [`script:step`](sim-2/script_step.htm) — Triggers the next simulation step
- [`script:yield`](sim-2/script_yield.htm) — Identical to step()
- [`scene.dynamics.mujoco.multithreaded`](sim-2/property_scene_dynamics_mujoco_multithreaded.htm)
- [`scene.dynamics.newton.multithreading`](sim-2/property_scene_dynamics_newton_multithreading.htm)
- [`scene.dynamics.vortex.multithreading`](sim-2/property_scene_dynamics_vortex_multithreading.htm)
- [`script.autoYieldDelay`](sim-2/property_script_autoYieldDelay.htm) — Automatic yield delay

## <a id="methodsAndProperties_blocking"></a><a id="methodsAndProperties_blockingFunctions"></a>Blocking methods (methods & properties)

- [`MoveToConfig:run`](sim-2/MoveToConfig_run.htm) — Executes the motion in a thread
- [`MoveToPose:run`](sim-2/MoveToPose_run.htm) — Executes the motion in a thread
- [`app:systemLock`](sim-2/app_systemLock.htm) — Acquires/releases a system-wide semaphore
- [`script:getStepping`](sim-2/script_getStepping.htm) — Informs whether the stepping operation mode is enabled
- [`script:lock`](sim-2/script_lock.htm) — Acquires/releases a script lock to forbid yielding
- [`script:setStepping`](sim-2/script_setStepping.htm) — Enables/disables stepping operation mode
- [`script:step`](sim-2/script_step.htm) — Triggers the next simulation step
- [`script:wait`](sim-2/script_wait.htm) — Waits for a certain amount of time
- [`script:yield`](sim-2/script_yield.htm) — Identical to step()

## <a id="methodsAndProperties_transformation"></a><a id="methodsAndProperties_pose"></a><a id="methodsAndProperties_transformations"></a><a id="methodsAndProperties_coordinatesAndTransformations"></a>[Coordinates and transformations](positionOrientationTransformation.md) (methods & properties)

- [`IKObject:getPose`](sim-2/IKObject_getPose.htm) — Retrieves the IK object's pose
- [`IKObject:getPosition`](sim-2/IKObject_getPosition.htm) — Retrieves the IK object's position
- [`IKObject:getQuaternion`](sim-2/IKObject_getQuaternion.htm) — Retrieves the IK object's quaternion
- [`IKObject:setPose`](sim-2/IKObject_setPose.htm) — Sets the IK object's pose
- [`IKObject:setPosition`](sim-2/IKObject_setPosition.htm) — Sets the IK object's position
- [`IKObject:setQuaternion`](sim-2/IKObject_setQuaternion.htm) — Sets the IK object's quaternion
- [`sceneObject:getPose`](sim-2/sceneObject_getPose.htm) — Retrieves the pose of the scene object
- [`sceneObject:getPosition`](sim-2/sceneObject_getPosition.htm) — Retrieves the position of the scene object
- [`sceneObject:getQuaternion`](sim-2/sceneObject_getQuaternion.htm) — Retrieves the quaternion of the scene object
- [`sceneObject:setPose`](sim-2/sceneObject_setPose.htm) — Sets the pose of the scene object
- [`sceneObject:setPosition`](sim-2/sceneObject_setPosition.htm) — Sets the position of the scene object
- [`sceneObject:setQuaternion`](sim-2/sceneObject_setQuaternion.htm) — Sets the quaternion of the scene object
- [`shape:alignBoundingBox`](sim-2/shape_alignBoundingBox.htm) — Reorients the shape's bounding box
- [`shape:relocateFrame`](sim-2/shape_relocateFrame.htm) — Repositions/reorients the shape's reference frame
- [`app.defaultRotationStepSize`](sim-2/property_app_defaultRotationStepSize.htm) — Rotation step size
- [`app.defaultTranslationStepSize`](sim-2/property_app_defaultTranslationStepSize.htm) — Translation step size
- [`joint.intrinsicPose`](sim-2/property_joint_intrinsicPose.htm) — Intrinsic pose
- [`joint.joint.quaternion`](sim-2/property_joint_joint_quaternion.htm) — Spherical joint quaternion
- [`marker.local`](sim-2/property_marker_local.htm) — Local
- [`marker.packedQuaternions`](sim-2/property_marker_packedQuaternions.htm) — Packed quaternions
- [`marker.quaternions`](sim-2/property_marker_quaternions.htm) — Quaternions
- [`sceneObject.eulerAngles`](sim-2/property_sceneObject_eulerAngles.htm) — Euler angles
- [`sceneObject.mov.altRot`](sim-2/property_sceneObject_mov_altRot.htm) — Alternate rotation axes enabled
- [`sceneObject.mov.altTransl`](sim-2/property_sceneObject_mov_altTransl.htm) — Alternate translation axes enabled
- [`sceneObject.mov.optionsFlags`](sim-2/property_sceneObject_mov_optionsFlags.htm) — Movement flags
- [`sceneObject.mov.prefRotX`](sim-2/property_sceneObject_mov_prefRotX.htm) — Preferred X-axis rotation
- [`sceneObject.mov.prefRotY`](sim-2/property_sceneObject_mov_prefRotY.htm) — Preferred Y-axis rotation
- [`sceneObject.mov.prefRotZ`](sim-2/property_sceneObject_mov_prefRotZ.htm) — Preferred Z-axis rotation
- [`sceneObject.mov.prefTranslX`](sim-2/property_sceneObject_mov_prefTranslX.htm) — Preferred X-translation
- [`sceneObject.mov.prefTranslY`](sim-2/property_sceneObject_mov_prefTranslY.htm) — Preferred Y-translation
- [`sceneObject.mov.prefTranslZ`](sim-2/property_sceneObject_mov_prefTranslZ.htm) — Preferred Z-translation
- [`sceneObject.mov.preferredAxesFlags`](sim-2/property_sceneObject_mov_preferredAxesFlags.htm) — Preferred axes
- [`sceneObject.mov.relativity`](sim-2/property_sceneObject_mov_relativity.htm) — Movement relativity
- [`sceneObject.mov.rotInSim`](sim-2/property_sceneObject_mov_rotInSim.htm) — Rotation enabled during simulation
- [`sceneObject.mov.rotNoSim`](sim-2/property_sceneObject_mov_rotNoSim.htm) — Rotation enabled
- [`sceneObject.mov.stepSize`](sim-2/property_sceneObject_mov_stepSize.htm) — Movement step sizes
- [`sceneObject.mov.translInSim`](sim-2/property_sceneObject_mov_translInSim.htm) — Translation enabled during simulation
- [`sceneObject.mov.translNoSim`](sim-2/property_sceneObject_mov_translNoSim.htm) — Translation enabled
- [`sceneObject.pose`](sim-2/property_sceneObject_pose.htm) — Pose
- [`sceneObject.position`](sim-2/property_sceneObject_position.htm) — Position
- [`sceneObject.quaternion`](sim-2/property_sceneObject_quaternion.htm) — Quaternion
- [`sceneObject.worldEulerAngles`](sim-2/property_sceneObject_worldEulerAngles.htm) — Euler angles
- [`sceneObject.worldPose`](sim-2/property_sceneObject_worldPose.htm) — Pose
- [`sceneObject.worldPosition`](sim-2/property_sceneObject_worldPosition.htm) — Position
- [`sceneObject.worldQuaternion`](sim-2/property_sceneObject_worldQuaternion.htm) — Quaternion

## <a id="methodsAndProperties_hierarchy"></a>Scene hierarchy (methods & properties)

- [`IKGroup:addElementFromScene`](sim-2/IKGroup_addElementFromScene.htm) — Creates an IK element from the simulation world
- [`collection:addItem`](sim-2/collection_addItem.htm) — Adds one or several items to the collection
- [`collection:removeItem`](sim-2/collection_removeItem.htm) — Removes one or several items from the collection
- [`scene:getDescendants`](sim-2/scene_getDescendants.htm) — Retrieves scene objects up to a specific depth
- [`scene:getObject`](sim-2/scene_getObject.htm) — Retrieves an object by its path and name
- [`scene:getObjects`](sim-2/scene_getObjects.htm) — Retrieves objects of a certain type
- [`scene:loadModel`](sim-2/scene_loadModel.htm) — Loads a previously saved model
- [`scene:loadModelFromBuffer`](sim-2/scene_loadModelFromBuffer.htm) — Loads a model from buffer
- [`sceneObject:getAncestors`](sim-2/sceneObject_getAncestors.htm) — Retrieves ancestor scene objects
- [`sceneObject:getDescendants`](sim-2/sceneObject_getDescendants.htm) — Retrieves descendant scene objects
- [`sceneObject:getObject`](sim-2/sceneObject_getObject.htm) — Retrieves an object by its path and name
- [`sceneObject:removeModel`](sim-2/sceneObject_removeModel.htm) — Removes the model from the scene
- [`sceneObject:saveModel`](sim-2/sceneObject_saveModel.htm) — Saves this model to a file
- [`sceneObject:saveModelToBuffer`](sim-2/sceneObject_saveModelToBuffer.htm) — Serializes this model to a buffer
- [`sceneObject:scaleTree`](sim-2/sceneObject_scaleTree.htm) — Scales the object tree isometrically
- [`IKElement.base`](sim-2/property_IKElement_base.htm)
- [`IKElement.jointList`](sim-2/property_IKElement_jointList.htm)
- [`IKElement.target`](sim-2/property_IKElement_target.htm)
- [`IKElement.tip`](sim-2/property_IKElement_tip.htm)
- [`scene.hierarchyChangeCounter`](sim-2/property_scene_hierarchyChangeCounter.htm) — Hierarchy change counter
- [`scene.orphans`](sim-2/property_scene_orphans.htm) — Orphan objects
- [`sceneObject.childOrder`](sim-2/property_sceneObject_childOrder.htm) — Child order
- [`sceneObject.children`](sim-2/property_sceneObject_children.htm) — Children
- [`sceneObject.collapsed`](sim-2/property_sceneObject_collapsed.htm) — Collapsed hierarchy
- [`sceneObject.collectionSelfCollisionIndicator`](sim-2/property_sceneObject_collectionSelfCollisionIndicator.htm) — Collection self-collision indicator
- [`sceneObject.hierarchyColor`](sim-2/property_sceneObject_hierarchyColor.htm) — Hierarchy color
- [`sceneObject.model.notInParentBB`](sim-2/property_sceneObject_model_notInParentBB.htm) — Model invisible to other models' bounding boxes
- [`sceneObject.modelHash`](sim-2/property_sceneObject_modelHash.htm) — Model hash
- [`sceneObject.parent`](sim-2/property_sceneObject_parent.htm) — Parent
- [`sceneObject.selectModel`](sim-2/property_sceneObject_selectModel.htm) — Select model instead
- [`sceneObject.tree`](sim-2/property_sceneObject_tree.htm) — Object tree

## <a id="methodsAndProperties_messaging"></a>[Messaging](meansOfCommunication.md) (methods & properties)

- [`app:getGenesisEvents`](sim-2/app_getGenesisEvents.htm) — Retrieves events to reconstruct the app's state
- [`app:logError`](sim-2/app_logError.htm) — Outputs an error message in the status bar
- [`app:logInfo`](sim-2/app_logInfo.htm) — Outputs an information message in the status bar
- [`app:logWarn`](sim-2/app_logWarn.htm) — Outputs a warning message in the status bar
- [`app:pushEvent`](sim-2/app_pushEvent.htm) — Pushes a user event for asynchronous reception
- [`app:systemLock`](sim-2/app_systemLock.htm) — Acquires/releases a system-wide semaphore
- [`script:broadcast`](sim-2/script_broadcast.htm) — Broadcasts a message to all other scripts
- [`script:callFunction`](sim-2/script_callFunction.htm) — Calls a function
- [`script:callMethod`](sim-2/script_callMethod.htm) — Calls a method
- [`script:executeString`](sim-2/script_executeString.htm) — Executes code from a string
- [`script:getFunctions`](sim-2/script_getFunctions.htm) — Retrieves callable functions of the script
- [`script:setEventFilters`](sim-2/script_setEventFilters.htm) — Specifies filters for the sysCall_event callback
- [`app.consoleVerbosity`](sim-2/property_app_consoleVerbosity.htm) — Console verbosity
- [`app.consoleVerbosityStr`](sim-2/property_app_consoleVerbosityStr.htm) — Console verbosity string
- [`app.dialogVerbosity`](sim-2/property_app_dialogVerbosity.htm) — Dialog verbosity
- [`app.dialogVerbosityStr`](sim-2/property_app_dialogVerbosityStr.htm) — Dialog verbosity string
- [`app.notifyDeprecated`](sim-2/property_app_notifyDeprecated.htm) — Notify deprecated
- [`app.protocolVersion`](sim-2/property_app_protocolVersion.htm) — Protocol
- [`app.statusbarVerbosity`](sim-2/property_app_statusbarVerbosity.htm) — Statusbar verbosity
- [`app.statusbarVerbosityStr`](sim-2/property_app_statusbarVerbosityStr.htm) — Statusbar verbosity string
- [`sceneObject.modelAcknowledgment`](sim-2/property_sceneObject_modelAcknowledgment.htm) — Acknowledgment
- [`visionSensor.emitDepthChangedEvent`](sim-2/property_visionSensor_emitDepthChangedEvent.htm) — Emit depth change event
- [`visionSensor.emitImageChangedEvent`](sim-2/property_visionSensor_emitImageChangedEvent.htm) — Emit image change event

## <a id="methodsAndProperties_console"></a><a id="methodsAndProperties_auxiliaryConsoles"></a><a id="methodsAndProperties_auxiliaryConsoleFunctions"></a>[console](dataVisualizationAndOutput.md#auxConsoles) (methods & properties)

- [`app:createObject`](sim-2/app_createObject.htm) — Creates various objects (collections, scripts, sensors, etc.)
- [`app:removeObjects`](sim-2/app_removeObjects.htm) — Removes one or several objects
- [`console:clear`](sim-2/console_clear.htm) — Clears the console
- [`console:print`](sim-2/console_print.htm) — Prints text to the console
- [`console:remove`](sim-2/console_remove.htm) — Removes the console
- [`scene:createObject`](sim-2/scene_createObject.htm) — Creates various objects (collections, scripts, sensors, etc.)
- [`scene:removeObjects`](sim-2/scene_removeObjects.htm) — Removes one or several objects
- [`console.hiddenInSimulation`](sim-2/property_console_hiddenInSimulation.htm) — Hides during simulation
- [`console.visible`](sim-2/property_console_visible.htm) — Visible

## <a id="methodsAndProperties_textEditor"></a><a id="methodsAndProperties_textEditors"></a>[textEditor](dataVisualizationAndOutput.md#textEditors) (methods & properties)

- [`app:createObject`](sim-2/app_createObject.htm) — Creates various objects (collections, scripts, sensors, etc.)
- [`app:removeObjects`](sim-2/app_removeObjects.htm) — Removes one or several objects
- [`scene:createObject`](sim-2/scene_createObject.htm) — Creates various objects (collections, scripts, sensors, etc.)
- [`scene:removeObjects`](sim-2/scene_removeObjects.htm) — Removes one or several objects
- [`textEditor:remove`](sim-2/textEditor_remove.htm) — Removes the text editor
- [`textEditor.hiddenInSimulation`](sim-2/property_textEditor_hiddenInSimulation.htm) — Hides during simulation
- [`textEditor.visible`](sim-2/property_textEditor_visible.htm) — Visible

## <a id="methodsAndProperties_importExport"></a><a id="methodsAndProperties_importExportFunctions"></a>[Import/export](importExport.md) (methods & properties)

- [`app:loadImage`](sim-2/app_loadImage.htm) — Loads an image from file
- [`app:loadImageFromBuffer`](sim-2/app_loadImageFromBuffer.htm) — Loads an image from memory
- [`app:saveImage`](sim-2/app_saveImage.htm) — Saves an image to file
- [`app:saveImageToBuffer`](sim-2/app_saveImageToBuffer.htm) — Saves an image to a buffer
- [`app.paths.importExport`](sim-2/property_app_paths_importExport.htm) — Import/export path
- [`app.paths.scenes`](sim-2/property_app_paths_scenes.htm) — Scene path

## <a id="methodsAndProperties_Motion"></a><a id="methodsAndProperties_rml"></a><a id="methodsAndProperties_ruckig"></a>Motion functionality (methods & properties)

- [`MoveToConfig:data`](sim-2/MoveToConfig_data.htm) — Returns motion information
- [`MoveToConfig:new`](sim-2/MoveToConfig_new.htm) — Initiates an n-DoF motion using Ruckig
- [`MoveToConfig:remove`](sim-2/MoveToConfig_remove.htm) — Destroys the motion object
- [`MoveToConfig:run`](sim-2/MoveToConfig_run.htm) — Executes the motion in a thread
- [`MoveToConfig:step`](sim-2/MoveToConfig_step.htm) — Steps the motion
- [`MoveToPose:data`](sim-2/MoveToPose_data.htm) — Returns motion information
- [`MoveToPose:new`](sim-2/MoveToPose_new.htm) — Initiates pose-based motion using Ruckig
- [`MoveToPose:remove`](sim-2/MoveToPose_remove.htm) — Destroys the motion object
- [`MoveToPose:run`](sim-2/MoveToPose_run.htm) — Executes the motion in a thread
- [`MoveToPose:step`](sim-2/MoveToPose_step.htm) — Steps the motion
- [`RuckigPosition:data`](sim-2/RuckigPosition_data.htm) — Returns motion information
- [`RuckigPosition:new`](sim-2/RuckigPosition_new.htm) — Initializes a Ruckig position trajectory generator
- [`RuckigPosition:remove`](sim-2/RuckigPosition_remove.htm) — Destroys the motion object
- [`RuckigPosition:step`](sim-2/RuckigPosition_step.htm) — Steps the motion
- [`RuckigVelocity:data`](sim-2/RuckigVelocity_data.htm) — Returns motion information
- [`RuckigVelocity:new`](sim-2/RuckigVelocity_new.htm) — Initializes a Ruckig velocity trajectory generator
- [`RuckigVelocity:remove`](sim-2/RuckigVelocity_remove.htm) — Destroys the motion object
- [`RuckigVelocity:step`](sim-2/RuckigVelocity_step.htm) — Steps the motion
- [`TimeOptimalTrajectory:generate`](sim-2/TimeOptimalTrajectory_generate.htm) — Generates a time optimal trajectory
- [`TimeOptimalTrajectory:new`](sim-2/TimeOptimalTrajectory_new.htm) — Initializes a time optimal trajectory generator
- [`TimeOptimalTrajectory:remove`](sim-2/TimeOptimalTrajectory_remove.htm) — Destroys the motion object

## <a id="methodsAndProperties_MoveToConfig"></a><a id="methodsAndProperties_rml-2"></a><a id="methodsAndProperties_ruckig-2"></a>MoveToConfig (methods & properties)

- [`MoveToConfig:data`](sim-2/MoveToConfig_data.htm) — Returns motion information
- [`MoveToConfig:new`](sim-2/MoveToConfig_new.htm) — Initiates an n-DoF motion using Ruckig
- [`MoveToConfig:remove`](sim-2/MoveToConfig_remove.htm) — Destroys the motion object
- [`MoveToConfig:run`](sim-2/MoveToConfig_run.htm) — Executes the motion in a thread
- [`MoveToConfig:step`](sim-2/MoveToConfig_step.htm) — Steps the motion

## <a id="methodsAndProperties_MoveToPose"></a><a id="methodsAndProperties_rml-3"></a><a id="methodsAndProperties_ruckig-3"></a>MoveToPose (methods & properties)

- [`MoveToPose:data`](sim-2/MoveToPose_data.htm) — Returns motion information
- [`MoveToPose:new`](sim-2/MoveToPose_new.htm) — Initiates pose-based motion using Ruckig
- [`MoveToPose:remove`](sim-2/MoveToPose_remove.htm) — Destroys the motion object
- [`MoveToPose:run`](sim-2/MoveToPose_run.htm) — Executes the motion in a thread
- [`MoveToPose:step`](sim-2/MoveToPose_step.htm) — Steps the motion

## <a id="methodsAndProperties_TimeOptimalTrajectory"></a><a id="methodsAndProperties_rml-4"></a><a id="methodsAndProperties_ruckig-4"></a>TimeOptimalTrajectory (methods & properties)

- [`TimeOptimalTrajectory:generate`](sim-2/TimeOptimalTrajectory_generate.htm) — Generates a time optimal trajectory
- [`TimeOptimalTrajectory:new`](sim-2/TimeOptimalTrajectory_new.htm) — Initializes a time optimal trajectory generator
- [`TimeOptimalTrajectory:remove`](sim-2/TimeOptimalTrajectory_remove.htm) — Destroys the motion object

## <a id="methodsAndProperties_RuckigPosition"></a><a id="methodsAndProperties_rml-5"></a><a id="methodsAndProperties_ruckig-5"></a>RuckigPosition (methods & properties)

- [`RuckigPosition:data`](sim-2/RuckigPosition_data.htm) — Returns motion information
- [`RuckigPosition:new`](sim-2/RuckigPosition_new.htm) — Initializes a Ruckig position trajectory generator
- [`RuckigPosition:remove`](sim-2/RuckigPosition_remove.htm) — Destroys the motion object
- [`RuckigPosition:step`](sim-2/RuckigPosition_step.htm) — Steps the motion

## <a id="methodsAndProperties_RuckigVelocity"></a><a id="methodsAndProperties_rml-6"></a><a id="methodsAndProperties_ruckig-6"></a>RuckigVelocity (methods & properties)

- [`RuckigVelocity:data`](sim-2/RuckigVelocity_data.htm) — Returns motion information
- [`RuckigVelocity:new`](sim-2/RuckigVelocity_new.htm) — Initializes a Ruckig velocity trajectory generator
- [`RuckigVelocity:remove`](sim-2/RuckigVelocity_remove.htm) — Destroys the motion object
- [`RuckigVelocity:step`](sim-2/RuckigVelocity_step.htm) — Steps the motion

## <a id="methodsAndProperties_packing"></a>Packing/unpacking (methods & properties)

- [`app:deserialize`](sim-2/app_deserialize.htm) — Deserializes a buffer using CBOR format
- [`app:pack`](sim-2/app_pack.htm) — Packs data using CoppeliaSim format
- [`app:packArray`](sim-2/app_packArray.htm) — Packs an array of numbers as little-endian
- [`app:serialize`](sim-2/app_serialize.htm) — Serializes data using CBOR format
- [`app:transformBuffer`](sim-2/app_transformBuffer.htm) — Modifies a buffer (format, scale, offset)
- [`app:transformImage`](sim-2/app_transformImage.htm) — Transforms an image (scaling, flipping)
- [`app:unpack`](sim-2/app_unpack.htm) — Unpacks data using CoppeliaSim format
- [`app:unpackArray`](sim-2/app_unpackArray.htm) — Unpacks a buffer into an array of numbers
- [`object:getBufferProperty`](sim-2/object_getBufferProperty.htm) — Fetches a buffer property
- [`object:setBufferProperty`](sim-2/object_setBufferProperty.htm) — Sets a buffer property

## <a id="methodsAndProperties_IK"></a>[IK](kinematics.md) (methods & properties)

- [`IK:createGroup`](sim-2/IK_createGroup.htm) — Creates an IK group
- [`IK:new`](sim-2/IK_new.htm) — Creates an IK world
- [`IK:remove`](sim-2/IK_remove.htm) — Removes the IK world
- [`IK:solve`](sim-2/IK_solve.htm) — Solves all enabled IK groups
- [`IK:syncFromScene`](sim-2/IK_syncFromScene.htm) — Synchronizes IK world from the simulation world
- [`IK:syncToScene`](sim-2/IK_syncToScene.htm) — Synchronizes simulation world from the IK world
- [`IK.groupList`](sim-2/property_IK_groupList.htm)
- [`IK.joints`](sim-2/property_IK_joints.htm)
- [`IK.objects`](sim-2/property_IK_objects.htm)

## <a id="methodsAndProperties_IKObject"></a>[IKObject](solvingIkAndFk.md) (methods & properties)

- [`IKObject:getPose`](sim-2/IKObject_getPose.htm) — Retrieves the IK object's pose
- [`IKObject:getPosition`](sim-2/IKObject_getPosition.htm) — Retrieves the IK object's position
- [`IKObject:getQuaternion`](sim-2/IKObject_getQuaternion.htm) — Retrieves the IK object's quaternion
- [`IKObject:setPose`](sim-2/IKObject_setPose.htm) — Sets the IK object's pose
- [`IKObject:setPosition`](sim-2/IKObject_setPosition.htm) — Sets the IK object's position
- [`IKObject:setQuaternion`](sim-2/IKObject_setQuaternion.htm) — Sets the IK object's quaternion
- [`IKObject.sceneObjectHandle`](sim-2/property_IKObject_sceneObjectHandle.htm)
- [`IKObject.type`](sim-2/property_IKObject_type.htm)

## <a id="methodsAndProperties_IKJoint"></a>[IKjoint](solvingIkAndFk.md) (methods & properties)

- [`IKJoint.bounds`](sim-2/property_IKJoint_bounds.htm)
- [`IKJoint.jointConfiguration`](sim-2/property_IKJoint_jointConfiguration.htm)
- [`IKJoint.jointPosition`](sim-2/property_IKJoint_jointPosition.htm)
- [`IKJoint.jointQuaternion`](sim-2/property_IKJoint_jointQuaternion.htm)
- [`IKJoint.jointType`](sim-2/property_IKJoint_jointType.htm)
- [`IKJoint.limitMargin`](sim-2/property_IKJoint_limitMargin.htm)
- [`IKJoint.maxStepSize`](sim-2/property_IKJoint_maxStepSize.htm)
- [`IKJoint.passive`](sim-2/property_IKJoint_passive.htm)
- [`IKJoint.weight`](sim-2/property_IKJoint_weight.htm)

## <a id="methodsAndProperties_IKGroup"></a>[IKGroup](solvingIkAndFk.md) (methods & properties)

- [`IKGroup:addElementFromScene`](sim-2/IKGroup_addElementFromScene.htm) — Creates an IK element from the simulation world
- [`IKGroup:computeJacobian`](sim-2/IKGroup_computeJacobian.htm) — Computes the Jacobian and error vector
- [`IKGroup:findConfig`](sim-2/IKGroup_findConfig.htm) — Searches for joint configurations satisfying target poses
- [`IKGroup:solve`](sim-2/IKGroup_solve.htm) — Solves the IK group's constraints
- [`IKGroup:syncFromScene`](sim-2/IKGroup_syncFromScene.htm) — Synchronizes this IK group from the simulation world
- [`IKGroup:syncToScene`](sim-2/IKGroup_syncToScene.htm) — Synchronizes simulation world from this IK group
- [`IKGroup.damping`](sim-2/property_IKGroup_damping.htm)
- [`IKGroup.elementList`](sim-2/property_IKGroup_elementList.htm)
- [`IKGroup.enabled`](sim-2/property_IKGroup_enabled.htm)
- [`IKGroup.maxIterations`](sim-2/property_IKGroup_maxIterations.htm)
- [`IKGroup.method`](sim-2/property_IKGroup_method.htm)

## <a id="methodsAndProperties_IKElement"></a>[IKElement](solvingIkAndFk.md) (methods & properties)

- [`IKElement.base`](sim-2/property_IKElement_base.htm)
- [`IKElement.constraints`](sim-2/property_IKElement_constraints.htm)
- [`IKElement.enabled`](sim-2/property_IKElement_enabled.htm)
- [`IKElement.jointList`](sim-2/property_IKElement_jointList.htm)
- [`IKElement.precision`](sim-2/property_IKElement_precision.htm)
- [`IKElement.target`](sim-2/property_IKElement_target.htm)
- [`IKElement.tip`](sim-2/property_IKElement_tip.htm)
- [`IKElement.weights`](sim-2/property_IKElement_weights.htm)

## <a id="methodsAndProperties_other"></a>Other (methods & properties)

- [`app:fastIdleLoop`](sim-2/app_fastIdleLoop.htm) — Speeds up the idle loop for reactivity
- [`app:getEnumInfo`](sim-2/app_getEnumInfo.htm) — Returns information about an enum
- [`app:getPluginInfo`](sim-2/app_getPluginInfo.htm) — Returns information about a loaded plugin
- [`app:openFile`](sim-2/app_openFile.htm) — Opens a file in a subprocess
- [`app:quit`](sim-2/app_quit.htm) — Triggers a quit signal for the application
- [`app:setPluginInfo`](sim-2/app_setPluginInfo.htm) — Modifies information of a loaded plugin
- [`object:isValid`](sim-2/object_isValid.htm) — Checks if the object is valid
- [`scene:announceChange`](sim-2/scene_announceChange.htm) — Announces a change in the scene for undo/redo
- [`scene:stepKinematicJoints`](sim-2/scene_stepKinematicJoints.htm) — Steps all kinematic mode joints
- [`script:setModuleEntry`](sim-2/script_setModuleEntry.htm) — Creates/modifies/destroys module menu entries

## <a id="methodsAndProperties_drawingObject"></a>drawingObject (deprecated, see marker instead) (methods & properties)

- [`drawingObject.appendColors`](sim-2/property_drawingObject_appendColors.htm)
- [`drawingObject.appendPoints`](sim-2/property_drawingObject_appendPoints.htm)
- [`drawingObject.appendQuaternions`](sim-2/property_drawingObject_appendQuaternions.htm)
- [`drawingObject.colors`](sim-2/property_drawingObject_colors.htm)
- [`drawingObject.cyclic`](sim-2/property_drawingObject_cyclic.htm)
- [`drawingObject.itemType`](sim-2/property_drawingObject_itemType.htm)
- [`drawingObject.maxCnt`](sim-2/property_drawingObject_maxCnt.htm)
- [`drawingObject.overlay`](sim-2/property_drawingObject_overlay.htm)
- [`drawingObject.parent`](sim-2/property_drawingObject_parent.htm) — Parent
- [`drawingObject.parentUid`](sim-2/property_drawingObject_parentUid.htm)
- [`drawingObject.points`](sim-2/property_drawingObject_points.htm)
- [`drawingObject.quaternions`](sim-2/property_drawingObject_quaternions.htm)
- [`drawingObject.size`](sim-2/property_drawingObject_size.htm)

---

## <a id="functions_c_main"></a>Main (C-functions)

- [`simCallMethod`](sim/simCallMethod_cpp.htm)
- [`simCreateBuffer`](sim/simCreateBuffer_cpp.htm)
- [`simGetLastError`](sim/simGetLastError_cpp.htm)
- [`simReleaseBuffer`](sim/simReleaseBuffer_cpp.htm)
- [`simSetLastError`](sim/simSetLastError_cpp.htm)

## <a id="functions_c_property"></a>[Properties](properties.md) (C-functions)

- [`simGetBoolProperty`](sim/simGetBoolProperty_cpp.htm)
- [`simGetBufferProperty`](sim/simGetBufferProperty_cpp.htm)
- [`simGetColor4Property`](sim/simGetColor4Property_cpp.htm)
- [`simGetFloatArrayProperty`](sim/simGetFloatArrayProperty_cpp.htm)
- [`simGetFloatProperty`](sim/simGetFloatProperty_cpp.htm)
- [`simGetHandleArrayProperty`](sim/simGetHandleArrayProperty_cpp.htm)
- [`simGetHandleProperty`](sim/simGetHandleProperty_cpp.htm)
- [`simGetIntArrayProperty`](sim/simGetIntArrayProperty_cpp.htm)
- [`simGetIntProperty`](sim/simGetIntProperty_cpp.htm)
- [`simGetLongProperty`](sim/simGetLongProperty_cpp.htm)
- [`simGetMatrixProperty`](sim/simGetMatrixProperty_cpp.htm)
- [`simGetMethodProperty`](sim/simGetMethodProperty_cpp.htm)
- [`simGetPoseProperty`](sim/simGetPoseProperty_cpp.htm)
- [`simGetPropertyInfo`](sim/simGetPropertyInfo_cpp.htm)
- [`simGetPropertyName`](sim/simGetPropertyName_cpp.htm)
- [`simGetQuaternionProperty`](sim/simGetQuaternionProperty_cpp.htm)
- [`simGetStringArrayProperty`](sim/simGetStringArrayProperty_cpp.htm)
- [`simGetStringProperty`](sim/simGetStringProperty_cpp.htm)
- [`simGetTableProperty`](sim/simGetTableProperty_cpp.htm)
- [`simGetVector3Property`](sim/simGetVector3Property_cpp.htm)
- [`simRemoveProperty`](sim/simRemoveProperty_cpp.htm)
- [`simSetBoolProperty`](sim/simSetBoolProperty_cpp.htm)
- [`simSetBufferProperty`](sim/simSetBufferProperty_cpp.htm)
- [`simSetColor4Property`](sim/simSetColor4Property_cpp.htm)
- [`simSetFloatArrayProperty`](sim/simSetFloatArrayProperty_cpp.htm)
- [`simSetFloatProperty`](sim/simSetFloatProperty_cpp.htm)
- [`simSetHandleArrayProperty`](sim/simSetHandleArrayProperty_cpp.htm)
- [`simSetHandleProperty`](sim/simSetHandleProperty_cpp.htm)
- [`simSetIntArrayProperty`](sim/simSetIntArrayProperty_cpp.htm)
- [`simSetIntProperty`](sim/simSetIntProperty_cpp.htm)
- [`simSetLongProperty`](sim/simSetLongProperty_cpp.htm)
- [`simSetMatrixProperty`](sim/simSetMatrixProperty_cpp.htm)
- [`simSetMethodProperty`](sim/simSetMethodProperty_cpp.htm)
- [`simSetPoseProperty`](sim/simSetPoseProperty_cpp.htm)
- [`simSetPropertyInfo`](sim/simSetPropertyInfo_cpp.htm)
- [`simSetQuaternionProperty`](sim/simSetQuaternionProperty_cpp.htm)
- [`simSetStringArrayProperty`](sim/simSetStringArrayProperty_cpp.htm)
- [`simSetStringProperty`](sim/simSetStringProperty_cpp.htm)
- [`simSetTableProperty`](sim/simSetTableProperty_cpp.htm)
- [`simSetVector3Property`](sim/simSetVector3Property_cpp.htm)

## <a id="functions_c_stack"></a>Stack (C-functions)

- [`simCallMethod`](sim/simCallMethod_cpp.htm)
- [`simCopyStack`](sim/simCopyStack_cpp.htm)
- [`simCreateStack`](sim/simCreateStack_cpp.htm)
- [`simDebugStack`](sim/simDebugStack_cpp.htm)
- [`simGetStackBoolValue`](sim/simGetStackBoolValue_cpp.htm)
- [`simGetStackColor4`](sim/simGetStackColor4_cpp.htm)
- [`simGetStackDoubleTable`](sim/simGetStackDoubleTable_cpp.htm)
- [`simGetStackDoubleValue`](sim/simGetStackDoubleValue_cpp.htm)
- [`simGetStackFloatTable`](sim/simGetStackFloatTable_cpp.htm)
- [`simGetStackFloatValue`](sim/simGetStackFloatValue_cpp.htm)
- [`simGetStackInt32Table`](sim/simGetStackInt32Table_cpp.htm)
- [`simGetStackInt32Value`](sim/simGetStackInt32Value_cpp.htm)
- [`simGetStackInt64Table`](sim/simGetStackInt64Table_cpp.htm)
- [`simGetStackInt64Value`](sim/simGetStackInt64Value_cpp.htm)
- [`simGetStackItemType`](sim/simGetStackItemType_cpp.htm)
- [`simGetStackMatrix`](sim/simGetStackMatrix_cpp.htm)
- [`simGetStackPose`](sim/simGetStackPose_cpp.htm)
- [`simGetStackQuaternion`](sim/simGetStackQuaternion_cpp.htm)
- [`simGetStackSize`](sim/simGetStackSize_cpp.htm)
- [`simGetStackStringType`](sim/simGetStackStringType_cpp.htm)
- [`simGetStackStringValue`](sim/simGetStackStringValue_cpp.htm)
- [`simGetStackTableInfo`](sim/simGetStackTableInfo_cpp.htm)
- [`simGetStackUInt8Table`](sim/simGetStackUInt8Table_cpp.htm)
- [`simInsertDataIntoStackTable`](sim/simInsertDataIntoStackTable_cpp.htm)
- [`simMoveStackItemToTop`](sim/simMoveStackItemToTop_cpp.htm)
- [`simPackTable`](sim/simPackTable_cpp.htm)
- [`simPopStackItem`](sim/simPopStackItem_cpp.htm)
- [`simPushBoolOntoStack`](sim/simPushBoolOntoStack_cpp.htm)
- [`simPushBufferOntoStack`](sim/simPushBufferOntoStack_cpp.htm)
- [`simPushColor4OntoStack`](sim/simPushColor4OntoStack_cpp.htm)
- [`simPushDoubleOntoStack`](sim/simPushDoubleOntoStack_cpp.htm)
- [`simPushDoubleTableOntoStack`](sim/simPushDoubleTableOntoStack_cpp.htm)
- [`simPushFloatOntoStack`](sim/simPushFloatOntoStack_cpp.htm)
- [`simPushFloatTableOntoStack`](sim/simPushFloatTableOntoStack_cpp.htm)
- [`simPushInt32OntoStack`](sim/simPushInt32OntoStack_cpp.htm)
- [`simPushInt32TableOntoStack`](sim/simPushInt32TableOntoStack_cpp.htm)
- [`simPushInt64OntoStack`](sim/simPushInt64OntoStack_cpp.htm)
- [`simPushInt64TableOntoStack`](sim/simPushInt64TableOntoStack_cpp.htm)
- [`simPushMatrixOntoStack`](sim/simPushMatrixOntoStack_cpp.htm)
- [`simPushNullOntoStack`](sim/simPushNullOntoStack_cpp.htm)
- [`simPushPoseOntoStack`](sim/simPushPoseOntoStack_cpp.htm)
- [`simPushQuaternionOntoStack`](sim/simPushQuaternionOntoStack_cpp.htm)
- [`simPushStringOntoStack`](sim/simPushStringOntoStack_cpp.htm)
- [`simPushTableOntoStack`](sim/simPushTableOntoStack_cpp.htm)
- [`simPushTextOntoStack`](sim/simPushTextOntoStack_cpp.htm)
- [`simPushUInt8TableOntoStack`](sim/simPushUInt8TableOntoStack_cpp.htm)
- [`simReleaseStack`](sim/simReleaseStack_cpp.htm)
- [`simUnfoldStackTable`](sim/simUnfoldStackTable_cpp.htm)
- [`simUnpackTable`](sim/simUnpackTable_cpp.htm)

## <a id="functions_c_aux"></a>Auxiliary functions (C-functions)

- [`simAddForce`](sim/simAddForce_cpp.htm)
- [`simAddForceAndTorque`](sim/simAddForceAndTorque_cpp.htm)
- [`simAddGraphCurve`](sim/simAddGraphCurve_cpp.htm)
- [`simAddGraphStream`](sim/simAddGraphStream_cpp.htm)
- [`simAddItemToCollection`](sim/simAddItemToCollection_cpp.htm)
- [`simAddLog`](sim/simAddLog_cpp.htm)
- [`simAdjustView`](sim/simAdjustView_cpp.htm)
- [`simAlignShapeBB`](sim/simAlignShapeBB_cpp.htm)
- [`simAnnounceSceneContentChange`](sim/simAnnounceSceneContentChange_cpp.htm)
- [`simApplyTexture`](sim/simApplyTexture_cpp.htm)
- [`simBuildMatrix`](sim/simBuildMatrix_cpp.htm)
- [`simBuildPose`](sim/simBuildPose_cpp.htm)
- [`simCallScriptFunctionEx`](sim/simCallScriptFunctionEx_cpp.htm)
- [`simCameraFitToView`](sim/simCameraFitToView_cpp.htm)
- [`simCheckCollision`](sim/simCheckCollision_cpp.htm)
- [`simCheckDistance`](sim/simCheckDistance_cpp.htm)
- [`simCheckOctreePointOccupancy`](sim/simCheckOctreePointOccupancy_cpp.htm)
- [`simCheckProximitySensor`](sim/simCheckProximitySensor_cpp.htm)
- [`simCheckVisionSensor`](sim/simCheckVisionSensor_cpp.htm)
- [`simCheckVisionSensorEx`](sim/simCheckVisionSensorEx_cpp.htm)
- [`simCloseScene`](sim/simCloseScene_cpp.htm)
- [`simComputeMassAndInertia`](sim/simComputeMassAndInertia_cpp.htm)
- [`simConvexDecompose`](sim/simConvexDecompose_cpp.htm)
- [`simCopyPasteObjects`](sim/simCopyPasteObjects_cpp.htm)
- [`simCreateCollectionEx`](sim/simCreateCollectionEx_cpp.htm)
- [`simCreateDummy`](sim/simCreateDummy_cpp.htm)
- [`simCreateForceSensor`](sim/simCreateForceSensor_cpp.htm)
- [`simCreateHeightfieldShape`](sim/simCreateHeightfieldShape_cpp.htm)
- [`simCreateJoint`](sim/simCreateJoint_cpp.htm)
- [`simCreateOctree`](sim/simCreateOctree_cpp.htm)
- [`simCreatePointCloud`](sim/simCreatePointCloud_cpp.htm)
- [`simCreatePrimitiveShape`](sim/simCreatePrimitiveShape_cpp.htm)
- [`simCreateProximitySensor`](sim/simCreateProximitySensor_cpp.htm)
- [`simCreateScript`](sim/simCreateScript_cpp.htm)
- [`simCreateShape`](sim/simCreateShape_cpp.htm)
- [`simCreateTexture`](sim/simCreateTexture_cpp.htm)
- [`simCreateVisionSensor`](sim/simCreateVisionSensor_cpp.htm)
- [`simDestroyCollection`](sim/simDestroyCollection_cpp.htm)
- [`simDestroyGraphCurve`](sim/simDestroyGraphCurve_cpp.htm)
- [`simDoesFileExist`](sim/simDoesFileExist_cpp.htm)
- [`simDuplicateGraphCurveToStatic`](sim/simDuplicateGraphCurveToStatic_cpp.htm)
- [`simExecuteScriptString`](sim/simExecuteScriptString_cpp.htm)
- [`simExportMesh`](sim/simExportMesh_cpp.htm)
- [`simFloatingViewAdd`](sim/simFloatingViewAdd_cpp.htm)
- [`simFloatingViewRemove`](sim/simFloatingViewRemove_cpp.htm)
- [`simGenerateShapeFromPath`](sim/simGenerateShapeFromPath_cpp.htm)
- [`simGetApiFunc`](sim/simGetApiFunc_cpp.htm)
- [`simGetApiInfo`](sim/simGetApiInfo_cpp.htm)
- [`simGetClosestPosOnPath`](sim/simGetClosestPosOnPath_cpp.htm)
- [`simGetCollectionObjects`](sim/simGetCollectionObjects_cpp.htm)
- [`simGetContactInfo`](sim/simGetContactInfo_cpp.htm)
- [`simGetDecimatedMesh`](sim/simGetDecimatedMesh_cpp.htm)
- [`simGetEulerAnglesFromMatrix`](sim/simGetEulerAnglesFromMatrix_cpp.htm)
- [`simGetExplicitHandling`](sim/simGetExplicitHandling_cpp.htm)
- [`simGetExtensionString`](sim/simGetExtensionString_cpp.htm)
- [`simGetJointDependency`](sim/simGetJointDependency_cpp.htm)
- [`simGetJointForce`](sim/simGetJointForce_cpp.htm)
- [`simGetJointInterval`](sim/simGetJointInterval_cpp.htm)
- [`simGetJointMode`](sim/simGetJointMode_cpp.htm)
- [`simGetJointPosition`](sim/simGetJointPosition_cpp.htm)
- [`simGetJointTargetForce`](sim/simGetJointTargetForce_cpp.htm)
- [`simGetJointTargetPosition`](sim/simGetJointTargetPosition_cpp.htm)
- [`simGetJointTargetVelocity`](sim/simGetJointTargetVelocity_cpp.htm)
- [`simGetJointType`](sim/simGetJointType_cpp.htm)
- [`simGetJointVelocity`](sim/simGetJointVelocity_cpp.htm)
- [`simGetLastInfo`](sim/simGetLastInfo_cpp.htm)
- [`simGetLinkDummy`](sim/simGetLinkDummy_cpp.htm)
- [`simGetMainWindow`](sim/simGetMainWindow_cpp.htm)
- [`simGetNavigationMode`](sim/simGetNavigationMode_cpp.htm)
- [`simGetObject`](sim/simGetObject_cpp.htm)
- [`simGetObjectAlias`](sim/simGetObjectAlias_cpp.htm)
- [`simGetObjectChild`](sim/simGetObjectChild_cpp.htm)
- [`simGetObjectChildPose`](sim/simGetObjectChildPose_cpp.htm)
- [`simGetObjectColor`](sim/simGetObjectColor_cpp.htm)
- [`simGetObjectHierarchyOrder`](sim/simGetObjectHierarchyOrder_cpp.htm)
- [`simGetObjectMatrix`](sim/simGetObjectMatrix_cpp.htm)
- [`simGetObjectOrientation`](sim/simGetObjectOrientation_cpp.htm)
- [`simGetObjectParent`](sim/simGetObjectParent_cpp.htm)
- [`simGetObjectPose`](sim/simGetObjectPose_cpp.htm)
- [`simGetObjectPosition`](sim/simGetObjectPosition_cpp.htm)
- [`simGetObjectQuaternion`](sim/simGetObjectQuaternion_cpp.htm)
- [`simGetObjectSel`](sim/simGetObjectSel_cpp.htm)
- [`simGetObjectType`](sim/simGetObjectType_cpp.htm)
- [`simGetObjectUid`](sim/simGetObjectUid_cpp.htm)
- [`simGetObjectVelocity`](sim/simGetObjectVelocity_cpp.htm)
- [`simGetObjectfromUid`](sim/simGetObjectfromUid_cpp.htm)
- [`simGetObjects`](sim/simGetObjects_cpp.htm)
- [`simGetObjectsInTree`](sim/simGetObjectsInTree_cpp.htm)
- [`simGetOctreeVoxels`](sim/simGetOctreeVoxels_cpp.htm)
- [`simGetPage`](sim/simGetPage_cpp.htm)
- [`simGetPluginInfo`](sim/simGetPluginInfo_cpp.htm)
- [`simGetPointCloudOptions`](sim/simGetPointCloudOptions_cpp.htm)
- [`simGetPointCloudPoints`](sim/simGetPointCloudPoints_cpp.htm)
- [`simGetQHull`](sim/simGetQHull_cpp.htm)
- [`simGetReferencedHandles`](sim/simGetReferencedHandles_cpp.htm)
- [`simGetRotationAxis`](sim/simGetRotationAxis_cpp.htm)
- [`simGetScaledImage`](sim/simGetScaledImage_cpp.htm)
- [`simGetScriptHandleEx`](sim/simGetScriptHandleEx_cpp.htm)
- [`simGetShapeColor`](sim/simGetShapeColor_cpp.htm)
- [`simGetShapeGeomInfo`](sim/simGetShapeGeomInfo_cpp.htm)
- [`simGetShapeInertia`](sim/simGetShapeInertia_cpp.htm)
- [`simGetShapeMass`](sim/simGetShapeMass_cpp.htm)
- [`simGetShapeMesh`](sim/simGetShapeMesh_cpp.htm)
- [`simGetShapeTextureId`](sim/simGetShapeTextureId_cpp.htm)
- [`simGetShapeViz`](sim/simGetShapeViz_cpp.htm)
- [`simGetSimulationState`](sim/simGetSimulationState_cpp.htm)
- [`simGetSimulationTime`](sim/simGetSimulationTime_cpp.htm)
- [`simGetSimulationTimeStep`](sim/simGetSimulationTimeStep_cpp.htm)
- [`simGetSimulatorMessage`](sim/simGetSimulatorMessage_cpp.htm)
- [`simGetTextureId`](sim/simGetTextureId_cpp.htm)
- [`simGetVelocity`](sim/simGetVelocity_cpp.htm)
- [`simGetVisionSensorDepth`](sim/simGetVisionSensorDepth_cpp.htm)
- [`simGetVisionSensorImg`](sim/simGetVisionSensorImg_cpp.htm)
- [`simGetVisionSensorRes`](sim/simGetVisionSensorRes_cpp.htm)
- [`simGroupShapes`](sim/simGroupShapes_cpp.htm)
- [`simHandleDynamics`](sim/simHandleDynamics_cpp.htm)
- [`simHandleGraph`](sim/simHandleGraph_cpp.htm)
- [`simHandleProximitySensor`](sim/simHandleProximitySensor_cpp.htm)
- [`simHandleVisionSensor`](sim/simHandleVisionSensor_cpp.htm)
- [`simImportMesh`](sim/simImportMesh_cpp.htm)
- [`simImportShape`](sim/simImportShape_cpp.htm)
- [`simInitScript`](sim/simInitScript_cpp.htm)
- [`simInsertObjectIntoOctree`](sim/simInsertObjectIntoOctree_cpp.htm)
- [`simInsertObjectIntoPointCloud`](sim/simInsertObjectIntoPointCloud_cpp.htm)
- [`simInsertPointsIntoPointCloud`](sim/simInsertPointsIntoPointCloud_cpp.htm)
- [`simInsertVoxelsIntoOctree`](sim/simInsertVoxelsIntoOctree_cpp.htm)
- [`simIntersectPointsWithPointCloud`](sim/simIntersectPointsWithPointCloud_cpp.htm)
- [`simInvertMatrix`](sim/simInvertMatrix_cpp.htm)
- [`simInvertPose`](sim/simInvertPose_cpp.htm)
- [`simIsDynamicallyEnabled`](sim/simIsDynamicallyEnabled_cpp.htm)
- [`simIsHandle`](sim/simIsHandle_cpp.htm)
- [`simLoadImage`](sim/simLoadImage_cpp.htm)
- [`simLoadModel`](sim/simLoadModel_cpp.htm)
- [`simLoadScene`](sim/simLoadScene_cpp.htm)
- [`simMatrixToPose`](sim/simMatrixToPose_cpp.htm)
- [`simModuleEntry`](sim/simModuleEntry_cpp.htm)
- [`simMultiplyMatrices`](sim/simMultiplyMatrices_cpp.htm)
- [`simMultiplyPoses`](sim/simMultiplyPoses_cpp.htm)
- [`simOpenTextEditor`](sim/simOpenTextEditor_cpp.htm)
- [`simPackTable`](sim/simPackTable_cpp.htm)
- [`simPauseSimulation`](sim/simPauseSimulation_cpp.htm)
- [`simPoseToMatrix`](sim/simPoseToMatrix_cpp.htm)
- [`simQuitSimulator`](sim/simQuitSimulator_cpp.htm)
- [`simReadForceSensor`](sim/simReadForceSensor_cpp.htm)
- [`simReadProximitySensor`](sim/simReadProximitySensor_cpp.htm)
- [`simReadTexture`](sim/simReadTexture_cpp.htm)
- [`simReadVisionSensor`](sim/simReadVisionSensor_cpp.htm)
- [`simRefreshDialogs`](sim/simRefreshDialogs_cpp.htm)
- [`simRegisterScriptCallbackFunction`](sim/simRegisterScriptCallbackFunction_cpp.htm)
- [`simRegisterScriptFuncHook`](sim/simRegisterScriptFuncHook_cpp.htm)
- [`simRegisterScriptVariable`](sim/simRegisterScriptVariable_cpp.htm)
- [`simRelocateShapeFrame`](sim/simRelocateShapeFrame_cpp.htm)
- [`simRemoveModel`](sim/simRemoveModel_cpp.htm)
- [`simRemoveObjects`](sim/simRemoveObjects_cpp.htm)
- [`simRemovePointsFromPointCloud`](sim/simRemovePointsFromPointCloud_cpp.htm)
- [`simRemoveVoxelsFromOctree`](sim/simRemoveVoxelsFromOctree_cpp.htm)
- [`simResetDynamicObject`](sim/simResetDynamicObject_cpp.htm)
- [`simResetGraph`](sim/simResetGraph_cpp.htm)
- [`simResetProximitySensor`](sim/simResetProximitySensor_cpp.htm)
- [`simResetScript`](sim/simResetScript_cpp.htm)
- [`simResetVisionSensor`](sim/simResetVisionSensor_cpp.htm)
- [`simRotateAroundAxis`](sim/simRotateAroundAxis_cpp.htm)
- [`simRuckigPos`](sim/simRuckigPos_cpp.htm)
- [`simRuckigRemove`](sim/simRuckigRemove_cpp.htm)
- [`simRuckigStep`](sim/simRuckigStep_cpp.htm)
- [`simRuckigVel`](sim/simRuckigVel_cpp.htm)
- [`simSaveImage`](sim/simSaveImage_cpp.htm)
- [`simSaveModel`](sim/simSaveModel_cpp.htm)
- [`simSaveScene`](sim/simSaveScene_cpp.htm)
- [`simScaleObject`](sim/simScaleObject_cpp.htm)
- [`simScaleObjects`](sim/simScaleObjects_cpp.htm)
- [`simSetExplicitHandling`](sim/simSetExplicitHandling_cpp.htm)
- [`simSetGraphStreamTransformation`](sim/simSetGraphStreamTransformation_cpp.htm)
- [`simSetGraphStreamValue`](sim/simSetGraphStreamValue_cpp.htm)
- [`simSetJointDependency`](sim/simSetJointDependency_cpp.htm)
- [`simSetJointInterval`](sim/simSetJointInterval_cpp.htm)
- [`simSetJointMode`](sim/simSetJointMode_cpp.htm)
- [`simSetJointPosition`](sim/simSetJointPosition_cpp.htm)
- [`simSetJointTargetForce`](sim/simSetJointTargetForce_cpp.htm)
- [`simSetJointTargetPosition`](sim/simSetJointTargetPosition_cpp.htm)
- [`simSetJointTargetVelocity`](sim/simSetJointTargetVelocity_cpp.htm)
- [`simSetLinkDummy`](sim/simSetLinkDummy_cpp.htm)
- [`simSetNavigationMode`](sim/simSetNavigationMode_cpp.htm)
- [`simSetObjectAlias`](sim/simSetObjectAlias_cpp.htm)
- [`simSetObjectChildPose`](sim/simSetObjectChildPose_cpp.htm)
- [`simSetObjectColor`](sim/simSetObjectColor_cpp.htm)
- [`simSetObjectHierarchyOrder`](sim/simSetObjectHierarchyOrder_cpp.htm)
- [`simSetObjectMatrix`](sim/simSetObjectMatrix_cpp.htm)
- [`simSetObjectOrientation`](sim/simSetObjectOrientation_cpp.htm)
- [`simSetObjectParent`](sim/simSetObjectParent_cpp.htm)
- [`simSetObjectPose`](sim/simSetObjectPose_cpp.htm)
- [`simSetObjectPosition`](sim/simSetObjectPosition_cpp.htm)
- [`simSetObjectQuaternion`](sim/simSetObjectQuaternion_cpp.htm)
- [`simSetObjectSel`](sim/simSetObjectSel_cpp.htm)
- [`simSetPage`](sim/simSetPage_cpp.htm)
- [`simSetPluginInfo`](sim/simSetPluginInfo_cpp.htm)
- [`simSetPointCloudOptions`](sim/simSetPointCloudOptions_cpp.htm)
- [`simSetReferencedHandles`](sim/simSetReferencedHandles_cpp.htm)
- [`simSetShapeColor`](sim/simSetShapeColor_cpp.htm)
- [`simSetShapeInertia`](sim/simSetShapeInertia_cpp.htm)
- [`simSetShapeMass`](sim/simSetShapeMass_cpp.htm)
- [`simSetShapeTexture`](sim/simSetShapeTexture_cpp.htm)
- [`simSetVisionSensorImg`](sim/simSetVisionSensorImg_cpp.htm)
- [`simStartSimulation`](sim/simStartSimulation_cpp.htm)
- [`simStopSimulation`](sim/simStopSimulation_cpp.htm)
- [`simSubtractObjectFromOctree`](sim/simSubtractObjectFromOctree_cpp.htm)
- [`simSubtractObjectFromPointCloud`](sim/simSubtractObjectFromPointCloud_cpp.htm)
- [`simTransformImage`](sim/simTransformImage_cpp.htm)
- [`simTransformVector`](sim/simTransformVector_cpp.htm)
- [`simUngroupShape`](sim/simUngroupShape_cpp.htm)
- [`simUnpackTable`](sim/simUnpackTable_cpp.htm)
- [`simWriteTexture`](sim/simWriteTexture_cpp.htm)

## <a id="functions_collection"></a><a id="collections"></a>[collection](collections.md) (C-functions)

- [`simAddItemToCollection`](sim/simAddItemToCollection_cpp.htm)
- [`simCreateCollectionEx`](sim/simCreateCollectionEx_cpp.htm)
- [`simDestroyCollection`](sim/simDestroyCollection_cpp.htm)
- [`simGetCollectionObjects`](sim/simGetCollectionObjects_cpp.htm)

## <a id="functions_textureData"></a><a id="textures"></a>[textureData](textureDialog.md) (C-functions)

- [`simApplyTexture`](sim/simApplyTexture_cpp.htm)
- [`simCreateTexture`](sim/simCreateTexture_cpp.htm)
- [`simGetScaledImage`](sim/simGetScaledImage_cpp.htm)
- [`simGetShapeTextureId`](sim/simGetShapeTextureId_cpp.htm)
- [`simGetTextureId`](sim/simGetTextureId_cpp.htm)
- [`simLoadImage`](sim/simLoadImage_cpp.htm)
- [`simReadTexture`](sim/simReadTexture_cpp.htm)
- [`simSaveImage`](sim/simSaveImage_cpp.htm)
- [`simSetShapeTexture`](sim/simSetShapeTexture_cpp.htm)
- [`simTransformImage`](sim/simTransformImage_cpp.htm)
- [`simWriteTexture`](sim/simWriteTexture_cpp.htm)

## <a id="functions_sceneObject"></a><a id="sceneObjectFunctionality"></a>[sceneObject](objects.md) (C-functions)

- [`simCopyPasteObjects`](sim/simCopyPasteObjects_cpp.htm)
- [`simGetObject`](sim/simGetObject_cpp.htm)
- [`simGetObjectAlias`](sim/simGetObjectAlias_cpp.htm)
- [`simGetObjectChild`](sim/simGetObjectChild_cpp.htm)
- [`simGetObjectColor`](sim/simGetObjectColor_cpp.htm)
- [`simGetObjectHierarchyOrder`](sim/simGetObjectHierarchyOrder_cpp.htm)
- [`simGetObjectMatrix`](sim/simGetObjectMatrix_cpp.htm)
- [`simGetObjectOrientation`](sim/simGetObjectOrientation_cpp.htm)
- [`simGetObjectParent`](sim/simGetObjectParent_cpp.htm)
- [`simGetObjectPose`](sim/simGetObjectPose_cpp.htm)
- [`simGetObjectPosition`](sim/simGetObjectPosition_cpp.htm)
- [`simGetObjectQuaternion`](sim/simGetObjectQuaternion_cpp.htm)
- [`simGetObjectSel`](sim/simGetObjectSel_cpp.htm)
- [`simGetObjectType`](sim/simGetObjectType_cpp.htm)
- [`simGetObjectUid`](sim/simGetObjectUid_cpp.htm)
- [`simGetObjectVelocity`](sim/simGetObjectVelocity_cpp.htm)
- [`simGetObjects`](sim/simGetObjects_cpp.htm)
- [`simGetObjectsInTree`](sim/simGetObjectsInTree_cpp.htm)
- [`simGetReferencedHandles`](sim/simGetReferencedHandles_cpp.htm)
- [`simIsDynamicallyEnabled`](sim/simIsDynamicallyEnabled_cpp.htm)
- [`simIsHandle`](sim/simIsHandle_cpp.htm)
- [`simRemoveModel`](sim/simRemoveModel_cpp.htm)
- [`simRemoveObjects`](sim/simRemoveObjects_cpp.htm)
- [`simScaleObject`](sim/simScaleObject_cpp.htm)
- [`simScaleObjects`](sim/simScaleObjects_cpp.htm)
- [`simSetObjectAlias`](sim/simSetObjectAlias_cpp.htm)
- [`simSetObjectColor`](sim/simSetObjectColor_cpp.htm)
- [`simSetObjectHierarchyOrder`](sim/simSetObjectHierarchyOrder_cpp.htm)
- [`simSetObjectMatrix`](sim/simSetObjectMatrix_cpp.htm)
- [`simSetObjectOrientation`](sim/simSetObjectOrientation_cpp.htm)
- [`simSetObjectParent`](sim/simSetObjectParent_cpp.htm)
- [`simSetObjectPose`](sim/simSetObjectPose_cpp.htm)
- [`simSetObjectPosition`](sim/simSetObjectPosition_cpp.htm)
- [`simSetObjectQuaternion`](sim/simSetObjectQuaternion_cpp.htm)
- [`simSetObjectSel`](sim/simSetObjectSel_cpp.htm)
- [`simSetReferencedHandles`](sim/simSetReferencedHandles_cpp.htm)

## <a id="functions_shape"></a><a id="shapeObject"></a>[shape](shapes.md) (C-functions)

- [`simAddForce`](sim/simAddForce_cpp.htm)
- [`simAddForceAndTorque`](sim/simAddForceAndTorque_cpp.htm)
- [`simAlignShapeBB`](sim/simAlignShapeBB_cpp.htm)
- [`simApplyTexture`](sim/simApplyTexture_cpp.htm)
- [`simComputeMassAndInertia`](sim/simComputeMassAndInertia_cpp.htm)
- [`simConvexDecompose`](sim/simConvexDecompose_cpp.htm)
- [`simCreateHeightfieldShape`](sim/simCreateHeightfieldShape_cpp.htm)
- [`simCreatePrimitiveShape`](sim/simCreatePrimitiveShape_cpp.htm)
- [`simCreateShape`](sim/simCreateShape_cpp.htm)
- [`simGenerateShapeFromPath`](sim/simGenerateShapeFromPath_cpp.htm)
- [`simGetDecimatedMesh`](sim/simGetDecimatedMesh_cpp.htm)
- [`simGetExtensionString`](sim/simGetExtensionString_cpp.htm)
- [`simGetQHull`](sim/simGetQHull_cpp.htm)
- [`simGetShapeColor`](sim/simGetShapeColor_cpp.htm)
- [`simGetShapeGeomInfo`](sim/simGetShapeGeomInfo_cpp.htm)
- [`simGetShapeInertia`](sim/simGetShapeInertia_cpp.htm)
- [`simGetShapeMass`](sim/simGetShapeMass_cpp.htm)
- [`simGetShapeMesh`](sim/simGetShapeMesh_cpp.htm)
- [`simGetShapeTextureId`](sim/simGetShapeTextureId_cpp.htm)
- [`simGetShapeViz`](sim/simGetShapeViz_cpp.htm)
- [`simGetVelocity`](sim/simGetVelocity_cpp.htm)
- [`simGroupShapes`](sim/simGroupShapes_cpp.htm)
- [`simImportShape`](sim/simImportShape_cpp.htm)
- [`simRelocateShapeFrame`](sim/simRelocateShapeFrame_cpp.htm)
- [`simSetShapeColor`](sim/simSetShapeColor_cpp.htm)
- [`simSetShapeInertia`](sim/simSetShapeInertia_cpp.htm)
- [`simSetShapeMass`](sim/simSetShapeMass_cpp.htm)
- [`simSetShapeTexture`](sim/simSetShapeTexture_cpp.htm)
- [`simUngroupShape`](sim/simUngroupShape_cpp.htm)

## <a id="functions_joint"></a><a id="jointObject"></a>[joint](joints.md) (C-functions)

- [`simCreateJoint`](sim/simCreateJoint_cpp.htm)
- [`simGetJointDependency`](sim/simGetJointDependency_cpp.htm)
- [`simGetJointForce`](sim/simGetJointForce_cpp.htm)
- [`simGetJointInterval`](sim/simGetJointInterval_cpp.htm)
- [`simGetJointMode`](sim/simGetJointMode_cpp.htm)
- [`simGetJointPosition`](sim/simGetJointPosition_cpp.htm)
- [`simGetJointTargetForce`](sim/simGetJointTargetForce_cpp.htm)
- [`simGetJointTargetPosition`](sim/simGetJointTargetPosition_cpp.htm)
- [`simGetJointTargetVelocity`](sim/simGetJointTargetVelocity_cpp.htm)
- [`simGetJointType`](sim/simGetJointType_cpp.htm)
- [`simGetJointVelocity`](sim/simGetJointVelocity_cpp.htm)
- [`simGetObjectChildPose`](sim/simGetObjectChildPose_cpp.htm)
- [`simSetJointDependency`](sim/simSetJointDependency_cpp.htm)
- [`simSetJointInterval`](sim/simSetJointInterval_cpp.htm)
- [`simSetJointMode`](sim/simSetJointMode_cpp.htm)
- [`simSetJointPosition`](sim/simSetJointPosition_cpp.htm)
- [`simSetJointTargetForce`](sim/simSetJointTargetForce_cpp.htm)
- [`simSetJointTargetPosition`](sim/simSetJointTargetPosition_cpp.htm)
- [`simSetJointTargetVelocity`](sim/simSetJointTargetVelocity_cpp.htm)
- [`simSetObjectChildPose`](sim/simSetObjectChildPose_cpp.htm)

## <a id="functions_dummy"></a><a id="dummyObject"></a>[dummy](dummies.md) (C-functions)

- [`simCreateDummy`](sim/simCreateDummy_cpp.htm)
- [`simGetLinkDummy`](sim/simGetLinkDummy_cpp.htm)
- [`simSetLinkDummy`](sim/simSetLinkDummy_cpp.htm)

## <a id="functions_camera"></a><a id="cameraObject"></a>[camera](cameras.md) (C-functions)

- [`simAdjustView`](sim/simAdjustView_cpp.htm)
- [`simCameraFitToView`](sim/simCameraFitToView_cpp.htm)
- [`simGetExtensionString`](sim/simGetExtensionString_cpp.htm)

## <a id="functions_light"></a><a id="lightObject"></a>[light](lights.md) (C-functions)

```cpp
simGetExtensionString
```

## <a id="functions_graph"></a><a id="graphs"></a>[graph](graphs.md) (C-functions)

- [`simAddGraphCurve`](sim/simAddGraphCurve_cpp.htm)
- [`simAddGraphStream`](sim/simAddGraphStream_cpp.htm)
- [`simDestroyGraphCurve`](sim/simDestroyGraphCurve_cpp.htm)
- [`simDuplicateGraphCurveToStatic`](sim/simDuplicateGraphCurveToStatic_cpp.htm)
- [`simHandleGraph`](sim/simHandleGraph_cpp.htm)
- [`simResetGraph`](sim/simResetGraph_cpp.htm)
- [`simSetGraphStreamTransformation`](sim/simSetGraphStreamTransformation_cpp.htm)
- [`simSetGraphStreamValue`](sim/simSetGraphStreamValue_cpp.htm)

## <a id="functions_proximitySensor"></a>[proximitySensor](proximitySensors.md) (C-functions)

- [`simCheckProximitySensor`](sim/simCheckProximitySensor_cpp.htm)
- [`simCreateProximitySensor`](sim/simCreateProximitySensor_cpp.htm)
- [`simHandleProximitySensor`](sim/simHandleProximitySensor_cpp.htm)
- [`simReadProximitySensor`](sim/simReadProximitySensor_cpp.htm)
- [`simResetProximitySensor`](sim/simResetProximitySensor_cpp.htm)

## <a id="functions_visionSensor"></a>[visionSensor](visionSensors.md) (C-functions)

- [`simAdjustView`](sim/simAdjustView_cpp.htm)
- [`simCheckVisionSensor`](sim/simCheckVisionSensor_cpp.htm)
- [`simCheckVisionSensorEx`](sim/simCheckVisionSensorEx_cpp.htm)
- [`simCreateVisionSensor`](sim/simCreateVisionSensor_cpp.htm)
- [`simGetExtensionString`](sim/simGetExtensionString_cpp.htm)
- [`simGetVisionSensorDepth`](sim/simGetVisionSensorDepth_cpp.htm)
- [`simGetVisionSensorImg`](sim/simGetVisionSensorImg_cpp.htm)
- [`simGetVisionSensorRes`](sim/simGetVisionSensorRes_cpp.htm)
- [`simHandleVisionSensor`](sim/simHandleVisionSensor_cpp.htm)
- [`simReadVisionSensor`](sim/simReadVisionSensor_cpp.htm)
- [`simResetVisionSensor`](sim/simResetVisionSensor_cpp.htm)
- [`simSetVisionSensorImg`](sim/simSetVisionSensorImg_cpp.htm)

## <a id="functions_forceSensor"></a>[forceSensor](forceSensors.md) (C-functions)

- [`simCreateForceSensor`](sim/simCreateForceSensor_cpp.htm)
- [`simReadForceSensor`](sim/simReadForceSensor_cpp.htm)

## <a id="functions_pointCloud"></a>[pointCloud](pointClouds.md) (C-functions)

- [`simCreatePointCloud`](sim/simCreatePointCloud_cpp.htm)
- [`simGetPointCloudOptions`](sim/simGetPointCloudOptions_cpp.htm)
- [`simGetPointCloudPoints`](sim/simGetPointCloudPoints_cpp.htm)
- [`simInsertObjectIntoPointCloud`](sim/simInsertObjectIntoPointCloud_cpp.htm)
- [`simInsertPointsIntoPointCloud`](sim/simInsertPointsIntoPointCloud_cpp.htm)
- [`simIntersectPointsWithPointCloud`](sim/simIntersectPointsWithPointCloud_cpp.htm)
- [`simRemovePointsFromPointCloud`](sim/simRemovePointsFromPointCloud_cpp.htm)
- [`simSetPointCloudOptions`](sim/simSetPointCloudOptions_cpp.htm)
- [`simSubtractObjectFromPointCloud`](sim/simSubtractObjectFromPointCloud_cpp.htm)

## <a id="functions_ocTree"></a><a id="octree"></a>[ocTree](octrees.md) (C-functions)

- [`simCheckOctreePointOccupancy`](sim/simCheckOctreePointOccupancy_cpp.htm)
- [`simCreateOctree`](sim/simCreateOctree_cpp.htm)
- [`simGetOctreeVoxels`](sim/simGetOctreeVoxels_cpp.htm)
- [`simInsertObjectIntoOctree`](sim/simInsertObjectIntoOctree_cpp.htm)
- [`simInsertVoxelsIntoOctree`](sim/simInsertVoxelsIntoOctree_cpp.htm)
- [`simRemoveVoxelsFromOctree`](sim/simRemoveVoxelsFromOctree_cpp.htm)
- [`simSubtractObjectFromOctree`](sim/simSubtractObjectFromOctree_cpp.htm)

## <a id="functions_Path"></a><a id="paths"></a>[Path](paths.md) (C-functions)

- [`simGenerateShapeFromPath`](sim/simGenerateShapeFromPath_cpp.htm)
- [`simGetClosestPosOnPath`](sim/simGetClosestPosOnPath_cpp.htm)

## <a id="functions_file"></a><a id="fileOperations"></a>File operations (C-functions)

- [`simCloseScene`](sim/simCloseScene_cpp.htm)
- [`simCreateTexture`](sim/simCreateTexture_cpp.htm)
- [`simDoesFileExist`](sim/simDoesFileExist_cpp.htm)
- [`simExportMesh`](sim/simExportMesh_cpp.htm)
- [`simImportMesh`](sim/simImportMesh_cpp.htm)
- [`simImportShape`](sim/simImportShape_cpp.htm)
- [`simLoadModel`](sim/simLoadModel_cpp.htm)
- [`simLoadScene`](sim/simLoadScene_cpp.htm)
- [`simSaveModel`](sim/simSaveModel_cpp.htm)
- [`simSaveScene`](sim/simSaveScene_cpp.htm)

## <a id="functions_main"></a><a id="mainFunctionalityHandling"></a>General functionality handling (C-functions)

- [`simGetCollectionObjects`](sim/simGetCollectionObjects_cpp.htm)
- [`simGetObject`](sim/simGetObject_cpp.htm)
- [`simGetObjects`](sim/simGetObjects_cpp.htm)
- [`simGetObjectsInTree`](sim/simGetObjectsInTree_cpp.htm)
- [`simGetReferencedHandles`](sim/simGetReferencedHandles_cpp.htm)
- [`simIsHandle`](sim/simIsHandle_cpp.htm)
- [`simSetReferencedHandles`](sim/simSetReferencedHandles_cpp.htm)

## <a id="functions_dynamics"></a><a id="dynamicsFunctionality"></a>[Dynamics](dynamicsModule.md) (C-functions)

- [`simAddForce`](sim/simAddForce_cpp.htm)
- [`simAddForceAndTorque`](sim/simAddForceAndTorque_cpp.htm)
- [`simComputeMassAndInertia`](sim/simComputeMassAndInertia_cpp.htm)
- [`simConvexDecompose`](sim/simConvexDecompose_cpp.htm)
- [`simCreateForceSensor`](sim/simCreateForceSensor_cpp.htm)
- [`simGetContactInfo`](sim/simGetContactInfo_cpp.htm)
- [`simGetDecimatedMesh`](sim/simGetDecimatedMesh_cpp.htm)
- [`simGetJointForce`](sim/simGetJointForce_cpp.htm)
- [`simGetJointTargetForce`](sim/simGetJointTargetForce_cpp.htm)
- [`simGetLinkDummy`](sim/simGetLinkDummy_cpp.htm)
- [`simGetQHull`](sim/simGetQHull_cpp.htm)
- [`simGetShapeInertia`](sim/simGetShapeInertia_cpp.htm)
- [`simGetShapeMass`](sim/simGetShapeMass_cpp.htm)
- [`simGetVelocity`](sim/simGetVelocity_cpp.htm)
- [`simHandleDynamics`](sim/simHandleDynamics_cpp.htm)
- [`simIsDynamicallyEnabled`](sim/simIsDynamicallyEnabled_cpp.htm)
- [`simReadForceSensor`](sim/simReadForceSensor_cpp.htm)
- [`simResetDynamicObject`](sim/simResetDynamicObject_cpp.htm)
- [`simSetJointTargetForce`](sim/simSetJointTargetForce_cpp.htm)
- [`simSetJointTargetPosition`](sim/simSetJointTargetPosition_cpp.htm)
- [`simSetJointTargetVelocity`](sim/simSetJointTargetVelocity_cpp.htm)
- [`simSetLinkDummy`](sim/simSetLinkDummy_cpp.htm)
- [`simSetShapeInertia`](sim/simSetShapeInertia_cpp.htm)
- [`simSetShapeMass`](sim/simSetShapeMass_cpp.htm)

## <a id="functions_collision"></a><a id="collisionDetection"></a>[Collision detection](collisionDetection.md) (C-functions)

```cpp
simCheckCollision
```

## <a id="functions_distance"></a><a id="distanceCalculation"></a>[Distance calculation](distanceCalculation.md) (C-functions)

```cpp
simCheckDistance
```

## <a id="functions_rendering"></a>[Rendering](dataVisualizationAndOutput.md) (C-functions)

- [`simGetObjectColor`](sim/simGetObjectColor_cpp.htm)
- [`simGetShapeColor`](sim/simGetShapeColor_cpp.htm)
- [`simSetObjectColor`](sim/simSetObjectColor_cpp.htm)
- [`simSetShapeColor`](sim/simSetShapeColor_cpp.htm)

## <a id="functions_model"></a><a id="modelFunctionality"></a>[Models](models.md) (C-functions)

- [`simLoadModel`](sim/simLoadModel_cpp.htm)
- [`simSaveModel`](sim/simSaveModel_cpp.htm)

## <a id="functions_selection"></a><a id="sceneObjectSelectionFunctionality"></a>Selection (C-functions)

- [`simGetObjectSel`](sim/simGetObjectSel_cpp.htm)
- [`simSetObjectSel`](sim/simSetObjectSel_cpp.htm)

## <a id="functions_creation"></a><a id="sceneObjectCreationFunctionality"></a>Object creation (C-functions)

- [`simCreateDummy`](sim/simCreateDummy_cpp.htm)
- [`simCreateForceSensor`](sim/simCreateForceSensor_cpp.htm)
- [`simCreateHeightfieldShape`](sim/simCreateHeightfieldShape_cpp.htm)
- [`simCreateJoint`](sim/simCreateJoint_cpp.htm)
- [`simCreateOctree`](sim/simCreateOctree_cpp.htm)
- [`simCreatePointCloud`](sim/simCreatePointCloud_cpp.htm)
- [`simCreatePrimitiveShape`](sim/simCreatePrimitiveShape_cpp.htm)
- [`simCreateProximitySensor`](sim/simCreateProximitySensor_cpp.htm)
- [`simCreateScript`](sim/simCreateScript_cpp.htm)
- [`simCreateShape`](sim/simCreateShape_cpp.htm)
- [`simCreateTexture`](sim/simCreateTexture_cpp.htm)
- [`simCreateVisionSensor`](sim/simCreateVisionSensor_cpp.htm)
- [`simGenerateShapeFromPath`](sim/simGenerateShapeFromPath_cpp.htm)

## <a id="functions_scriptRelated"></a>[Script related](scripts.md) (C-functions)

- [`simCallScriptFunctionEx`](sim/simCallScriptFunctionEx_cpp.htm)
- [`simCreateScript`](sim/simCreateScript_cpp.htm)
- [`simExecuteScriptString`](sim/simExecuteScriptString_cpp.htm)
- [`simGetApiFunc`](sim/simGetApiFunc_cpp.htm)
- [`simGetApiInfo`](sim/simGetApiInfo_cpp.htm)
- [`simGetScriptHandleEx`](sim/simGetScriptHandleEx_cpp.htm)
- [`simInitScript`](sim/simInitScript_cpp.htm)
- [`simIsHandle`](sim/simIsHandle_cpp.htm)
- [`simRegisterScriptCallbackFunction`](sim/simRegisterScriptCallbackFunction_cpp.htm)
- [`simRegisterScriptFuncHook`](sim/simRegisterScriptFuncHook_cpp.htm)
- [`simRegisterScriptVariable`](sim/simRegisterScriptVariable_cpp.htm)
- [`simResetScript`](sim/simResetScript_cpp.htm)

## <a id="functions_simulation"></a><a id="SimulationFunctionality"></a>[Simulation](simulation.md) (C-functions)

- [`simGetSimulationState`](sim/simGetSimulationState_cpp.htm)
- [`simGetSimulationTime`](sim/simGetSimulationTime_cpp.htm)
- [`simGetSimulationTimeStep`](sim/simGetSimulationTimeStep_cpp.htm)
- [`simPauseSimulation`](sim/simPauseSimulation_cpp.htm)
- [`simStartSimulation`](sim/simStartSimulation_cpp.htm)
- [`simStopSimulation`](sim/simStopSimulation_cpp.htm)

## <a id="functions_transformation"></a><a id="pose"></a><a id="transformations"></a><a id="coordinatesAndTransformations"></a>[Coordinates and transformations](positionOrientationTransformation.md) (C-functions)

- [`simAlignShapeBB`](sim/simAlignShapeBB_cpp.htm)
- [`simBuildMatrix`](sim/simBuildMatrix_cpp.htm)
- [`simBuildPose`](sim/simBuildPose_cpp.htm)
- [`simGetEulerAnglesFromMatrix`](sim/simGetEulerAnglesFromMatrix_cpp.htm)
- [`simGetObjectChildPose`](sim/simGetObjectChildPose_cpp.htm)
- [`simGetObjectMatrix`](sim/simGetObjectMatrix_cpp.htm)
- [`simGetObjectOrientation`](sim/simGetObjectOrientation_cpp.htm)
- [`simGetObjectPose`](sim/simGetObjectPose_cpp.htm)
- [`simGetObjectPosition`](sim/simGetObjectPosition_cpp.htm)
- [`simGetObjectQuaternion`](sim/simGetObjectQuaternion_cpp.htm)
- [`simGetObjectVelocity`](sim/simGetObjectVelocity_cpp.htm)
- [`simGetRotationAxis`](sim/simGetRotationAxis_cpp.htm)
- [`simInvertMatrix`](sim/simInvertMatrix_cpp.htm)
- [`simInvertPose`](sim/simInvertPose_cpp.htm)
- [`simMatrixToPose`](sim/simMatrixToPose_cpp.htm)
- [`simMultiplyMatrices`](sim/simMultiplyMatrices_cpp.htm)
- [`simMultiplyPoses`](sim/simMultiplyPoses_cpp.htm)
- [`simPoseToMatrix`](sim/simPoseToMatrix_cpp.htm)
- [`simRelocateShapeFrame`](sim/simRelocateShapeFrame_cpp.htm)
- [`simRotateAroundAxis`](sim/simRotateAroundAxis_cpp.htm)
- [`simSetObjectChildPose`](sim/simSetObjectChildPose_cpp.htm)
- [`simSetObjectMatrix`](sim/simSetObjectMatrix_cpp.htm)
- [`simSetObjectOrientation`](sim/simSetObjectOrientation_cpp.htm)
- [`simSetObjectPose`](sim/simSetObjectPose_cpp.htm)
- [`simSetObjectPosition`](sim/simSetObjectPosition_cpp.htm)
- [`simSetObjectQuaternion`](sim/simSetObjectQuaternion_cpp.htm)
- [`simTransformVector`](sim/simTransformVector_cpp.htm)

## <a id="functions_messaging"></a>[Messaging](meansOfCommunication.md) (C-functions)

- [`simAddLog`](sim/simAddLog_cpp.htm)
- [`simCallScriptFunctionEx`](sim/simCallScriptFunctionEx_cpp.htm)
- [`simExecuteScriptString`](sim/simExecuteScriptString_cpp.htm)
- [`simGetLastError`](sim/simGetLastError_cpp.htm)
- [`simGetObjectUid`](sim/simGetObjectUid_cpp.htm)
- [`simGetSimulatorMessage`](sim/simGetSimulatorMessage_cpp.htm)
- [`simSetLastError`](sim/simSetLastError_cpp.htm)

## <a id="functions_importExport"></a><a id="importExportFunctions"></a>[Import/export](importExport.md) (C-functions)

- [`simCreateTexture`](sim/simCreateTexture_cpp.htm)
- [`simExportMesh`](sim/simExportMesh_cpp.htm)
- [`simImportMesh`](sim/simImportMesh_cpp.htm)
- [`simImportShape`](sim/simImportShape_cpp.htm)
- [`simLoadImage`](sim/simLoadImage_cpp.htm)
- [`simSaveImage`](sim/simSaveImage_cpp.htm)

## <a id="functions_Motion"></a><a id="rml"></a><a id="ruckig"></a>Motion functionality (C-functions)

- [`simRuckigPos`](sim/simRuckigPos_cpp.htm)
- [`simRuckigRemove`](sim/simRuckigRemove_cpp.htm)
- [`simRuckigStep`](sim/simRuckigStep_cpp.htm)
- [`simRuckigVel`](sim/simRuckigVel_cpp.htm)

## <a id="functions_packing"></a>Packing/unpacking (C-functions)

- [`simGetBufferProperty`](sim/simGetBufferProperty_cpp.htm)
- [`simPackTable`](sim/simPackTable_cpp.htm)
- [`simSetBufferProperty`](sim/simSetBufferProperty_cpp.htm)
- [`simUnpackTable`](sim/simUnpackTable_cpp.htm)

## <a id="functions_other"></a>Other (C-functions)

- [`simAnnounceSceneContentChange`](sim/simAnnounceSceneContentChange_cpp.htm)
- [`simCreateBuffer`](sim/simCreateBuffer_cpp.htm)
- [`simFloatingViewAdd`](sim/simFloatingViewAdd_cpp.htm)
- [`simFloatingViewRemove`](sim/simFloatingViewRemove_cpp.htm)
- [`simGetExplicitHandling`](sim/simGetExplicitHandling_cpp.htm)
- [`simGetLastError`](sim/simGetLastError_cpp.htm)
- [`simGetLastInfo`](sim/simGetLastInfo_cpp.htm)
- [`simGetMainWindow`](sim/simGetMainWindow_cpp.htm)
- [`simGetNavigationMode`](sim/simGetNavigationMode_cpp.htm)
- [`simGetObjectfromUid`](sim/simGetObjectfromUid_cpp.htm)
- [`simGetPage`](sim/simGetPage_cpp.htm)
- [`simGetPluginInfo`](sim/simGetPluginInfo_cpp.htm)
- [`simModuleEntry`](sim/simModuleEntry_cpp.htm)
- [`simOpenTextEditor`](sim/simOpenTextEditor_cpp.htm)
- [`simQuitSimulator`](sim/simQuitSimulator_cpp.htm)
- [`simRefreshDialogs`](sim/simRefreshDialogs_cpp.htm)
- [`simReleaseBuffer`](sim/simReleaseBuffer_cpp.htm)
- [`simSetExplicitHandling`](sim/simSetExplicitHandling_cpp.htm)
- [`simSetLastError`](sim/simSetLastError_cpp.htm)
- [`simSetNavigationMode`](sim/simSetNavigationMode_cpp.htm)
- [`simSetPage`](sim/simSetPage_cpp.htm)
- [`simSetPluginInfo`](sim/simSetPluginInfo_cpp.htm)
