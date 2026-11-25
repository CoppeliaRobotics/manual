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

Keep in mind that **all** methods can also be called from C/C++ via the [`simCallMethod`](sim-2/simCallMethod_cpp.md) function.

---

## <a id="methodsAndProperties_object"></a>object (methods & properties)

- [`object:getBoolProperty`](sim-2/object_getBoolProperty.md) — Fetches a boolean property
- [`object:getBufferProperty`](sim-2/object_getBufferProperty.md) — Fetches a buffer property
- [`object:getColorProperty`](sim-2/object_getColorProperty.md) — Fetches a color property
- [`object:getEnumProperty`](sim-2/object_getEnumProperty.md) — Fetches an enum property
- [`object:getFloatArrayProperty`](sim-2/object_getFloatArrayProperty.md) — Fetches a float array property
- [`object:getFloatProperty`](sim-2/object_getFloatProperty.md) — Fetches a float property
- [`object:getHandleArrayProperty`](sim-2/object_getHandleArrayProperty.md) — Fetches a handle array property
- [`object:getHandleProperty`](sim-2/object_getHandleProperty.md) — Fetches a handle property
- [`object:getIntArrayProperty`](sim-2/object_getIntArrayProperty.md) — Fetches an int array property
- [`object:getIntProperty`](sim-2/object_getIntProperty.md) — Fetches an int32 property
- [`object:getLongProperty`](sim-2/object_getLongProperty.md) — Fetches an int64 property
- [`object:getMatrixProperty`](sim-2/object_getMatrixProperty.md) — Fetches a matrix property
- [`object:getMethodProperty`](sim-2/object_getMethodProperty.md) — Fetches a method property
- [`object:getPoseProperty`](sim-2/object_getPoseProperty.md) — Fetches a pose property
- [`object:getProperties`](sim-2/object_getProperties.md) — Fetches all properties of a target
- [`object:getPropertiesInfos`](sim-2/object_getPropertiesInfos.md) — Fetches all property infos of a target
- [`object:getProperty`](sim-2/object_getProperty.md) — Convenience function to fetch a property
- [`object:getPropertyInfo`](sim-2/object_getPropertyInfo.md) — Fetches information about a property
- [`object:getPropertyInfos`](sim-2/object_getPropertyInfos.md) — Fetches an extended set of property infos
- [`object:getPropertyName`](sim-2/object_getPropertyName.md) — Fetches a property name by index
- [`object:getPropertyTypeString`](sim-2/object_getPropertyTypeString.md) — Gets string for a property type
- [`object:getQuaternionProperty`](sim-2/object_getQuaternionProperty.md) — Fetches a quaternion property
- [`object:getStringArrayProperty`](sim-2/object_getStringArrayProperty.md) — Fetches a text array property
- [`object:getStringProperty`](sim-2/object_getStringProperty.md) — Fetches a string property
- [`object:getTableProperty`](sim-2/object_getTableProperty.md) — Fetches a table property
- [`object:getVector3Property`](sim-2/object_getVector3Property.md) — Fetches a vector3 property
- [`object:isValid`](sim-2/object_isValid.md) — Checks if the object is valid
- [`object:removeProperty`](sim-2/object_removeProperty.md) — Removes a removable property
- [`object:setBoolProperty`](sim-2/object_setBoolProperty.md) — Sets a boolean property
- [`object:setBufferProperty`](sim-2/object_setBufferProperty.md) — Sets a buffer property
- [`object:setColorProperty`](sim-2/object_setColorProperty.md) — Sets a color property
- [`object:setEnumProperty`](sim-2/object_setEnumProperty.md) — Sets an enum property
- [`object:setFloatArrayProperty`](sim-2/object_setFloatArrayProperty.md) — Sets a float array property
- [`object:setFloatProperty`](sim-2/object_setFloatProperty.md) — Sets a float property
- [`object:setHandleArrayProperty`](sim-2/object_setHandleArrayProperty.md) — Sets a handle array property
- [`object:setHandleProperty`](sim-2/object_setHandleProperty.md) — Sets a handle property
- [`object:setIntArrayProperty`](sim-2/object_setIntArrayProperty.md) — Sets an int array property
- [`object:setIntProperty`](sim-2/object_setIntProperty.md) — Sets an int32 property
- [`object:setLongProperty`](sim-2/object_setLongProperty.md) — Sets an int64 property
- [`object:setMatrixProperty`](sim-2/object_setMatrixProperty.md) — Sets a matrix property
- [`object:setMethodProperty`](sim-2/object_setMethodProperty.md) — Sets a method property
- [`object:setPoseProperty`](sim-2/object_setPoseProperty.md) — Sets a pose property
- [`object:setProperties`](sim-2/object_setProperties.md) — Sets several properties at once
- [`object:setProperty`](sim-2/object_setProperty.md) — Convenience function to set a property
- [`object:setPropertyInfo`](sim-2/object_setPropertyInfo.md) — Sets information about a property
- [`object:setQuaternionProperty`](sim-2/object_setQuaternionProperty.md) — Sets a quaternion property
- [`object:setStringArrayProperty`](sim-2/object_setStringArrayProperty.md) — Sets a text array property
- [`object:setStringProperty`](sim-2/object_setStringProperty.md) — Sets a string property
- [`object:setTableProperty`](sim-2/object_setTableProperty.md) — Sets a table property
- [`object:setVector3Property`](sim-2/object_setVector3Property.md) — Sets a vector3 property
- [`object.handle`](sim-2/property_object_handle.md) — Handle
- [`object.metaInfo.isClass`](sim-2/property_object_metaInfo_isClass.md) — Class flag
- [`object.metaInfo.isSceneObject`](sim-2/property_object_metaInfo_isSceneObject.md) — Scene object flag
- [`object.metaInfo.namespaces`](sim-2/property_object_metaInfo_namespaces.md) — Object namespaces
- [`object.metaInfo.superClass`](sim-2/property_object_metaInfo_superClass.md) — Object superclass
- [`object.type`](sim-2/property_object_type.md) — Object type

## <a id="methodsAndProperties_app"></a>app (methods & properties)

- [`app:createCustomObjectClass`](sim-2/app_createCustomObjectClass.md) — Creates a custom object class
- [`app:createObject`](sim-2/app_createObject.md) — Creates various objects (collections, scripts, sensors, etc.)
- [`app:deserialize`](sim-2/app_deserialize.md) — Deserializes a buffer using CBOR format
- [`app:fastIdleLoop`](sim-2/app_fastIdleLoop.md) — Speeds up the idle loop for reactivity
- [`app:getEnumInfo`](sim-2/app_getEnumInfo.md) — Returns information about an enum
- [`app:getGenesisEvents`](sim-2/app_getGenesisEvents.md) — Retrieves events to reconstruct the app's state
- [`app:getObjects`](sim-2/app_getObjects.md) — Retrieves objects of a certain type
- [`app:getPluginInfo`](sim-2/app_getPluginInfo.md) — Returns information about a loaded plugin
- [`app:handleAddOns`](sim-2/app_handleAddOns.md) — Calls a system callback in add-ons
- [`app:handleMessagePump`](sim-2/app_handleMessagePump.md) — Handles the message pump explicitly
- [`app:handleSandboxes`](sim-2/app_handleSandboxes.md) — Calls a system callback in the sandbox
- [`app:loadImage`](sim-2/app_loadImage.md) — Loads an image from file
- [`app:loadImageFromBuffer`](sim-2/app_loadImageFromBuffer.md) — Loads an image from memory
- [`app:loadModelInfo`](sim-2/app_loadModelInfo.md) — Loads a model thumbnail
- [`app:loadModelInfoFromBuffer`](sim-2/app_loadModelInfoFromBuffer.md) — Loads a model thumbnail from buffer
- [`app:loadScene`](sim-2/app_loadScene.md) — Loads a scene from file
- [`app:loadSceneFromBuffer`](sim-2/app_loadSceneFromBuffer.md) — Loads a scene from buffer
- [`app:logError`](sim-2/app_logError.md) — Outputs an error message in the status bar
- [`app:logInfo`](sim-2/app_logInfo.md) — Outputs an information message in the status bar
- [`app:logWarn`](sim-2/app_logWarn.md) — Outputs a warning message in the status bar
- [`app:openFile`](sim-2/app_openFile.md) — Opens a file in a subprocess
- [`app:pack`](sim-2/app_pack.md) — Packs data using CoppeliaSim format
- [`app:packArray`](sim-2/app_packArray.md) — Packs an array of numbers as little-endian
- [`app:pushEvent`](sim-2/app_pushEvent.md) — Pushes a user event for asynchronous reception
- [`app:quit`](sim-2/app_quit.md) — Triggers a quit signal for the application
- [`app:removeObjects`](sim-2/app_removeObjects.md) — Removes one or several objects
- [`app:saveImage`](sim-2/app_saveImage.md) — Saves an image to file
- [`app:saveImageToBuffer`](sim-2/app_saveImageToBuffer.md) — Saves an image to a buffer
- [`app:serialize`](sim-2/app_serialize.md) — Serializes data using CBOR format
- [`app:setPluginInfo`](sim-2/app_setPluginInfo.md) — Modifies information of a loaded plugin
- [`app:systemLock`](sim-2/app_systemLock.md) — Acquires/releases a system-wide semaphore
- [`app:test`](sim-2/app_test.md) — Test method
- [`app:transformBuffer`](sim-2/app_transformBuffer.md) — Modifies a buffer (format, scale, offset)
- [`app:transformImage`](sim-2/app_transformImage.md) — Transforms an image (scaling, flipping)
- [`app:unpack`](sim-2/app_unpack.md) — Unpacks data using CoppeliaSim format
- [`app:unpackArray`](sim-2/app_unpackArray.md) — Unpacks a buffer into an array of numbers
- [`app.addOns`](sim-2/property_app_addOns.md) — Add-ons
- [`app.args`](sim-2/property_app_args.md) — App args
- [`app.auxAddOn1`](sim-2/property_app_auxAddOn1.md) — Aux. add-on 1
- [`app.auxAddOn2`](sim-2/property_app_auxAddOn2.md) — Aux. add-on 2
- [`app.browserEnabled`](sim-2/property_app_browserEnabled.md) — Browser enabled
- [`app.canSave`](sim-2/property_app_canSave.md) — Can save
- [`app.consoleVerbosity`](sim-2/property_app_consoleVerbosity.md) — Console verbosity
- [`app.consoleVerbosityStr`](sim-2/property_app_consoleVerbosityStr.md) — Console verbosity string
- [`app.current`](sim-2/property_app_current.md) — Current
- [`app.customClasses`](sim-2/property_app_customClasses.md) — Custom classes
- [`app.customObjects`](sim-2/property_app_customObjects.md) — Custom objects
- [`app.customSceneObjectClasses`](sim-2/property_app_customSceneObjectClasses.md) — Custom scene object classes
- [`app.defaultPython`](sim-2/property_app_defaultPython.md) — Default Python
- [`app.defaultRotationStepSize`](sim-2/property_app_defaultRotationStepSize.md) — Rotation step size
- [`app.defaultTranslationStepSize`](sim-2/property_app_defaultTranslationStepSize.md) — Translation step size
- [`app.dialogVerbosity`](sim-2/property_app_dialogVerbosity.md) — Dialog verbosity
- [`app.dialogVerbosityStr`](sim-2/property_app_dialogVerbosityStr.md) — Dialog verbosity string
- [`app.displayEnabled`](sim-2/property_app_displayEnabled.md) — Display enabled
- [`app.dongleId`](sim-2/property_app_dongleId.md)
- [`app.dongleSerial`](sim-2/property_app_dongleSerial.md)
- [`app.enumTypes`](sim-2/property_app_enumTypes.md) — Enum types
- [`app.execUnsafe`](sim-2/property_app_execUnsafe.md) — Execute unsafe
- [`app.execUnsafeExt`](sim-2/property_app_execUnsafeExt.md) — Execute unsafe extended
- [`app.flavor`](sim-2/property_app_flavor.md) — Flavor
- [`app.headlessMode`](sim-2/property_app_headlessMode.md) — Headless mode
- [`app.hierarchyEnabled`](sim-2/property_app_hierarchyEnabled.md) — Hierarchy enabled
- [`app.idleFps`](sim-2/property_app_idleFps.md) — Idle FPS
- [`app.legacyMachineId`](sim-2/property_app_legacyMachineId.md) — Legacy machine ID
- [`app.machineId`](sim-2/property_app_machineId.md) — Machine ID
- [`app.machineId0`](sim-2/property_app_machineId0.md)
- [`app.machineId1`](sim-2/property_app_machineId1.md)
- [`app.machineId2`](sim-2/property_app_machineId2.md)
- [`app.machineId3`](sim-2/property_app_machineId3.md)
- [`app.machineIdX`](sim-2/property_app_machineIdX.md)
- [`app.machineSerial`](sim-2/property_app_machineSerial.md)
- [`app.machineSerialND`](sim-2/property_app_machineSerialND.md)
- [`app.notifyDeprecated`](sim-2/property_app_notifyDeprecated.md) — Notify deprecated
- [`app.paths.addOns`](sim-2/property_app_paths_addOns.md) — Add-on path
- [`app.paths.app`](sim-2/property_app_paths_app.md) — Application path
- [`app.paths.importExport`](sim-2/property_app_paths_importExport.md) — Import/export path
- [`app.paths.lua`](sim-2/property_app_paths_lua.md) — Lua path
- [`app.paths.models`](sim-2/property_app_paths_models.md) — Model path
- [`app.paths.mujoco`](sim-2/property_app_paths_mujoco.md) — MuJoCo path
- [`app.paths.python`](sim-2/property_app_paths_python.md) — Python path
- [`app.paths.resources`](sim-2/property_app_paths_resources.md) — Resource path
- [`app.paths.sceneTemp`](sim-2/property_app_paths_sceneTemp.md) — Scene temporary path
- [`app.paths.scenes`](sim-2/property_app_paths_scenes.md) — Scene path
- [`app.paths.settings`](sim-2/property_app_paths_settings.md) — Settings path
- [`app.paths.system`](sim-2/property_app_paths_system.md) — System path
- [`app.paths.temp`](sim-2/property_app_paths_temp.md) — Temporary path
- [`app.pid`](sim-2/property_app_pid.md) — PID
- [`app.platform`](sim-2/property_app_platform.md) — OS type
- [`app.pluginNames`](sim-2/property_app_pluginNames.md) — Plugins
- [`app.processCnt`](sim-2/property_app_processCnt.md) — Processes
- [`app.processId`](sim-2/property_app_processId.md) — Process
- [`app.productVersion`](sim-2/property_app_productVersion.md) — Product string
- [`app.productVersionNb`](sim-2/property_app_productVersionNb.md) — Product
- [`app.protocolVersion`](sim-2/property_app_protocolVersion.md) — Protocol
- [`app.qtVersion`](sim-2/property_app_qtVersion.md) — Qt
- [`app.randomFloat`](sim-2/property_app_randomFloat.md) — Random number
- [`app.randomQuaternion`](sim-2/property_app_randomQuaternion.md) — Random quaternion
- [`app.randomString`](sim-2/property_app_randomString.md) — Random string
- [`app.luaSandbox`](sim-2/property_app_luaSandbox.md) — Lua sandbox
- [`app.sandbox2`](sim-2/property_app_sandbox2.md) — Python sandbox
- [`app.sessionId`](sim-2/property_app_sessionId.md) — Session ID
- [`app.startupCode`](sim-2/property_app_startupCode.md) — Start-up code
- [`app.statusbarVerbosity`](sim-2/property_app_statusbarVerbosity.md) — Statusbar verbosity
- [`app.statusbarVerbosityStr`](sim-2/property_app_statusbarVerbosityStr.md) — Statusbar verbosity string
- [`app.systemTime`](sim-2/property_app_systemTime.md) — System time

## <a id="methodsAndProperties_scene"></a>[scene](scenes.md) (methods & properties)

- [`scene:announceChange`](sim-2/scene_announceChange.md) — Announces a change in the scene for undo/redo
- [`scene:copyObjects`](sim-2/scene_copyObjects.md) — Copies selected objects
- [`scene:createObject`](sim-2/scene_createObject.md) — Creates various objects (collections, scripts, sensors, etc.)
- [`scene:cutObjects`](sim-2/scene_cutObjects.md) — Cuts selected objects
- [`scene:duplicateObjects`](sim-2/scene_duplicateObjects.md) — Duplicates scene objects
- [`scene:getDescendants`](sim-2/scene_getDescendants.md) — Retrieves scene objects up to a specific depth
- [`scene:getObject`](sim-2/scene_getObject.md) — Retrieves an object by its path and name
- [`scene:getObjectFromUid`](sim-2/scene_getObjectFromUid.md) — Retrieves an object by its unique identifier
- [`scene:getObjects`](sim-2/scene_getObjects.md) — Retrieves objects of a certain type
- [`scene:groupShapes`](sim-2/scene_groupShapes.md) — Groups shapes into a compound shape
- [`scene:handleCustomizationScripts`](sim-2/scene_handleCustomizationScripts.md) — Calls a system callback in customization scripts
- [`scene:handleSimulationScripts`](sim-2/scene_handleSimulationScripts.md) — Calls a system callback in simulation scripts
- [`scene:loadModel`](sim-2/scene_loadModel.md) — Loads a previously saved model
- [`scene:loadModelFromBuffer`](sim-2/scene_loadModelFromBuffer.md) — Loads a model from buffer
- [`scene:mergeShapes`](sim-2/scene_mergeShapes.md) — Merges several shapes
- [`scene:pasteObjects`](sim-2/scene_pasteObjects.md) — Pastes objects
- [`scene:remove`](sim-2/scene_remove.md) — Closes the scene
- [`scene:removeObjects`](sim-2/scene_removeObjects.md) — Removes one or several objects
- [`scene:save`](sim-2/scene_save.md) — Saves the scene to file
- [`scene:saveToBuffer`](sim-2/scene_saveToBuffer.md) — Serializes the scene to a buffer
- [`scene:stepKinematicJoints`](sim-2/scene_stepKinematicJoints.md) — Steps all kinematic mode joints
- [`scene.dynamics:getContacts`](sim-2/scene_dynamics_getContacts.md) — Retrieves contact information from the dynamics world
- [`scene.dynamics:step`](sim-2/scene_dynamics_step.md) — Steps the dynamics engine
- [`scene.simulation:pause`](sim-2/scene_simulation_pause.md) — Requests a simulation pause
- [`scene.simulation:start`](sim-2/scene_simulation_start.md) — Requests a simulation start or resume
- [`scene.simulation:stop`](sim-2/scene_simulation_stop.md) — Requests a simulation stop
- [`scene.acknowledgment`](sim-2/property_scene_acknowledgment.md) — Acknowledgment
- [`scene.ambientLight`](sim-2/property_scene_ambientLight.md) — Ambient light
- [`scene.collections`](sim-2/property_scene_collections.md) — Collections
- [`scene.customObjects`](sim-2/property_scene_customObjects.md) — Custom objects
- [`scene.drawingObjects`](sim-2/property_scene_drawingObjects.md) — Drawing objects
- [`scene.dynamics.bullet.collisionMarginScaling`](sim-2/property_scene_dynamics_bullet_collisionMarginScaling.md)
- [`scene.dynamics.bullet.computeInertias`](sim-2/property_scene_dynamics_bullet_computeInertias.md)
- [`scene.dynamics.bullet.internalScalingFull`](sim-2/property_scene_dynamics_bullet_internalScalingFull.md)
- [`scene.dynamics.bullet.internalScalingValue`](sim-2/property_scene_dynamics_bullet_internalScalingValue.md)
- [`scene.dynamics.bullet.iterations`](sim-2/property_scene_dynamics_bullet_iterations.md)
- [`scene.dynamics.bullet.solver`](sim-2/property_scene_dynamics_bullet_solver.md)
- [`scene.dynamics.enabled`](sim-2/property_scene_dynamics_enabled.md) — Dynamics enabled
- [`scene.dynamics.engine`](sim-2/property_scene_dynamics_engine.md) — Dynamics engine
- [`scene.dynamics.engineProperties`](sim-2/property_scene_dynamics_engineProperties.md) — Engine properties
- [`scene.dynamics.engineVersion`](sim-2/property_scene_dynamics_engineVersion.md) — Dynamics engine version
- [`scene.dynamics.gravity`](sim-2/property_scene_dynamics_gravity.md) — Gravity
- [`scene.dynamics.mujoco.actuationEnable`](sim-2/property_scene_dynamics_mujoco_actuationEnable.md)
- [`scene.dynamics.mujoco.alignfree`](sim-2/property_scene_dynamics_mujoco_alignfree.md)
- [`scene.dynamics.mujoco.autoresetEnable`](sim-2/property_scene_dynamics_mujoco_autoresetEnable.md)
- [`scene.dynamics.mujoco.balanceInertias`](sim-2/property_scene_dynamics_mujoco_balanceInertias.md)
- [`scene.dynamics.mujoco.boundInertia`](sim-2/property_scene_dynamics_mujoco_boundInertia.md)
- [`scene.dynamics.mujoco.boundMass`](sim-2/property_scene_dynamics_mujoco_boundMass.md)
- [`scene.dynamics.mujoco.ccd_iterations`](sim-2/property_scene_dynamics_mujoco_ccd_iterations.md)
- [`scene.dynamics.mujoco.ccd_tolerance`](sim-2/property_scene_dynamics_mujoco_ccd_tolerance.md)
- [`scene.dynamics.mujoco.computeInertias`](sim-2/property_scene_dynamics_mujoco_computeInertias.md)
- [`scene.dynamics.mujoco.cone`](sim-2/property_scene_dynamics_mujoco_cone.md)
- [`scene.dynamics.mujoco.contactEnable`](sim-2/property_scene_dynamics_mujoco_contactEnable.md)
- [`scene.dynamics.mujoco.contactParamsMargin`](sim-2/property_scene_dynamics_mujoco_contactParamsMargin.md)
- [`scene.dynamics.mujoco.contactParamsOverride`](sim-2/property_scene_dynamics_mujoco_contactParamsOverride.md)
- [`scene.dynamics.mujoco.contactParamsSolimp`](sim-2/property_scene_dynamics_mujoco_contactParamsSolimp.md)
- [`scene.dynamics.mujoco.contactParamsSolref`](sim-2/property_scene_dynamics_mujoco_contactParamsSolref.md)
- [`scene.dynamics.mujoco.density`](sim-2/property_scene_dynamics_mujoco_density.md)
- [`scene.dynamics.mujoco.energyEnable`](sim-2/property_scene_dynamics_mujoco_energyEnable.md)
- [`scene.dynamics.mujoco.equalityEnable`](sim-2/property_scene_dynamics_mujoco_equalityEnable.md)
- [`scene.dynamics.mujoco.eulerdampEnable`](sim-2/property_scene_dynamics_mujoco_eulerdampEnable.md)
- [`scene.dynamics.mujoco.frictionlossEnable`](sim-2/property_scene_dynamics_mujoco_frictionlossEnable.md)
- [`scene.dynamics.mujoco.gravityEnable`](sim-2/property_scene_dynamics_mujoco_gravityEnable.md)
- [`scene.dynamics.mujoco.impratio`](sim-2/property_scene_dynamics_mujoco_impratio.md)
- [`scene.dynamics.mujoco.integrator`](sim-2/property_scene_dynamics_mujoco_integrator.md)
- [`scene.dynamics.mujoco.invdiscreteEnable`](sim-2/property_scene_dynamics_mujoco_invdiscreteEnable.md)
- [`scene.dynamics.mujoco.iterations`](sim-2/property_scene_dynamics_mujoco_iterations.md)
- [`scene.dynamics.mujoco.jacobian`](sim-2/property_scene_dynamics_mujoco_jacobian.md)
- [`scene.dynamics.mujoco.kinematicBodiesInertia`](sim-2/property_scene_dynamics_mujoco_kinematicBodiesInertia.md)
- [`scene.dynamics.mujoco.kinematicBodiesMass`](sim-2/property_scene_dynamics_mujoco_kinematicBodiesMass.md)
- [`scene.dynamics.mujoco.kinematicBodiesOverrideFlags`](sim-2/property_scene_dynamics_mujoco_kinematicBodiesOverrideFlags.md)
- [`scene.dynamics.mujoco.kinematicWeldSolimp`](sim-2/property_scene_dynamics_mujoco_kinematicWeldSolimp.md)
- [`scene.dynamics.mujoco.kinematicWeldSolref`](sim-2/property_scene_dynamics_mujoco_kinematicWeldSolref.md)
- [`scene.dynamics.mujoco.kinematicWeldTorquescale`](sim-2/property_scene_dynamics_mujoco_kinematicWeldTorquescale.md)
- [`scene.dynamics.mujoco.limitEnable`](sim-2/property_scene_dynamics_mujoco_limitEnable.md)
- [`scene.dynamics.mujoco.ls_iterations`](sim-2/property_scene_dynamics_mujoco_ls_iterations.md)
- [`scene.dynamics.mujoco.ls_tolerance`](sim-2/property_scene_dynamics_mujoco_ls_tolerance.md)
- [`scene.dynamics.mujoco.mbmemory`](sim-2/property_scene_dynamics_mujoco_mbmemory.md)
- [`scene.dynamics.mujoco.midphaseEnable`](sim-2/property_scene_dynamics_mujoco_midphaseEnable.md)
- [`scene.dynamics.mujoco.multiccd`](sim-2/property_scene_dynamics_mujoco_multiccd.md)
- [`scene.dynamics.mujoco.multithreaded`](sim-2/property_scene_dynamics_mujoco_multithreaded.md)
- [`scene.dynamics.mujoco.nativeccdEnable`](sim-2/property_scene_dynamics_mujoco_nativeccdEnable.md)
- [`scene.dynamics.mujoco.nconmax`](sim-2/property_scene_dynamics_mujoco_nconmax.md)
- [`scene.dynamics.mujoco.njmax`](sim-2/property_scene_dynamics_mujoco_njmax.md)
- [`scene.dynamics.mujoco.noslip_iterations`](sim-2/property_scene_dynamics_mujoco_noslip_iterations.md)
- [`scene.dynamics.mujoco.noslip_tolerance`](sim-2/property_scene_dynamics_mujoco_noslip_tolerance.md)
- [`scene.dynamics.mujoco.nstack`](sim-2/property_scene_dynamics_mujoco_nstack.md)
- [`scene.dynamics.mujoco.passiveEnable`](sim-2/property_scene_dynamics_mujoco_passiveEnable.md)
- [`scene.dynamics.mujoco.rebuildTrigger`](sim-2/property_scene_dynamics_mujoco_rebuildTrigger.md)
- [`scene.dynamics.mujoco.refsafeEnable`](sim-2/property_scene_dynamics_mujoco_refsafeEnable.md)
- [`scene.dynamics.mujoco.sdf_initpoints`](sim-2/property_scene_dynamics_mujoco_sdf_initpoints.md)
- [`scene.dynamics.mujoco.sdf_iterations`](sim-2/property_scene_dynamics_mujoco_sdf_iterations.md)
- [`scene.dynamics.mujoco.sensorEnable`](sim-2/property_scene_dynamics_mujoco_sensorEnable.md)
- [`scene.dynamics.mujoco.solver`](sim-2/property_scene_dynamics_mujoco_solver.md)
- [`scene.dynamics.mujoco.tolerance`](sim-2/property_scene_dynamics_mujoco_tolerance.md)
- [`scene.dynamics.mujoco.viscosity`](sim-2/property_scene_dynamics_mujoco_viscosity.md)
- [`scene.dynamics.mujoco.warmstartEnable`](sim-2/property_scene_dynamics_mujoco_warmstartEnable.md)
- [`scene.dynamics.mujoco.wind`](sim-2/property_scene_dynamics_mujoco_wind.md)
- [`scene.dynamics.newton.computeInertias`](sim-2/property_scene_dynamics_newton_computeInertias.md)
- [`scene.dynamics.newton.contactMergeTolerance`](sim-2/property_scene_dynamics_newton_contactMergeTolerance.md)
- [`scene.dynamics.newton.exactSolver`](sim-2/property_scene_dynamics_newton_exactSolver.md)
- [`scene.dynamics.newton.highJointAccuracy`](sim-2/property_scene_dynamics_newton_highJointAccuracy.md)
- [`scene.dynamics.newton.iterations`](sim-2/property_scene_dynamics_newton_iterations.md)
- [`scene.dynamics.newton.multithreading`](sim-2/property_scene_dynamics_newton_multithreading.md)
- [`scene.dynamics.ode.computeInertias`](sim-2/property_scene_dynamics_ode_computeInertias.md)
- [`scene.dynamics.ode.globalCfm`](sim-2/property_scene_dynamics_ode_globalCfm.md)
- [`scene.dynamics.ode.globalErp`](sim-2/property_scene_dynamics_ode_globalErp.md)
- [`scene.dynamics.ode.internalScalingFull`](sim-2/property_scene_dynamics_ode_internalScalingFull.md)
- [`scene.dynamics.ode.internalScalingValue`](sim-2/property_scene_dynamics_ode_internalScalingValue.md)
- [`scene.dynamics.ode.quickStepEnabled`](sim-2/property_scene_dynamics_ode_quickStepEnabled.md)
- [`scene.dynamics.ode.quickStepIterations`](sim-2/property_scene_dynamics_ode_quickStepIterations.md)
- [`scene.dynamics.showContactPoints`](sim-2/property_scene_dynamics_showContactPoints.md) — Show contact points
- [`scene.dynamics.stepSize`](sim-2/property_scene_dynamics_stepSize.md) — Dynamics dt
- [`scene.dynamics.vortex.autoSleep`](sim-2/property_scene_dynamics_vortex_autoSleep.md)
- [`scene.dynamics.vortex.computeInertias`](sim-2/property_scene_dynamics_vortex_computeInertias.md)
- [`scene.dynamics.vortex.constraintsAngularCompliance`](sim-2/property_scene_dynamics_vortex_constraintsAngularCompliance.md)
- [`scene.dynamics.vortex.constraintsAngularDamping`](sim-2/property_scene_dynamics_vortex_constraintsAngularDamping.md)
- [`scene.dynamics.vortex.constraintsAngularKineticLoss`](sim-2/property_scene_dynamics_vortex_constraintsAngularKineticLoss.md)
- [`scene.dynamics.vortex.constraintsLinearCompliance`](sim-2/property_scene_dynamics_vortex_constraintsLinearCompliance.md)
- [`scene.dynamics.vortex.constraintsLinearDamping`](sim-2/property_scene_dynamics_vortex_constraintsLinearDamping.md)
- [`scene.dynamics.vortex.constraintsLinearKineticLoss`](sim-2/property_scene_dynamics_vortex_constraintsLinearKineticLoss.md)
- [`scene.dynamics.vortex.contactTolerance`](sim-2/property_scene_dynamics_vortex_contactTolerance.md)
- [`scene.dynamics.vortex.multithreading`](sim-2/property_scene_dynamics_vortex_multithreading.md)
- [`scene.finalSaveRequest`](sim-2/property_scene_finalSaveRequest.md) — Final save
- [`scene.hierarchyChangeCounter`](sim-2/property_scene_hierarchyChangeCounter.md) — Hierarchy change counter
- [`scene.locked`](sim-2/property_scene_locked.md) — Scene is locked
- [`scene.mainScript`](sim-2/property_scene_mainScript.md) — Main script
- [`scene.objectCreationCounter`](sim-2/property_scene_objectCreationCounter.md) — Object creation counter
- [`scene.objectDestructionCounter`](sim-2/property_scene_objectDestructionCounter.md) — Object destruction counter
- [`scene.objects`](sim-2/property_scene_objects.md) — Objects
- [`scene.orphans`](sim-2/property_scene_orphans.md) — Orphan objects
- [`scene.path`](sim-2/property_scene_path.md) — Scene path
- [`scene.saveCalculationStructs`](sim-2/property_scene_saveCalculationStructs.md) — Save calculation structures
- [`scene.selection`](sim-2/property_scene_selection.md) — Selected objects
- [`scene.simulation.pauseAtError`](sim-2/property_scene_simulation_pauseAtError.md) — Pause simulation on script error
- [`scene.simulation.pauseAtTime`](sim-2/property_scene_simulation_pauseAtTime.md) — Pause simulation at time
- [`scene.simulation.realtime`](sim-2/property_scene_simulation_realtime.md) — Real-time simulation
- [`scene.simulation.realtimeModifier`](sim-2/property_scene_simulation_realtimeModifier.md) — Real-time modifier
- [`scene.simulation.removeNewObjects`](sim-2/property_scene_simulation_removeNewObjects.md) — Remove new objects
- [`scene.simulation.speedModifier`](sim-2/property_scene_simulation_speedModifier.md) — Speed modifier
- [`scene.simulation.state`](sim-2/property_scene_simulation_state.md) — Simulation state
- [`scene.simulation.stepCount`](sim-2/property_scene_simulation_stepCount.md) — Simulation steps
- [`scene.simulation.stepsPerRendering`](sim-2/property_scene_simulation_stepsPerRendering.md) — Steps per frame
- [`scene.simulation.time`](sim-2/property_scene_simulation_time.md) — Simulation time
- [`scene.simulation.timeStep`](sim-2/property_scene_simulation_timeStep.md) — Simulation dt
- [`scene.simulation.timeToPause`](sim-2/property_scene_simulation_timeToPause.md) — Simulation pause time
- [`scene.textures`](sim-2/property_scene_textures.md) — Textures
- [`scene.uid`](sim-2/property_scene_uid.md) — Scene UID
- [`scene.uidString`](sim-2/property_scene_uidString.md) — Scene UID string
- [`scene.visibilityLayers`](sim-2/property_scene_visibilityLayers.md) — Visibility layers

## <a id="methodsAndProperties_collection"></a><a id="methodsAndProperties_collections"></a>[collection](collections.md) (methods & properties)

- [`collection:addItem`](sim-2/collection_addItem.md) — Adds one or several items to the collection
- [`collection:changeColor`](sim-2/collection_changeColor.md) — Changes the color of all shapes in the collection
- [`collection:checkCollision`](sim-2/collection_checkCollision.md) — Checks collision with another entity
- [`collection:checkDistance`](sim-2/collection_checkDistance.md) — Checks minimum distance with another entity
- [`collection:remove`](sim-2/collection_remove.md) — Removes the collection
- [`collection:removeItem`](sim-2/collection_removeItem.md) — Removes one or several items from the collection
- [`collection:restoreColor`](sim-2/collection_restoreColor.md) — Restores the color of shapes in the collection
- [`app:createObject`](sim-2/app_createObject.md) — Creates various objects (collections, scripts, sensors, etc.)
- [`app:removeObjects`](sim-2/app_removeObjects.md) — Removes one or several objects
- [`scene:createObject`](sim-2/scene_createObject.md) — Creates various objects (collections, scripts, sensors, etc.)
- [`scene:removeObjects`](sim-2/scene_removeObjects.md) — Removes one or several objects
- [`collection.objects`](sim-2/property_collection_objects.md) — Children
- [`sceneObject.collectionSelfCollisionIndicator`](sim-2/property_sceneObject_collectionSelfCollisionIndicator.md) — Collection self-collision indicator

## <a id="methodsAndProperties_customObject"></a>customObject (methods & properties)

- [`customObject:makeObject`](sim-2/customObject_makeObject.md) — Instantiates a custom object from a class
- [`customObject:remove`](sim-2/customObject_remove.md) — Removes the custom scene object

## <a id="methodsAndProperties_script"></a>[script](scripts.md) (methods & properties)

- [`script:broadcast`](sim-2/script_broadcast.md) — Broadcasts a message to all other scripts
- [`script:callFunction`](sim-2/script_callFunction.md) — Calls a function
- [`script:callMethod`](sim-2/script_callMethod.md) — Calls a method
- [`script:cancelScheduledExecution`](sim-2/script_cancelScheduledExecution.md) — Cancels a scheduled function execution
- [`script:executeString`](sim-2/script_executeString.md) — Executes code from a string
- [`script:getFunctions`](sim-2/script_getFunctions.md) — Retrieves callable functions of the script
- [`script:getObject`](sim-2/script_getObject.md) — Retrieves an object by its path and name
- [`script:getStackTraceback`](sim-2/script_getStackTraceback.md) — Retrieves and clears the last stack traceback
- [`script:getStepping`](sim-2/script_getStepping.md) — Informs whether the stepping operation mode is enabled
- [`script:init`](sim-2/script_init.md) — Initializes/reinitializes the script
- [`script:lock`](sim-2/script_lock.md) — Acquires/releases a script lock to forbid yielding
- [`script:registerFunctionHook`](sim-2/script_registerFunctionHook.md) — Registers a function hook for callbacks
- [`script:remove`](sim-2/script_remove.md) — Removes the script
- [`script:removeFunctionHook`](sim-2/script_removeFunctionHook.md) — Removes a function hook
- [`script:reset`](sim-2/script_reset.md) — Resets/ends the script
- [`script:resume`](sim-2/script_resume.md) — Resumes the suspended script
- [`script:scheduleExecution`](sim-2/script_scheduleExecution.md) — Schedules a function for execution after a delay
- [`script:setEventFilters`](sim-2/script_setEventFilters.md) — Specifies filters for the sysCall_event callback
- [`script:setModuleEntry`](sim-2/script_setModuleEntry.md) — Creates/modifies/destroys module menu entries
- [`script:setStepping`](sim-2/script_setStepping.md) — Enables/disables stepping operation mode
- [`script:step`](sim-2/script_step.md) — Triggers the next simulation step
- [`script:suspend`](sim-2/script_suspend.md) — Suspends the script
- [`script:throttle`](sim-2/script_throttle.md) — Limits the rate of a function call
- [`script:wait`](sim-2/script_wait.md) — Waits for a certain amount of time
- [`script:yield`](sim-2/script_yield.md) — Identical to step()
- [`app:createObject`](sim-2/app_createObject.md) — Creates various objects (collections, scripts, sensors, etc.)
- [`app:handleAddOns`](sim-2/app_handleAddOns.md) — Calls a system callback in add-ons
- [`app:handleSandboxes`](sim-2/app_handleSandboxes.md) — Calls a system callback in the sandbox
- [`app:removeObjects`](sim-2/app_removeObjects.md) — Removes one or several objects
- [`scene:createObject`](sim-2/scene_createObject.md) — Creates various objects (collections, scripts, sensors, etc.)
- [`scene:removeObjects`](sim-2/scene_removeObjects.md) — Removes one or several objects
- [`app.luaSandbox`](sim-2/property_app_luaSandbox.md) — Lua sandbox
- [`app.sandbox2`](sim-2/property_app_sandbox2.md) — Python sandbox
- [`scene.mainScript`](sim-2/property_scene_mainScript.md) — Main script
- [`script.addOnMenuPath`](sim-2/property_script_addOnMenuPath.md) — Add-on menu path
- [`script.addOnPath`](sim-2/property_script_addOnPath.md) — Add-on path
- [`script.autoYieldDelay`](sim-2/property_script_autoYieldDelay.md) — Automatic yield delay
- [`script.code`](sim-2/property_script_code.md) — Code
- [`script.enabled`](sim-2/property_script_enabled.md) — Enabled
- [`script.execPriority`](sim-2/property_script_execPriority.md) — Execution priority
- [`script.executionDepth`](sim-2/property_script_executionDepth.md) — Execution depth
- [`script.language`](sim-2/property_script_language.md) — Language
- [`script.restartOnError`](sim-2/property_script_restartOnError.md) — Restart
- [`script.script.type`](sim-2/property_script_script_type.md) — Type
- [`script.scriptName`](sim-2/property_script_scriptName.md) — Name
- [`script.state`](sim-2/property_script_state.md) — State
- [`scriptObject.script`](sim-2/property_scriptObject_script.md) — Script

## <a id="methodsAndProperties_mesh"></a>[mesh](geometryDialog.md) (methods & properties)

- [`mesh:setTexture`](sim-2/mesh_setTexture.md) — Sets a texture
- [`mesh.color.diffuse`](sim-2/property_mesh_color_diffuse.md) — Diffuse color
- [`mesh.color.emission`](sim-2/property_mesh_color_emission.md) — Emission color
- [`mesh.color.specular`](sim-2/property_mesh_color_specular.md) — Specular color
- [`mesh.color.transparency`](sim-2/property_mesh_color_transparency.md) — Transparency
- [`mesh.colorName`](sim-2/property_mesh_colorName.md) — Color name
- [`mesh.convex`](sim-2/property_mesh_convex.md) — Convex
- [`mesh.culling`](sim-2/property_mesh_culling.md) — Backface culling
- [`mesh.indices`](sim-2/property_mesh_indices.md) — Indices
- [`mesh.normals`](sim-2/property_mesh_normals.md) — Normals
- [`mesh.primitive`](sim-2/property_mesh_primitive.md) — Primitive type
- [`mesh.shadingAngle`](sim-2/property_mesh_shadingAngle.md) — Shading angle
- [`mesh.shape`](sim-2/property_mesh_shape.md) — Shape
- [`mesh.shapeUid`](sim-2/property_mesh_shapeUid.md) — Shape UID
- [`mesh.showEdges`](sim-2/property_mesh_showEdges.md) — Visible edges
- [`mesh.texture.applyMode`](sim-2/property_mesh_texture_applyMode.md) — Texture apply mode
- [`mesh.texture.interpolate`](sim-2/property_mesh_texture_interpolate.md) — Interpolate texture
- [`mesh.texture.repeatU`](sim-2/property_mesh_texture_repeatU.md) — Texture repeat U
- [`mesh.texture.repeatV`](sim-2/property_mesh_texture_repeatV.md) — Texture repeat V
- [`mesh.texture.textureData`](sim-2/property_mesh_texture_textureData.md) — Texture
- [`mesh.textureCoordinates`](sim-2/property_mesh_textureCoordinates.md) — Texture coordinates
- [`mesh.vertices`](sim-2/property_mesh_vertices.md) — Vertices
- [`mesh.wireframe`](sim-2/property_mesh_wireframe.md) — Wireframe

## <a id="methodsAndProperties_textureData"></a><a id="methodsAndProperties_textures"></a>[textureData](textureDialog.md) (methods & properties)

- [`app:loadImage`](sim-2/app_loadImage.md) — Loads an image from file
- [`app:loadImageFromBuffer`](sim-2/app_loadImageFromBuffer.md) — Loads an image from memory
- [`app:saveImage`](sim-2/app_saveImage.md) — Saves an image to file
- [`app:saveImageToBuffer`](sim-2/app_saveImageToBuffer.md) — Saves an image to a buffer
- [`app:transformBuffer`](sim-2/app_transformBuffer.md) — Modifies a buffer (format, scale, offset)
- [`app:transformImage`](sim-2/app_transformImage.md) — Transforms an image (scaling, flipping)
- [`mesh:setTexture`](sim-2/mesh_setTexture.md) — Sets a texture
- [`textureData:getData`](sim-2/textureData_getData.md) — Reads a portion of the texture
- [`textureData:remove`](sim-2/textureData_remove.md) — Removes the texture
- [`textureData:setData`](sim-2/textureData_setData.md) — Overwrites a portion of the texture
- [`mesh.texture.applyMode`](sim-2/property_mesh_texture_applyMode.md) — Texture apply mode
- [`mesh.texture.interpolate`](sim-2/property_mesh_texture_interpolate.md) — Interpolate texture
- [`mesh.texture.repeatU`](sim-2/property_mesh_texture_repeatU.md) — Texture repeat U
- [`mesh.texture.repeatV`](sim-2/property_mesh_texture_repeatV.md) — Texture repeat V
- [`mesh.texture.textureData`](sim-2/property_mesh_texture_textureData.md) — Texture
- [`mesh.textureCoordinates`](sim-2/property_mesh_textureCoordinates.md) — Texture coordinates
- [`scene.textures`](sim-2/property_scene_textures.md) — Textures
- [`textureData.image`](sim-2/property_textureData_image.md) — Image
- [`textureData.resolution`](sim-2/property_textureData_resolution.md) — Resolution

## <a id="methodsAndProperties_sceneObject"></a><a id="methodsAndProperties_sceneObjectFunctionality"></a>[sceneObject](objects.md) (methods & properties)

- [`app:removeObjects`](sim-2/app_removeObjects.md) — Removes one or several objects
- [`scene:copyObjects`](sim-2/scene_copyObjects.md) — Copies selected objects
- [`scene:cutObjects`](sim-2/scene_cutObjects.md) — Cuts selected objects
- [`scene:duplicateObjects`](sim-2/scene_duplicateObjects.md) — Duplicates scene objects
- [`scene:pasteObjects`](sim-2/scene_pasteObjects.md) — Pastes objects
- [`scene:removeObjects`](sim-2/scene_removeObjects.md) — Removes one or several objects
- [`sceneObject:changeColor`](sim-2/sceneObject_changeColor.md) — Changes the color of the object (if shape)
- [`sceneObject:checkCollision`](sim-2/sceneObject_checkCollision.md) — Checks collision with another entity
- [`sceneObject:checkDistance`](sim-2/sceneObject_checkDistance.md) — Checks minimum distance with another entity
- [`sceneObject:dynamicReset`](sim-2/sceneObject_dynamicReset.md) — Dynamically resets the object in the physics engine
- [`sceneObject:getAncestors`](sim-2/sceneObject_getAncestors.md) — Retrieves ancestor scene objects
- [`sceneObject:getDescendants`](sim-2/sceneObject_getDescendants.md) — Retrieves descendant scene objects
- [`sceneObject:getName`](sim-2/sceneObject_getName.md) — Retrieves the name or path of the object
- [`sceneObject:getObject`](sim-2/sceneObject_getObject.md) — Retrieves an object by its path and name
- [`sceneObject:getPose`](sim-2/sceneObject_getPose.md) — Retrieves the pose of the scene object
- [`sceneObject:getPosition`](sim-2/sceneObject_getPosition.md) — Retrieves the position of the scene object
- [`sceneObject:getQuaternion`](sim-2/sceneObject_getQuaternion.md) — Retrieves the quaternion of the scene object
- [`sceneObject:makeClass`](sim-2/sceneObject_makeClass.md) — Creates a class from this object
- [`sceneObject:makeObject`](sim-2/sceneObject_makeObject.md) — Instantiates a customized scene object from a class
- [`sceneObject:remove`](sim-2/sceneObject_remove.md) — Removes the object from the scene
- [`sceneObject:removeModel`](sim-2/sceneObject_removeModel.md) — Removes the model from the scene
- [`sceneObject:restoreColor`](sim-2/sceneObject_restoreColor.md) — Restores the object's color (if shape)
- [`sceneObject:saveModel`](sim-2/sceneObject_saveModel.md) — Saves this model to a file
- [`sceneObject:saveModelToBuffer`](sim-2/sceneObject_saveModelToBuffer.md) — Serializes this model to a buffer
- [`sceneObject:scale`](sim-2/sceneObject_scale.md) — Scales the object non-isometrically
- [`sceneObject:scaleTree`](sim-2/sceneObject_scaleTree.md) — Scales the object tree isometrically
- [`sceneObject:setParent`](sim-2/sceneObject_setParent.md) — Sets the object's parent
- [`sceneObject:setPose`](sim-2/sceneObject_setPose.md) — Sets the pose of the scene object
- [`sceneObject:setPosition`](sim-2/sceneObject_setPosition.md) — Sets the position of the scene object
- [`sceneObject:setQuaternion`](sim-2/sceneObject_setQuaternion.md) — Sets the quaternion of the scene object
- [`sceneObject.angularVelocity`](sim-2/property_sceneObject_angularVelocity.md) — Angular velocity
- [`sceneObject.bbPose`](sim-2/property_sceneObject_bbPose.md) — Bounding box pose
- [`sceneObject.cannotDelete`](sim-2/property_sceneObject_cannotDelete.md) — Cannot delete
- [`sceneObject.cannotDeleteInSim`](sim-2/property_sceneObject_cannotDeleteInSim.md) — Cannot delete during simulation
- [`sceneObject.childOrder`](sim-2/property_sceneObject_childOrder.md) — Child order
- [`sceneObject.children`](sim-2/property_sceneObject_children.md) — Children
- [`sceneObject.collapsed`](sim-2/property_sceneObject_collapsed.md) — Collapsed hierarchy
- [`sceneObject.collectionSelfCollisionIndicator`](sim-2/property_sceneObject_collectionSelfCollisionIndicator.md) — Collection self-collision indicator
- [`sceneObject.collidable`](sim-2/property_sceneObject_collidable.md) — Collidable
- [`sceneObject.depthInvisible`](sim-2/property_sceneObject_depthInvisible.md) — Depth pass invisible
- [`sceneObject.detectable`](sim-2/property_sceneObject_detectable.md) — Detectable
- [`sceneObject.dimension`](sim-2/property_sceneObject_dimension.md) — Bounding box size
- [`sceneObject.dna`](sim-2/property_sceneObject_dna.md) — DNA
- [`sceneObject.dynamicFlag`](sim-2/property_sceneObject_dynamicFlag.md) — Dynamic flag
- [`sceneObject.dynamicIcon`](sim-2/property_sceneObject_dynamicIcon.md) — Dynamic icon
- [`sceneObject.dynamicallyEnabled`](sim-2/property_sceneObject_dynamicallyEnabled.md) — Dynamically enabled
- [`sceneObject.eulerAngles`](sim-2/property_sceneObject_eulerAngles.md) — Euler angles
- [`sceneObject.hideFromModelBB`](sim-2/property_sceneObject_hideFromModelBB.md) — Hide from model bounding box
- [`sceneObject.hierarchyColor`](sim-2/property_sceneObject_hierarchyColor.md) — Hierarchy color
- [`sceneObject.ignoreViewFitting`](sim-2/property_sceneObject_ignoreViewFitting.md) — Ignore view fitting
- [`sceneObject.layer`](sim-2/property_sceneObject_layer.md) — Visibility layer
- [`sceneObject.linearVelocity`](sim-2/property_sceneObject_linearVelocity.md) — Linear velocity
- [`sceneObject.measurable`](sim-2/property_sceneObject_measurable.md) — Measurable
- [`sceneObject.model.bbPos`](sim-2/property_sceneObject_model_bbPos.md) — Model bounding box position
- [`sceneObject.model.bbSize`](sim-2/property_sceneObject_model_bbSize.md) — Model bounding box size
- [`sceneObject.model.notCollidable`](sim-2/property_sceneObject_model_notCollidable.md) — Model not collidable
- [`sceneObject.model.notDetectable`](sim-2/property_sceneObject_model_notDetectable.md) — Model not detectable
- [`sceneObject.model.notDynamic`](sim-2/property_sceneObject_model_notDynamic.md) — Model not dynamic
- [`sceneObject.model.notInParentBB`](sim-2/property_sceneObject_model_notInParentBB.md) — Model invisible to other models' bounding boxes
- [`sceneObject.model.notMeasurable`](sim-2/property_sceneObject_model_notMeasurable.md) — Model not measurable
- [`sceneObject.model.notRespondable`](sim-2/property_sceneObject_model_notRespondable.md) — Model not respondable
- [`sceneObject.model.notVisible`](sim-2/property_sceneObject_model_notVisible.md) — Model not visible
- [`sceneObject.model.propertyFlags`](sim-2/property_sceneObject_model_propertyFlags.md) — Model flags
- [`sceneObject.model.scriptsNotActive`](sim-2/property_sceneObject_model_scriptsNotActive.md) — Model scripts inactive
- [`sceneObject.modelAcknowledgment`](sim-2/property_sceneObject_modelAcknowledgment.md) — Acknowledgment
- [`sceneObject.modelBase`](sim-2/property_sceneObject_modelBase.md) — Model base
- [`sceneObject.modelHash`](sim-2/property_sceneObject_modelHash.md) — Model hash
- [`sceneObject.modelInvisible`](sim-2/property_sceneObject_modelInvisible.md) — Inherited model invisibility
- [`sceneObject.mov.altRot`](sim-2/property_sceneObject_mov_altRot.md) — Alternate rotation axes enabled
- [`sceneObject.mov.altTransl`](sim-2/property_sceneObject_mov_altTransl.md) — Alternate translation axes enabled
- [`sceneObject.mov.optionsFlags`](sim-2/property_sceneObject_mov_optionsFlags.md) — Movement flags
- [`sceneObject.mov.prefRotX`](sim-2/property_sceneObject_mov_prefRotX.md) — Preferred X-axis rotation
- [`sceneObject.mov.prefRotY`](sim-2/property_sceneObject_mov_prefRotY.md) — Preferred Y-axis rotation
- [`sceneObject.mov.prefRotZ`](sim-2/property_sceneObject_mov_prefRotZ.md) — Preferred Z-axis rotation
- [`sceneObject.mov.prefTranslX`](sim-2/property_sceneObject_mov_prefTranslX.md) — Preferred X-translation
- [`sceneObject.mov.prefTranslY`](sim-2/property_sceneObject_mov_prefTranslY.md) — Preferred Y-translation
- [`sceneObject.mov.prefTranslZ`](sim-2/property_sceneObject_mov_prefTranslZ.md) — Preferred Z-translation
- [`sceneObject.mov.preferredAxesFlags`](sim-2/property_sceneObject_mov_preferredAxesFlags.md) — Preferred axes
- [`sceneObject.mov.relativity`](sim-2/property_sceneObject_mov_relativity.md) — Movement relativity
- [`sceneObject.mov.rotInSim`](sim-2/property_sceneObject_mov_rotInSim.md) — Rotation enabled during simulation
- [`sceneObject.mov.rotNoSim`](sim-2/property_sceneObject_mov_rotNoSim.md) — Rotation enabled
- [`sceneObject.mov.stepSize`](sim-2/property_sceneObject_mov_stepSize.md) — Movement step sizes
- [`sceneObject.mov.translInSim`](sim-2/property_sceneObject_mov_translInSim.md) — Translation enabled during simulation
- [`sceneObject.mov.translNoSim`](sim-2/property_sceneObject_mov_translNoSim.md) — Translation enabled
- [`sceneObject.name`](sim-2/property_sceneObject_name.md) — Name
- [`sceneObject.objectPropertyFlags`](sim-2/property_sceneObject_objectPropertyFlags.md) — Object flags
- [`sceneObject.parent`](sim-2/property_sceneObject_parent.md) — Parent
- [`sceneObject.parentUid`](sim-2/property_sceneObject_parentUid.md) — Parent UID
- [`sceneObject.persistentUid`](sim-2/property_sceneObject_persistentUid.md) — Persistent UID
- [`sceneObject.pose`](sim-2/property_sceneObject_pose.md) — Pose
- [`sceneObject.position`](sim-2/property_sceneObject_position.md) — Position
- [`sceneObject.quaternion`](sim-2/property_sceneObject_quaternion.md) — Quaternion
- [`sceneObject.selectInvisible`](sim-2/property_sceneObject_selectInvisible.md) — Select invisible
- [`sceneObject.selectModel`](sim-2/property_sceneObject_selectModel.md) — Select model instead
- [`sceneObject.selectable`](sim-2/property_sceneObject_selectable.md) — Selectable
- [`sceneObject.selected`](sim-2/property_sceneObject_selected.md) — Selected
- [`sceneObject.tree`](sim-2/property_sceneObject_tree.md) — Object tree
- [`sceneObject.uid`](sim-2/property_sceneObject_uid.md) — Object UID
- [`sceneObject.visible`](sim-2/property_sceneObject_visible.md) — Visible
- [`sceneObject.worldEulerAngles`](sim-2/property_sceneObject_worldEulerAngles.md) — Euler angles
- [`sceneObject.worldPose`](sim-2/property_sceneObject_worldPose.md) — Pose
- [`sceneObject.worldPosition`](sim-2/property_sceneObject_worldPosition.md) — Position
- [`sceneObject.worldQuaternion`](sim-2/property_sceneObject_worldQuaternion.md) — Quaternion

## <a id="methodsAndProperties_shape"></a><a id="methodsAndProperties_shapeObject"></a>[shape](shapes.md) (methods & properties)

- [`shape:alignBoundingBox`](sim-2/shape_alignBoundingBox.md) — Reorients the shape's bounding box
- [`shape:divide`](sim-2/shape_divide.md) — Divides a simple shape into separate ones
- [`shape:getAppearance`](sim-2/shape_getAppearance.md) — Fetches the shape's main appearance properties
- [`shape:relocateFrame`](sim-2/shape_relocateFrame.md) — Repositions/reorients the shape's reference frame
- [`shape:setAppearance`](sim-2/shape_setAppearance.md) — Sets the shape's main appearance properties
- [`shape:ungroup`](sim-2/shape_ungroup.md) — Ungroups a compound shape
- [`app:createObject`](sim-2/app_createObject.md) — Creates various objects (collections, scripts, sensors, etc.)
- [`collection:changeColor`](sim-2/collection_changeColor.md) — Changes the color of all shapes in the collection
- [`collection:restoreColor`](sim-2/collection_restoreColor.md) — Restores the color of shapes in the collection
- [`mesh:setTexture`](sim-2/mesh_setTexture.md) — Sets a texture
- [`ocTree:addFromObjects`](sim-2/ocTree_addFromObjects.md) — Adds voxels from scene objects
- [`ocTree:subtractFromObjects`](sim-2/ocTree_subtractFromObjects.md) — Subtracts voxels using scene objects
- [`pointCloud:addFromObjects`](sim-2/pointCloud_addFromObjects.md) — Adds points from scene objects
- [`pointCloud:subtractFromObjects`](sim-2/pointCloud_subtractFromObjects.md) — Subtracts points using scene objects
- [`scene:createObject`](sim-2/scene_createObject.md) — Creates various objects (collections, scripts, sensors, etc.)
- [`scene:groupShapes`](sim-2/scene_groupShapes.md) — Groups shapes into a compound shape
- [`scene:mergeShapes`](sim-2/scene_mergeShapes.md) — Merges several shapes
- [`sceneObject:changeColor`](sim-2/sceneObject_changeColor.md) — Changes the color of the object (if shape)
- [`sceneObject:restoreColor`](sim-2/sceneObject_restoreColor.md) — Restores the object's color (if shape)
- [`shape.dynamics:addForce`](sim-2/shape_dynamics_addForce.md) — Applies a force to the dynamically enabled shape
- [`shape.dynamics:addTorque`](sim-2/shape_dynamics_addTorque.md) — Applies a torque to the dynamically enabled shape
- [`shape.dynamics:computeInertia`](sim-2/shape_dynamics_computeInertia.md) — Computes and applies mass/inertia properties
- [`shape.dynamics:getContacts`](sim-2/shape_dynamics_getContacts.md) — Retrieves the shape's contact information
- [`shape.dynamics:getInertia`](sim-2/shape_dynamics_getInertia.md) — Retrieves the shape's inertia information
- [`shape.dynamics:setInertia`](sim-2/shape_dynamics_setInertia.md) — Applies a new inertia matrix
- [`textureData:getData`](sim-2/textureData_getData.md) — Reads a portion of the texture
- [`textureData:setData`](sim-2/textureData_setData.md) — Overwrites a portion of the texture
- [`scene.saveCalculationStructs`](sim-2/property_scene_saveCalculationStructs.md) — Save calculation structures
- [`shape.applyColor.diffuse`](sim-2/property_shape_applyColor_diffuse.md) — Apply diffuse color
- [`shape.applyColor.emission`](sim-2/property_shape_applyColor_emission.md) — Apply emission color
- [`shape.applyColor.specular`](sim-2/property_shape_applyColor_specular.md) — Apply specular color
- [`shape.applyColor.transparency`](sim-2/property_shape_applyColor_transparency.md) — Apply transparency
- [`shape.applyCulling`](sim-2/property_shape_applyCulling.md) — Apply culling
- [`shape.applyShadingAngle`](sim-2/property_shape_applyShadingAngle.md) — Apply shading
- [`shape.applyShowEdges`](sim-2/property_shape_applyShowEdges.md) — Apply edges
- [`shape.compound`](sim-2/property_shape_compound.md) — Compound
- [`shape.compoundColors.diffuse`](sim-2/property_shape_compoundColors_diffuse.md) — Diffuse color data
- [`shape.compoundColors.emission`](sim-2/property_shape_compoundColors_emission.md) — Emission color data
- [`shape.compoundColors.specular`](sim-2/property_shape_compoundColors_specular.md) — Specular color data
- [`shape.compoundColors.transparency`](sim-2/property_shape_compoundColors_transparency.md) — Transparency data
- [`shape.compoundCullings`](sim-2/property_shape_compoundCullings.md) — Culling data
- [`shape.compoundEdges`](sim-2/property_shape_compoundEdges.md) — Edge visibility data
- [`shape.compoundShadingAngles`](sim-2/property_shape_compoundShadingAngles.md) — Shading angle data
- [`shape.compoundWireframe`](sim-2/property_shape_compoundWireframe.md) — Wireframe data
- [`shape.convex`](sim-2/property_shape_convex.md) — Convex
- [`shape.dynamics.angularVelocity`](sim-2/property_shape_dynamics_angularVelocity.md) — Rotational velocity
- [`shape.dynamics.bullet.angularDamping`](sim-2/property_shape_dynamics_bullet_angularDamping.md)
- [`shape.dynamics.bullet.autoShrinkConvexMeshes`](sim-2/property_shape_dynamics_bullet_autoShrinkConvexMeshes.md)
- [`shape.dynamics.bullet.customCollisionMarginConvexEnabled`](sim-2/property_shape_dynamics_bullet_customCollisionMarginConvexEnabled.md)
- [`shape.dynamics.bullet.customCollisionMarginConvexValue`](sim-2/property_shape_dynamics_bullet_customCollisionMarginConvexValue.md)
- [`shape.dynamics.bullet.customCollisionMarginEnabled`](sim-2/property_shape_dynamics_bullet_customCollisionMarginEnabled.md)
- [`shape.dynamics.bullet.customCollisionMarginValue`](sim-2/property_shape_dynamics_bullet_customCollisionMarginValue.md)
- [`shape.dynamics.bullet.friction`](sim-2/property_shape_dynamics_bullet_friction.md)
- [`shape.dynamics.bullet.frictionOld`](sim-2/property_shape_dynamics_bullet_frictionOld.md)
- [`shape.dynamics.bullet.linearDamping`](sim-2/property_shape_dynamics_bullet_linearDamping.md)
- [`shape.dynamics.bullet.restitution`](sim-2/property_shape_dynamics_bullet_restitution.md)
- [`shape.dynamics.bullet.stickyContact`](sim-2/property_shape_dynamics_bullet_stickyContact.md)
- [`shape.dynamics.centerOfMass`](sim-2/property_shape_dynamics_centerOfMass.md) — Center of mass
- [`shape.dynamics.dynamic`](sim-2/property_shape_dynamics_dynamic.md) — Dynamic
- [`shape.dynamics.engineProperties`](sim-2/property_shape_dynamics_engineProperties.md) — Engine properties
- [`shape.dynamics.inertiaMatrix`](sim-2/property_shape_dynamics_inertiaMatrix.md) — Inertia matrix
- [`shape.dynamics.initAngularVelocity`](sim-2/property_shape_dynamics_initAngularVelocity.md) — Initial rotational velocity
- [`shape.dynamics.initLinearVelocity`](sim-2/property_shape_dynamics_initLinearVelocity.md) — Initial linear velocity
- [`shape.dynamics.kinematic`](sim-2/property_shape_dynamics_kinematic.md) — Kinematic
- [`shape.dynamics.linearVelocity`](sim-2/property_shape_dynamics_linearVelocity.md) — Linear velocity
- [`shape.dynamics.mass`](sim-2/property_shape_dynamics_mass.md) — Mass
- [`shape.dynamics.mujoco.adhesion`](sim-2/property_shape_dynamics_mujoco_adhesion.md)
- [`shape.dynamics.mujoco.adhesionctrl`](sim-2/property_shape_dynamics_mujoco_adhesionctrl.md)
- [`shape.dynamics.mujoco.adhesionctrlrange`](sim-2/property_shape_dynamics_mujoco_adhesionctrlrange.md)
- [`shape.dynamics.mujoco.adhesionforcelimited`](sim-2/property_shape_dynamics_mujoco_adhesionforcelimited.md)
- [`shape.dynamics.mujoco.adhesionforcerange`](sim-2/property_shape_dynamics_mujoco_adhesionforcerange.md)
- [`shape.dynamics.mujoco.adhesiongain`](sim-2/property_shape_dynamics_mujoco_adhesiongain.md)
- [`shape.dynamics.mujoco.condim`](sim-2/property_shape_dynamics_mujoco_condim.md)
- [`shape.dynamics.mujoco.friction`](sim-2/property_shape_dynamics_mujoco_friction.md)
- [`shape.dynamics.mujoco.gap`](sim-2/property_shape_dynamics_mujoco_gap.md)
- [`shape.dynamics.mujoco.gravcomp`](sim-2/property_shape_dynamics_mujoco_gravcomp.md)
- [`shape.dynamics.mujoco.margin`](sim-2/property_shape_dynamics_mujoco_margin.md)
- [`shape.dynamics.mujoco.priority`](sim-2/property_shape_dynamics_mujoco_priority.md)
- [`shape.dynamics.mujoco.solimp`](sim-2/property_shape_dynamics_mujoco_solimp.md)
- [`shape.dynamics.mujoco.solmix`](sim-2/property_shape_dynamics_mujoco_solmix.md)
- [`shape.dynamics.mujoco.solref`](sim-2/property_shape_dynamics_mujoco_solref.md)
- [`shape.dynamics.newton.angularDrag`](sim-2/property_shape_dynamics_newton_angularDrag.md)
- [`shape.dynamics.newton.fastMoving`](sim-2/property_shape_dynamics_newton_fastMoving.md)
- [`shape.dynamics.newton.kineticFriction`](sim-2/property_shape_dynamics_newton_kineticFriction.md)
- [`shape.dynamics.newton.linearDrag`](sim-2/property_shape_dynamics_newton_linearDrag.md)
- [`shape.dynamics.newton.restitution`](sim-2/property_shape_dynamics_newton_restitution.md)
- [`shape.dynamics.newton.staticFriction`](sim-2/property_shape_dynamics_newton_staticFriction.md)
- [`shape.dynamics.ode.angularDamping`](sim-2/property_shape_dynamics_ode_angularDamping.md)
- [`shape.dynamics.ode.friction`](sim-2/property_shape_dynamics_ode_friction.md)
- [`shape.dynamics.ode.linearDamping`](sim-2/property_shape_dynamics_ode_linearDamping.md)
- [`shape.dynamics.ode.maxContacts`](sim-2/property_shape_dynamics_ode_maxContacts.md)
- [`shape.dynamics.ode.softCfm`](sim-2/property_shape_dynamics_ode_softCfm.md)
- [`shape.dynamics.ode.softErp`](sim-2/property_shape_dynamics_ode_softErp.md)
- [`shape.dynamics.pmi`](sim-2/property_shape_dynamics_pmi.md) — Principal moment of inertia
- [`shape.dynamics.pmiQuaternion`](sim-2/property_shape_dynamics_pmiQuaternion.md) — Quaternion of the principal moment of inertia
- [`shape.dynamics.respondable`](sim-2/property_shape_dynamics_respondable.md) — Respondable
- [`shape.dynamics.respondableMask`](sim-2/property_shape_dynamics_respondableMask.md) — Respondable mask
- [`shape.dynamics.setToDynamicWithParent`](sim-2/property_shape_dynamics_setToDynamicWithParent.md) — Set to dynamic if gets parent
- [`shape.dynamics.startInSleepMode`](sim-2/property_shape_dynamics_startInSleepMode.md) — Start in sleep mode
- [`shape.dynamics.vortex.adhesiveForce`](sim-2/property_shape_dynamics_vortex_adhesiveForce.md)
- [`shape.dynamics.vortex.angularNormalAxisFollowPrimaryAxis`](sim-2/property_shape_dynamics_vortex_angularNormalAxisFollowPrimaryAxis.md)
- [`shape.dynamics.vortex.angularNormalAxisFrictionModel`](sim-2/property_shape_dynamics_vortex_angularNormalAxisFrictionModel.md)
- [`shape.dynamics.vortex.angularNormalAxisFrictionValue`](sim-2/property_shape_dynamics_vortex_angularNormalAxisFrictionValue.md)
- [`shape.dynamics.vortex.angularNormalAxisSlide`](sim-2/property_shape_dynamics_vortex_angularNormalAxisSlide.md)
- [`shape.dynamics.vortex.angularNormalAxisSlip`](sim-2/property_shape_dynamics_vortex_angularNormalAxisSlip.md)
- [`shape.dynamics.vortex.angularNormalAxisStaticFrictionScale`](sim-2/property_shape_dynamics_vortex_angularNormalAxisStaticFrictionScale.md)
- [`shape.dynamics.vortex.angularPrimaryAxisFrictionModel`](sim-2/property_shape_dynamics_vortex_angularPrimaryAxisFrictionModel.md)
- [`shape.dynamics.vortex.angularPrimaryAxisFrictionValue`](sim-2/property_shape_dynamics_vortex_angularPrimaryAxisFrictionValue.md)
- [`shape.dynamics.vortex.angularPrimaryAxisSlide`](sim-2/property_shape_dynamics_vortex_angularPrimaryAxisSlide.md)
- [`shape.dynamics.vortex.angularPrimaryAxisSlip`](sim-2/property_shape_dynamics_vortex_angularPrimaryAxisSlip.md)
- [`shape.dynamics.vortex.angularPrimaryAxisStaticFrictionScale`](sim-2/property_shape_dynamics_vortex_angularPrimaryAxisStaticFrictionScale.md)
- [`shape.dynamics.vortex.angularSecondaryAxisFollowPrimaryAxis`](sim-2/property_shape_dynamics_vortex_angularSecondaryAxisFollowPrimaryAxis.md)
- [`shape.dynamics.vortex.angularSecondaryAxisFrictionModel`](sim-2/property_shape_dynamics_vortex_angularSecondaryAxisFrictionModel.md)
- [`shape.dynamics.vortex.angularSecondaryAxisFrictionValue`](sim-2/property_shape_dynamics_vortex_angularSecondaryAxisFrictionValue.md)
- [`shape.dynamics.vortex.angularSecondaryAxisSlide`](sim-2/property_shape_dynamics_vortex_angularSecondaryAxisSlide.md)
- [`shape.dynamics.vortex.angularSecondaryAxisSlip`](sim-2/property_shape_dynamics_vortex_angularSecondaryAxisSlip.md)
- [`shape.dynamics.vortex.angularSecondaryAxisStaticFrictionScale`](sim-2/property_shape_dynamics_vortex_angularSecondaryAxisStaticFrictionScale.md)
- [`shape.dynamics.vortex.angularVelDamping`](sim-2/property_shape_dynamics_vortex_angularVelDamping.md)
- [`shape.dynamics.vortex.autoAngularDampingEnabled`](sim-2/property_shape_dynamics_vortex_autoAngularDampingEnabled.md)
- [`shape.dynamics.vortex.autoAngularDampingTensionRatio`](sim-2/property_shape_dynamics_vortex_autoAngularDampingTensionRatio.md)
- [`shape.dynamics.vortex.autoSleepThresholdAngularAccel`](sim-2/property_shape_dynamics_vortex_autoSleepThresholdAngularAccel.md)
- [`shape.dynamics.vortex.autoSleepThresholdAngularSpeed`](sim-2/property_shape_dynamics_vortex_autoSleepThresholdAngularSpeed.md)
- [`shape.dynamics.vortex.autoSleepThresholdLinearAccel`](sim-2/property_shape_dynamics_vortex_autoSleepThresholdLinearAccel.md)
- [`shape.dynamics.vortex.autoSleepThresholdLinearSpeed`](sim-2/property_shape_dynamics_vortex_autoSleepThresholdLinearSpeed.md)
- [`shape.dynamics.vortex.autoSleepThresholdSteps`](sim-2/property_shape_dynamics_vortex_autoSleepThresholdSteps.md)
- [`shape.dynamics.vortex.autoSlip`](sim-2/property_shape_dynamics_vortex_autoSlip.md)
- [`shape.dynamics.vortex.compliance`](sim-2/property_shape_dynamics_vortex_compliance.md)
- [`shape.dynamics.vortex.convexAsRandom`](sim-2/property_shape_dynamics_vortex_convexAsRandom.md)
- [`shape.dynamics.vortex.damping`](sim-2/property_shape_dynamics_vortex_damping.md)
- [`shape.dynamics.vortex.fastMoving`](sim-2/property_shape_dynamics_vortex_fastMoving.md)
- [`shape.dynamics.vortex.linearPrimaryAxisFrictionModel`](sim-2/property_shape_dynamics_vortex_linearPrimaryAxisFrictionModel.md)
- [`shape.dynamics.vortex.linearPrimaryAxisFrictionValue`](sim-2/property_shape_dynamics_vortex_linearPrimaryAxisFrictionValue.md)
- [`shape.dynamics.vortex.linearPrimaryAxisSlide`](sim-2/property_shape_dynamics_vortex_linearPrimaryAxisSlide.md)
- [`shape.dynamics.vortex.linearPrimaryAxisSlip`](sim-2/property_shape_dynamics_vortex_linearPrimaryAxisSlip.md)
- [`shape.dynamics.vortex.linearPrimaryAxisStaticFrictionScale`](sim-2/property_shape_dynamics_vortex_linearPrimaryAxisStaticFrictionScale.md)
- [`shape.dynamics.vortex.linearPrimaryValue`](sim-2/property_shape_dynamics_vortex_linearPrimaryValue.md)
- [`shape.dynamics.vortex.linearSecondaryAxisFollowPrimaryAxis`](sim-2/property_shape_dynamics_vortex_linearSecondaryAxisFollowPrimaryAxis.md)
- [`shape.dynamics.vortex.linearSecondaryAxisFrictionModel`](sim-2/property_shape_dynamics_vortex_linearSecondaryAxisFrictionModel.md)
- [`shape.dynamics.vortex.linearSecondaryAxisFrictionValue`](sim-2/property_shape_dynamics_vortex_linearSecondaryAxisFrictionValue.md)
- [`shape.dynamics.vortex.linearSecondaryAxisSlide`](sim-2/property_shape_dynamics_vortex_linearSecondaryAxisSlide.md)
- [`shape.dynamics.vortex.linearSecondaryAxisSlip`](sim-2/property_shape_dynamics_vortex_linearSecondaryAxisSlip.md)
- [`shape.dynamics.vortex.linearSecondaryAxisStaticFrictionScale`](sim-2/property_shape_dynamics_vortex_linearSecondaryAxisStaticFrictionScale.md)
- [`shape.dynamics.vortex.linearVelDamping`](sim-2/property_shape_dynamics_vortex_linearVelDamping.md)
- [`shape.dynamics.vortex.materialUniqueId`](sim-2/property_shape_dynamics_vortex_materialUniqueId.md)
- [`shape.dynamics.vortex.primitiveAsConvex`](sim-2/property_shape_dynamics_vortex_primitiveAsConvex.md)
- [`shape.dynamics.vortex.randomAsTerrain`](sim-2/property_shape_dynamics_vortex_randomAsTerrain.md)
- [`shape.dynamics.vortex.restitution`](sim-2/property_shape_dynamics_vortex_restitution.md)
- [`shape.dynamics.vortex.restitutionThreshold`](sim-2/property_shape_dynamics_vortex_restitutionThreshold.md)
- [`shape.dynamics.vortex.skinThickness`](sim-2/property_shape_dynamics_vortex_skinThickness.md)
- [`shape.flipFaces`](sim-2/property_shape_flipFaces.md) — Flip faces
- [`shape.meshes`](sim-2/property_shape_meshes.md) — Meshes
- [`shape.primitive`](sim-2/property_shape_primitive.md) — Primitive

## <a id="methodsAndProperties_joint"></a><a id="methodsAndProperties_jointObject"></a>[joint](joints.md) (methods & properties)

- [`joint:setTargetPosition`](sim-2/joint_setTargetPosition.md) — Sets the joint's desired linear/angular position
- [`joint:setTargetVelocity`](sim-2/joint_setTargetVelocity.md) — Sets the joint's desired linear/angular velocity
- [`app:createObject`](sim-2/app_createObject.md) — Creates various objects (collections, scripts, sensors, etc.)
- [`scene:createObject`](sim-2/scene_createObject.md) — Creates various objects (collections, scripts, sensors, etc.)
- [`joint.bounds`](sim-2/property_joint_bounds.md) — Bounds
- [`joint.color.diffuse`](sim-2/property_joint_color_diffuse.md) — Diffuse color
- [`joint.color.emission`](sim-2/property_joint_color_emission.md) — Emission color
- [`joint.color.specular`](sim-2/property_joint_color_specular.md) — Specular color
- [`joint.configuration`](sim-2/property_joint_configuration.md) — Configuration
- [`joint.cyclic`](sim-2/property_joint_cyclic.md) — Cyclic
- [`joint.dependencyMaster`](sim-2/property_joint_dependencyMaster.md) — Dependency master
- [`joint.dependencyParams`](sim-2/property_joint_dependencyParams.md) — Dependency parameters
- [`joint.diameter`](sim-2/property_joint_diameter.md) — Diameter
- [`joint.dynamics.averageForce`](sim-2/property_joint_dynamics_averageForce.md) — Average force
- [`joint.dynamics.bullet.normalCfm`](sim-2/property_joint_dynamics_bullet_normalCfm.md)
- [`joint.dynamics.bullet.posPid`](sim-2/property_joint_dynamics_bullet_posPid.md)
- [`joint.dynamics.bullet.stopCfm`](sim-2/property_joint_dynamics_bullet_stopCfm.md)
- [`joint.dynamics.bullet.stopErp`](sim-2/property_joint_dynamics_bullet_stopErp.md)
- [`joint.dynamics.ctrlMode`](sim-2/property_joint_dynamics_ctrlMode.md) — Control mode
- [`joint.dynamics.engineProperties`](sim-2/property_joint_dynamics_engineProperties.md) — Engine properties
- [`joint.dynamics.force`](sim-2/property_joint_dynamics_force.md) — Force
- [`joint.dynamics.mujoco.armature`](sim-2/property_joint_dynamics_mujoco_armature.md)
- [`joint.dynamics.mujoco.dependencyPolyCoeff`](sim-2/property_joint_dynamics_mujoco_dependencyPolyCoeff.md)
- [`joint.dynamics.mujoco.frictionLoss`](sim-2/property_joint_dynamics_mujoco_frictionLoss.md)
- [`joint.dynamics.mujoco.frictionSolimp`](sim-2/property_joint_dynamics_mujoco_frictionSolimp.md)
- [`joint.dynamics.mujoco.frictionSolref`](sim-2/property_joint_dynamics_mujoco_frictionSolref.md)
- [`joint.dynamics.mujoco.limitsSolimp`](sim-2/property_joint_dynamics_mujoco_limitsSolimp.md)
- [`joint.dynamics.mujoco.limitsSolref`](sim-2/property_joint_dynamics_mujoco_limitsSolref.md)
- [`joint.dynamics.mujoco.margin`](sim-2/property_joint_dynamics_mujoco_margin.md)
- [`joint.dynamics.mujoco.posPid`](sim-2/property_joint_dynamics_mujoco_posPid.md)
- [`joint.dynamics.mujoco.springDamping`](sim-2/property_joint_dynamics_mujoco_springDamping.md)
- [`joint.dynamics.mujoco.springRef`](sim-2/property_joint_dynamics_mujoco_springRef.md)
- [`joint.dynamics.mujoco.springSpringDamper`](sim-2/property_joint_dynamics_mujoco_springSpringDamper.md)
- [`joint.dynamics.mujoco.springStiffness`](sim-2/property_joint_dynamics_mujoco_springStiffness.md)
- [`joint.dynamics.newton.posPid`](sim-2/property_joint_dynamics_newton_posPid.md)
- [`joint.dynamics.ode.bounce`](sim-2/property_joint_dynamics_ode_bounce.md)
- [`joint.dynamics.ode.fudge`](sim-2/property_joint_dynamics_ode_fudge.md)
- [`joint.dynamics.ode.normalCfm`](sim-2/property_joint_dynamics_ode_normalCfm.md)
- [`joint.dynamics.ode.posPid`](sim-2/property_joint_dynamics_ode_posPid.md)
- [`joint.dynamics.ode.stopCfm`](sim-2/property_joint_dynamics_ode_stopCfm.md)
- [`joint.dynamics.ode.stopErp`](sim-2/property_joint_dynamics_ode_stopErp.md)
- [`joint.dynamics.smoothMotionProfile`](sim-2/property_joint_dynamics_smoothMotionProfile.md) — Smooth dynamics motion profile
- [`joint.dynamics.springDamper`](sim-2/property_joint_dynamics_springDamper.md) — Spring damper parameters
- [`joint.dynamics.targetForce`](sim-2/property_joint_dynamics_targetForce.md) — Target force
- [`joint.dynamics.vortex.axisFrictionEnabled`](sim-2/property_joint_dynamics_vortex_axisFrictionEnabled.md)
- [`joint.dynamics.vortex.axisFrictionLoss`](sim-2/property_joint_dynamics_vortex_axisFrictionLoss.md)
- [`joint.dynamics.vortex.axisFrictionMaxForce`](sim-2/property_joint_dynamics_vortex_axisFrictionMaxForce.md)
- [`joint.dynamics.vortex.axisFrictionProportional`](sim-2/property_joint_dynamics_vortex_axisFrictionProportional.md)
- [`joint.dynamics.vortex.axisFrictionValue`](sim-2/property_joint_dynamics_vortex_axisFrictionValue.md)
- [`joint.dynamics.vortex.axisLimitsLowerDamping`](sim-2/property_joint_dynamics_vortex_axisLimitsLowerDamping.md)
- [`joint.dynamics.vortex.axisLimitsLowerMaxForce`](sim-2/property_joint_dynamics_vortex_axisLimitsLowerMaxForce.md)
- [`joint.dynamics.vortex.axisLimitsLowerRestitution`](sim-2/property_joint_dynamics_vortex_axisLimitsLowerRestitution.md)
- [`joint.dynamics.vortex.axisLimitsLowerStiffness`](sim-2/property_joint_dynamics_vortex_axisLimitsLowerStiffness.md)
- [`joint.dynamics.vortex.axisLimitsUpperDamping`](sim-2/property_joint_dynamics_vortex_axisLimitsUpperDamping.md)
- [`joint.dynamics.vortex.axisLimitsUpperMaxForce`](sim-2/property_joint_dynamics_vortex_axisLimitsUpperMaxForce.md)
- [`joint.dynamics.vortex.axisLimitsUpperRestitution`](sim-2/property_joint_dynamics_vortex_axisLimitsUpperRestitution.md)
- [`joint.dynamics.vortex.axisLimitsUpperStiffness`](sim-2/property_joint_dynamics_vortex_axisLimitsUpperStiffness.md)
- [`joint.dynamics.vortex.frictionEnabledBits`](sim-2/property_joint_dynamics_vortex_frictionEnabledBits.md)
- [`joint.dynamics.vortex.frictionProportionalBits`](sim-2/property_joint_dynamics_vortex_frictionProportionalBits.md)
- [`joint.dynamics.vortex.posPid`](sim-2/property_joint_dynamics_vortex_posPid.md)
- [`joint.dynamics.vortex.relaxationEnabledBits`](sim-2/property_joint_dynamics_vortex_relaxationEnabledBits.md)
- [`joint.dynamics.vortex.xAxisOrientFrictionCoeff`](sim-2/property_joint_dynamics_vortex_xAxisOrientFrictionCoeff.md)
- [`joint.dynamics.vortex.xAxisOrientFrictionLoss`](sim-2/property_joint_dynamics_vortex_xAxisOrientFrictionLoss.md)
- [`joint.dynamics.vortex.xAxisOrientFrictionMaxTorque`](sim-2/property_joint_dynamics_vortex_xAxisOrientFrictionMaxTorque.md)
- [`joint.dynamics.vortex.xAxisOrientRelaxationDamping`](sim-2/property_joint_dynamics_vortex_xAxisOrientRelaxationDamping.md)
- [`joint.dynamics.vortex.xAxisOrientRelaxationLoss`](sim-2/property_joint_dynamics_vortex_xAxisOrientRelaxationLoss.md)
- [`joint.dynamics.vortex.xAxisOrientRelaxationStiffness`](sim-2/property_joint_dynamics_vortex_xAxisOrientRelaxationStiffness.md)
- [`joint.dynamics.vortex.xAxisPosFrictionCoeff`](sim-2/property_joint_dynamics_vortex_xAxisPosFrictionCoeff.md)
- [`joint.dynamics.vortex.xAxisPosFrictionLoss`](sim-2/property_joint_dynamics_vortex_xAxisPosFrictionLoss.md)
- [`joint.dynamics.vortex.xAxisPosFrictionMaxForce`](sim-2/property_joint_dynamics_vortex_xAxisPosFrictionMaxForce.md)
- [`joint.dynamics.vortex.xAxisPosRelaxationDamping`](sim-2/property_joint_dynamics_vortex_xAxisPosRelaxationDamping.md)
- [`joint.dynamics.vortex.xAxisPosRelaxationLoss`](sim-2/property_joint_dynamics_vortex_xAxisPosRelaxationLoss.md)
- [`joint.dynamics.vortex.xAxisPosRelaxationStiffness`](sim-2/property_joint_dynamics_vortex_xAxisPosRelaxationStiffness.md)
- [`joint.dynamics.vortex.yAxisOrientFrictionCoeff`](sim-2/property_joint_dynamics_vortex_yAxisOrientFrictionCoeff.md)
- [`joint.dynamics.vortex.yAxisOrientFrictionLoss`](sim-2/property_joint_dynamics_vortex_yAxisOrientFrictionLoss.md)
- [`joint.dynamics.vortex.yAxisOrientFrictionMaxTorque`](sim-2/property_joint_dynamics_vortex_yAxisOrientFrictionMaxTorque.md)
- [`joint.dynamics.vortex.yAxisOrientRelaxationDamping`](sim-2/property_joint_dynamics_vortex_yAxisOrientRelaxationDamping.md)
- [`joint.dynamics.vortex.yAxisOrientRelaxationLoss`](sim-2/property_joint_dynamics_vortex_yAxisOrientRelaxationLoss.md)
- [`joint.dynamics.vortex.yAxisOrientRelaxationStiffness`](sim-2/property_joint_dynamics_vortex_yAxisOrientRelaxationStiffness.md)
- [`joint.dynamics.vortex.yAxisPosFrictionCoeff`](sim-2/property_joint_dynamics_vortex_yAxisPosFrictionCoeff.md)
- [`joint.dynamics.vortex.yAxisPosFrictionLoss`](sim-2/property_joint_dynamics_vortex_yAxisPosFrictionLoss.md)
- [`joint.dynamics.vortex.yAxisPosFrictionMaxForce`](sim-2/property_joint_dynamics_vortex_yAxisPosFrictionMaxForce.md)
- [`joint.dynamics.vortex.yAxisPosRelaxationDamping`](sim-2/property_joint_dynamics_vortex_yAxisPosRelaxationDamping.md)
- [`joint.dynamics.vortex.yAxisPosRelaxationLoss`](sim-2/property_joint_dynamics_vortex_yAxisPosRelaxationLoss.md)
- [`joint.dynamics.vortex.yAxisPosRelaxationStiffness`](sim-2/property_joint_dynamics_vortex_yAxisPosRelaxationStiffness.md)
- [`joint.dynamics.vortex.zAxisOrientFrictionCoeff`](sim-2/property_joint_dynamics_vortex_zAxisOrientFrictionCoeff.md)
- [`joint.dynamics.vortex.zAxisOrientFrictionLoss`](sim-2/property_joint_dynamics_vortex_zAxisOrientFrictionLoss.md)
- [`joint.dynamics.vortex.zAxisOrientFrictionMaxTorque`](sim-2/property_joint_dynamics_vortex_zAxisOrientFrictionMaxTorque.md)
- [`joint.dynamics.vortex.zAxisOrientRelaxationDamping`](sim-2/property_joint_dynamics_vortex_zAxisOrientRelaxationDamping.md)
- [`joint.dynamics.vortex.zAxisOrientRelaxationLoss`](sim-2/property_joint_dynamics_vortex_zAxisOrientRelaxationLoss.md)
- [`joint.dynamics.vortex.zAxisOrientRelaxationStiffness`](sim-2/property_joint_dynamics_vortex_zAxisOrientRelaxationStiffness.md)
- [`joint.dynamics.vortex.zAxisPosFrictionCoeff`](sim-2/property_joint_dynamics_vortex_zAxisPosFrictionCoeff.md)
- [`joint.dynamics.vortex.zAxisPosFrictionLoss`](sim-2/property_joint_dynamics_vortex_zAxisPosFrictionLoss.md)
- [`joint.dynamics.vortex.zAxisPosFrictionMaxForce`](sim-2/property_joint_dynamics_vortex_zAxisPosFrictionMaxForce.md)
- [`joint.dynamics.vortex.zAxisPosRelaxationDamping`](sim-2/property_joint_dynamics_vortex_zAxisPosRelaxationDamping.md)
- [`joint.dynamics.vortex.zAxisPosRelaxationLoss`](sim-2/property_joint_dynamics_vortex_zAxisPosRelaxationLoss.md)
- [`joint.dynamics.vortex.zAxisPosRelaxationStiffness`](sim-2/property_joint_dynamics_vortex_zAxisPosRelaxationStiffness.md)
- [`joint.enforceBounds`](sim-2/property_joint_enforceBounds.md) — Enforce bounds
- [`joint.intrinsicError`](sim-2/property_joint_intrinsicError.md) — Intrinsic error
- [`joint.intrinsicPose`](sim-2/property_joint_intrinsicPose.md) — Intrinsic pose
- [`joint.joint.position`](sim-2/property_joint_joint_position.md) — Position
- [`joint.joint.quaternion`](sim-2/property_joint_joint_quaternion.md) — Spherical joint quaternion
- [`joint.joint.type`](sim-2/property_joint_joint_type.md) — Type
- [`joint.length`](sim-2/property_joint_length.md) — Length
- [`joint.maxVelAccelJerk`](sim-2/property_joint_maxVelAccelJerk.md) — Maximum velocity, acceleration and jerk
- [`joint.mode`](sim-2/property_joint_mode.md) — Mode
- [`joint.screwLead`](sim-2/property_joint_screwLead.md) — Screw lead
- [`joint.targetPosition`](sim-2/property_joint_targetPosition.md) — Target position
- [`joint.targetVelocity`](sim-2/property_joint_targetVelocity.md) — Target velocity
- [`joint.velocity`](sim-2/property_joint_velocity.md) — Velocity

## <a id="methodsAndProperties_dummy"></a><a id="methodsAndProperties_dummyObject"></a>[dummy](dummies.md) (methods & properties)

- [`app:createObject`](sim-2/app_createObject.md) — Creates various objects (collections, scripts, sensors, etc.)
- [`ocTree:addFromObjects`](sim-2/ocTree_addFromObjects.md) — Adds voxels from scene objects
- [`ocTree:subtractFromObjects`](sim-2/ocTree_subtractFromObjects.md) — Subtracts voxels using scene objects
- [`pointCloud:addFromObjects`](sim-2/pointCloud_addFromObjects.md) — Adds points from scene objects
- [`pointCloud:subtractFromObjects`](sim-2/pointCloud_subtractFromObjects.md) — Subtracts points using scene objects
- [`scene:createObject`](sim-2/scene_createObject.md) — Creates various objects (collections, scripts, sensors, etc.)
- [`dummy.assemblyTag`](sim-2/property_dummy_assemblyTag.md) — Assembly tag
- [`dummy.color.diffuse`](sim-2/property_dummy_color_diffuse.md) — Diffuse color
- [`dummy.color.emission`](sim-2/property_dummy_color_emission.md) — Emission color
- [`dummy.color.specular`](sim-2/property_dummy_color_specular.md) — Specular color
- [`dummy.dummy.type`](sim-2/property_dummy_dummy_type.md) — Type
- [`dummy.dynamics.engineProperties`](sim-2/property_dummy_dynamics_engineProperties.md) — Engine properties
- [`dummy.dynamics.mujoco.jointProxyHandle`](sim-2/property_dummy_dynamics_mujoco_jointProxyHandle.md) — Joint proxy
- [`dummy.dynamics.mujoco.limitsEnabled`](sim-2/property_dummy_dynamics_mujoco_limitsEnabled.md)
- [`dummy.dynamics.mujoco.limitsRange`](sim-2/property_dummy_dynamics_mujoco_limitsRange.md)
- [`dummy.dynamics.mujoco.limitsSolimp`](sim-2/property_dummy_dynamics_mujoco_limitsSolimp.md)
- [`dummy.dynamics.mujoco.limitsSolref`](sim-2/property_dummy_dynamics_mujoco_limitsSolref.md)
- [`dummy.dynamics.mujoco.margin`](sim-2/property_dummy_dynamics_mujoco_margin.md)
- [`dummy.dynamics.mujoco.overlapConstrSolimp`](sim-2/property_dummy_dynamics_mujoco_overlapConstrSolimp.md)
- [`dummy.dynamics.mujoco.overlapConstrSolref`](sim-2/property_dummy_dynamics_mujoco_overlapConstrSolref.md)
- [`dummy.dynamics.mujoco.overlapConstrTorquescale`](sim-2/property_dummy_dynamics_mujoco_overlapConstrTorquescale.md)
- [`dummy.dynamics.mujoco.springDamping`](sim-2/property_dummy_dynamics_mujoco_springDamping.md)
- [`dummy.dynamics.mujoco.springLength`](sim-2/property_dummy_dynamics_mujoco_springLength.md)
- [`dummy.dynamics.mujoco.springStiffness`](sim-2/property_dummy_dynamics_mujoco_springStiffness.md)
- [`dummy.linkedDummy`](sim-2/property_dummy_linkedDummy.md) — Linked dummy
- [`dummy.size`](sim-2/property_dummy_size.md) — Size

## <a id="methodsAndProperties_marker"></a>[marker](markers.md) (methods & properties)

- [`marker:addItems`](sim-2/marker_addItems.md) — Adds items to a marker
- [`marker:clearItems`](sim-2/marker_clearItems.md) — Clears a marker
- [`marker:removeItems`](sim-2/marker_removeItems.md) — Removes specific items from a marker
- [`app:createObject`](sim-2/app_createObject.md) — Creates various objects (collections, scripts, sensors, etc.)
- [`scene:createObject`](sim-2/scene_createObject.md) — Creates various objects (collections, scripts, sensors, etc.)
- [`marker.colors`](sim-2/property_marker_colors.md) — Colors
- [`marker.cyclic`](sim-2/property_marker_cyclic.md) — Cyclic
- [`marker.indices`](sim-2/property_marker_indices.md) — Indices
- [`marker.local`](sim-2/property_marker_local.md) — Local
- [`marker.marker.type`](sim-2/property_marker_marker_type.md) — Type
- [`marker.normals`](sim-2/property_marker_normals.md) — Normals
- [`marker.overlay`](sim-2/property_marker_overlay.md) — Overlay
- [`marker.packedPoints`](sim-2/property_marker_packedPoints.md) — Packed points
- [`marker.packedQuaternions`](sim-2/property_marker_packedQuaternions.md) — Packed quaternions
- [`marker.packedSizes`](sim-2/property_marker_packedSizes.md) — Packed sizes
- [`marker.points`](sim-2/property_marker_points.md) — Points
- [`marker.quaternions`](sim-2/property_marker_quaternions.md) — Quaternions
- [`marker.sizes`](sim-2/property_marker_sizes.md) — Sizes
- [`marker.vertices`](sim-2/property_marker_vertices.md) — Vertices

## <a id="methodsAndProperties_scriptObject"></a><a id="methodsAndProperties_scriptObject"></a>  
[scriptObject](scriptObjects.md) (methods & properties)

- [`app:createObject`](sim-2/app_createObject.md) — Creates various objects (collections, scripts, sensors, etc.)
- [`scene:createObject`](sim-2/scene_createObject.md) — Creates various objects (collections, scripts, sensors, etc.)
- [`script:callFunction`](sim-2/script_callFunction.md) — Calls a function
- [`script:callMethod`](sim-2/script_callMethod.md) — Calls a method
- [`script:executeString`](sim-2/script_executeString.md) — Executes code from a string
- [`script:getFunctions`](sim-2/script_getFunctions.md) — Retrieves callable functions of the script
- [`script:getStackTraceback`](sim-2/script_getStackTraceback.md) — Retrieves and clears the last stack traceback
- [`script:init`](sim-2/script_init.md) — Initializes/reinitializes the script
- [`script:reset`](sim-2/script_reset.md) — Resets/ends the script
- [`script:resume`](sim-2/script_resume.md) — Resumes the suspended script
- [`script:suspend`](sim-2/script_suspend.md) — Suspends the script
- [`sceneObject.model.scriptsNotActive`](sim-2/property_sceneObject_model_scriptsNotActive.md) — Model scripts inactive
- [`scriptObject.color.diffuse`](sim-2/property_scriptObject_color_diffuse.md) — Diffuse color
- [`scriptObject.color.emission`](sim-2/property_scriptObject_color_emission.md) — Emission color
- [`scriptObject.color.specular`](sim-2/property_scriptObject_color_specular.md) — Specular color
- [`scriptObject.resetAfterSimError`](sim-2/property_scriptObject_resetAfterSimError.md) — Reset after simulation error
- [`scriptObject.script`](sim-2/property_scriptObject_script.md) — Script
- [`scriptObject.scriptObject.type`](sim-2/property_scriptObject_scriptObject_type.md) — Type
- [`scriptObject.size`](sim-2/property_scriptObject_size.md) — Size

## <a id="methodsAndProperties_camera"></a><a id="methodsAndProperties_cameraObject"></a>[camera](cameras.md) (methods & properties)

- [`camera:getImage`](sim-2/camera_getImage.md) — Returns an image as seen by the camera
- [`app:createObject`](sim-2/app_createObject.md) — Creates various objects (collections, scripts, sensors, etc.)
- [`scene:createObject`](sim-2/scene_createObject.md) — Creates various objects (collections, scripts, sensors, etc.)
- [`camera.clippingPlanes`](sim-2/property_camera_clippingPlanes.md) — Clipping planes
- [`camera.color.diffuse`](sim-2/property_camera_color_diffuse.md) — Diffuse color
- [`camera.color.emission`](sim-2/property_camera_color_emission.md) — Emission color
- [`camera.color.specular`](sim-2/property_camera_color_specular.md) — Specular color
- [`camera.frustumCornerFar`](sim-2/property_camera_frustumCornerFar.md) — Far corner of view frustum
- [`camera.frustumCornerNear`](sim-2/property_camera_frustumCornerNear.md) — Near corner of view frustum
- [`camera.parentAsManipulationProxy`](sim-2/property_camera_parentAsManipulationProxy.md) — Parent as proxy
- [`camera.perspective`](sim-2/property_camera_perspective.md) — Perspective
- [`camera.resolution`](sim-2/property_camera_resolution.md) — Resolution
- [`camera.rotationEnabled`](sim-2/property_camera_rotationEnabled.md) — Rotation enabled
- [`camera.showFrustum`](sim-2/property_camera_showFrustum.md) — Show view frustum
- [`camera.size`](sim-2/property_camera_size.md) — Size
- [`camera.trackedObject`](sim-2/property_camera_trackedObject.md) — Tracked object
- [`camera.translationEnabled`](sim-2/property_camera_translationEnabled.md) — Translation enabled
- [`camera.viewAngle`](sim-2/property_camera_viewAngle.md) — View angle
- [`camera.viewSize`](sim-2/property_camera_viewSize.md) — View size

## <a id="methodsAndProperties_light"></a><a id="methodsAndProperties_lightObject"></a>[light](lights.md) (methods & properties)

- [`app:createObject`](sim-2/app_createObject.md) — Creates various objects (collections, scripts, sensors, etc.)
- [`scene:createObject`](sim-2/scene_createObject.md) — Creates various objects (collections, scripts, sensors, etc.)
- [`light.attenuationFactors`](sim-2/property_light_attenuationFactors.md) — Attenuation factors
- [`light.color.diffuse`](sim-2/property_light_color_diffuse.md) — Diffuse color
- [`light.color.emission`](sim-2/property_light_color_emission.md) — Emission color
- [`light.color.specular`](sim-2/property_light_color_specular.md) — Specular color
- [`light.enabled`](sim-2/property_light_enabled.md) — Enabled
- [`light.light.type`](sim-2/property_light_light_type.md) — Type
- [`light.lightColor.diffuse`](sim-2/property_light_lightColor_diffuse.md) — Diffuse color
- [`light.lightColor.emission`](sim-2/property_light_lightColor_emission.md) — Emission color
- [`light.lightColor.specular`](sim-2/property_light_lightColor_specular.md) — Specular color
- [`light.povray.castShadows`](sim-2/property_light_povray_castShadows.md) — POV-Ray: Cast shadows
- [`light.size`](sim-2/property_light_size.md) — Size
- [`light.spotCutoffAngle`](sim-2/property_light_spotCutoffAngle.md) — Cutoff angle
- [`light.spotExponent`](sim-2/property_light_spotExponent.md) — Spot exponent

## <a id="methodsAndProperties_graph"></a><a id="methodsAndProperties_graphs"></a>[graph](graphs.md) (methods & properties)

- [`graph:addCurve`](sim-2/graph_addCurve.md) — Adds or updates a graph curve
- [`graph:addSignal`](sim-2/graph_addSignal.md) — Adds or updates a graph signal
- [`graph:removeTrace`](sim-2/graph_removeTrace.md) — Removes a signal or curve
- [`graph:reset`](sim-2/graph_reset.md) — Resets the graph, clearing all signals
- [`graph:setSignalPoint`](sim-2/graph_setSignalPoint.md) — Sets the next signal value to record
- [`graph:snapshotTrace`](sim-2/graph_snapshotTrace.md) — Duplicates and freezes a graph trace
- [`graph:step`](sim-2/graph_step.md) — Records signal values for the current time
- [`app:createObject`](sim-2/app_createObject.md) — Creates various objects (collections, scripts, sensors, etc.)
- [`scene:createObject`](sim-2/scene_createObject.md) — Creates various objects (collections, scripts, sensors, etc.)
- [`graph.backgroundColor`](sim-2/property_graph_backgroundColor.md) — Background color
- [`graph.bufferSize`](sim-2/property_graph_bufferSize.md) — Buffer size
- [`graph.color.diffuse`](sim-2/property_graph_color_diffuse.md) — Diffuse color
- [`graph.color.emission`](sim-2/property_graph_color_emission.md) — Emission color
- [`graph.color.specular`](sim-2/property_graph_color_specular.md) — Specular color
- [`graph.cyclic`](sim-2/property_graph_cyclic.md) — Cyclic
- [`graph.foregroundColor`](sim-2/property_graph_foregroundColor.md) — Foreground color
- [`graph.size`](sim-2/property_graph_size.md) — Size

## <a id="methodsAndProperties_proximitySensor"></a>[proximitySensor](proximitySensors.md) (methods & properties)

- [`app:createObject`](sim-2/app_createObject.md) — Creates various objects (collections, scripts, sensors, etc.)
- [`proximitySensor:checkSensor`](sim-2/proximitySensor_checkSensor.md) — Checks sensor detection silently
- [`proximitySensor:handleSensor`](sim-2/proximitySensor_handleSensor.md) — Handles the sensor with visual feedback
- [`proximitySensor:resetSensor`](sim-2/proximitySensor_resetSensor.md) — Clears the sensor's detection state
- [`scene:createObject`](sim-2/scene_createObject.md) — Creates various objects (collections, scripts, sensors, etc.)
- [`proximitySensor.angleThreshold`](sim-2/property_proximitySensor_angleThreshold.md) — Angle threshold
- [`proximitySensor.backFaceDetection`](sim-2/property_proximitySensor_backFaceDetection.md) — Back face detection
- [`proximitySensor.closeThreshold`](sim-2/property_proximitySensor_closeThreshold.md) — Close threshold
- [`proximitySensor.color.diffuse`](sim-2/property_proximitySensor_color_diffuse.md) — Diffuse color
- [`proximitySensor.color.emission`](sim-2/property_proximitySensor_color_emission.md) — Emission color
- [`proximitySensor.color.specular`](sim-2/property_proximitySensor_color_specular.md) — Specular color
- [`proximitySensor.detectedDistance`](sim-2/property_proximitySensor_detectedDistance.md) — Detected distance
- [`proximitySensor.detectedNormal`](sim-2/property_proximitySensor_detectedNormal.md) — Detected normal
- [`proximitySensor.detectedObject`](sim-2/property_proximitySensor_detectedObject.md) — Detected object
- [`proximitySensor.detectedPoint`](sim-2/property_proximitySensor_detectedPoint.md) — Detected point
- [`proximitySensor.exactMode`](sim-2/property_proximitySensor_exactMode.md) — Exact mode
- [`proximitySensor.explicitHandling`](sim-2/property_proximitySensor_explicitHandling.md) — Explicit handling
- [`proximitySensor.frontFaceDetection`](sim-2/property_proximitySensor_frontFaceDetection.md) — Front face detection
- [`proximitySensor.pointSize`](sim-2/property_proximitySensor_pointSize.md) — Sensor point size
- [`proximitySensor.proximitySensor.type`](sim-2/property_proximitySensor_proximitySensor_type.md) — Type
- [`proximitySensor.randomizedDetection`](sim-2/property_proximitySensor_randomizedDetection.md) — Randomized detection
- [`proximitySensor.rayColor.diffuse`](sim-2/property_proximitySensor_rayColor_diffuse.md) — Diffuse color
- [`proximitySensor.rayColor.emission`](sim-2/property_proximitySensor_rayColor_emission.md) — Emission color
- [`proximitySensor.rayColor.specular`](sim-2/property_proximitySensor_rayColor_specular.md) — Specular color
- [`proximitySensor.showVolume`](sim-2/property_proximitySensor_showVolume.md) — Show volume
- [`proximitySensor.volume.angle`](sim-2/property_proximitySensor_volume_angle.md) — Angles
- [`proximitySensor.volume.closeEdges`](sim-2/property_proximitySensor_volume_closeEdges.md) — Volume close edges
- [`proximitySensor.volume.edges`](sim-2/property_proximitySensor_volume_edges.md) — Volume edges
- [`proximitySensor.volume.faces`](sim-2/property_proximitySensor_volume_faces.md) — Faces
- [`proximitySensor.volume.offset`](sim-2/property_proximitySensor_volume_offset.md) — Offset
- [`proximitySensor.volume.radius`](sim-2/property_proximitySensor_volume_radius.md) — Radius
- [`proximitySensor.volume.range`](sim-2/property_proximitySensor_volume_range.md) — Range
- [`proximitySensor.volume.subdivisions`](sim-2/property_proximitySensor_volume_subdivisions.md) — Subdivisions
- [`proximitySensor.volume.xSize`](sim-2/property_proximitySensor_volume_xSize.md) — X-sizes
- [`proximitySensor.volume.ySize`](sim-2/property_proximitySensor_volume_ySize.md) — Y-sizes
- [`sceneObject.detectable`](sim-2/property_sceneObject_detectable.md) — Detectable
- [`sceneObject.model.notDetectable`](sim-2/property_sceneObject_model_notDetectable.md) — Model not detectable

## <a id="methodsAndProperties_visionSensor"></a>[visionSensor](visionSensors.md) (methods & properties)

- [`app:createObject`](sim-2/app_createObject.md) — Creates various objects (collections, scripts, sensors, etc.)
- [`scene:createObject`](sim-2/scene_createObject.md) — Creates various objects (collections, scripts, sensors, etc.)
- [`visionSensor:checkSensor`](sim-2/visionSensor_checkSensor.md) — Checks vision sensor detection silently
- [`visionSensor:getDepth`](sim-2/visionSensor_getDepth.md) — Reads the vision sensor's depth buffer
- [`visionSensor:getImage`](sim-2/visionSensor_getImage.md) — Reads the vision sensor's image
- [`visionSensor:handleSensor`](sim-2/visionSensor_handleSensor.md) — Handles the vision sensor (sensing, image processing)
- [`visionSensor:resetSensor`](sim-2/visionSensor_resetSensor.md) — Clears the vision sensor's detection state
- [`visionSensor:setImage`](sim-2/visionSensor_setImage.md) — Writes an image to the vision sensor
- [`visionSensor.backgroundColor`](sim-2/property_visionSensor_backgroundColor.md) — Background color
- [`visionSensor.backgroundColorFromEnvironment`](sim-2/property_visionSensor_backgroundColorFromEnvironment.md) — Background color from environment
- [`visionSensor.clippingPlanes`](sim-2/property_visionSensor_clippingPlanes.md) — Clipping planes
- [`visionSensor.color.diffuse`](sim-2/property_visionSensor_color_diffuse.md) — Diffuse color
- [`visionSensor.color.emission`](sim-2/property_visionSensor_color_emission.md) — Emission color
- [`visionSensor.color.specular`](sim-2/property_visionSensor_color_specular.md) — Specular color
- [`visionSensor.depth`](sim-2/property_visionSensor_depth.md) — Depth buffer
- [`visionSensor.emitDepthChangedEvent`](sim-2/property_visionSensor_emitDepthChangedEvent.md) — Emit depth change event
- [`visionSensor.emitImageChangedEvent`](sim-2/property_visionSensor_emitImageChangedEvent.md) — Emit image change event
- [`visionSensor.explicitHandling`](sim-2/property_visionSensor_explicitHandling.md) — Explicit handling
- [`visionSensor.frustumCornerFar`](sim-2/property_visionSensor_frustumCornerFar.md) — Far corner of view frustum
- [`visionSensor.frustumCornerNear`](sim-2/property_visionSensor_frustumCornerNear.md) — Near corner of view frustum
- [`visionSensor.ignoreDepthInfo`](sim-2/property_visionSensor_ignoreDepthInfo.md) — Ignore depth buffer
- [`visionSensor.ignoreImageInfo`](sim-2/property_visionSensor_ignoreImageInfo.md) — Ignore RGB buffer
- [`visionSensor.image`](sim-2/property_visionSensor_image.md) — RGB buffer
- [`visionSensor.omitPacket1`](sim-2/property_visionSensor_omitPacket1.md) — Packet 1 is blank
- [`visionSensor.packedDepth`](sim-2/property_visionSensor_packedDepth.md) — Packed depth buffer
- [`visionSensor.packet1`](sim-2/property_visionSensor_packet1.md) — Data packet 1
- [`visionSensor.packet2`](sim-2/property_visionSensor_packet2.md) — Data packet 2
- [`visionSensor.perspective`](sim-2/property_visionSensor_perspective.md) — Perspective
- [`visionSensor.povray.aperture`](sim-2/property_visionSensor_povray_aperture.md) — POV-Ray: aperture
- [`visionSensor.povray.blurDistance`](sim-2/property_visionSensor_povray_blurDistance.md) — POV-Ray: blur distance
- [`visionSensor.povray.blurSamples`](sim-2/property_visionSensor_povray_blurSamples.md) — POV-Ray: blur samples
- [`visionSensor.povray.focalBlur`](sim-2/property_visionSensor_povray_focalBlur.md) — POV-Ray: focal blur
- [`visionSensor.renderMode`](sim-2/property_visionSensor_renderMode.md) — Render mode
- [`visionSensor.resolution`](sim-2/property_visionSensor_resolution.md) — Resolution
- [`visionSensor.showFrustum`](sim-2/property_visionSensor_showFrustum.md) — Show view frustum
- [`visionSensor.size`](sim-2/property_visionSensor_size.md) — Size
- [`visionSensor.triggerState`](sim-2/property_visionSensor_triggerState.md) — Trigger state
- [`visionSensor.useExtImage`](sim-2/property_visionSensor_useExtImage.md) — External input
- [`visionSensor.viewAngle`](sim-2/property_visionSensor_viewAngle.md) — View angle
- [`visionSensor.viewSize`](sim-2/property_visionSensor_viewSize.md) — View size

## <a id="methodsAndProperties_forceSensor"></a>[forceSensor](forceSensors.md) (methods & properties)

- [`app:createObject`](sim-2/app_createObject.md) — Creates various objects (collections, scripts, sensors, etc.)
- [`scene:createObject`](sim-2/scene_createObject.md) — Creates various objects (collections, scripts, sensors, etc.)
- [`forceSensor.color.diffuse`](sim-2/property_forceSensor_color_diffuse.md) — Diffuse color
- [`forceSensor.color.emission`](sim-2/property_forceSensor_color_emission.md) — Emission color
- [`forceSensor.color.specular`](sim-2/property_forceSensor_color_specular.md) — Specular color
- [`forceSensor.dynamics.consecutiveViolationsToTrigger`](sim-2/property_forceSensor_dynamics_consecutiveViolationsToTrigger.md) — Consecutive violations to trigger
- [`forceSensor.dynamics.filter`](sim-2/property_forceSensor_dynamics_filter.md) — Filter
- [`forceSensor.dynamics.filterSampleSize`](sim-2/property_forceSensor_dynamics_filterSampleSize.md) — Filter sample size
- [`forceSensor.dynamics.filteredForce`](sim-2/property_forceSensor_dynamics_filteredForce.md) — Filtered force
- [`forceSensor.dynamics.filteredTorque`](sim-2/property_forceSensor_dynamics_filteredTorque.md) — Filtered torque
- [`forceSensor.dynamics.force`](sim-2/property_forceSensor_dynamics_force.md) — Force
- [`forceSensor.dynamics.forceThreshold`](sim-2/property_forceSensor_dynamics_forceThreshold.md) — Force threshold
- [`forceSensor.dynamics.forceThresholdEnabled`](sim-2/property_forceSensor_dynamics_forceThresholdEnabled.md) — Force threshold enabled
- [`forceSensor.dynamics.torque`](sim-2/property_forceSensor_dynamics_torque.md) — Torque
- [`forceSensor.dynamics.torqueThreshold`](sim-2/property_forceSensor_dynamics_torqueThreshold.md) — Torque threshold
- [`forceSensor.dynamics.torqueThresholdEnabled`](sim-2/property_forceSensor_dynamics_torqueThresholdEnabled.md) — Torque threshold enabled
- [`forceSensor.intrinsicError`](sim-2/property_forceSensor_intrinsicError.md) — Intrinsic error
- [`forceSensor.size`](sim-2/property_forceSensor_size.md) — Size

## <a id="methodsAndProperties_pointCloud"></a>[pointCloud](pointClouds.md) (methods & properties)

- [`app:createObject`](sim-2/app_createObject.md) — Creates various objects (collections, scripts, sensors, etc.)
- [`ocTree:addFromObjects`](sim-2/ocTree_addFromObjects.md) — Adds voxels from scene objects
- [`ocTree:subtractFromObjects`](sim-2/ocTree_subtractFromObjects.md) — Subtracts voxels using scene objects
- [`pointCloud:addFromObjects`](sim-2/pointCloud_addFromObjects.md) — Adds points from scene objects
- [`pointCloud:addPackedPoints`](sim-2/pointCloud_addPackedPoints.md) — Inserts points from a packed buffer
- [`pointCloud:addPoints`](sim-2/pointCloud_addPoints.md) — Inserts points
- [`pointCloud:clear`](sim-2/pointCloud_clear.md) — Removes all points
- [`pointCloud:intersectPackedPoints`](sim-2/pointCloud_intersectPackedPoints.md) — Keeps only points intersecting with provided packed points
- [`pointCloud:intersectPoints`](sim-2/pointCloud_intersectPoints.md) — Keeps only points intersecting with provided points
- [`pointCloud:subtractFromObjects`](sim-2/pointCloud_subtractFromObjects.md) — Subtracts points using scene objects
- [`pointCloud:subtractPackedPoints`](sim-2/pointCloud_subtractPackedPoints.md) — Removes points from a packed buffer
- [`pointCloud:subtractPoints`](sim-2/pointCloud_subtractPoints.md) — Removes points
- [`scene:createObject`](sim-2/scene_createObject.md) — Creates various objects (collections, scripts, sensors, etc.)
- [`pointCloud.cellSize`](sim-2/property_pointCloud_cellSize.md) — Cell size
- [`pointCloud.color.diffuse`](sim-2/property_pointCloud_color_diffuse.md) — Diffuse color
- [`pointCloud.color.emission`](sim-2/property_pointCloud_color_emission.md) — Emission color
- [`pointCloud.color.specular`](sim-2/property_pointCloud_color_specular.md) — Specular color
- [`pointCloud.colors`](sim-2/property_pointCloud_colors.md) — Colors
- [`pointCloud.maxPointsInCell`](sim-2/property_pointCloud_maxPointsInCell.md) — Max. points in cell
- [`pointCloud.octreeStruct`](sim-2/property_pointCloud_octreeStruct.md) — OC-Tree structure Enabled
- [`pointCloud.packedPoints`](sim-2/property_pointCloud_packedPoints.md) — Packed points
- [`pointCloud.pointDisplayFraction`](sim-2/property_pointCloud_pointDisplayFraction.md) — Display fraction
- [`pointCloud.pointSize`](sim-2/property_pointCloud_pointSize.md) — Point size
- [`pointCloud.points`](sim-2/property_pointCloud_points.md) — Points
- [`pointCloud.randomColors`](sim-2/property_pointCloud_randomColors.md) — Random point colors

## <a id="methodsAndProperties_ocTree"></a><a id="methodsAndProperties_octree"></a>[ocTree](octrees.md) (methods & properties)

- [`app:createObject`](sim-2/app_createObject.md) — Creates various objects (collections, scripts, sensors, etc.)
- [`ocTree:addFromObjects`](sim-2/ocTree_addFromObjects.md) — Adds voxels from scene objects
- [`ocTree:addPackedVoxels`](sim-2/ocTree_addPackedVoxels.md) — Inserts voxels from a packed buffer
- [`ocTree:addVoxels`](sim-2/ocTree_addVoxels.md) — Inserts voxels
- [`ocTree:checkPackedPoints`](sim-2/ocTree_checkPackedPoints.md) — Checks if packed points collide with voxels
- [`ocTree:checkPoints`](sim-2/ocTree_checkPoints.md) — Checks if points collide with the voxels
- [`ocTree:clear`](sim-2/ocTree_clear.md) — Removes all voxels
- [`ocTree:subtractFromObjects`](sim-2/ocTree_subtractFromObjects.md) — Subtracts voxels using scene objects
- [`ocTree:subtractPackedVoxels`](sim-2/ocTree_subtractPackedVoxels.md) — Removes voxels from a packed buffer
- [`ocTree:subtractVoxels`](sim-2/ocTree_subtractVoxels.md) — Removes voxels
- [`pointCloud:addFromObjects`](sim-2/pointCloud_addFromObjects.md) — Adds points from scene objects
- [`pointCloud:subtractFromObjects`](sim-2/pointCloud_subtractFromObjects.md) — Subtracts points using scene objects
- [`scene:createObject`](sim-2/scene_createObject.md) — Creates various objects (collections, scripts, sensors, etc.)
- [`ocTree.color.diffuse`](sim-2/property_ocTree_color_diffuse.md) — Diffuse color
- [`ocTree.color.emission`](sim-2/property_ocTree_color_emission.md) — Emission color
- [`ocTree.color.specular`](sim-2/property_ocTree_color_specular.md) — Specular color
- [`ocTree.colors`](sim-2/property_ocTree_colors.md) — Voxel colors
- [`ocTree.packedPoints`](sim-2/property_ocTree_packedPoints.md) — Packed voxels
- [`ocTree.points`](sim-2/property_ocTree_points.md) — Voxels
- [`ocTree.randomColors`](sim-2/property_ocTree_randomColors.md) — Random voxel colors
- [`ocTree.showPoints`](sim-2/property_ocTree_showPoints.md) — Show points instead of voxels
- [`ocTree.voxelSize`](sim-2/property_ocTree_voxelSize.md) — Voxel size

## <a id="methodsAndProperties_customSceneObject"></a>customSceneObject (methods & properties)

- [`app:createObject`](sim-2/app_createObject.md) — Creates various objects (collections, scripts, sensors, etc.)
- [`scene:createObject`](sim-2/scene_createObject.md) — Creates various objects (collections, scripts, sensors, etc.)

## <a id="methodsAndProperties_Path"></a><a id="methodsAndProperties_paths"></a>[Path](paths.md) (methods & properties)

- [`Path:appendFromJoints`](sim-2/Path_appendFromJoints.md) — Appends a point from the joints' current configuration
- [`Path:appendFromObject`](sim-2/Path_appendFromObject.md) — Appends a point from the object's current pose
- [`Path:appendPoints`](sim-2/Path_appendPoints.md) — Appends path control points
- [`Path:clearPoints`](sim-2/Path_clearPoints.md) — Clears all path control points
- [`Path:closest`](sim-2/Path_closest.md) — Returns the closest point on the path
- [`Path:configs`](sim-2/Path_configs.md) — Returns equivalent configurations for a given one
- [`Path:createMarkers`](sim-2/Path_createMarkers.md) — Creates markers for path visualization
- [`Path:createShape`](sim-2/Path_createShape.md) — Creates an extrusion shape from the path
- [`Path:data`](sim-2/Path_data.md) — Returns path information
- [`Path:distance`](sim-2/Path_distance.md) — Returns distance between two points
- [`Path:fromBuffer`](sim-2/Path_fromBuffer.md) — Creates a path from serialized data
- [`Path:fromJoints`](sim-2/Path_fromJoints.md) — Creates an empty path from joints
- [`Path:fromObject`](sim-2/Path_fromObject.md) — Creates an empty path from an object's pose
- [`Path:getPoint`](sim-2/Path_getPoint.md) — Returns a point on the path at a specific distance
- [`Path:interpolate`](sim-2/Path_interpolate.md) — Returns linear interpolation between two points
- [`Path:new`](sim-2/Path_new.md) — Creates a path
- [`Path:removeMarkers`](sim-2/Path_removeMarkers.md) — Removes path visualization markers
- [`Path:setPoints`](sim-2/Path_setPoints.md) — Sets the path control points
- [`Path:toBuffer`](sim-2/Path_toBuffer.md) — Returns serialized path data
- [`app:createObject`](sim-2/app_createObject.md) — Creates various objects (collections, scripts, sensors, etc.)
- [`scene:createObject`](sim-2/scene_createObject.md) — Creates various objects (collections, scripts, sensors, etc.)

## <a id="methodsAndProperties_file"></a><a id="methodsAndProperties_fileOperations"></a>File operations (methods & properties)

- [`app:loadModelInfo`](sim-2/app_loadModelInfo.md) — Loads a model thumbnail
- [`app:loadModelInfoFromBuffer`](sim-2/app_loadModelInfoFromBuffer.md) — Loads a model thumbnail from buffer
- [`app:loadScene`](sim-2/app_loadScene.md) — Loads a scene from file
- [`app:loadSceneFromBuffer`](sim-2/app_loadSceneFromBuffer.md) — Loads a scene from buffer
- [`scene:loadModel`](sim-2/scene_loadModel.md) — Loads a previously saved model
- [`scene:loadModelFromBuffer`](sim-2/scene_loadModelFromBuffer.md) — Loads a model from buffer
- [`scene:remove`](sim-2/scene_remove.md) — Closes the scene
- [`scene:save`](sim-2/scene_save.md) — Saves the scene to file
- [`scene:saveToBuffer`](sim-2/scene_saveToBuffer.md) — Serializes the scene to a buffer
- [`sceneObject:saveModel`](sim-2/sceneObject_saveModel.md) — Saves this model to a file
- [`sceneObject:saveModelToBuffer`](sim-2/sceneObject_saveModelToBuffer.md) — Serializes this model to a buffer
- [`scene.finalSaveRequest`](sim-2/property_scene_finalSaveRequest.md) — Final save
- [`scene.locked`](sim-2/property_scene_locked.md) — Scene is locked
- [`scene.saveCalculationStructs`](sim-2/property_scene_saveCalculationStructs.md) — Save calculation structures

## <a id="methodsAndProperties_main"></a><a id="methodsAndProperties_mainFunctionalityHandling"></a>General functionality handling (methods & properties)

- [`scene:getObject`](sim-2/scene_getObject.md) — Retrieves an object by its path and name
- [`scene:getObjectFromUid`](sim-2/scene_getObjectFromUid.md) — Retrieves an object by its unique identifier
- [`sceneObject:getObject`](sim-2/sceneObject_getObject.md) — Retrieves an object by its path and name
- [`script:getObject`](sim-2/script_getObject.md) — Retrieves an object by its path and name

## <a id="methodsAndProperties_dynamics"></a><a id="methodsAndProperties_dynamicsFunctionality"></a>[Dynamics](dynamicsModule.md) (methods & properties)

- [`joint:setTargetPosition`](sim-2/joint_setTargetPosition.md) — Sets the joint's desired linear/angular position
- [`joint:setTargetVelocity`](sim-2/joint_setTargetVelocity.md) — Sets the joint's desired linear/angular velocity
- [`scene.dynamics:getContacts`](sim-2/scene_dynamics_getContacts.md) — Retrieves contact information from the dynamics world
- [`scene.dynamics:step`](sim-2/scene_dynamics_step.md) — Steps the dynamics engine
- [`sceneObject:dynamicReset`](sim-2/sceneObject_dynamicReset.md) — Dynamically resets the object in the physics engine
- [`shape.dynamics:addForce`](sim-2/shape_dynamics_addForce.md) — Applies a force to the dynamically enabled shape
- [`shape.dynamics:addTorque`](sim-2/shape_dynamics_addTorque.md) — Applies a torque to the dynamically enabled shape
- [`shape.dynamics:computeInertia`](sim-2/shape_dynamics_computeInertia.md) — Computes and applies mass/inertia properties
- [`shape.dynamics:getContacts`](sim-2/shape_dynamics_getContacts.md) — Retrieves the shape's contact information
- [`shape.dynamics:getInertia`](sim-2/shape_dynamics_getInertia.md) — Retrieves the shape's inertia information
- [`shape.dynamics:setInertia`](sim-2/shape_dynamics_setInertia.md) — Applies a new inertia matrix
- [`app.paths.mujoco`](sim-2/property_app_paths_mujoco.md) — MuJoCo path
- [`dummy.dynamics.engineProperties`](sim-2/property_dummy_dynamics_engineProperties.md) — Engine properties
- [`dummy.dynamics.mujoco.jointProxyHandle`](sim-2/property_dummy_dynamics_mujoco_jointProxyHandle.md) — Joint proxy
- [`dummy.dynamics.mujoco.limitsEnabled`](sim-2/property_dummy_dynamics_mujoco_limitsEnabled.md)
- [`dummy.dynamics.mujoco.limitsRange`](sim-2/property_dummy_dynamics_mujoco_limitsRange.md)
- [`dummy.dynamics.mujoco.limitsSolimp`](sim-2/property_dummy_dynamics_mujoco_limitsSolimp.md)
- [`dummy.dynamics.mujoco.limitsSolref`](sim-2/property_dummy_dynamics_mujoco_limitsSolref.md)
- [`dummy.dynamics.mujoco.margin`](sim-2/property_dummy_dynamics_mujoco_margin.md)
- [`dummy.dynamics.mujoco.overlapConstrSolimp`](sim-2/property_dummy_dynamics_mujoco_overlapConstrSolimp.md)
- [`dummy.dynamics.mujoco.overlapConstrSolref`](sim-2/property_dummy_dynamics_mujoco_overlapConstrSolref.md)
- [`dummy.dynamics.mujoco.overlapConstrTorquescale`](sim-2/property_dummy_dynamics_mujoco_overlapConstrTorquescale.md)
- [`dummy.dynamics.mujoco.springDamping`](sim-2/property_dummy_dynamics_mujoco_springDamping.md)
- [`dummy.dynamics.mujoco.springLength`](sim-2/property_dummy_dynamics_mujoco_springLength.md)
- [`dummy.dynamics.mujoco.springStiffness`](sim-2/property_dummy_dynamics_mujoco_springStiffness.md)
- [`forceSensor.dynamics.filter`](sim-2/property_forceSensor_dynamics_filter.md) — Filter
- [`forceSensor.dynamics.filterSampleSize`](sim-2/property_forceSensor_dynamics_filterSampleSize.md) — Filter sample size
- [`forceSensor.dynamics.filteredForce`](sim-2/property_forceSensor_dynamics_filteredForce.md) — Filtered force
- [`forceSensor.dynamics.filteredTorque`](sim-2/property_forceSensor_dynamics_filteredTorque.md) — Filtered torque
- [`forceSensor.dynamics.force`](sim-2/property_forceSensor_dynamics_force.md) — Force
- [`forceSensor.dynamics.forceThreshold`](sim-2/property_forceSensor_dynamics_forceThreshold.md) — Force threshold
- [`forceSensor.dynamics.forceThresholdEnabled`](sim-2/property_forceSensor_dynamics_forceThresholdEnabled.md) — Force threshold enabled
- [`forceSensor.dynamics.torque`](sim-2/property_forceSensor_dynamics_torque.md) — Torque
- [`forceSensor.dynamics.torqueThreshold`](sim-2/property_forceSensor_dynamics_torqueThreshold.md) — Torque threshold
- [`forceSensor.dynamics.torqueThresholdEnabled`](sim-2/property_forceSensor_dynamics_torqueThresholdEnabled.md) — Torque threshold enabled
- [`forceSensor.intrinsicError`](sim-2/property_forceSensor_intrinsicError.md) — Intrinsic error
- [`joint.dynamics.averageForce`](sim-2/property_joint_dynamics_averageForce.md) — Average force
- [`joint.dynamics.bullet.normalCfm`](sim-2/property_joint_dynamics_bullet_normalCfm.md)
- [`joint.dynamics.bullet.posPid`](sim-2/property_joint_dynamics_bullet_posPid.md)
- [`joint.dynamics.bullet.stopCfm`](sim-2/property_joint_dynamics_bullet_stopCfm.md)
- [`joint.dynamics.bullet.stopErp`](sim-2/property_joint_dynamics_bullet_stopErp.md)
- [`joint.dynamics.ctrlMode`](sim-2/property_joint_dynamics_ctrlMode.md) — Control mode
- [`joint.dynamics.engineProperties`](sim-2/property_joint_dynamics_engineProperties.md) — Engine properties
- [`joint.dynamics.force`](sim-2/property_joint_dynamics_force.md) — Force
- [`joint.dynamics.mujoco.armature`](sim-2/property_joint_dynamics_mujoco_armature.md)
- [`joint.dynamics.mujoco.dependencyPolyCoeff`](sim-2/property_joint_dynamics_mujoco_dependencyPolyCoeff.md)
- [`joint.dynamics.mujoco.frictionLoss`](sim-2/property_joint_dynamics_mujoco_frictionLoss.md)
- [`joint.dynamics.mujoco.frictionSolimp`](sim-2/property_joint_dynamics_mujoco_frictionSolimp.md)
- [`joint.dynamics.mujoco.frictionSolref`](sim-2/property_joint_dynamics_mujoco_frictionSolref.md)
- [`joint.dynamics.mujoco.limitsSolimp`](sim-2/property_joint_dynamics_mujoco_limitsSolimp.md)
- [`joint.dynamics.mujoco.limitsSolref`](sim-2/property_joint_dynamics_mujoco_limitsSolref.md)
- [`joint.dynamics.mujoco.margin`](sim-2/property_joint_dynamics_mujoco_margin.md)
- [`joint.dynamics.mujoco.posPid`](sim-2/property_joint_dynamics_mujoco_posPid.md)
- [`joint.dynamics.mujoco.springDamping`](sim-2/property_joint_dynamics_mujoco_springDamping.md)
- [`joint.dynamics.mujoco.springRef`](sim-2/property_joint_dynamics_mujoco_springRef.md)
- [`joint.dynamics.mujoco.springSpringDamper`](sim-2/property_joint_dynamics_mujoco_springSpringDamper.md)
- [`joint.dynamics.mujoco.springStiffness`](sim-2/property_joint_dynamics_mujoco_springStiffness.md)
- [`joint.dynamics.newton.posPid`](sim-2/property_joint_dynamics_newton_posPid.md)
- [`joint.dynamics.ode.bounce`](sim-2/property_joint_dynamics_ode_bounce.md)
- [`joint.dynamics.ode.fudge`](sim-2/property_joint_dynamics_ode_fudge.md)
- [`joint.dynamics.ode.normalCfm`](sim-2/property_joint_dynamics_ode_normalCfm.md)
- [`joint.dynamics.ode.posPid`](sim-2/property_joint_dynamics_ode_posPid.md)
- [`joint.dynamics.ode.stopCfm`](sim-2/property_joint_dynamics_ode_stopCfm.md)
- [`joint.dynamics.ode.stopErp`](sim-2/property_joint_dynamics_ode_stopErp.md)
- [`joint.dynamics.smoothMotionProfile`](sim-2/property_joint_dynamics_smoothMotionProfile.md) — Smooth dynamics motion profile
- [`joint.dynamics.springDamper`](sim-2/property_joint_dynamics_springDamper.md) — Spring damper parameters
- [`joint.dynamics.targetForce`](sim-2/property_joint_dynamics_targetForce.md) — Target force
- [`joint.dynamics.vortex.axisFrictionEnabled`](sim-2/property_joint_dynamics_vortex_axisFrictionEnabled.md)
- [`joint.dynamics.vortex.axisFrictionLoss`](sim-2/property_joint_dynamics_vortex_axisFrictionLoss.md)
- [`joint.dynamics.vortex.axisFrictionMaxForce`](sim-2/property_joint_dynamics_vortex_axisFrictionMaxForce.md)
- [`joint.dynamics.vortex.axisFrictionProportional`](sim-2/property_joint_dynamics_vortex_axisFrictionProportional.md)
- [`joint.dynamics.vortex.axisFrictionValue`](sim-2/property_joint_dynamics_vortex_axisFrictionValue.md)
- [`joint.dynamics.vortex.axisLimitsLowerDamping`](sim-2/property_joint_dynamics_vortex_axisLimitsLowerDamping.md)
- [`joint.dynamics.vortex.axisLimitsLowerMaxForce`](sim-2/property_joint_dynamics_vortex_axisLimitsLowerMaxForce.md)
- [`joint.dynamics.vortex.axisLimitsLowerRestitution`](sim-2/property_joint_dynamics_vortex_axisLimitsLowerRestitution.md)
- [`joint.dynamics.vortex.axisLimitsLowerStiffness`](sim-2/property_joint_dynamics_vortex_axisLimitsLowerStiffness.md)
- [`joint.dynamics.vortex.axisLimitsUpperDamping`](sim-2/property_joint_dynamics_vortex_axisLimitsUpperDamping.md)
- [`joint.dynamics.vortex.axisLimitsUpperMaxForce`](sim-2/property_joint_dynamics_vortex_axisLimitsUpperMaxForce.md)
- [`joint.dynamics.vortex.axisLimitsUpperRestitution`](sim-2/property_joint_dynamics_vortex_axisLimitsUpperRestitution.md)
- [`joint.dynamics.vortex.axisLimitsUpperStiffness`](sim-2/property_joint_dynamics_vortex_axisLimitsUpperStiffness.md)
- [`joint.dynamics.vortex.frictionEnabledBits`](sim-2/property_joint_dynamics_vortex_frictionEnabledBits.md)
- [`joint.dynamics.vortex.frictionProportionalBits`](sim-2/property_joint_dynamics_vortex_frictionProportionalBits.md)
- [`joint.dynamics.vortex.posPid`](sim-2/property_joint_dynamics_vortex_posPid.md)
- [`joint.dynamics.vortex.relaxationEnabledBits`](sim-2/property_joint_dynamics_vortex_relaxationEnabledBits.md)
- [`joint.dynamics.vortex.xAxisOrientFrictionCoeff`](sim-2/property_joint_dynamics_vortex_xAxisOrientFrictionCoeff.md)
- [`joint.dynamics.vortex.xAxisOrientFrictionLoss`](sim-2/property_joint_dynamics_vortex_xAxisOrientFrictionLoss.md)
- [`joint.dynamics.vortex.xAxisOrientFrictionMaxTorque`](sim-2/property_joint_dynamics_vortex_xAxisOrientFrictionMaxTorque.md)
- [`joint.dynamics.vortex.xAxisOrientRelaxationDamping`](sim-2/property_joint_dynamics_vortex_xAxisOrientRelaxationDamping.md)
- [`joint.dynamics.vortex.xAxisOrientRelaxationLoss`](sim-2/property_joint_dynamics_vortex_xAxisOrientRelaxationLoss.md)
- [`joint.dynamics.vortex.xAxisOrientRelaxationStiffness`](sim-2/property_joint_dynamics_vortex_xAxisOrientRelaxationStiffness.md)
- [`joint.dynamics.vortex.xAxisPosFrictionCoeff`](sim-2/property_joint_dynamics_vortex_xAxisPosFrictionCoeff.md)
- [`joint.dynamics.vortex.xAxisPosFrictionLoss`](sim-2/property_joint_dynamics_vortex_xAxisPosFrictionLoss.md)
- [`joint.dynamics.vortex.xAxisPosFrictionMaxForce`](sim-2/property_joint_dynamics_vortex_xAxisPosFrictionMaxForce.md)
- [`joint.dynamics.vortex.xAxisPosRelaxationDamping`](sim-2/property_joint_dynamics_vortex_xAxisPosRelaxationDamping.md)
- [`joint.dynamics.vortex.xAxisPosRelaxationLoss`](sim-2/property_joint_dynamics_vortex_xAxisPosRelaxationLoss.md)
- [`joint.dynamics.vortex.xAxisPosRelaxationStiffness`](sim-2/property_joint_dynamics_vortex_xAxisPosRelaxationStiffness.md)
- [`joint.dynamics.vortex.yAxisOrientFrictionCoeff`](sim-2/property_joint_dynamics_vortex_yAxisOrientFrictionCoeff.md)
- [`joint.dynamics.vortex.yAxisOrientFrictionLoss`](sim-2/property_joint_dynamics_vortex_yAxisOrientFrictionLoss.md)
- [`joint.dynamics.vortex.yAxisOrientFrictionMaxTorque`](sim-2/property_joint_dynamics_vortex_yAxisOrientFrictionMaxTorque.md)
- [`joint.dynamics.vortex.yAxisOrientRelaxationDamping`](sim-2/property_joint_dynamics_vortex_yAxisOrientRelaxationDamping.md)
- [`joint.dynamics.vortex.yAxisOrientRelaxationLoss`](sim-2/property_joint_dynamics_vortex_yAxisOrientRelaxationLoss.md)
- [`joint.dynamics.vortex.yAxisOrientRelaxationStiffness`](sim-2/property_joint_dynamics_vortex_yAxisOrientRelaxationStiffness.md)
- [`joint.dynamics.vortex.yAxisPosFrictionCoeff`](sim-2/property_joint_dynamics_vortex_yAxisPosFrictionCoeff.md)
- [`joint.dynamics.vortex.yAxisPosFrictionLoss`](sim-2/property_joint_dynamics_vortex_yAxisPosFrictionLoss.md)
- [`joint.dynamics.vortex.yAxisPosFrictionMaxForce`](sim-2/property_joint_dynamics_vortex_yAxisPosFrictionMaxForce.md)
- [`joint.dynamics.vortex.yAxisPosRelaxationDamping`](sim-2/property_joint_dynamics_vortex_yAxisPosRelaxationDamping.md)
- [`joint.dynamics.vortex.yAxisPosRelaxationLoss`](sim-2/property_joint_dynamics_vortex_yAxisPosRelaxationLoss.md)
- [`joint.dynamics.vortex.yAxisPosRelaxationStiffness`](sim-2/property_joint_dynamics_vortex_yAxisPosRelaxationStiffness.md)
- [`joint.dynamics.vortex.zAxisOrientFrictionCoeff`](sim-2/property_joint_dynamics_vortex_zAxisOrientFrictionCoeff.md)
- [`joint.dynamics.vortex.zAxisOrientFrictionLoss`](sim-2/property_joint_dynamics_vortex_zAxisOrientFrictionLoss.md)
- [`joint.dynamics.vortex.zAxisOrientFrictionMaxTorque`](sim-2/property_joint_dynamics_vortex_zAxisOrientFrictionMaxTorque.md)
- [`joint.dynamics.vortex.zAxisOrientRelaxationDamping`](sim-2/property_joint_dynamics_vortex_zAxisOrientRelaxationDamping.md)
- [`joint.dynamics.vortex.zAxisOrientRelaxationLoss`](sim-2/property_joint_dynamics_vortex_zAxisOrientRelaxationLoss.md)
- [`joint.dynamics.vortex.zAxisOrientRelaxationStiffness`](sim-2/property_joint_dynamics_vortex_zAxisOrientRelaxationStiffness.md)
- [`joint.dynamics.vortex.zAxisPosFrictionCoeff`](sim-2/property_joint_dynamics_vortex_zAxisPosFrictionCoeff.md)
- [`joint.dynamics.vortex.zAxisPosFrictionLoss`](sim-2/property_joint_dynamics_vortex_zAxisPosFrictionLoss.md)
- [`joint.dynamics.vortex.zAxisPosFrictionMaxForce`](sim-2/property_joint_dynamics_vortex_zAxisPosFrictionMaxForce.md)
- [`joint.dynamics.vortex.zAxisPosRelaxationDamping`](sim-2/property_joint_dynamics_vortex_zAxisPosRelaxationDamping.md)
- [`joint.dynamics.vortex.zAxisPosRelaxationLoss`](sim-2/property_joint_dynamics_vortex_zAxisPosRelaxationLoss.md)
- [`joint.dynamics.vortex.zAxisPosRelaxationStiffness`](sim-2/property_joint_dynamics_vortex_zAxisPosRelaxationStiffness.md)
- [`joint.enforceBounds`](sim-2/property_joint_enforceBounds.md) — Enforce bounds
- [`joint.intrinsicError`](sim-2/property_joint_intrinsicError.md) — Intrinsic error
- [`joint.targetPosition`](sim-2/property_joint_targetPosition.md) — Target position
- [`joint.targetVelocity`](sim-2/property_joint_targetVelocity.md) — Target velocity
- [`joint.velocity`](sim-2/property_joint_velocity.md) — Velocity
- [`scene.dynamics.bullet.collisionMarginScaling`](sim-2/property_scene_dynamics_bullet_collisionMarginScaling.md)
- [`scene.dynamics.bullet.computeInertias`](sim-2/property_scene_dynamics_bullet_computeInertias.md)
- [`scene.dynamics.bullet.internalScalingFull`](sim-2/property_scene_dynamics_bullet_internalScalingFull.md)
- [`scene.dynamics.bullet.internalScalingValue`](sim-2/property_scene_dynamics_bullet_internalScalingValue.md)
- [`scene.dynamics.bullet.iterations`](sim-2/property_scene_dynamics_bullet_iterations.md)
- [`scene.dynamics.bullet.solver`](sim-2/property_scene_dynamics_bullet_solver.md)
- [`scene.dynamics.enabled`](sim-2/property_scene_dynamics_enabled.md) — Dynamics enabled
- [`scene.dynamics.engine`](sim-2/property_scene_dynamics_engine.md) — Dynamics engine
- [`scene.dynamics.engineProperties`](sim-2/property_scene_dynamics_engineProperties.md) — Engine properties
- [`scene.dynamics.engineVersion`](sim-2/property_scene_dynamics_engineVersion.md) — Dynamics engine version
- [`scene.dynamics.gravity`](sim-2/property_scene_dynamics_gravity.md) — Gravity
- [`scene.dynamics.mujoco.actuationEnable`](sim-2/property_scene_dynamics_mujoco_actuationEnable.md)
- [`scene.dynamics.mujoco.alignfree`](sim-2/property_scene_dynamics_mujoco_alignfree.md)
- [`scene.dynamics.mujoco.autoresetEnable`](sim-2/property_scene_dynamics_mujoco_autoresetEnable.md)
- [`scene.dynamics.mujoco.balanceInertias`](sim-2/property_scene_dynamics_mujoco_balanceInertias.md)
- [`scene.dynamics.mujoco.boundInertia`](sim-2/property_scene_dynamics_mujoco_boundInertia.md)
- [`scene.dynamics.mujoco.boundMass`](sim-2/property_scene_dynamics_mujoco_boundMass.md)
- [`scene.dynamics.mujoco.ccd_iterations`](sim-2/property_scene_dynamics_mujoco_ccd_iterations.md)
- [`scene.dynamics.mujoco.ccd_tolerance`](sim-2/property_scene_dynamics_mujoco_ccd_tolerance.md)
- [`scene.dynamics.mujoco.computeInertias`](sim-2/property_scene_dynamics_mujoco_computeInertias.md)
- [`scene.dynamics.mujoco.cone`](sim-2/property_scene_dynamics_mujoco_cone.md)
- [`scene.dynamics.mujoco.contactEnable`](sim-2/property_scene_dynamics_mujoco_contactEnable.md)
- [`scene.dynamics.mujoco.contactParamsMargin`](sim-2/property_scene_dynamics_mujoco_contactParamsMargin.md)
- [`scene.dynamics.mujoco.contactParamsOverride`](sim-2/property_scene_dynamics_mujoco_contactParamsOverride.md)
- [`scene.dynamics.mujoco.contactParamsSolimp`](sim-2/property_scene_dynamics_mujoco_contactParamsSolimp.md)
- [`scene.dynamics.mujoco.contactParamsSolref`](sim-2/property_scene_dynamics_mujoco_contactParamsSolref.md)
- [`scene.dynamics.mujoco.density`](sim-2/property_scene_dynamics_mujoco_density.md)
- [`scene.dynamics.mujoco.energyEnable`](sim-2/property_scene_dynamics_mujoco_energyEnable.md)
- [`scene.dynamics.mujoco.equalityEnable`](sim-2/property_scene_dynamics_mujoco_equalityEnable.md)
- [`scene.dynamics.mujoco.eulerdampEnable`](sim-2/property_scene_dynamics_mujoco_eulerdampEnable.md)
- [`scene.dynamics.mujoco.frictionlossEnable`](sim-2/property_scene_dynamics_mujoco_frictionlossEnable.md)
- [`scene.dynamics.mujoco.gravityEnable`](sim-2/property_scene_dynamics_mujoco_gravityEnable.md)
- [`scene.dynamics.mujoco.impratio`](sim-2/property_scene_dynamics_mujoco_impratio.md)
- [`scene.dynamics.mujoco.integrator`](sim-2/property_scene_dynamics_mujoco_integrator.md)
- [`scene.dynamics.mujoco.invdiscreteEnable`](sim-2/property_scene_dynamics_mujoco_invdiscreteEnable.md)
- [`scene.dynamics.mujoco.iterations`](sim-2/property_scene_dynamics_mujoco_iterations.md)
- [`scene.dynamics.mujoco.jacobian`](sim-2/property_scene_dynamics_mujoco_jacobian.md)
- [`scene.dynamics.mujoco.kinematicBodiesInertia`](sim-2/property_scene_dynamics_mujoco_kinematicBodiesInertia.md)
- [`scene.dynamics.mujoco.kinematicBodiesMass`](sim-2/property_scene_dynamics_mujoco_kinematicBodiesMass.md)
- [`scene.dynamics.mujoco.kinematicBodiesOverrideFlags`](sim-2/property_scene_dynamics_mujoco_kinematicBodiesOverrideFlags.md)
- [`scene.dynamics.mujoco.kinematicWeldSolimp`](sim-2/property_scene_dynamics_mujoco_kinematicWeldSolimp.md)
- [`scene.dynamics.mujoco.kinematicWeldSolref`](sim-2/property_scene_dynamics_mujoco_kinematicWeldSolref.md)
- [`scene.dynamics.mujoco.kinematicWeldTorquescale`](sim-2/property_scene_dynamics_mujoco_kinematicWeldTorquescale.md)
- [`scene.dynamics.mujoco.limitEnable`](sim-2/property_scene_dynamics_mujoco_limitEnable.md)
- [`scene.dynamics.mujoco.ls_iterations`](sim-2/property_scene_dynamics_mujoco_ls_iterations.md)
- [`scene.dynamics.mujoco.ls_tolerance`](sim-2/property_scene_dynamics_mujoco_ls_tolerance.md)
- [`scene.dynamics.mujoco.mbmemory`](sim-2/property_scene_dynamics_mujoco_mbmemory.md)
- [`scene.dynamics.mujoco.midphaseEnable`](sim-2/property_scene_dynamics_mujoco_midphaseEnable.md)
- [`scene.dynamics.mujoco.multiccd`](sim-2/property_scene_dynamics_mujoco_multiccd.md)
- [`scene.dynamics.mujoco.multithreaded`](sim-2/property_scene_dynamics_mujoco_multithreaded.md)
- [`scene.dynamics.mujoco.nativeccdEnable`](sim-2/property_scene_dynamics_mujoco_nativeccdEnable.md)
- [`scene.dynamics.mujoco.nconmax`](sim-2/property_scene_dynamics_mujoco_nconmax.md)
- [`scene.dynamics.mujoco.njmax`](sim-2/property_scene_dynamics_mujoco_njmax.md)
- [`scene.dynamics.mujoco.noslip_iterations`](sim-2/property_scene_dynamics_mujoco_noslip_iterations.md)
- [`scene.dynamics.mujoco.noslip_tolerance`](sim-2/property_scene_dynamics_mujoco_noslip_tolerance.md)
- [`scene.dynamics.mujoco.nstack`](sim-2/property_scene_dynamics_mujoco_nstack.md)
- [`scene.dynamics.mujoco.passiveEnable`](sim-2/property_scene_dynamics_mujoco_passiveEnable.md)
- [`scene.dynamics.mujoco.rebuildTrigger`](sim-2/property_scene_dynamics_mujoco_rebuildTrigger.md)
- [`scene.dynamics.mujoco.refsafeEnable`](sim-2/property_scene_dynamics_mujoco_refsafeEnable.md)
- [`scene.dynamics.mujoco.sdf_initpoints`](sim-2/property_scene_dynamics_mujoco_sdf_initpoints.md)
- [`scene.dynamics.mujoco.sdf_iterations`](sim-2/property_scene_dynamics_mujoco_sdf_iterations.md)
- [`scene.dynamics.mujoco.sensorEnable`](sim-2/property_scene_dynamics_mujoco_sensorEnable.md)
- [`scene.dynamics.mujoco.solver`](sim-2/property_scene_dynamics_mujoco_solver.md)
- [`scene.dynamics.mujoco.tolerance`](sim-2/property_scene_dynamics_mujoco_tolerance.md)
- [`scene.dynamics.mujoco.viscosity`](sim-2/property_scene_dynamics_mujoco_viscosity.md)
- [`scene.dynamics.mujoco.warmstartEnable`](sim-2/property_scene_dynamics_mujoco_warmstartEnable.md)
- [`scene.dynamics.mujoco.wind`](sim-2/property_scene_dynamics_mujoco_wind.md)
- [`scene.dynamics.newton.computeInertias`](sim-2/property_scene_dynamics_newton_computeInertias.md)
- [`scene.dynamics.newton.contactMergeTolerance`](sim-2/property_scene_dynamics_newton_contactMergeTolerance.md)
- [`scene.dynamics.newton.exactSolver`](sim-2/property_scene_dynamics_newton_exactSolver.md)
- [`scene.dynamics.newton.highJointAccuracy`](sim-2/property_scene_dynamics_newton_highJointAccuracy.md)
- [`scene.dynamics.newton.iterations`](sim-2/property_scene_dynamics_newton_iterations.md)
- [`scene.dynamics.newton.multithreading`](sim-2/property_scene_dynamics_newton_multithreading.md)
- [`scene.dynamics.ode.computeInertias`](sim-2/property_scene_dynamics_ode_computeInertias.md)
- [`scene.dynamics.ode.globalCfm`](sim-2/property_scene_dynamics_ode_globalCfm.md)
- [`scene.dynamics.ode.globalErp`](sim-2/property_scene_dynamics_ode_globalErp.md)
- [`scene.dynamics.ode.internalScalingFull`](sim-2/property_scene_dynamics_ode_internalScalingFull.md)
- [`scene.dynamics.ode.internalScalingValue`](sim-2/property_scene_dynamics_ode_internalScalingValue.md)
- [`scene.dynamics.ode.quickStepEnabled`](sim-2/property_scene_dynamics_ode_quickStepEnabled.md)
- [`scene.dynamics.ode.quickStepIterations`](sim-2/property_scene_dynamics_ode_quickStepIterations.md)
- [`scene.dynamics.showContactPoints`](sim-2/property_scene_dynamics_showContactPoints.md) — Show contact points
- [`scene.dynamics.stepSize`](sim-2/property_scene_dynamics_stepSize.md) — Dynamics dt
- [`scene.dynamics.vortex.autoSleep`](sim-2/property_scene_dynamics_vortex_autoSleep.md)
- [`scene.dynamics.vortex.computeInertias`](sim-2/property_scene_dynamics_vortex_computeInertias.md)
- [`scene.dynamics.vortex.constraintsAngularCompliance`](sim-2/property_scene_dynamics_vortex_constraintsAngularCompliance.md)
- [`scene.dynamics.vortex.constraintsAngularDamping`](sim-2/property_scene_dynamics_vortex_constraintsAngularDamping.md)
- [`scene.dynamics.vortex.constraintsAngularKineticLoss`](sim-2/property_scene_dynamics_vortex_constraintsAngularKineticLoss.md)
- [`scene.dynamics.vortex.constraintsLinearCompliance`](sim-2/property_scene_dynamics_vortex_constraintsLinearCompliance.md)
- [`scene.dynamics.vortex.constraintsLinearDamping`](sim-2/property_scene_dynamics_vortex_constraintsLinearDamping.md)
- [`scene.dynamics.vortex.constraintsLinearKineticLoss`](sim-2/property_scene_dynamics_vortex_constraintsLinearKineticLoss.md)
- [`scene.dynamics.vortex.contactTolerance`](sim-2/property_scene_dynamics_vortex_contactTolerance.md)
- [`scene.dynamics.vortex.multithreading`](sim-2/property_scene_dynamics_vortex_multithreading.md)
- [`sceneObject.dynamicFlag`](sim-2/property_sceneObject_dynamicFlag.md) — Dynamic flag
- [`sceneObject.dynamicIcon`](sim-2/property_sceneObject_dynamicIcon.md) — Dynamic icon
- [`sceneObject.dynamicallyEnabled`](sim-2/property_sceneObject_dynamicallyEnabled.md) — Dynamically enabled
- [`sceneObject.model.notDynamic`](sim-2/property_sceneObject_model_notDynamic.md) — Model not dynamic
- [`sceneObject.model.notRespondable`](sim-2/property_sceneObject_model_notRespondable.md) — Model not respondable
- [`shape.convex`](sim-2/property_shape_convex.md) — Convex
- [`shape.dynamics.angularVelocity`](sim-2/property_shape_dynamics_angularVelocity.md) — Rotational velocity
- [`shape.dynamics.bullet.angularDamping`](sim-2/property_shape_dynamics_bullet_angularDamping.md)
- [`shape.dynamics.bullet.autoShrinkConvexMeshes`](sim-2/property_shape_dynamics_bullet_autoShrinkConvexMeshes.md)
- [`shape.dynamics.bullet.customCollisionMarginConvexEnabled`](sim-2/property_shape_dynamics_bullet_customCollisionMarginConvexEnabled.md)
- [`shape.dynamics.bullet.customCollisionMarginConvexValue`](sim-2/property_shape_dynamics_bullet_customCollisionMarginConvexValue.md)
- [`shape.dynamics.bullet.customCollisionMarginEnabled`](sim-2/property_shape_dynamics_bullet_customCollisionMarginEnabled.md)
- [`shape.dynamics.bullet.customCollisionMarginValue`](sim-2/property_shape_dynamics_bullet_customCollisionMarginValue.md)
- [`shape.dynamics.bullet.friction`](sim-2/property_shape_dynamics_bullet_friction.md)
- [`shape.dynamics.bullet.frictionOld`](sim-2/property_shape_dynamics_bullet_frictionOld.md)
- [`shape.dynamics.bullet.linearDamping`](sim-2/property_shape_dynamics_bullet_linearDamping.md)
- [`shape.dynamics.bullet.restitution`](sim-2/property_shape_dynamics_bullet_restitution.md)
- [`shape.dynamics.bullet.stickyContact`](sim-2/property_shape_dynamics_bullet_stickyContact.md)
- [`shape.dynamics.centerOfMass`](sim-2/property_shape_dynamics_centerOfMass.md) — Center of mass
- [`shape.dynamics.dynamic`](sim-2/property_shape_dynamics_dynamic.md) — Dynamic
- [`shape.dynamics.engineProperties`](sim-2/property_shape_dynamics_engineProperties.md) — Engine properties
- [`shape.dynamics.inertiaMatrix`](sim-2/property_shape_dynamics_inertiaMatrix.md) — Inertia matrix
- [`shape.dynamics.initAngularVelocity`](sim-2/property_shape_dynamics_initAngularVelocity.md) — Initial rotational velocity
- [`shape.dynamics.initLinearVelocity`](sim-2/property_shape_dynamics_initLinearVelocity.md) — Initial linear velocity
- [`shape.dynamics.kinematic`](sim-2/property_shape_dynamics_kinematic.md) — Kinematic
- [`shape.dynamics.linearVelocity`](sim-2/property_shape_dynamics_linearVelocity.md) — Linear velocity
- [`shape.dynamics.mass`](sim-2/property_shape_dynamics_mass.md) — Mass
- [`shape.dynamics.mujoco.adhesion`](sim-2/property_shape_dynamics_mujoco_adhesion.md)
- [`shape.dynamics.mujoco.adhesionctrl`](sim-2/property_shape_dynamics_mujoco_adhesionctrl.md)
- [`shape.dynamics.mujoco.adhesionctrlrange`](sim-2/property_shape_dynamics_mujoco_adhesionctrlrange.md)
- [`shape.dynamics.mujoco.adhesionforcelimited`](sim-2/property_shape_dynamics_mujoco_adhesionforcelimited.md)
- [`shape.dynamics.mujoco.adhesionforcerange`](sim-2/property_shape_dynamics_mujoco_adhesionforcerange.md)
- [`shape.dynamics.mujoco.adhesiongain`](sim-2/property_shape_dynamics_mujoco_adhesiongain.md)
- [`shape.dynamics.mujoco.condim`](sim-2/property_shape_dynamics_mujoco_condim.md)
- [`shape.dynamics.mujoco.friction`](sim-2/property_shape_dynamics_mujoco_friction.md)
- [`shape.dynamics.mujoco.gap`](sim-2/property_shape_dynamics_mujoco_gap.md)
- [`shape.dynamics.mujoco.gravcomp`](sim-2/property_shape_dynamics_mujoco_gravcomp.md)
- [`shape.dynamics.mujoco.margin`](sim-2/property_shape_dynamics_mujoco_margin.md)
- [`shape.dynamics.mujoco.priority`](sim-2/property_shape_dynamics_mujoco_priority.md)
- [`shape.dynamics.mujoco.solimp`](sim-2/property_shape_dynamics_mujoco_solimp.md)
- [`shape.dynamics.mujoco.solmix`](sim-2/property_shape_dynamics_mujoco_solmix.md)
- [`shape.dynamics.mujoco.solref`](sim-2/property_shape_dynamics_mujoco_solref.md)
- [`shape.dynamics.newton.angularDrag`](sim-2/property_shape_dynamics_newton_angularDrag.md)
- [`shape.dynamics.newton.fastMoving`](sim-2/property_shape_dynamics_newton_fastMoving.md)
- [`shape.dynamics.newton.kineticFriction`](sim-2/property_shape_dynamics_newton_kineticFriction.md)
- [`shape.dynamics.newton.linearDrag`](sim-2/property_shape_dynamics_newton_linearDrag.md)
- [`shape.dynamics.newton.restitution`](sim-2/property_shape_dynamics_newton_restitution.md)
- [`shape.dynamics.newton.staticFriction`](sim-2/property_shape_dynamics_newton_staticFriction.md)
- [`shape.dynamics.ode.angularDamping`](sim-2/property_shape_dynamics_ode_angularDamping.md)
- [`shape.dynamics.ode.friction`](sim-2/property_shape_dynamics_ode_friction.md)
- [`shape.dynamics.ode.linearDamping`](sim-2/property_shape_dynamics_ode_linearDamping.md)
- [`shape.dynamics.ode.maxContacts`](sim-2/property_shape_dynamics_ode_maxContacts.md)
- [`shape.dynamics.ode.softCfm`](sim-2/property_shape_dynamics_ode_softCfm.md)
- [`shape.dynamics.ode.softErp`](sim-2/property_shape_dynamics_ode_softErp.md)
- [`shape.dynamics.pmi`](sim-2/property_shape_dynamics_pmi.md) — Principal moment of inertia
- [`shape.dynamics.pmiQuaternion`](sim-2/property_shape_dynamics_pmiQuaternion.md) — Quaternion of the principal moment of inertia
- [`shape.dynamics.respondable`](sim-2/property_shape_dynamics_respondable.md) — Respondable
- [`shape.dynamics.respondableMask`](sim-2/property_shape_dynamics_respondableMask.md) — Respondable mask
- [`shape.dynamics.setToDynamicWithParent`](sim-2/property_shape_dynamics_setToDynamicWithParent.md) — Set to dynamic if gets parent
- [`shape.dynamics.startInSleepMode`](sim-2/property_shape_dynamics_startInSleepMode.md) — Start in sleep mode
- [`shape.dynamics.vortex.adhesiveForce`](sim-2/property_shape_dynamics_vortex_adhesiveForce.md)
- [`shape.dynamics.vortex.angularNormalAxisFollowPrimaryAxis`](sim-2/property_shape_dynamics_vortex_angularNormalAxisFollowPrimaryAxis.md)
- [`shape.dynamics.vortex.angularNormalAxisFrictionModel`](sim-2/property_shape_dynamics_vortex_angularNormalAxisFrictionModel.md)
- [`shape.dynamics.vortex.angularNormalAxisFrictionValue`](sim-2/property_shape_dynamics_vortex_angularNormalAxisFrictionValue.md)
- [`shape.dynamics.vortex.angularNormalAxisSlide`](sim-2/property_shape_dynamics_vortex_angularNormalAxisSlide.md)
- [`shape.dynamics.vortex.angularNormalAxisSlip`](sim-2/property_shape_dynamics_vortex_angularNormalAxisSlip.md)
- [`shape.dynamics.vortex.angularNormalAxisStaticFrictionScale`](sim-2/property_shape_dynamics_vortex_angularNormalAxisStaticFrictionScale.md)
- [`shape.dynamics.vortex.angularPrimaryAxisFrictionModel`](sim-2/property_shape_dynamics_vortex_angularPrimaryAxisFrictionModel.md)
- [`shape.dynamics.vortex.angularPrimaryAxisFrictionValue`](sim-2/property_shape_dynamics_vortex_angularPrimaryAxisFrictionValue.md)
- [`shape.dynamics.vortex.angularPrimaryAxisSlide`](sim-2/property_shape_dynamics_vortex_angularPrimaryAxisSlide.md)
- [`shape.dynamics.vortex.angularPrimaryAxisSlip`](sim-2/property_shape_dynamics_vortex_angularPrimaryAxisSlip.md)
- [`shape.dynamics.vortex.angularPrimaryAxisStaticFrictionScale`](sim-2/property_shape_dynamics_vortex_angularPrimaryAxisStaticFrictionScale.md)
- [`shape.dynamics.vortex.angularSecondaryAxisFollowPrimaryAxis`](sim-2/property_shape_dynamics_vortex_angularSecondaryAxisFollowPrimaryAxis.md)
- [`shape.dynamics.vortex.angularSecondaryAxisFrictionModel`](sim-2/property_shape_dynamics_vortex_angularSecondaryAxisFrictionModel.md)
- [`shape.dynamics.vortex.angularSecondaryAxisFrictionValue`](sim-2/property_shape_dynamics_vortex_angularSecondaryAxisFrictionValue.md)
- [`shape.dynamics.vortex.angularSecondaryAxisSlide`](sim-2/property_shape_dynamics_vortex_angularSecondaryAxisSlide.md)
- [`shape.dynamics.vortex.angularSecondaryAxisSlip`](sim-2/property_shape_dynamics_vortex_angularSecondaryAxisSlip.md)
- [`shape.dynamics.vortex.angularSecondaryAxisStaticFrictionScale`](sim-2/property_shape_dynamics_vortex_angularSecondaryAxisStaticFrictionScale.md)
- [`shape.dynamics.vortex.angularVelDamping`](sim-2/property_shape_dynamics_vortex_angularVelDamping.md)
- [`shape.dynamics.vortex.autoAngularDampingEnabled`](sim-2/property_shape_dynamics_vortex_autoAngularDampingEnabled.md)
- [`shape.dynamics.vortex.autoAngularDampingTensionRatio`](sim-2/property_shape_dynamics_vortex_autoAngularDampingTensionRatio.md)
- [`shape.dynamics.vortex.autoSleepThresholdAngularAccel`](sim-2/property_shape_dynamics_vortex_autoSleepThresholdAngularAccel.md)
- [`shape.dynamics.vortex.autoSleepThresholdAngularSpeed`](sim-2/property_shape_dynamics_vortex_autoSleepThresholdAngularSpeed.md)
- [`shape.dynamics.vortex.autoSleepThresholdLinearAccel`](sim-2/property_shape_dynamics_vortex_autoSleepThresholdLinearAccel.md)
- [`shape.dynamics.vortex.autoSleepThresholdLinearSpeed`](sim-2/property_shape_dynamics_vortex_autoSleepThresholdLinearSpeed.md)
- [`shape.dynamics.vortex.autoSleepThresholdSteps`](sim-2/property_shape_dynamics_vortex_autoSleepThresholdSteps.md)
- [`shape.dynamics.vortex.autoSlip`](sim-2/property_shape_dynamics_vortex_autoSlip.md)
- [`shape.dynamics.vortex.compliance`](sim-2/property_shape_dynamics_vortex_compliance.md)
- [`shape.dynamics.vortex.convexAsRandom`](sim-2/property_shape_dynamics_vortex_convexAsRandom.md)
- [`shape.dynamics.vortex.damping`](sim-2/property_shape_dynamics_vortex_damping.md)
- [`shape.dynamics.vortex.fastMoving`](sim-2/property_shape_dynamics_vortex_fastMoving.md)
- [`shape.dynamics.vortex.linearPrimaryAxisFrictionModel`](sim-2/property_shape_dynamics_vortex_linearPrimaryAxisFrictionModel.md)
- [`shape.dynamics.vortex.linearPrimaryAxisFrictionValue`](sim-2/property_shape_dynamics_vortex_linearPrimaryAxisFrictionValue.md)
- [`shape.dynamics.vortex.linearPrimaryAxisSlide`](sim-2/property_shape_dynamics_vortex_linearPrimaryAxisSlide.md)
- [`shape.dynamics.vortex.linearPrimaryAxisSlip`](sim-2/property_shape_dynamics_vortex_linearPrimaryAxisSlip.md)
- [`shape.dynamics.vortex.linearPrimaryAxisStaticFrictionScale`](sim-2/property_shape_dynamics_vortex_linearPrimaryAxisStaticFrictionScale.md)
- [`shape.dynamics.vortex.linearPrimaryValue`](sim-2/property_shape_dynamics_vortex_linearPrimaryValue.md)
- [`shape.dynamics.vortex.linearSecondaryAxisFollowPrimaryAxis`](sim-2/property_shape_dynamics_vortex_linearSecondaryAxisFollowPrimaryAxis.md)
- [`shape.dynamics.vortex.linearSecondaryAxisFrictionModel`](sim-2/property_shape_dynamics_vortex_linearSecondaryAxisFrictionModel.md)
- [`shape.dynamics.vortex.linearSecondaryAxisFrictionValue`](sim-2/property_shape_dynamics_vortex_linearSecondaryAxisFrictionValue.md)
- [`shape.dynamics.vortex.linearSecondaryAxisSlide`](sim-2/property_shape_dynamics_vortex_linearSecondaryAxisSlide.md)
- [`shape.dynamics.vortex.linearSecondaryAxisSlip`](sim-2/property_shape_dynamics_vortex_linearSecondaryAxisSlip.md)
- [`shape.dynamics.vortex.linearSecondaryAxisStaticFrictionScale`](sim-2/property_shape_dynamics_vortex_linearSecondaryAxisStaticFrictionScale.md)
- [`shape.dynamics.vortex.linearVelDamping`](sim-2/property_shape_dynamics_vortex_linearVelDamping.md)
- [`shape.dynamics.vortex.materialUniqueId`](sim-2/property_shape_dynamics_vortex_materialUniqueId.md)
- [`shape.dynamics.vortex.primitiveAsConvex`](sim-2/property_shape_dynamics_vortex_primitiveAsConvex.md)
- [`shape.dynamics.vortex.randomAsTerrain`](sim-2/property_shape_dynamics_vortex_randomAsTerrain.md)
- [`shape.dynamics.vortex.restitution`](sim-2/property_shape_dynamics_vortex_restitution.md)
- [`shape.dynamics.vortex.restitutionThreshold`](sim-2/property_shape_dynamics_vortex_restitutionThreshold.md)
- [`shape.dynamics.vortex.skinThickness`](sim-2/property_shape_dynamics_vortex_skinThickness.md)
- [`shape.primitive`](sim-2/property_shape_primitive.md) — Primitive

## <a id="methodsAndProperties_property"></a><a id="methodsAndProperties_properties"></a><a id="methodsAndProperties_scriptParameters"></a>[Properties](properties.md) (methods & properties)

- [`object:getBoolProperty`](sim-2/object_getBoolProperty.md) — Fetches a boolean property
- [`object:getBufferProperty`](sim-2/object_getBufferProperty.md) — Fetches a buffer property
- [`object:getColorProperty`](sim-2/object_getColorProperty.md) — Fetches a color property
- [`object:getEnumProperty`](sim-2/object_getEnumProperty.md) — Fetches an enum property
- [`object:getFloatArrayProperty`](sim-2/object_getFloatArrayProperty.md) — Fetches a float array property
- [`object:getFloatProperty`](sim-2/object_getFloatProperty.md) — Fetches a float property
- [`object:getHandleArrayProperty`](sim-2/object_getHandleArrayProperty.md) — Fetches a handle array property
- [`object:getHandleProperty`](sim-2/object_getHandleProperty.md) — Fetches a handle property
- [`object:getIntArrayProperty`](sim-2/object_getIntArrayProperty.md) — Fetches an int array property
- [`object:getIntProperty`](sim-2/object_getIntProperty.md) — Fetches an int32 property
- [`object:getLongProperty`](sim-2/object_getLongProperty.md) — Fetches an int64 property
- [`object:getMatrixProperty`](sim-2/object_getMatrixProperty.md) — Fetches a matrix property
- [`object:getMethodProperty`](sim-2/object_getMethodProperty.md) — Fetches a method property
- [`object:getPoseProperty`](sim-2/object_getPoseProperty.md) — Fetches a pose property
- [`object:getProperties`](sim-2/object_getProperties.md) — Fetches all properties of a target
- [`object:getPropertiesInfos`](sim-2/object_getPropertiesInfos.md) — Fetches all property infos of a target
- [`object:getProperty`](sim-2/object_getProperty.md) — Convenience function to fetch a property
- [`object:getPropertyInfo`](sim-2/object_getPropertyInfo.md) — Fetches information about a property
- [`object:getPropertyInfos`](sim-2/object_getPropertyInfos.md) — Fetches an extended set of property infos
- [`object:getPropertyName`](sim-2/object_getPropertyName.md) — Fetches a property name by index
- [`object:getPropertyTypeString`](sim-2/object_getPropertyTypeString.md) — Gets string for a property type
- [`object:getQuaternionProperty`](sim-2/object_getQuaternionProperty.md) — Fetches a quaternion property
- [`object:getStringArrayProperty`](sim-2/object_getStringArrayProperty.md) — Fetches a text array property
- [`object:getStringProperty`](sim-2/object_getStringProperty.md) — Fetches a string property
- [`object:getTableProperty`](sim-2/object_getTableProperty.md) — Fetches a table property
- [`object:getVector3Property`](sim-2/object_getVector3Property.md) — Fetches a vector3 property
- [`object:removeProperty`](sim-2/object_removeProperty.md) — Removes a removable property
- [`object:setBoolProperty`](sim-2/object_setBoolProperty.md) — Sets a boolean property
- [`object:setBufferProperty`](sim-2/object_setBufferProperty.md) — Sets a buffer property
- [`object:setColorProperty`](sim-2/object_setColorProperty.md) — Sets a color property
- [`object:setEnumProperty`](sim-2/object_setEnumProperty.md) — Sets an enum property
- [`object:setFloatArrayProperty`](sim-2/object_setFloatArrayProperty.md) — Sets a float array property
- [`object:setFloatProperty`](sim-2/object_setFloatProperty.md) — Sets a float property
- [`object:setHandleArrayProperty`](sim-2/object_setHandleArrayProperty.md) — Sets a handle array property
- [`object:setHandleProperty`](sim-2/object_setHandleProperty.md) — Sets a handle property
- [`object:setIntArrayProperty`](sim-2/object_setIntArrayProperty.md) — Sets an int array property
- [`object:setIntProperty`](sim-2/object_setIntProperty.md) — Sets an int32 property
- [`object:setLongProperty`](sim-2/object_setLongProperty.md) — Sets an int64 property
- [`object:setMatrixProperty`](sim-2/object_setMatrixProperty.md) — Sets a matrix property
- [`object:setMethodProperty`](sim-2/object_setMethodProperty.md) — Sets a method property
- [`object:setPoseProperty`](sim-2/object_setPoseProperty.md) — Sets a pose property
- [`object:setProperties`](sim-2/object_setProperties.md) — Sets several properties at once
- [`object:setProperty`](sim-2/object_setProperty.md) — Convenience function to set a property
- [`object:setPropertyInfo`](sim-2/object_setPropertyInfo.md) — Sets information about a property
- [`object:setQuaternionProperty`](sim-2/object_setQuaternionProperty.md) — Sets a quaternion property
- [`object:setStringArrayProperty`](sim-2/object_setStringArrayProperty.md) — Sets a text array property
- [`object:setStringProperty`](sim-2/object_setStringProperty.md) — Sets a string property
- [`object:setTableProperty`](sim-2/object_setTableProperty.md) — Sets a table property
- [`object:setVector3Property`](sim-2/object_setVector3Property.md) — Sets a vector3 property

## <a id="methodsAndProperties_collision"></a><a id="methodsAndProperties_collisionDetection"></a>[Collision detection](collisionDetection.md) (methods & properties)

- [`collection:checkCollision`](sim-2/collection_checkCollision.md) — Checks collision with another entity
- [`ocTree:checkPackedPoints`](sim-2/ocTree_checkPackedPoints.md) — Checks if packed points collide with voxels
- [`ocTree:checkPoints`](sim-2/ocTree_checkPoints.md) — Checks if points collide with the voxels
- [`sceneObject:checkCollision`](sim-2/sceneObject_checkCollision.md) — Checks collision with another entity
- [`sceneObject.collectionSelfCollisionIndicator`](sim-2/property_sceneObject_collectionSelfCollisionIndicator.md) — Collection self-collision indicator
- [`sceneObject.collidable`](sim-2/property_sceneObject_collidable.md) — Collidable
- [`sceneObject.model.notCollidable`](sim-2/property_sceneObject_model_notCollidable.md) — Model not collidable

## <a id="methodsAndProperties_distance"></a><a id="methodsAndProperties_distanceCalculation"></a>[Distance calculation](distanceCalculation.md) (methods & properties)

- [`collection:checkDistance`](sim-2/collection_checkDistance.md) — Checks minimum distance with another entity
- [`sceneObject:checkDistance`](sim-2/sceneObject_checkDistance.md) — Checks minimum distance with another entity
- [`proximitySensor.detectedDistance`](sim-2/property_proximitySensor_detectedDistance.md) — Detected distance
- [`sceneObject.measurable`](sim-2/property_sceneObject_measurable.md) — Measurable
- [`sceneObject.model.notMeasurable`](sim-2/property_sceneObject_model_notMeasurable.md) — Model not measurable

## <a id="methodsAndProperties_rendering"></a>[Rendering](dataVisualizationAndOutput.md) (methods & properties)

- [`collection:changeColor`](sim-2/collection_changeColor.md) — Changes the color of all shapes in the collection
- [`collection:restoreColor`](sim-2/collection_restoreColor.md) — Restores the color of shapes in the collection
- [`marker:addItems`](sim-2/marker_addItems.md) — Adds items to a marker
- [`marker:clearItems`](sim-2/marker_clearItems.md) — Clears a marker
- [`marker:removeItems`](sim-2/marker_removeItems.md) — Removes specific items from a marker
- [`sceneObject:changeColor`](sim-2/sceneObject_changeColor.md) — Changes the color of the object (if shape)
- [`sceneObject:restoreColor`](sim-2/sceneObject_restoreColor.md) — Restores the object's color (if shape)
- [`shape:getAppearance`](sim-2/shape_getAppearance.md) — Fetches the shape's main appearance properties
- [`shape:setAppearance`](sim-2/shape_setAppearance.md) — Sets the shape's main appearance properties
- [`app.displayEnabled`](sim-2/property_app_displayEnabled.md) — Display enabled
- [`app.headlessMode`](sim-2/property_app_headlessMode.md) — Headless mode
- [`camera.clippingPlanes`](sim-2/property_camera_clippingPlanes.md) — Clipping planes
- [`camera.color.diffuse`](sim-2/property_camera_color_diffuse.md) — Diffuse color
- [`camera.color.emission`](sim-2/property_camera_color_emission.md) — Emission color
- [`camera.color.specular`](sim-2/property_camera_color_specular.md) — Specular color
- [`camera.frustumCornerFar`](sim-2/property_camera_frustumCornerFar.md) — Far corner of view frustum
- [`camera.frustumCornerNear`](sim-2/property_camera_frustumCornerNear.md) — Near corner of view frustum
- [`camera.perspective`](sim-2/property_camera_perspective.md) — Perspective
- [`camera.resolution`](sim-2/property_camera_resolution.md) — Resolution
- [`camera.showFrustum`](sim-2/property_camera_showFrustum.md) — Show view frustum
- [`camera.size`](sim-2/property_camera_size.md) — Size
- [`camera.viewAngle`](sim-2/property_camera_viewAngle.md) — View angle
- [`camera.viewSize`](sim-2/property_camera_viewSize.md) — View size
- [`console.hiddenInSimulation`](sim-2/property_console_hiddenInSimulation.md) — Hides during simulation
- [`console.visible`](sim-2/property_console_visible.md) — Visible
- [`dummy.color.diffuse`](sim-2/property_dummy_color_diffuse.md) — Diffuse color
- [`dummy.color.emission`](sim-2/property_dummy_color_emission.md) — Emission color
- [`dummy.color.specular`](sim-2/property_dummy_color_specular.md) — Specular color
- [`dummy.size`](sim-2/property_dummy_size.md) — Size
- [`forceSensor.color.diffuse`](sim-2/property_forceSensor_color_diffuse.md) — Diffuse color
- [`forceSensor.color.emission`](sim-2/property_forceSensor_color_emission.md) — Emission color
- [`forceSensor.color.specular`](sim-2/property_forceSensor_color_specular.md) — Specular color
- [`forceSensor.size`](sim-2/property_forceSensor_size.md) — Size
- [`graph.backgroundColor`](sim-2/property_graph_backgroundColor.md) — Background color
- [`graph.color.diffuse`](sim-2/property_graph_color_diffuse.md) — Diffuse color
- [`graph.color.emission`](sim-2/property_graph_color_emission.md) — Emission color
- [`graph.color.specular`](sim-2/property_graph_color_specular.md) — Specular color
- [`graph.foregroundColor`](sim-2/property_graph_foregroundColor.md) — Foreground color
- [`graph.size`](sim-2/property_graph_size.md) — Size
- [`joint.color.diffuse`](sim-2/property_joint_color_diffuse.md) — Diffuse color
- [`joint.color.emission`](sim-2/property_joint_color_emission.md) — Emission color
- [`joint.color.specular`](sim-2/property_joint_color_specular.md) — Specular color
- [`joint.length`](sim-2/property_joint_length.md) — Length
- [`light.attenuationFactors`](sim-2/property_light_attenuationFactors.md) — Attenuation factors
- [`light.color.diffuse`](sim-2/property_light_color_diffuse.md) — Diffuse color
- [`light.color.emission`](sim-2/property_light_color_emission.md) — Emission color
- [`light.color.specular`](sim-2/property_light_color_specular.md) — Specular color
- [`light.enabled`](sim-2/property_light_enabled.md) — Enabled
- [`light.light.type`](sim-2/property_light_light_type.md) — Type
- [`light.lightColor.diffuse`](sim-2/property_light_lightColor_diffuse.md) — Diffuse color
- [`light.lightColor.emission`](sim-2/property_light_lightColor_emission.md) — Emission color
- [`light.lightColor.specular`](sim-2/property_light_lightColor_specular.md) — Specular color
- [`light.povray.castShadows`](sim-2/property_light_povray_castShadows.md) — POV-Ray: Cast shadows
- [`light.size`](sim-2/property_light_size.md) — Size
- [`light.spotCutoffAngle`](sim-2/property_light_spotCutoffAngle.md) — Cutoff angle
- [`light.spotExponent`](sim-2/property_light_spotExponent.md) — Spot exponent
- [`marker.colors`](sim-2/property_marker_colors.md) — Colors
- [`marker.indices`](sim-2/property_marker_indices.md) — Indices
- [`marker.local`](sim-2/property_marker_local.md) — Local
- [`marker.marker.type`](sim-2/property_marker_marker_type.md) — Type
- [`marker.normals`](sim-2/property_marker_normals.md) — Normals
- [`marker.overlay`](sim-2/property_marker_overlay.md) — Overlay
- [`marker.packedPoints`](sim-2/property_marker_packedPoints.md) — Packed points
- [`marker.packedQuaternions`](sim-2/property_marker_packedQuaternions.md) — Packed quaternions
- [`marker.packedSizes`](sim-2/property_marker_packedSizes.md) — Packed sizes
- [`marker.points`](sim-2/property_marker_points.md) — Points
- [`marker.quaternions`](sim-2/property_marker_quaternions.md) — Quaternions
- [`marker.sizes`](sim-2/property_marker_sizes.md) — Sizes
- [`marker.vertices`](sim-2/property_marker_vertices.md) — Vertices
- [`mesh.color.diffuse`](sim-2/property_mesh_color_diffuse.md) — Diffuse color
- [`mesh.color.emission`](sim-2/property_mesh_color_emission.md) — Emission color
- [`mesh.color.specular`](sim-2/property_mesh_color_specular.md) — Specular color
- [`mesh.color.transparency`](sim-2/property_mesh_color_transparency.md) — Transparency
- [`mesh.colorName`](sim-2/property_mesh_colorName.md) — Color name
- [`mesh.culling`](sim-2/property_mesh_culling.md) — Backface culling
- [`mesh.indices`](sim-2/property_mesh_indices.md) — Indices
- [`mesh.normals`](sim-2/property_mesh_normals.md) — Normals
- [`mesh.primitive`](sim-2/property_mesh_primitive.md) — Primitive type
- [`mesh.shadingAngle`](sim-2/property_mesh_shadingAngle.md) — Shading angle
- [`mesh.showEdges`](sim-2/property_mesh_showEdges.md) — Visible edges
- [`mesh.texture.applyMode`](sim-2/property_mesh_texture_applyMode.md) — Texture apply mode
- [`mesh.texture.interpolate`](sim-2/property_mesh_texture_interpolate.md) — Interpolate texture
- [`mesh.texture.repeatU`](sim-2/property_mesh_texture_repeatU.md) — Texture repeat U
- [`mesh.texture.repeatV`](sim-2/property_mesh_texture_repeatV.md) — Texture repeat V
- [`mesh.textureCoordinates`](sim-2/property_mesh_textureCoordinates.md) — Texture coordinates
- [`mesh.vertices`](sim-2/property_mesh_vertices.md) — Vertices
- [`mesh.wireframe`](sim-2/property_mesh_wireframe.md) — Wireframe
- [`ocTree.color.diffuse`](sim-2/property_ocTree_color_diffuse.md) — Diffuse color
- [`ocTree.color.emission`](sim-2/property_ocTree_color_emission.md) — Emission color
- [`ocTree.color.specular`](sim-2/property_ocTree_color_specular.md) — Specular color
- [`ocTree.colors`](sim-2/property_ocTree_colors.md) — Voxel colors
- [`ocTree.packedPoints`](sim-2/property_ocTree_packedPoints.md) — Packed voxels
- [`ocTree.points`](sim-2/property_ocTree_points.md) — Voxels
- [`ocTree.randomColors`](sim-2/property_ocTree_randomColors.md) — Random voxel colors
- [`ocTree.showPoints`](sim-2/property_ocTree_showPoints.md) — Show points instead of voxels
- [`ocTree.voxelSize`](sim-2/property_ocTree_voxelSize.md) — Voxel size
- [`pointCloud.cellSize`](sim-2/property_pointCloud_cellSize.md) — Cell size
- [`pointCloud.color.diffuse`](sim-2/property_pointCloud_color_diffuse.md) — Diffuse color
- [`pointCloud.color.emission`](sim-2/property_pointCloud_color_emission.md) — Emission color
- [`pointCloud.color.specular`](sim-2/property_pointCloud_color_specular.md) — Specular color
- [`pointCloud.colors`](sim-2/property_pointCloud_colors.md) — Colors
- [`pointCloud.maxPointsInCell`](sim-2/property_pointCloud_maxPointsInCell.md) — Max. points in cell
- [`pointCloud.packedPoints`](sim-2/property_pointCloud_packedPoints.md) — Packed points
- [`pointCloud.pointDisplayFraction`](sim-2/property_pointCloud_pointDisplayFraction.md) — Display fraction
- [`pointCloud.pointSize`](sim-2/property_pointCloud_pointSize.md) — Point size
- [`pointCloud.points`](sim-2/property_pointCloud_points.md) — Points
- [`pointCloud.randomColors`](sim-2/property_pointCloud_randomColors.md) — Random point colors
- [`proximitySensor.color.diffuse`](sim-2/property_proximitySensor_color_diffuse.md) — Diffuse color
- [`proximitySensor.color.emission`](sim-2/property_proximitySensor_color_emission.md) — Emission color
- [`proximitySensor.color.specular`](sim-2/property_proximitySensor_color_specular.md) — Specular color
- [`proximitySensor.pointSize`](sim-2/property_proximitySensor_pointSize.md) — Sensor point size
- [`proximitySensor.rayColor.diffuse`](sim-2/property_proximitySensor_rayColor_diffuse.md) — Diffuse color
- [`proximitySensor.rayColor.emission`](sim-2/property_proximitySensor_rayColor_emission.md) — Emission color
- [`proximitySensor.rayColor.specular`](sim-2/property_proximitySensor_rayColor_specular.md) — Specular color
- [`proximitySensor.showVolume`](sim-2/property_proximitySensor_showVolume.md) — Show volume
- [`scene.ambientLight`](sim-2/property_scene_ambientLight.md) — Ambient light
- [`scene.drawingObjects`](sim-2/property_scene_drawingObjects.md) — Drawing objects
- [`scene.dynamics.showContactPoints`](sim-2/property_scene_dynamics_showContactPoints.md) — Show contact points
- [`scene.visibilityLayers`](sim-2/property_scene_visibilityLayers.md) — Visibility layers
- [`sceneObject.depthInvisible`](sim-2/property_sceneObject_depthInvisible.md) — Depth pass invisible
- [`sceneObject.hideFromModelBB`](sim-2/property_sceneObject_hideFromModelBB.md) — Hide from model bounding box
- [`sceneObject.layer`](sim-2/property_sceneObject_layer.md) — Visibility layer
- [`sceneObject.model.notInParentBB`](sim-2/property_sceneObject_model_notInParentBB.md) — Model invisible to other models' bounding boxes
- [`sceneObject.model.notVisible`](sim-2/property_sceneObject_model_notVisible.md) — Model not visible
- [`sceneObject.visible`](sim-2/property_sceneObject_visible.md) — Visible
- [`scriptObject.color.diffuse`](sim-2/property_scriptObject_color_diffuse.md) — Diffuse color
- [`scriptObject.color.emission`](sim-2/property_scriptObject_color_emission.md) — Emission color
- [`scriptObject.color.specular`](sim-2/property_scriptObject_color_specular.md) — Specular color
- [`scriptObject.size`](sim-2/property_scriptObject_size.md) — Size
- [`shape.applyColor.diffuse`](sim-2/property_shape_applyColor_diffuse.md) — Apply diffuse color
- [`shape.applyColor.emission`](sim-2/property_shape_applyColor_emission.md) — Apply emission color
- [`shape.applyColor.specular`](sim-2/property_shape_applyColor_specular.md) — Apply specular color
- [`shape.applyColor.transparency`](sim-2/property_shape_applyColor_transparency.md) — Apply transparency
- [`shape.applyCulling`](sim-2/property_shape_applyCulling.md) — Apply culling
- [`shape.applyShadingAngle`](sim-2/property_shape_applyShadingAngle.md) — Apply shading
- [`shape.applyShowEdges`](sim-2/property_shape_applyShowEdges.md) — Apply edges
- [`shape.compoundColors.diffuse`](sim-2/property_shape_compoundColors_diffuse.md) — Diffuse color data
- [`shape.compoundColors.emission`](sim-2/property_shape_compoundColors_emission.md) — Emission color data
- [`shape.compoundColors.specular`](sim-2/property_shape_compoundColors_specular.md) — Specular color data
- [`shape.compoundColors.transparency`](sim-2/property_shape_compoundColors_transparency.md) — Transparency data
- [`shape.compoundCullings`](sim-2/property_shape_compoundCullings.md) — Culling data
- [`shape.compoundEdges`](sim-2/property_shape_compoundEdges.md) — Edge visibility data
- [`shape.compoundShadingAngles`](sim-2/property_shape_compoundShadingAngles.md) — Shading angle data
- [`shape.compoundWireframe`](sim-2/property_shape_compoundWireframe.md) — Wireframe data
- [`shape.flipFaces`](sim-2/property_shape_flipFaces.md) — Flip faces
- [`shape.meshes`](sim-2/property_shape_meshes.md) — Meshes
- [`textEditor.hiddenInSimulation`](sim-2/property_textEditor_hiddenInSimulation.md) — Hides during simulation
- [`textEditor.visible`](sim-2/property_textEditor_visible.md) — Visible
- [`textureData.image`](sim-2/property_textureData_image.md) — Image
- [`textureData.resolution`](sim-2/property_textureData_resolution.md) — Resolution
- [`visionSensor.backgroundColor`](sim-2/property_visionSensor_backgroundColor.md) — Background color
- [`visionSensor.backgroundColorFromEnvironment`](sim-2/property_visionSensor_backgroundColorFromEnvironment.md) — Background color from environment
- [`visionSensor.clippingPlanes`](sim-2/property_visionSensor_clippingPlanes.md) — Clipping planes
- [`visionSensor.color.diffuse`](sim-2/property_visionSensor_color_diffuse.md) — Diffuse color
- [`visionSensor.color.emission`](sim-2/property_visionSensor_color_emission.md) — Emission color
- [`visionSensor.color.specular`](sim-2/property_visionSensor_color_specular.md) — Specular color
- [`visionSensor.depth`](sim-2/property_visionSensor_depth.md) — Depth buffer
- [`visionSensor.frustumCornerFar`](sim-2/property_visionSensor_frustumCornerFar.md) — Far corner of view frustum
- [`visionSensor.frustumCornerNear`](sim-2/property_visionSensor_frustumCornerNear.md) — Near corner of view frustum
- [`visionSensor.image`](sim-2/property_visionSensor_image.md) — RGB buffer
- [`visionSensor.perspective`](sim-2/property_visionSensor_perspective.md) — Perspective
- [`visionSensor.povray.aperture`](sim-2/property_visionSensor_povray_aperture.md) — POV-Ray: aperture
- [`visionSensor.povray.blurDistance`](sim-2/property_visionSensor_povray_blurDistance.md) — POV-Ray: blur distance
- [`visionSensor.povray.blurSamples`](sim-2/property_visionSensor_povray_blurSamples.md) — POV-Ray: blur samples
- [`visionSensor.povray.focalBlur`](sim-2/property_visionSensor_povray_focalBlur.md) — POV-Ray: focal blur
- [`visionSensor.renderMode`](sim-2/property_visionSensor_renderMode.md) — Render mode
- [`visionSensor.resolution`](sim-2/property_visionSensor_resolution.md) — Resolution
- [`visionSensor.showFrustum`](sim-2/property_visionSensor_showFrustum.md) — Show view frustum
- [`visionSensor.size`](sim-2/property_visionSensor_size.md) — Size
- [`visionSensor.viewAngle`](sim-2/property_visionSensor_viewAngle.md) — View angle
- [`visionSensor.viewSize`](sim-2/property_visionSensor_viewSize.md) — View size

## <a id="methodsAndProperties_customization"></a><a id="methodsAndProperties_customizingLuaFunctions"></a><a id="methodsAndProperties_customScriptFunctions"></a>Customization (methods & properties)

- [`app:createCustomObjectClass`](sim-2/app_createCustomObjectClass.md) — Creates a custom object class
- [`customObject:makeObject`](sim-2/customObject_makeObject.md) — Instantiates a custom object from a class
- [`sceneObject:makeClass`](sim-2/sceneObject_makeClass.md) — Creates a class from this object
- [`sceneObject:makeObject`](sim-2/sceneObject_makeObject.md) — Instantiates a customized scene object from a class
- [`app.addOns`](sim-2/property_app_addOns.md) — Add-ons
- [`app.auxAddOn1`](sim-2/property_app_auxAddOn1.md) — Aux. add-on 1
- [`app.auxAddOn2`](sim-2/property_app_auxAddOn2.md) — Aux. add-on 2
- [`app.customClasses`](sim-2/property_app_customClasses.md) — Custom classes
- [`app.customObjects`](sim-2/property_app_customObjects.md) — Custom objects
- [`app.customSceneObjectClasses`](sim-2/property_app_customSceneObjectClasses.md) — Custom scene object classes
- [`app.paths.addOns`](sim-2/property_app_paths_addOns.md) — Add-on path
- [`app.paths.settings`](sim-2/property_app_paths_settings.md) — Settings path
- [`app.pluginNames`](sim-2/property_app_pluginNames.md) — Plugins
- [`camera.rotationEnabled`](sim-2/property_camera_rotationEnabled.md) — Rotation enabled
- [`camera.translationEnabled`](sim-2/property_camera_translationEnabled.md) — Translation enabled
- [`dummy.assemblyTag`](sim-2/property_dummy_assemblyTag.md) — Assembly tag
- [`scene.customObjects`](sim-2/property_scene_customObjects.md) — Custom objects
- [`sceneObject.cannotDelete`](sim-2/property_sceneObject_cannotDelete.md) — Cannot delete
- [`sceneObject.cannotDeleteInSim`](sim-2/property_sceneObject_cannotDeleteInSim.md) — Cannot delete during simulation
- [`sceneObject.hierarchyColor`](sim-2/property_sceneObject_hierarchyColor.md) — Hierarchy color

## <a id="methodsAndProperties_model"></a><a id="methodsAndProperties_modelFunctionality"></a>[Models](models.md) (methods & properties)

- [`app:loadModelInfo`](sim-2/app_loadModelInfo.md) — Loads a model thumbnail
- [`app:loadModelInfoFromBuffer`](sim-2/app_loadModelInfoFromBuffer.md) — Loads a model thumbnail from buffer
- [`scene:copyObjects`](sim-2/scene_copyObjects.md) — Copies selected objects
- [`scene:cutObjects`](sim-2/scene_cutObjects.md) — Cuts selected objects
- [`scene:loadModel`](sim-2/scene_loadModel.md) — Loads a previously saved model
- [`scene:loadModelFromBuffer`](sim-2/scene_loadModelFromBuffer.md) — Loads a model from buffer
- [`scene:pasteObjects`](sim-2/scene_pasteObjects.md) — Pastes objects
- [`sceneObject:saveModel`](sim-2/sceneObject_saveModel.md) — Saves this model to a file
- [`sceneObject:saveModelToBuffer`](sim-2/sceneObject_saveModelToBuffer.md) — Serializes this model to a buffer
- [`app.paths.models`](sim-2/property_app_paths_models.md) — Model path
- [`scene.collections`](sim-2/property_scene_collections.md) — Collections
- [`sceneObject.childOrder`](sim-2/property_sceneObject_childOrder.md) — Child order
- [`sceneObject.children`](sim-2/property_sceneObject_children.md) — Children
- [`sceneObject.collapsed`](sim-2/property_sceneObject_collapsed.md) — Collapsed hierarchy
- [`sceneObject.hideFromModelBB`](sim-2/property_sceneObject_hideFromModelBB.md) — Hide from model bounding box
- [`sceneObject.model.bbPos`](sim-2/property_sceneObject_model_bbPos.md) — Model bounding box position
- [`sceneObject.model.bbSize`](sim-2/property_sceneObject_model_bbSize.md) — Model bounding box size
- [`sceneObject.model.notCollidable`](sim-2/property_sceneObject_model_notCollidable.md) — Model not collidable
- [`sceneObject.model.notDetectable`](sim-2/property_sceneObject_model_notDetectable.md) — Model not detectable
- [`sceneObject.model.notDynamic`](sim-2/property_sceneObject_model_notDynamic.md) — Model not dynamic
- [`sceneObject.model.notInParentBB`](sim-2/property_sceneObject_model_notInParentBB.md) — Model invisible to other models' bounding boxes
- [`sceneObject.model.notMeasurable`](sim-2/property_sceneObject_model_notMeasurable.md) — Model not measurable
- [`sceneObject.model.notRespondable`](sim-2/property_sceneObject_model_notRespondable.md) — Model not respondable
- [`sceneObject.model.notVisible`](sim-2/property_sceneObject_model_notVisible.md) — Model not visible
- [`sceneObject.model.propertyFlags`](sim-2/property_sceneObject_model_propertyFlags.md) — Model flags
- [`sceneObject.model.scriptsNotActive`](sim-2/property_sceneObject_model_scriptsNotActive.md) — Model scripts inactive
- [`sceneObject.modelAcknowledgment`](sim-2/property_sceneObject_modelAcknowledgment.md) — Acknowledgment
- [`sceneObject.modelBase`](sim-2/property_sceneObject_modelBase.md) — Model base
- [`sceneObject.modelHash`](sim-2/property_sceneObject_modelHash.md) — Model hash
- [`sceneObject.modelInvisible`](sim-2/property_sceneObject_modelInvisible.md) — Inherited model invisibility
- [`sceneObject.parent`](sim-2/property_sceneObject_parent.md) — Parent
- [`sceneObject.parentUid`](sim-2/property_sceneObject_parentUid.md) — Parent UID
- [`sceneObject.persistentUid`](sim-2/property_sceneObject_persistentUid.md) — Persistent UID
- [`sceneObject.selectModel`](sim-2/property_sceneObject_selectModel.md) — Select model instead
- [`sceneObject.tree`](sim-2/property_sceneObject_tree.md) — Object tree

## <a id="methodsAndProperties_selection"></a><a id="methodsAndProperties_sceneObjectSelectionFunctionality"></a>Selection (methods & properties)

- [`app.current`](sim-2/property_app_current.md) — Current
- [`scene.selection`](sim-2/property_scene_selection.md) — Selected objects
- [`sceneObject.selectInvisible`](sim-2/property_sceneObject_selectInvisible.md) — Select invisible
- [`sceneObject.selectModel`](sim-2/property_sceneObject_selectModel.md) — Select model instead
- [`sceneObject.selectable`](sim-2/property_sceneObject_selectable.md) — Selectable
- [`sceneObject.selected`](sim-2/property_sceneObject_selected.md) — Selected

## <a id="methodsAndProperties_creation"></a><a id="methodsAndProperties_sceneObjectCreationFunctionality"></a>Object creation (methods & properties)

- [`app:createCustomObjectClass`](sim-2/app_createCustomObjectClass.md) — Creates a custom object class
- [`app:createObject`](sim-2/app_createObject.md) — Creates various objects (collections, scripts, sensors, etc.)
- [`app:removeObjects`](sim-2/app_removeObjects.md) — Removes one or several objects
- [`collection:remove`](sim-2/collection_remove.md) — Removes the collection
- [`console:remove`](sim-2/console_remove.md) — Removes the console
- [`customObject:makeObject`](sim-2/customObject_makeObject.md) — Instantiates a custom object from a class
- [`customObject:remove`](sim-2/customObject_remove.md) — Removes the custom scene object
- [`scene:createObject`](sim-2/scene_createObject.md) — Creates various objects (collections, scripts, sensors, etc.)
- [`scene:pasteObjects`](sim-2/scene_pasteObjects.md) — Pastes objects
- [`scene:removeObjects`](sim-2/scene_removeObjects.md) — Removes one or several objects
- [`sceneObject:remove`](sim-2/sceneObject_remove.md) — Removes the object from the scene
- [`sceneObject:removeModel`](sim-2/sceneObject_removeModel.md) — Removes the model from the scene
- [`script:remove`](sim-2/script_remove.md) — Removes the script
- [`textEditor:remove`](sim-2/textEditor_remove.md) — Removes the text editor
- [`textureData:remove`](sim-2/textureData_remove.md) — Removes the texture
- [`object.type`](sim-2/property_object_type.md) — Object type
- [`scene.objectCreationCounter`](sim-2/property_scene_objectCreationCounter.md) — Object creation counter
- [`scene.objectDestructionCounter`](sim-2/property_scene_objectDestructionCounter.md) — Object destruction counter
- [`scene.objects`](sim-2/property_scene_objects.md) — Objects
- [`scene.orphans`](sim-2/property_scene_orphans.md) — Orphan objects
- [`scene.simulation.removeNewObjects`](sim-2/property_scene_simulation_removeNewObjects.md) — Remove new objects

## <a id="methodsAndProperties_scriptRelated"></a>[Script related](scripts.md) (methods & properties)

- [`app:handleAddOns`](sim-2/app_handleAddOns.md) — Calls a system callback in add-ons
- [`app:handleSandboxes`](sim-2/app_handleSandboxes.md) — Calls a system callback in the sandbox
- [`scene:handleCustomizationScripts`](sim-2/scene_handleCustomizationScripts.md) — Calls a system callback in customization scripts
- [`scene:handleSimulationScripts`](sim-2/scene_handleSimulationScripts.md) — Calls a system callback in simulation scripts
- [`script:broadcast`](sim-2/script_broadcast.md) — Broadcasts a message to all other scripts
- [`script:callFunction`](sim-2/script_callFunction.md) — Calls a function
- [`script:callMethod`](sim-2/script_callMethod.md) — Calls a method
- [`script:cancelScheduledExecution`](sim-2/script_cancelScheduledExecution.md) — Cancels a scheduled function execution
- [`script:executeString`](sim-2/script_executeString.md) — Executes code from a string
- [`script:getFunctions`](sim-2/script_getFunctions.md) — Retrieves callable functions of the script
- [`script:getStackTraceback`](sim-2/script_getStackTraceback.md) — Retrieves and clears the last stack traceback
- [`script:getStepping`](sim-2/script_getStepping.md) — Informs whether the stepping operation mode is enabled
- [`script:init`](sim-2/script_init.md) — Initializes/reinitializes the script
- [`script:lock`](sim-2/script_lock.md) — Acquires/releases a script lock to forbid yielding
- [`script:registerFunctionHook`](sim-2/script_registerFunctionHook.md) — Registers a function hook for callbacks
- [`script:removeFunctionHook`](sim-2/script_removeFunctionHook.md) — Removes a function hook
- [`script:reset`](sim-2/script_reset.md) — Resets/ends the script
- [`script:resume`](sim-2/script_resume.md) — Resumes the suspended script
- [`script:scheduleExecution`](sim-2/script_scheduleExecution.md) — Schedules a function for execution after a delay
- [`script:setEventFilters`](sim-2/script_setEventFilters.md) — Specifies filters for the sysCall_event callback
- [`script:setStepping`](sim-2/script_setStepping.md) — Enables/disables stepping operation mode
- [`script:step`](sim-2/script_step.md) — Triggers the next simulation step
- [`script:suspend`](sim-2/script_suspend.md) — Suspends the script
- [`script:throttle`](sim-2/script_throttle.md) — Limits the rate of a function call
- [`script:yield`](sim-2/script_yield.md) — Identical to step()
- [`app.defaultPython`](sim-2/property_app_defaultPython.md) — Default Python
- [`app.execUnsafe`](sim-2/property_app_execUnsafe.md) — Execute unsafe
- [`app.execUnsafeExt`](sim-2/property_app_execUnsafeExt.md) — Execute unsafe extended
- [`app.paths.lua`](sim-2/property_app_paths_lua.md) — Lua path
- [`app.paths.python`](sim-2/property_app_paths_python.md) — Python path
- [`app.luaSandbox`](sim-2/property_app_luaSandbox.md) — Lua sandbox
- [`app.sandbox2`](sim-2/property_app_sandbox2.md) — Python sandbox
- [`app.startupCode`](sim-2/property_app_startupCode.md) — Start-up code
- [`proximitySensor.explicitHandling`](sim-2/property_proximitySensor_explicitHandling.md) — Explicit handling
- [`scene.mainScript`](sim-2/property_scene_mainScript.md) — Main script
- [`sceneObject.model.scriptsNotActive`](sim-2/property_sceneObject_model_scriptsNotActive.md) — Model scripts inactive
- [`script.addOnMenuPath`](sim-2/property_script_addOnMenuPath.md) — Add-on menu path
- [`script.addOnPath`](sim-2/property_script_addOnPath.md) — Add-on path
- [`script.autoYieldDelay`](sim-2/property_script_autoYieldDelay.md) — Automatic yield delay
- [`script.code`](sim-2/property_script_code.md) — Code
- [`script.enabled`](sim-2/property_script_enabled.md) — Enabled
- [`script.execPriority`](sim-2/property_script_execPriority.md) — Execution priority
- [`script.executionDepth`](sim-2/property_script_executionDepth.md) — Execution depth
- [`script.language`](sim-2/property_script_language.md) — Language
- [`script.restartOnError`](sim-2/property_script_restartOnError.md) — Restart
- [`script.script.type`](sim-2/property_script_script_type.md) — Type
- [`script.scriptName`](sim-2/property_script_scriptName.md) — Name
- [`script.state`](sim-2/property_script_state.md) — State
- [`visionSensor.explicitHandling`](sim-2/property_visionSensor_explicitHandling.md) — Explicit handling

## <a id="methodsAndProperties_simulation"></a><a id="methodsAndProperties_SimulationFunctionality"></a>[Simulation](simulation.md) (methods & properties)

- [`scene.simulation:pause`](sim-2/scene_simulation_pause.md) — Requests a simulation pause
- [`scene.simulation:start`](sim-2/scene_simulation_start.md) — Requests a simulation start or resume
- [`scene.simulation:stop`](sim-2/scene_simulation_stop.md) — Requests a simulation stop
- [`app.paths.mujoco`](sim-2/property_app_paths_mujoco.md) — MuJoCo path
- [`scene.dynamics.stepSize`](sim-2/property_scene_dynamics_stepSize.md) — Dynamics dt
- [`scene.simulation.pauseAtError`](sim-2/property_scene_simulation_pauseAtError.md) — Pause simulation on script error
- [`scene.simulation.pauseAtTime`](sim-2/property_scene_simulation_pauseAtTime.md) — Pause simulation at time
- [`scene.simulation.realtime`](sim-2/property_scene_simulation_realtime.md) — Real-time simulation
- [`scene.simulation.realtimeModifier`](sim-2/property_scene_simulation_realtimeModifier.md) — Real-time modifier
- [`scene.simulation.removeNewObjects`](sim-2/property_scene_simulation_removeNewObjects.md) — Remove new objects
- [`scene.simulation.speedModifier`](sim-2/property_scene_simulation_speedModifier.md) — Speed modifier
- [`scene.simulation.state`](sim-2/property_scene_simulation_state.md) — Simulation state
- [`scene.simulation.stepCount`](sim-2/property_scene_simulation_stepCount.md) — Simulation steps
- [`scene.simulation.stepsPerRendering`](sim-2/property_scene_simulation_stepsPerRendering.md) — Steps per frame
- [`scene.simulation.time`](sim-2/property_scene_simulation_time.md) — Simulation time
- [`scene.simulation.timeStep`](sim-2/property_scene_simulation_timeStep.md) — Simulation dt
- [`scene.simulation.timeToPause`](sim-2/property_scene_simulation_timeToPause.md) — Simulation pause time
- [`scriptObject.resetAfterSimError`](sim-2/property_scriptObject_resetAfterSimError.md) — Reset after simulation error

## <a id="methodsAndProperties_thread"></a><a id="methodsAndProperties_threads"></a><a id="methodsAndProperties_threadRelatedFunctionality"></a>[Threads](threadedAndNonThreadedCode.md) (methods & properties)

- [`app:handleMessagePump`](sim-2/app_handleMessagePump.md) — Handles the message pump explicitly
- [`script:getStepping`](sim-2/script_getStepping.md) — Informs whether the stepping operation mode is enabled
- [`script:lock`](sim-2/script_lock.md) — Acquires/releases a script lock to forbid yielding
- [`script:setStepping`](sim-2/script_setStepping.md) — Enables/disables stepping operation mode
- [`script:step`](sim-2/script_step.md) — Triggers the next simulation step
- [`script:yield`](sim-2/script_yield.md) — Identical to step()
- [`scene.dynamics.mujoco.multithreaded`](sim-2/property_scene_dynamics_mujoco_multithreaded.md)
- [`scene.dynamics.newton.multithreading`](sim-2/property_scene_dynamics_newton_multithreading.md)
- [`scene.dynamics.vortex.multithreading`](sim-2/property_scene_dynamics_vortex_multithreading.md)
- [`script.autoYieldDelay`](sim-2/property_script_autoYieldDelay.md) — Automatic yield delay

## <a id="methodsAndProperties_blocking"></a><a id="methodsAndProperties_blockingFunctions"></a>Blocking methods (methods & properties)

- [`MoveToConfig:run`](sim-2/MoveToConfig_run.md) — Executes the motion in a thread
- [`MoveToPose:run`](sim-2/MoveToPose_run.md) — Executes the motion in a thread
- [`app:systemLock`](sim-2/app_systemLock.md) — Acquires/releases a system-wide semaphore
- [`script:getStepping`](sim-2/script_getStepping.md) — Informs whether the stepping operation mode is enabled
- [`script:lock`](sim-2/script_lock.md) — Acquires/releases a script lock to forbid yielding
- [`script:setStepping`](sim-2/script_setStepping.md) — Enables/disables stepping operation mode
- [`script:step`](sim-2/script_step.md) — Triggers the next simulation step
- [`script:wait`](sim-2/script_wait.md) — Waits for a certain amount of time
- [`script:yield`](sim-2/script_yield.md) — Identical to step()

## <a id="methodsAndProperties_transformation"></a><a id="methodsAndProperties_pose"></a><a id="methodsAndProperties_transformations"></a><a id="methodsAndProperties_coordinatesAndTransformations"></a>[Coordinates and transformations](positionOrientationTransformation.md) (methods & properties)

- [`IKObject:getPose`](sim-2/IKObject_getPose.md) — Retrieves the IK object's pose
- [`IKObject:getPosition`](sim-2/IKObject_getPosition.md) — Retrieves the IK object's position
- [`IKObject:getQuaternion`](sim-2/IKObject_getQuaternion.md) — Retrieves the IK object's quaternion
- [`IKObject:setPose`](sim-2/IKObject_setPose.md) — Sets the IK object's pose
- [`IKObject:setPosition`](sim-2/IKObject_setPosition.md) — Sets the IK object's position
- [`IKObject:setQuaternion`](sim-2/IKObject_setQuaternion.md) — Sets the IK object's quaternion
- [`sceneObject:getPose`](sim-2/sceneObject_getPose.md) — Retrieves the pose of the scene object
- [`sceneObject:getPosition`](sim-2/sceneObject_getPosition.md) — Retrieves the position of the scene object
- [`sceneObject:getQuaternion`](sim-2/sceneObject_getQuaternion.md) — Retrieves the quaternion of the scene object
- [`sceneObject:setPose`](sim-2/sceneObject_setPose.md) — Sets the pose of the scene object
- [`sceneObject:setPosition`](sim-2/sceneObject_setPosition.md) — Sets the position of the scene object
- [`sceneObject:setQuaternion`](sim-2/sceneObject_setQuaternion.md) — Sets the quaternion of the scene object
- [`shape:alignBoundingBox`](sim-2/shape_alignBoundingBox.md) — Reorients the shape's bounding box
- [`shape:relocateFrame`](sim-2/shape_relocateFrame.md) — Repositions/reorients the shape's reference frame
- [`app.defaultRotationStepSize`](sim-2/property_app_defaultRotationStepSize.md) — Rotation step size
- [`app.defaultTranslationStepSize`](sim-2/property_app_defaultTranslationStepSize.md) — Translation step size
- [`joint.intrinsicPose`](sim-2/property_joint_intrinsicPose.md) — Intrinsic pose
- [`joint.joint.quaternion`](sim-2/property_joint_joint_quaternion.md) — Spherical joint quaternion
- [`marker.local`](sim-2/property_marker_local.md) — Local
- [`marker.packedQuaternions`](sim-2/property_marker_packedQuaternions.md) — Packed quaternions
- [`marker.quaternions`](sim-2/property_marker_quaternions.md) — Quaternions
- [`sceneObject.eulerAngles`](sim-2/property_sceneObject_eulerAngles.md) — Euler angles
- [`sceneObject.mov.altRot`](sim-2/property_sceneObject_mov_altRot.md) — Alternate rotation axes enabled
- [`sceneObject.mov.altTransl`](sim-2/property_sceneObject_mov_altTransl.md) — Alternate translation axes enabled
- [`sceneObject.mov.optionsFlags`](sim-2/property_sceneObject_mov_optionsFlags.md) — Movement flags
- [`sceneObject.mov.prefRotX`](sim-2/property_sceneObject_mov_prefRotX.md) — Preferred X-axis rotation
- [`sceneObject.mov.prefRotY`](sim-2/property_sceneObject_mov_prefRotY.md) — Preferred Y-axis rotation
- [`sceneObject.mov.prefRotZ`](sim-2/property_sceneObject_mov_prefRotZ.md) — Preferred Z-axis rotation
- [`sceneObject.mov.prefTranslX`](sim-2/property_sceneObject_mov_prefTranslX.md) — Preferred X-translation
- [`sceneObject.mov.prefTranslY`](sim-2/property_sceneObject_mov_prefTranslY.md) — Preferred Y-translation
- [`sceneObject.mov.prefTranslZ`](sim-2/property_sceneObject_mov_prefTranslZ.md) — Preferred Z-translation
- [`sceneObject.mov.preferredAxesFlags`](sim-2/property_sceneObject_mov_preferredAxesFlags.md) — Preferred axes
- [`sceneObject.mov.relativity`](sim-2/property_sceneObject_mov_relativity.md) — Movement relativity
- [`sceneObject.mov.rotInSim`](sim-2/property_sceneObject_mov_rotInSim.md) — Rotation enabled during simulation
- [`sceneObject.mov.rotNoSim`](sim-2/property_sceneObject_mov_rotNoSim.md) — Rotation enabled
- [`sceneObject.mov.stepSize`](sim-2/property_sceneObject_mov_stepSize.md) — Movement step sizes
- [`sceneObject.mov.translInSim`](sim-2/property_sceneObject_mov_translInSim.md) — Translation enabled during simulation
- [`sceneObject.mov.translNoSim`](sim-2/property_sceneObject_mov_translNoSim.md) — Translation enabled
- [`sceneObject.pose`](sim-2/property_sceneObject_pose.md) — Pose
- [`sceneObject.position`](sim-2/property_sceneObject_position.md) — Position
- [`sceneObject.quaternion`](sim-2/property_sceneObject_quaternion.md) — Quaternion
- [`sceneObject.worldEulerAngles`](sim-2/property_sceneObject_worldEulerAngles.md) — Euler angles
- [`sceneObject.worldPose`](sim-2/property_sceneObject_worldPose.md) — Pose
- [`sceneObject.worldPosition`](sim-2/property_sceneObject_worldPosition.md) — Position
- [`sceneObject.worldQuaternion`](sim-2/property_sceneObject_worldQuaternion.md) — Quaternion

## <a id="methodsAndProperties_hierarchy"></a>Scene hierarchy (methods & properties)

- [`IKGroup:addElementFromScene`](sim-2/IKGroup_addElementFromScene.md) — Creates an IK element from the simulation world
- [`collection:addItem`](sim-2/collection_addItem.md) — Adds one or several items to the collection
- [`collection:removeItem`](sim-2/collection_removeItem.md) — Removes one or several items from the collection
- [`scene:getDescendants`](sim-2/scene_getDescendants.md) — Retrieves scene objects up to a specific depth
- [`scene:getObject`](sim-2/scene_getObject.md) — Retrieves an object by its path and name
- [`scene:getObjects`](sim-2/scene_getObjects.md) — Retrieves objects of a certain type
- [`scene:loadModel`](sim-2/scene_loadModel.md) — Loads a previously saved model
- [`scene:loadModelFromBuffer`](sim-2/scene_loadModelFromBuffer.md) — Loads a model from buffer
- [`sceneObject:getAncestors`](sim-2/sceneObject_getAncestors.md) — Retrieves ancestor scene objects
- [`sceneObject:getDescendants`](sim-2/sceneObject_getDescendants.md) — Retrieves descendant scene objects
- [`sceneObject:getObject`](sim-2/sceneObject_getObject.md) — Retrieves an object by its path and name
- [`sceneObject:removeModel`](sim-2/sceneObject_removeModel.md) — Removes the model from the scene
- [`sceneObject:saveModel`](sim-2/sceneObject_saveModel.md) — Saves this model to a file
- [`sceneObject:saveModelToBuffer`](sim-2/sceneObject_saveModelToBuffer.md) — Serializes this model to a buffer
- [`sceneObject:scaleTree`](sim-2/sceneObject_scaleTree.md) — Scales the object tree isometrically
- [`IKElement.base`](sim-2/property_IKElement_base.md)
- [`IKElement.jointList`](sim-2/property_IKElement_jointList.md)
- [`IKElement.target`](sim-2/property_IKElement_target.md)
- [`IKElement.tip`](sim-2/property_IKElement_tip.md)
- [`scene.hierarchyChangeCounter`](sim-2/property_scene_hierarchyChangeCounter.md) — Hierarchy change counter
- [`scene.orphans`](sim-2/property_scene_orphans.md) — Orphan objects
- [`sceneObject.childOrder`](sim-2/property_sceneObject_childOrder.md) — Child order
- [`sceneObject.children`](sim-2/property_sceneObject_children.md) — Children
- [`sceneObject.collapsed`](sim-2/property_sceneObject_collapsed.md) — Collapsed hierarchy
- [`sceneObject.collectionSelfCollisionIndicator`](sim-2/property_sceneObject_collectionSelfCollisionIndicator.md) — Collection self-collision indicator
- [`sceneObject.hierarchyColor`](sim-2/property_sceneObject_hierarchyColor.md) — Hierarchy color
- [`sceneObject.model.notInParentBB`](sim-2/property_sceneObject_model_notInParentBB.md) — Model invisible to other models' bounding boxes
- [`sceneObject.modelHash`](sim-2/property_sceneObject_modelHash.md) — Model hash
- [`sceneObject.parent`](sim-2/property_sceneObject_parent.md) — Parent
- [`sceneObject.selectModel`](sim-2/property_sceneObject_selectModel.md) — Select model instead
- [`sceneObject.tree`](sim-2/property_sceneObject_tree.md) — Object tree

## <a id="methodsAndProperties_messaging"></a>[Messaging](meansOfCommunication.md) (methods & properties)

- [`app:getGenesisEvents`](sim-2/app_getGenesisEvents.md) — Retrieves events to reconstruct the app's state
- [`app:logError`](sim-2/app_logError.md) — Outputs an error message in the status bar
- [`app:logInfo`](sim-2/app_logInfo.md) — Outputs an information message in the status bar
- [`app:logWarn`](sim-2/app_logWarn.md) — Outputs a warning message in the status bar
- [`app:pushEvent`](sim-2/app_pushEvent.md) — Pushes a user event for asynchronous reception
- [`app:systemLock`](sim-2/app_systemLock.md) — Acquires/releases a system-wide semaphore
- [`script:broadcast`](sim-2/script_broadcast.md) — Broadcasts a message to all other scripts
- [`script:callFunction`](sim-2/script_callFunction.md) — Calls a function
- [`script:callMethod`](sim-2/script_callMethod.md) — Calls a method
- [`script:executeString`](sim-2/script_executeString.md) — Executes code from a string
- [`script:getFunctions`](sim-2/script_getFunctions.md) — Retrieves callable functions of the script
- [`script:setEventFilters`](sim-2/script_setEventFilters.md) — Specifies filters for the sysCall_event callback
- [`app.consoleVerbosity`](sim-2/property_app_consoleVerbosity.md) — Console verbosity
- [`app.consoleVerbosityStr`](sim-2/property_app_consoleVerbosityStr.md) — Console verbosity string
- [`app.dialogVerbosity`](sim-2/property_app_dialogVerbosity.md) — Dialog verbosity
- [`app.dialogVerbosityStr`](sim-2/property_app_dialogVerbosityStr.md) — Dialog verbosity string
- [`app.notifyDeprecated`](sim-2/property_app_notifyDeprecated.md) — Notify deprecated
- [`app.protocolVersion`](sim-2/property_app_protocolVersion.md) — Protocol
- [`app.statusbarVerbosity`](sim-2/property_app_statusbarVerbosity.md) — Statusbar verbosity
- [`app.statusbarVerbosityStr`](sim-2/property_app_statusbarVerbosityStr.md) — Statusbar verbosity string
- [`sceneObject.modelAcknowledgment`](sim-2/property_sceneObject_modelAcknowledgment.md) — Acknowledgment
- [`visionSensor.emitDepthChangedEvent`](sim-2/property_visionSensor_emitDepthChangedEvent.md) — Emit depth change event
- [`visionSensor.emitImageChangedEvent`](sim-2/property_visionSensor_emitImageChangedEvent.md) — Emit image change event

## <a id="methodsAndProperties_console"></a><a id="methodsAndProperties_auxiliaryConsoles"></a><a id="methodsAndProperties_auxiliaryConsoleFunctions"></a>[console](dataVisualizationAndOutput.md#auxConsoles) (methods & properties)

- [`app:createObject`](sim-2/app_createObject.md) — Creates various objects (collections, scripts, sensors, etc.)
- [`app:removeObjects`](sim-2/app_removeObjects.md) — Removes one or several objects
- [`console:clear`](sim-2/console_clear.md) — Clears the console
- [`console:print`](sim-2/console_print.md) — Prints text to the console
- [`console:remove`](sim-2/console_remove.md) — Removes the console
- [`scene:createObject`](sim-2/scene_createObject.md) — Creates various objects (collections, scripts, sensors, etc.)
- [`scene:removeObjects`](sim-2/scene_removeObjects.md) — Removes one or several objects
- [`console.hiddenInSimulation`](sim-2/property_console_hiddenInSimulation.md) — Hides during simulation
- [`console.visible`](sim-2/property_console_visible.md) — Visible

## <a id="methodsAndProperties_textEditor"></a><a id="methodsAndProperties_textEditors"></a>[textEditor](dataVisualizationAndOutput.md#textEditors) (methods & properties)

- [`app:createObject`](sim-2/app_createObject.md) — Creates various objects (collections, scripts, sensors, etc.)
- [`app:removeObjects`](sim-2/app_removeObjects.md) — Removes one or several objects
- [`scene:createObject`](sim-2/scene_createObject.md) — Creates various objects (collections, scripts, sensors, etc.)
- [`scene:removeObjects`](sim-2/scene_removeObjects.md) — Removes one or several objects
- [`textEditor:remove`](sim-2/textEditor_remove.md) — Removes the text editor
- [`textEditor.hiddenInSimulation`](sim-2/property_textEditor_hiddenInSimulation.md) — Hides during simulation
- [`textEditor.visible`](sim-2/property_textEditor_visible.md) — Visible

## <a id="methodsAndProperties_importExport"></a><a id="methodsAndProperties_importExportFunctions"></a>[Import/export](importExport.md) (methods & properties)

- [`app:loadImage`](sim-2/app_loadImage.md) — Loads an image from file
- [`app:loadImageFromBuffer`](sim-2/app_loadImageFromBuffer.md) — Loads an image from memory
- [`app:saveImage`](sim-2/app_saveImage.md) — Saves an image to file
- [`app:saveImageToBuffer`](sim-2/app_saveImageToBuffer.md) — Saves an image to a buffer
- [`app.paths.importExport`](sim-2/property_app_paths_importExport.md) — Import/export path
- [`app.paths.scenes`](sim-2/property_app_paths_scenes.md) — Scene path

## <a id="methodsAndProperties_Motion"></a><a id="methodsAndProperties_rml"></a><a id="methodsAndProperties_ruckig"></a>Motion functionality (methods & properties)

- [`MoveToConfig:data`](sim-2/MoveToConfig_data.md) — Returns motion information
- [`MoveToConfig:new`](sim-2/MoveToConfig_new.md) — Initiates an n-DoF motion using Ruckig
- [`MoveToConfig:remove`](sim-2/MoveToConfig_remove.md) — Destroys the motion object
- [`MoveToConfig:run`](sim-2/MoveToConfig_run.md) — Executes the motion in a thread
- [`MoveToConfig:step`](sim-2/MoveToConfig_step.md) — Steps the motion
- [`MoveToPose:data`](sim-2/MoveToPose_data.md) — Returns motion information
- [`MoveToPose:new`](sim-2/MoveToPose_new.md) — Initiates pose-based motion using Ruckig
- [`MoveToPose:remove`](sim-2/MoveToPose_remove.md) — Destroys the motion object
- [`MoveToPose:run`](sim-2/MoveToPose_run.md) — Executes the motion in a thread
- [`MoveToPose:step`](sim-2/MoveToPose_step.md) — Steps the motion
- [`RuckigPosition:data`](sim-2/RuckigPosition_data.md) — Returns motion information
- [`RuckigPosition:new`](sim-2/RuckigPosition_new.md) — Initializes a Ruckig position trajectory generator
- [`RuckigPosition:remove`](sim-2/RuckigPosition_remove.md) — Destroys the motion object
- [`RuckigPosition:step`](sim-2/RuckigPosition_step.md) — Steps the motion
- [`RuckigVelocity:data`](sim-2/RuckigVelocity_data.md) — Returns motion information
- [`RuckigVelocity:new`](sim-2/RuckigVelocity_new.md) — Initializes a Ruckig velocity trajectory generator
- [`RuckigVelocity:remove`](sim-2/RuckigVelocity_remove.md) — Destroys the motion object
- [`RuckigVelocity:step`](sim-2/RuckigVelocity_step.md) — Steps the motion
- [`TimeOptimalTrajectory:generate`](sim-2/TimeOptimalTrajectory_generate.md) — Generates a time optimal trajectory
- [`TimeOptimalTrajectory:new`](sim-2/TimeOptimalTrajectory_new.md) — Initializes a time optimal trajectory generator
- [`TimeOptimalTrajectory:remove`](sim-2/TimeOptimalTrajectory_remove.md) — Destroys the motion object

## <a id="methodsAndProperties_MoveToConfig"></a><a id="methodsAndProperties_rml-2"></a><a id="methodsAndProperties_ruckig-2"></a>MoveToConfig (methods & properties)

- [`MoveToConfig:data`](sim-2/MoveToConfig_data.md) — Returns motion information
- [`MoveToConfig:new`](sim-2/MoveToConfig_new.md) — Initiates an n-DoF motion using Ruckig
- [`MoveToConfig:remove`](sim-2/MoveToConfig_remove.md) — Destroys the motion object
- [`MoveToConfig:run`](sim-2/MoveToConfig_run.md) — Executes the motion in a thread
- [`MoveToConfig:step`](sim-2/MoveToConfig_step.md) — Steps the motion

## <a id="methodsAndProperties_MoveToPose"></a><a id="methodsAndProperties_rml-3"></a><a id="methodsAndProperties_ruckig-3"></a>MoveToPose (methods & properties)

- [`MoveToPose:data`](sim-2/MoveToPose_data.md) — Returns motion information
- [`MoveToPose:new`](sim-2/MoveToPose_new.md) — Initiates pose-based motion using Ruckig
- [`MoveToPose:remove`](sim-2/MoveToPose_remove.md) — Destroys the motion object
- [`MoveToPose:run`](sim-2/MoveToPose_run.md) — Executes the motion in a thread
- [`MoveToPose:step`](sim-2/MoveToPose_step.md) — Steps the motion

## <a id="methodsAndProperties_TimeOptimalTrajectory"></a><a id="methodsAndProperties_rml-4"></a><a id="methodsAndProperties_ruckig-4"></a>TimeOptimalTrajectory (methods & properties)

- [`TimeOptimalTrajectory:generate`](sim-2/TimeOptimalTrajectory_generate.md) — Generates a time optimal trajectory
- [`TimeOptimalTrajectory:new`](sim-2/TimeOptimalTrajectory_new.md) — Initializes a time optimal trajectory generator
- [`TimeOptimalTrajectory:remove`](sim-2/TimeOptimalTrajectory_remove.md) — Destroys the motion object

## <a id="methodsAndProperties_RuckigPosition"></a><a id="methodsAndProperties_rml-5"></a><a id="methodsAndProperties_ruckig-5"></a>RuckigPosition (methods & properties)

- [`RuckigPosition:data`](sim-2/RuckigPosition_data.md) — Returns motion information
- [`RuckigPosition:new`](sim-2/RuckigPosition_new.md) — Initializes a Ruckig position trajectory generator
- [`RuckigPosition:remove`](sim-2/RuckigPosition_remove.md) — Destroys the motion object
- [`RuckigPosition:step`](sim-2/RuckigPosition_step.md) — Steps the motion

## <a id="methodsAndProperties_RuckigVelocity"></a><a id="methodsAndProperties_rml-6"></a><a id="methodsAndProperties_ruckig-6"></a>RuckigVelocity (methods & properties)

- [`RuckigVelocity:data`](sim-2/RuckigVelocity_data.md) — Returns motion information
- [`RuckigVelocity:new`](sim-2/RuckigVelocity_new.md) — Initializes a Ruckig velocity trajectory generator
- [`RuckigVelocity:remove`](sim-2/RuckigVelocity_remove.md) — Destroys the motion object
- [`RuckigVelocity:step`](sim-2/RuckigVelocity_step.md) — Steps the motion

## <a id="methodsAndProperties_packing"></a>Packing/unpacking (methods & properties)

- [`app:deserialize`](sim-2/app_deserialize.md) — Deserializes a buffer using CBOR format
- [`app:pack`](sim-2/app_pack.md) — Packs data using CoppeliaSim format
- [`app:packArray`](sim-2/app_packArray.md) — Packs an array of numbers as little-endian
- [`app:serialize`](sim-2/app_serialize.md) — Serializes data using CBOR format
- [`app:transformBuffer`](sim-2/app_transformBuffer.md) — Modifies a buffer (format, scale, offset)
- [`app:transformImage`](sim-2/app_transformImage.md) — Transforms an image (scaling, flipping)
- [`app:unpack`](sim-2/app_unpack.md) — Unpacks data using CoppeliaSim format
- [`app:unpackArray`](sim-2/app_unpackArray.md) — Unpacks a buffer into an array of numbers
- [`object:getBufferProperty`](sim-2/object_getBufferProperty.md) — Fetches a buffer property
- [`object:setBufferProperty`](sim-2/object_setBufferProperty.md) — Sets a buffer property

## <a id="methodsAndProperties_IK"></a>[IK](kinematics.md) (methods & properties)

- [`IK:createGroup`](sim-2/IK_createGroup.md) — Creates an IK group
- [`IK:new`](sim-2/IK_new.md) — Creates an IK world
- [`IK:remove`](sim-2/IK_remove.md) — Removes the IK world
- [`IK:solve`](sim-2/IK_solve.md) — Solves all enabled IK groups
- [`IK:syncFromScene`](sim-2/IK_syncFromScene.md) — Synchronizes IK world from the simulation world
- [`IK:syncToScene`](sim-2/IK_syncToScene.md) — Synchronizes simulation world from the IK world
- [`IK.groupList`](sim-2/property_IK_groupList.md)
- [`IK.joints`](sim-2/property_IK_joints.md)
- [`IK.objects`](sim-2/property_IK_objects.md)

## <a id="methodsAndProperties_IKObject"></a>[IKObject](solvingIkAndFk.md) (methods & properties)

- [`IKObject:getPose`](sim-2/IKObject_getPose.md) — Retrieves the IK object's pose
- [`IKObject:getPosition`](sim-2/IKObject_getPosition.md) — Retrieves the IK object's position
- [`IKObject:getQuaternion`](sim-2/IKObject_getQuaternion.md) — Retrieves the IK object's quaternion
- [`IKObject:setPose`](sim-2/IKObject_setPose.md) — Sets the IK object's pose
- [`IKObject:setPosition`](sim-2/IKObject_setPosition.md) — Sets the IK object's position
- [`IKObject:setQuaternion`](sim-2/IKObject_setQuaternion.md) — Sets the IK object's quaternion
- [`IKObject.sceneObjectHandle`](sim-2/property_IKObject_sceneObjectHandle.md)
- [`IKObject.type`](sim-2/property_IKObject_type.md)

## <a id="methodsAndProperties_IKJoint"></a>[IKjoint](solvingIkAndFk.md) (methods & properties)

- [`IKJoint.bounds`](sim-2/property_IKJoint_bounds.md)
- [`IKJoint.jointConfiguration`](sim-2/property_IKJoint_jointConfiguration.md)
- [`IKJoint.jointPosition`](sim-2/property_IKJoint_jointPosition.md)
- [`IKJoint.jointQuaternion`](sim-2/property_IKJoint_jointQuaternion.md)
- [`IKJoint.jointType`](sim-2/property_IKJoint_jointType.md)
- [`IKJoint.limitMargin`](sim-2/property_IKJoint_limitMargin.md)
- [`IKJoint.maxStepSize`](sim-2/property_IKJoint_maxStepSize.md)
- [`IKJoint.passive`](sim-2/property_IKJoint_passive.md)
- [`IKJoint.weight`](sim-2/property_IKJoint_weight.md)

## <a id="methodsAndProperties_IKGroup"></a>[IKGroup](solvingIkAndFk.md) (methods & properties)

- [`IKGroup:addElementFromScene`](sim-2/IKGroup_addElementFromScene.md) — Creates an IK element from the simulation world
- [`IKGroup:computeJacobian`](sim-2/IKGroup_computeJacobian.md) — Computes the Jacobian and error vector
- [`IKGroup:findConfig`](sim-2/IKGroup_findConfig.md) — Searches for joint configurations satisfying target poses
- [`IKGroup:solve`](sim-2/IKGroup_solve.md) — Solves the IK group's constraints
- [`IKGroup:syncFromScene`](sim-2/IKGroup_syncFromScene.md) — Synchronizes this IK group from the simulation world
- [`IKGroup:syncToScene`](sim-2/IKGroup_syncToScene.md) — Synchronizes simulation world from this IK group
- [`IKGroup.damping`](sim-2/property_IKGroup_damping.md)
- [`IKGroup.elementList`](sim-2/property_IKGroup_elementList.md)
- [`IKGroup.enabled`](sim-2/property_IKGroup_enabled.md)
- [`IKGroup.maxIterations`](sim-2/property_IKGroup_maxIterations.md)
- [`IKGroup.method`](sim-2/property_IKGroup_method.md)

## <a id="methodsAndProperties_IKElement"></a>[IKElement](solvingIkAndFk.md) (methods & properties)

- [`IKElement.base`](sim-2/property_IKElement_base.md)
- [`IKElement.constraints`](sim-2/property_IKElement_constraints.md)
- [`IKElement.enabled`](sim-2/property_IKElement_enabled.md)
- [`IKElement.jointList`](sim-2/property_IKElement_jointList.md)
- [`IKElement.precision`](sim-2/property_IKElement_precision.md)
- [`IKElement.target`](sim-2/property_IKElement_target.md)
- [`IKElement.tip`](sim-2/property_IKElement_tip.md)
- [`IKElement.weights`](sim-2/property_IKElement_weights.md)

## <a id="methodsAndProperties_other"></a>Other (methods & properties)

- [`app:fastIdleLoop`](sim-2/app_fastIdleLoop.md) — Speeds up the idle loop for reactivity
- [`app:getEnumInfo`](sim-2/app_getEnumInfo.md) — Returns information about an enum
- [`app:getPluginInfo`](sim-2/app_getPluginInfo.md) — Returns information about a loaded plugin
- [`app:openFile`](sim-2/app_openFile.md) — Opens a file in a subprocess
- [`app:quit`](sim-2/app_quit.md) — Triggers a quit signal for the application
- [`app:setPluginInfo`](sim-2/app_setPluginInfo.md) — Modifies information of a loaded plugin
- [`object:isValid`](sim-2/object_isValid.md) — Checks if the object is valid
- [`scene:announceChange`](sim-2/scene_announceChange.md) — Announces a change in the scene for undo/redo
- [`scene:stepKinematicJoints`](sim-2/scene_stepKinematicJoints.md) — Steps all kinematic mode joints
- [`script:setModuleEntry`](sim-2/script_setModuleEntry.md) — Creates/modifies/destroys module menu entries

## <a id="methodsAndProperties_drawingObject"></a>drawingObject (deprecated, see marker instead) (methods & properties)

- [`drawingObject.appendColors`](sim-2/property_drawingObject_appendColors.md)
- [`drawingObject.appendPoints`](sim-2/property_drawingObject_appendPoints.md)
- [`drawingObject.appendQuaternions`](sim-2/property_drawingObject_appendQuaternions.md)
- [`drawingObject.colors`](sim-2/property_drawingObject_colors.md)
- [`drawingObject.cyclic`](sim-2/property_drawingObject_cyclic.md)
- [`drawingObject.itemType`](sim-2/property_drawingObject_itemType.md)
- [`drawingObject.maxCnt`](sim-2/property_drawingObject_maxCnt.md)
- [`drawingObject.overlay`](sim-2/property_drawingObject_overlay.md)
- [`drawingObject.parent`](sim-2/property_drawingObject_parent.md) — Parent
- [`drawingObject.parentUid`](sim-2/property_drawingObject_parentUid.md)
- [`drawingObject.points`](sim-2/property_drawingObject_points.md)
- [`drawingObject.quaternions`](sim-2/property_drawingObject_quaternions.md)
- [`drawingObject.size`](sim-2/property_drawingObject_size.md)

---

## <a id="functions_c_main"></a>Main (C-functions)

- [`simCallMethod`](sim-2/simCallMethod_cpp.md)
- [`simCreateBuffer`](sim-2/simCreateBuffer_cpp.md)
- [`simGetLastError`](sim-2/simGetLastError_cpp.md)
- [`simReleaseBuffer`](sim-2/simReleaseBuffer_cpp.md)
- [`simSetLastError`](sim-2/simSetLastError_cpp.md)

## <a id="functions_c_property"></a>[Properties](properties.md) (C-functions)

- [`simGetBoolProperty`](sim-2/simGetBoolProperty_cpp.md)
- [`simGetBufferProperty`](sim-2/simGetBufferProperty_cpp.md)
- [`simGetColor4Property`](sim-2/simGetColor4Property_cpp.md)
- [`simGetFloatArrayProperty`](sim-2/simGetFloatArrayProperty_cpp.md)
- [`simGetFloatProperty`](sim-2/simGetFloatProperty_cpp.md)
- [`simGetHandleArrayProperty`](sim-2/simGetHandleArrayProperty_cpp.md)
- [`simGetHandleProperty`](sim-2/simGetHandleProperty_cpp.md)
- [`simGetIntArrayProperty`](sim-2/simGetIntArrayProperty_cpp.md)
- [`simGetIntProperty`](sim-2/simGetIntProperty_cpp.md)
- [`simGetLongProperty`](sim-2/simGetLongProperty_cpp.md)
- [`simGetMatrixProperty`](sim-2/simGetMatrixProperty_cpp.md)
- [`simGetMethodProperty`](sim-2/simGetMethodProperty_cpp.md)
- [`simGetPoseProperty`](sim-2/simGetPoseProperty_cpp.md)
- [`simGetPropertyInfo`](sim-2/simGetPropertyInfo_cpp.md)
- [`simGetPropertyName`](sim-2/simGetPropertyName_cpp.md)
- [`simGetQuaternionProperty`](sim-2/simGetQuaternionProperty_cpp.md)
- [`simGetStringArrayProperty`](sim-2/simGetStringArrayProperty_cpp.md)
- [`simGetStringProperty`](sim-2/simGetStringProperty_cpp.md)
- [`simGetTableProperty`](sim-2/simGetTableProperty_cpp.md)
- [`simGetVector3Property`](sim-2/simGetVector3Property_cpp.md)
- [`simRemoveProperty`](sim-2/simRemoveProperty_cpp.md)
- [`simSetBoolProperty`](sim-2/simSetBoolProperty_cpp.md)
- [`simSetBufferProperty`](sim-2/simSetBufferProperty_cpp.md)
- [`simSetColor4Property`](sim-2/simSetColor4Property_cpp.md)
- [`simSetFloatArrayProperty`](sim-2/simSetFloatArrayProperty_cpp.md)
- [`simSetFloatProperty`](sim-2/simSetFloatProperty_cpp.md)
- [`simSetHandleArrayProperty`](sim-2/simSetHandleArrayProperty_cpp.md)
- [`simSetHandleProperty`](sim-2/simSetHandleProperty_cpp.md)
- [`simSetIntArrayProperty`](sim-2/simSetIntArrayProperty_cpp.md)
- [`simSetIntProperty`](sim-2/simSetIntProperty_cpp.md)
- [`simSetLongProperty`](sim-2/simSetLongProperty_cpp.md)
- [`simSetMatrixProperty`](sim-2/simSetMatrixProperty_cpp.md)
- [`simSetMethodProperty`](sim-2/simSetMethodProperty_cpp.md)
- [`simSetPoseProperty`](sim-2/simSetPoseProperty_cpp.md)
- [`simSetPropertyInfo`](sim-2/simSetPropertyInfo_cpp.md)
- [`simSetQuaternionProperty`](sim-2/simSetQuaternionProperty_cpp.md)
- [`simSetStringArrayProperty`](sim-2/simSetStringArrayProperty_cpp.md)
- [`simSetStringProperty`](sim-2/simSetStringProperty_cpp.md)
- [`simSetTableProperty`](sim-2/simSetTableProperty_cpp.md)
- [`simSetVector3Property`](sim-2/simSetVector3Property_cpp.md)

## <a id="functions_c_stack"></a>Stack (C-functions)

- [`simCallMethod`](sim-2/simCallMethod_cpp.md)
- [`simCopyStack`](sim-2/simCopyStack_cpp.md)
- [`simCreateStack`](sim-2/simCreateStack_cpp.md)
- [`simDebugStack`](sim-2/simDebugStack_cpp.md)
- [`simGetStackBoolValue`](sim-2/simGetStackBoolValue_cpp.md)
- [`simGetStackColor4`](sim-2/simGetStackColor4_cpp.md)
- [`simGetStackDoubleTable`](sim-2/simGetStackDoubleTable_cpp.md)
- [`simGetStackDoubleValue`](sim-2/simGetStackDoubleValue_cpp.md)
- [`simGetStackFloatTable`](sim-2/simGetStackFloatTable_cpp.md)
- [`simGetStackFloatValue`](sim-2/simGetStackFloatValue_cpp.md)
- [`simGetStackInt32Table`](sim-2/simGetStackInt32Table_cpp.md)
- [`simGetStackInt32Value`](sim-2/simGetStackInt32Value_cpp.md)
- [`simGetStackInt64Table`](sim-2/simGetStackInt64Table_cpp.md)
- [`simGetStackInt64Value`](sim-2/simGetStackInt64Value_cpp.md)
- [`simGetStackItemType`](sim-2/simGetStackItemType_cpp.md)
- [`simGetStackMatrix`](sim-2/simGetStackMatrix_cpp.md)
- [`simGetStackPose`](sim-2/simGetStackPose_cpp.md)
- [`simGetStackQuaternion`](sim-2/simGetStackQuaternion_cpp.md)
- [`simGetStackSize`](sim-2/simGetStackSize_cpp.md)
- [`simGetStackStringType`](sim-2/simGetStackStringType_cpp.md)
- [`simGetStackStringValue`](sim-2/simGetStackStringValue_cpp.md)
- [`simGetStackTableInfo`](sim-2/simGetStackTableInfo_cpp.md)
- [`simGetStackUInt8Table`](sim-2/simGetStackUInt8Table_cpp.md)
- [`simInsertDataIntoStackTable`](sim-2/simInsertDataIntoStackTable_cpp.md)
- [`simMoveStackItemToTop`](sim-2/simMoveStackItemToTop_cpp.md)
- [`simPackTable`](sim-2/simPackTable_cpp.md)
- [`simPopStackItem`](sim-2/simPopStackItem_cpp.md)
- [`simPushBoolOntoStack`](sim-2/simPushBoolOntoStack_cpp.md)
- [`simPushBufferOntoStack`](sim-2/simPushBufferOntoStack_cpp.md)
- [`simPushColor4OntoStack`](sim-2/simPushColor4OntoStack_cpp.md)
- [`simPushDoubleOntoStack`](sim-2/simPushDoubleOntoStack_cpp.md)
- [`simPushDoubleTableOntoStack`](sim-2/simPushDoubleTableOntoStack_cpp.md)
- [`simPushFloatOntoStack`](sim-2/simPushFloatOntoStack_cpp.md)
- [`simPushFloatTableOntoStack`](sim-2/simPushFloatTableOntoStack_cpp.md)
- [`simPushInt32OntoStack`](sim-2/simPushInt32OntoStack_cpp.md)
- [`simPushInt32TableOntoStack`](sim-2/simPushInt32TableOntoStack_cpp.md)
- [`simPushInt64OntoStack`](sim-2/simPushInt64OntoStack_cpp.md)
- [`simPushInt64TableOntoStack`](sim-2/simPushInt64TableOntoStack_cpp.md)
- [`simPushMatrixOntoStack`](sim-2/simPushMatrixOntoStack_cpp.md)
- [`simPushNullOntoStack`](sim-2/simPushNullOntoStack_cpp.md)
- [`simPushPoseOntoStack`](sim-2/simPushPoseOntoStack_cpp.md)
- [`simPushQuaternionOntoStack`](sim-2/simPushQuaternionOntoStack_cpp.md)
- [`simPushStringOntoStack`](sim-2/simPushStringOntoStack_cpp.md)
- [`simPushTableOntoStack`](sim-2/simPushTableOntoStack_cpp.md)
- [`simPushTextOntoStack`](sim-2/simPushTextOntoStack_cpp.md)
- [`simPushUInt8TableOntoStack`](sim-2/simPushUInt8TableOntoStack_cpp.md)
- [`simReleaseStack`](sim-2/simReleaseStack_cpp.md)
- [`simUnfoldStackTable`](sim-2/simUnfoldStackTable_cpp.md)
- [`simUnpackTable`](sim-2/simUnpackTable_cpp.md)

## <a id="functions_c_aux"></a>Auxiliary functions (C-functions)

- [`simAddForce`](sim-2/simAddForce_cpp.md)
- [`simAddForceAndTorque`](sim-2/simAddForceAndTorque_cpp.md)
- [`simAddGraphCurve`](sim-2/simAddGraphCurve_cpp.md)
- [`simAddGraphStream`](sim-2/simAddGraphStream_cpp.md)
- [`simAddItemToCollection`](sim-2/simAddItemToCollection_cpp.md)
- [`simAddLog`](sim-2/simAddLog_cpp.md)
- [`simAdjustView`](sim-2/simAdjustView_cpp.md)
- [`simAlignShapeBB`](sim-2/simAlignShapeBB_cpp.md)
- [`simAnnounceSceneContentChange`](sim-2/simAnnounceSceneContentChange_cpp.md)
- [`simApplyTexture`](sim-2/simApplyTexture_cpp.md)
- [`simBuildMatrix`](sim-2/simBuildMatrix_cpp.md)
- [`simBuildPose`](sim-2/simBuildPose_cpp.md)
- [`simCallScriptFunctionEx`](sim-2/simCallScriptFunctionEx_cpp.md)
- [`simCameraFitToView`](sim-2/simCameraFitToView_cpp.md)
- [`simCheckCollision`](sim-2/simCheckCollision_cpp.md)
- [`simCheckDistance`](sim-2/simCheckDistance_cpp.md)
- [`simCheckOctreePointOccupancy`](sim-2/simCheckOctreePointOccupancy_cpp.md)
- [`simCheckProximitySensor`](sim-2/simCheckProximitySensor_cpp.md)
- [`simCheckVisionSensor`](sim-2/simCheckVisionSensor_cpp.md)
- [`simCheckVisionSensorEx`](sim-2/simCheckVisionSensorEx_cpp.md)
- [`simCloseScene`](sim-2/simCloseScene_cpp.md)
- [`simComputeMassAndInertia`](sim-2/simComputeMassAndInertia_cpp.md)
- [`simConvexDecompose`](sim-2/simConvexDecompose_cpp.md)
- [`simCopyPasteObjects`](sim-2/simCopyPasteObjects_cpp.md)
- [`simCreateCollectionEx`](sim-2/simCreateCollectionEx_cpp.md)
- [`simCreateDummy`](sim-2/simCreateDummy_cpp.md)
- [`simCreateForceSensor`](sim-2/simCreateForceSensor_cpp.md)
- [`simCreateHeightfieldShape`](sim-2/simCreateHeightfieldShape_cpp.md)
- [`simCreateJoint`](sim-2/simCreateJoint_cpp.md)
- [`simCreateOctree`](sim-2/simCreateOctree_cpp.md)
- [`simCreatePointCloud`](sim-2/simCreatePointCloud_cpp.md)
- [`simCreatePrimitiveShape`](sim-2/simCreatePrimitiveShape_cpp.md)
- [`simCreateProximitySensor`](sim-2/simCreateProximitySensor_cpp.md)
- [`simCreateScript`](sim-2/simCreateScript_cpp.md)
- [`simCreateShape`](sim-2/simCreateShape_cpp.md)
- [`simCreateTexture`](sim-2/simCreateTexture_cpp.md)
- [`simCreateVisionSensor`](sim-2/simCreateVisionSensor_cpp.md)
- [`simDestroyCollection`](sim-2/simDestroyCollection_cpp.md)
- [`simDestroyGraphCurve`](sim-2/simDestroyGraphCurve_cpp.md)
- [`simDoesFileExist`](sim-2/simDoesFileExist_cpp.md)
- [`simDuplicateGraphCurveToStatic`](sim-2/simDuplicateGraphCurveToStatic_cpp.md)
- [`simExecuteScriptString`](sim-2/simExecuteScriptString_cpp.md)
- [`simExportMesh`](sim-2/simExportMesh_cpp.md)
- [`simFloatingViewAdd`](sim-2/simFloatingViewAdd_cpp.md)
- [`simFloatingViewRemove`](sim-2/simFloatingViewRemove_cpp.md)
- [`simGenerateShapeFromPath`](sim-2/simGenerateShapeFromPath_cpp.md)
- [`simGetApiFunc`](sim-2/simGetApiFunc_cpp.md)
- [`simGetApiInfo`](sim-2/simGetApiInfo_cpp.md)
- [`simGetClosestPosOnPath`](sim-2/simGetClosestPosOnPath_cpp.md)
- [`simGetCollectionObjects`](sim-2/simGetCollectionObjects_cpp.md)
- [`simGetContactInfo`](sim-2/simGetContactInfo_cpp.md)
- [`simGetDecimatedMesh`](sim-2/simGetDecimatedMesh_cpp.md)
- [`simGetEulerAnglesFromMatrix`](sim-2/simGetEulerAnglesFromMatrix_cpp.md)
- [`simGetExplicitHandling`](sim-2/simGetExplicitHandling_cpp.md)
- [`simGetExtensionString`](sim-2/simGetExtensionString_cpp.md)
- [`simGetJointDependency`](sim-2/simGetJointDependency_cpp.md)
- [`simGetJointForce`](sim-2/simGetJointForce_cpp.md)
- [`simGetJointInterval`](sim-2/simGetJointInterval_cpp.md)
- [`simGetJointMode`](sim-2/simGetJointMode_cpp.md)
- [`simGetJointPosition`](sim-2/simGetJointPosition_cpp.md)
- [`simGetJointTargetForce`](sim-2/simGetJointTargetForce_cpp.md)
- [`simGetJointTargetPosition`](sim-2/simGetJointTargetPosition_cpp.md)
- [`simGetJointTargetVelocity`](sim-2/simGetJointTargetVelocity_cpp.md)
- [`simGetJointType`](sim-2/simGetJointType_cpp.md)
- [`simGetJointVelocity`](sim-2/simGetJointVelocity_cpp.md)
- [`simGetLastInfo`](sim-2/simGetLastInfo_cpp.md)
- [`simGetLinkDummy`](sim-2/simGetLinkDummy_cpp.md)
- [`simGetMainWindow`](sim-2/simGetMainWindow_cpp.md)
- [`simGetNavigationMode`](sim-2/simGetNavigationMode_cpp.md)
- [`simGetObject`](sim-2/simGetObject_cpp.md)
- [`simGetObjectAlias`](sim-2/simGetObjectAlias_cpp.md)
- [`simGetObjectChild`](sim-2/simGetObjectChild_cpp.md)
- [`simGetObjectChildPose`](sim-2/simGetObjectChildPose_cpp.md)
- [`simGetObjectColor`](sim-2/simGetObjectColor_cpp.md)
- [`simGetObjectHierarchyOrder`](sim-2/simGetObjectHierarchyOrder_cpp.md)
- [`simGetObjectMatrix`](sim-2/simGetObjectMatrix_cpp.md)
- [`simGetObjectOrientation`](sim-2/simGetObjectOrientation_cpp.md)
- [`simGetObjectParent`](sim-2/simGetObjectParent_cpp.md)
- [`simGetObjectPose`](sim-2/simGetObjectPose_cpp.md)
- [`simGetObjectPosition`](sim-2/simGetObjectPosition_cpp.md)
- [`simGetObjectQuaternion`](sim-2/simGetObjectQuaternion_cpp.md)
- [`simGetObjectSel`](sim-2/simGetObjectSel_cpp.md)
- [`simGetObjectType`](sim-2/simGetObjectType_cpp.md)
- [`simGetObjectUid`](sim-2/simGetObjectUid_cpp.md)
- [`simGetObjectVelocity`](sim-2/simGetObjectVelocity_cpp.md)
- [`simGetObjectfromUid`](sim-2/simGetObjectfromUid_cpp.md)
- [`simGetObjects`](sim-2/simGetObjects_cpp.md)
- [`simGetObjectsInTree`](sim-2/simGetObjectsInTree_cpp.md)
- [`simGetOctreeVoxels`](sim-2/simGetOctreeVoxels_cpp.md)
- [`simGetPage`](sim-2/simGetPage_cpp.md)
- [`simGetPluginInfo`](sim-2/simGetPluginInfo_cpp.md)
- [`simGetPointCloudOptions`](sim-2/simGetPointCloudOptions_cpp.md)
- [`simGetPointCloudPoints`](sim-2/simGetPointCloudPoints_cpp.md)
- [`simGetQHull`](sim-2/simGetQHull_cpp.md)
- [`simGetReferencedHandles`](sim-2/simGetReferencedHandles_cpp.md)
- [`simGetRotationAxis`](sim-2/simGetRotationAxis_cpp.md)
- [`simGetScaledImage`](sim-2/simGetScaledImage_cpp.md)
- [`simGetScriptHandleEx`](sim-2/simGetScriptHandleEx_cpp.md)
- [`simGetShapeColor`](sim-2/simGetShapeColor_cpp.md)
- [`simGetShapeGeomInfo`](sim-2/simGetShapeGeomInfo_cpp.md)
- [`simGetShapeInertia`](sim-2/simGetShapeInertia_cpp.md)
- [`simGetShapeMass`](sim-2/simGetShapeMass_cpp.md)
- [`simGetShapeMesh`](sim-2/simGetShapeMesh_cpp.md)
- [`simGetShapeTextureId`](sim-2/simGetShapeTextureId_cpp.md)
- [`simGetShapeViz`](sim-2/simGetShapeViz_cpp.md)
- [`simGetSimulationState`](sim-2/simGetSimulationState_cpp.md)
- [`simGetSimulationTime`](sim-2/simGetSimulationTime_cpp.md)
- [`simGetSimulationTimeStep`](sim-2/simGetSimulationTimeStep_cpp.md)
- [`simGetSimulatorMessage`](sim-2/simGetSimulatorMessage_cpp.md)
- [`simGetTextureId`](sim-2/simGetTextureId_cpp.md)
- [`simGetVelocity`](sim-2/simGetVelocity_cpp.md)
- [`simGetVisionSensorDepth`](sim-2/simGetVisionSensorDepth_cpp.md)
- [`simGetVisionSensorImg`](sim-2/simGetVisionSensorImg_cpp.md)
- [`simGetVisionSensorRes`](sim-2/simGetVisionSensorRes_cpp.md)
- [`simGroupShapes`](sim-2/simGroupShapes_cpp.md)
- [`simHandleDynamics`](sim-2/simHandleDynamics_cpp.md)
- [`simHandleGraph`](sim-2/simHandleGraph_cpp.md)
- [`simHandleProximitySensor`](sim-2/simHandleProximitySensor_cpp.md)
- [`simHandleVisionSensor`](sim-2/simHandleVisionSensor_cpp.md)
- [`simImportMesh`](sim-2/simImportMesh_cpp.md)
- [`simImportShape`](sim-2/simImportShape_cpp.md)
- [`simInitScript`](sim-2/simInitScript_cpp.md)
- [`simInsertObjectIntoOctree`](sim-2/simInsertObjectIntoOctree_cpp.md)
- [`simInsertObjectIntoPointCloud`](sim-2/simInsertObjectIntoPointCloud_cpp.md)
- [`simInsertPointsIntoPointCloud`](sim-2/simInsertPointsIntoPointCloud_cpp.md)
- [`simInsertVoxelsIntoOctree`](sim-2/simInsertVoxelsIntoOctree_cpp.md)
- [`simIntersectPointsWithPointCloud`](sim-2/simIntersectPointsWithPointCloud_cpp.md)
- [`simInvertMatrix`](sim-2/simInvertMatrix_cpp.md)
- [`simInvertPose`](sim-2/simInvertPose_cpp.md)
- [`simIsDynamicallyEnabled`](sim-2/simIsDynamicallyEnabled_cpp.md)
- [`simIsHandle`](sim-2/simIsHandle_cpp.md)
- [`simLoadImage`](sim-2/simLoadImage_cpp.md)
- [`simLoadModel`](sim-2/simLoadModel_cpp.md)
- [`simLoadScene`](sim-2/simLoadScene_cpp.md)
- [`simMatrixToPose`](sim-2/simMatrixToPose_cpp.md)
- [`simModuleEntry`](sim-2/simModuleEntry_cpp.md)
- [`simMultiplyMatrices`](sim-2/simMultiplyMatrices_cpp.md)
- [`simMultiplyPoses`](sim-2/simMultiplyPoses_cpp.md)
- [`simOpenTextEditor`](sim-2/simOpenTextEditor_cpp.md)
- [`simPackTable`](sim-2/simPackTable_cpp.md)
- [`simPauseSimulation`](sim-2/simPauseSimulation_cpp.md)
- [`simPoseToMatrix`](sim-2/simPoseToMatrix_cpp.md)
- [`simQuitSimulator`](sim-2/simQuitSimulator_cpp.md)
- [`simReadForceSensor`](sim-2/simReadForceSensor_cpp.md)
- [`simReadProximitySensor`](sim-2/simReadProximitySensor_cpp.md)
- [`simReadTexture`](sim-2/simReadTexture_cpp.md)
- [`simReadVisionSensor`](sim-2/simReadVisionSensor_cpp.md)
- [`simRefreshDialogs`](sim-2/simRefreshDialogs_cpp.md)
- [`simRegisterScriptCallbackFunction`](sim-2/simRegisterScriptCallbackFunction_cpp.md)
- [`simRegisterScriptFuncHook`](sim-2/simRegisterScriptFuncHook_cpp.md)
- [`simRegisterScriptVariable`](sim-2/simRegisterScriptVariable_cpp.md)
- [`simRelocateShapeFrame`](sim-2/simRelocateShapeFrame_cpp.md)
- [`simRemoveModel`](sim-2/simRemoveModel_cpp.md)
- [`simRemoveObjects`](sim-2/simRemoveObjects_cpp.md)
- [`simRemovePointsFromPointCloud`](sim-2/simRemovePointsFromPointCloud_cpp.md)
- [`simRemoveVoxelsFromOctree`](sim-2/simRemoveVoxelsFromOctree_cpp.md)
- [`simResetDynamicObject`](sim-2/simResetDynamicObject_cpp.md)
- [`simResetGraph`](sim-2/simResetGraph_cpp.md)
- [`simResetProximitySensor`](sim-2/simResetProximitySensor_cpp.md)
- [`simResetScript`](sim-2/simResetScript_cpp.md)
- [`simResetVisionSensor`](sim-2/simResetVisionSensor_cpp.md)
- [`simRotateAroundAxis`](sim-2/simRotateAroundAxis_cpp.md)
- [`simRuckigPos`](sim-2/simRuckigPos_cpp.md)
- [`simRuckigRemove`](sim-2/simRuckigRemove_cpp.md)
- [`simRuckigStep`](sim-2/simRuckigStep_cpp.md)
- [`simRuckigVel`](sim-2/simRuckigVel_cpp.md)
- [`simSaveImage`](sim-2/simSaveImage_cpp.md)
- [`simSaveModel`](sim-2/simSaveModel_cpp.md)
- [`simSaveScene`](sim-2/simSaveScene_cpp.md)
- [`simScaleObject`](sim-2/simScaleObject_cpp.md)
- [`simScaleObjects`](sim-2/simScaleObjects_cpp.md)
- [`simSetExplicitHandling`](sim-2/simSetExplicitHandling_cpp.md)
- [`simSetGraphStreamTransformation`](sim-2/simSetGraphStreamTransformation_cpp.md)
- [`simSetGraphStreamValue`](sim-2/simSetGraphStreamValue_cpp.md)
- [`simSetJointDependency`](sim-2/simSetJointDependency_cpp.md)
- [`simSetJointInterval`](sim-2/simSetJointInterval_cpp.md)
- [`simSetJointMode`](sim-2/simSetJointMode_cpp.md)
- [`simSetJointPosition`](sim-2/simSetJointPosition_cpp.md)
- [`simSetJointTargetForce`](sim-2/simSetJointTargetForce_cpp.md)
- [`simSetJointTargetPosition`](sim-2/simSetJointTargetPosition_cpp.md)
- [`simSetJointTargetVelocity`](sim-2/simSetJointTargetVelocity_cpp.md)
- [`simSetLinkDummy`](sim-2/simSetLinkDummy_cpp.md)
- [`simSetNavigationMode`](sim-2/simSetNavigationMode_cpp.md)
- [`simSetObjectAlias`](sim-2/simSetObjectAlias_cpp.md)
- [`simSetObjectChildPose`](sim-2/simSetObjectChildPose_cpp.md)
- [`simSetObjectColor`](sim-2/simSetObjectColor_cpp.md)
- [`simSetObjectHierarchyOrder`](sim-2/simSetObjectHierarchyOrder_cpp.md)
- [`simSetObjectMatrix`](sim-2/simSetObjectMatrix_cpp.md)
- [`simSetObjectOrientation`](sim-2/simSetObjectOrientation_cpp.md)
- [`simSetObjectParent`](sim-2/simSetObjectParent_cpp.md)
- [`simSetObjectPose`](sim-2/simSetObjectPose_cpp.md)
- [`simSetObjectPosition`](sim-2/simSetObjectPosition_cpp.md)
- [`simSetObjectQuaternion`](sim-2/simSetObjectQuaternion_cpp.md)
- [`simSetObjectSel`](sim-2/simSetObjectSel_cpp.md)
- [`simSetPage`](sim-2/simSetPage_cpp.md)
- [`simSetPluginInfo`](sim-2/simSetPluginInfo_cpp.md)
- [`simSetPointCloudOptions`](sim-2/simSetPointCloudOptions_cpp.md)
- [`simSetReferencedHandles`](sim-2/simSetReferencedHandles_cpp.md)
- [`simSetShapeColor`](sim-2/simSetShapeColor_cpp.md)
- [`simSetShapeInertia`](sim-2/simSetShapeInertia_cpp.md)
- [`simSetShapeMass`](sim-2/simSetShapeMass_cpp.md)
- [`simSetShapeTexture`](sim-2/simSetShapeTexture_cpp.md)
- [`simSetVisionSensorImg`](sim-2/simSetVisionSensorImg_cpp.md)
- [`simStartSimulation`](sim-2/simStartSimulation_cpp.md)
- [`simStopSimulation`](sim-2/simStopSimulation_cpp.md)
- [`simSubtractObjectFromOctree`](sim-2/simSubtractObjectFromOctree_cpp.md)
- [`simSubtractObjectFromPointCloud`](sim-2/simSubtractObjectFromPointCloud_cpp.md)
- [`simTransformImage`](sim-2/simTransformImage_cpp.md)
- [`simTransformVector`](sim-2/simTransformVector_cpp.md)
- [`simUngroupShape`](sim-2/simUngroupShape_cpp.md)
- [`simUnpackTable`](sim-2/simUnpackTable_cpp.md)
- [`simWriteTexture`](sim-2/simWriteTexture_cpp.md)

## <a id="functions_collection"></a><a id="collections"></a>[collection](collections.md) (C-functions)

- [`simAddItemToCollection`](sim-2/simAddItemToCollection_cpp.md)
- [`simCreateCollectionEx`](sim-2/simCreateCollectionEx_cpp.md)
- [`simDestroyCollection`](sim-2/simDestroyCollection_cpp.md)
- [`simGetCollectionObjects`](sim-2/simGetCollectionObjects_cpp.md)

## <a id="functions_textureData"></a><a id="textures"></a>[textureData](textureDialog.md) (C-functions)

- [`simApplyTexture`](sim-2/simApplyTexture_cpp.md)
- [`simCreateTexture`](sim-2/simCreateTexture_cpp.md)
- [`simGetScaledImage`](sim-2/simGetScaledImage_cpp.md)
- [`simGetShapeTextureId`](sim-2/simGetShapeTextureId_cpp.md)
- [`simGetTextureId`](sim-2/simGetTextureId_cpp.md)
- [`simLoadImage`](sim-2/simLoadImage_cpp.md)
- [`simReadTexture`](sim-2/simReadTexture_cpp.md)
- [`simSaveImage`](sim-2/simSaveImage_cpp.md)
- [`simSetShapeTexture`](sim-2/simSetShapeTexture_cpp.md)
- [`simTransformImage`](sim-2/simTransformImage_cpp.md)
- [`simWriteTexture`](sim-2/simWriteTexture_cpp.md)

## <a id="functions_sceneObject"></a><a id="sceneObjectFunctionality"></a>[sceneObject](objects.md) (C-functions)

- [`simCopyPasteObjects`](sim-2/simCopyPasteObjects_cpp.md)
- [`simGetObject`](sim-2/simGetObject_cpp.md)
- [`simGetObjectAlias`](sim-2/simGetObjectAlias_cpp.md)
- [`simGetObjectChild`](sim-2/simGetObjectChild_cpp.md)
- [`simGetObjectColor`](sim-2/simGetObjectColor_cpp.md)
- [`simGetObjectHierarchyOrder`](sim-2/simGetObjectHierarchyOrder_cpp.md)
- [`simGetObjectMatrix`](sim-2/simGetObjectMatrix_cpp.md)
- [`simGetObjectOrientation`](sim-2/simGetObjectOrientation_cpp.md)
- [`simGetObjectParent`](sim-2/simGetObjectParent_cpp.md)
- [`simGetObjectPose`](sim-2/simGetObjectPose_cpp.md)
- [`simGetObjectPosition`](sim-2/simGetObjectPosition_cpp.md)
- [`simGetObjectQuaternion`](sim-2/simGetObjectQuaternion_cpp.md)
- [`simGetObjectSel`](sim-2/simGetObjectSel_cpp.md)
- [`simGetObjectType`](sim-2/simGetObjectType_cpp.md)
- [`simGetObjectUid`](sim-2/simGetObjectUid_cpp.md)
- [`simGetObjectVelocity`](sim-2/simGetObjectVelocity_cpp.md)
- [`simGetObjects`](sim-2/simGetObjects_cpp.md)
- [`simGetObjectsInTree`](sim-2/simGetObjectsInTree_cpp.md)
- [`simGetReferencedHandles`](sim-2/simGetReferencedHandles_cpp.md)
- [`simIsDynamicallyEnabled`](sim-2/simIsDynamicallyEnabled_cpp.md)
- [`simIsHandle`](sim-2/simIsHandle_cpp.md)
- [`simRemoveModel`](sim-2/simRemoveModel_cpp.md)
- [`simRemoveObjects`](sim-2/simRemoveObjects_cpp.md)
- [`simScaleObject`](sim-2/simScaleObject_cpp.md)
- [`simScaleObjects`](sim-2/simScaleObjects_cpp.md)
- [`simSetObjectAlias`](sim-2/simSetObjectAlias_cpp.md)
- [`simSetObjectColor`](sim-2/simSetObjectColor_cpp.md)
- [`simSetObjectHierarchyOrder`](sim-2/simSetObjectHierarchyOrder_cpp.md)
- [`simSetObjectMatrix`](sim-2/simSetObjectMatrix_cpp.md)
- [`simSetObjectOrientation`](sim-2/simSetObjectOrientation_cpp.md)
- [`simSetObjectParent`](sim-2/simSetObjectParent_cpp.md)
- [`simSetObjectPose`](sim-2/simSetObjectPose_cpp.md)
- [`simSetObjectPosition`](sim-2/simSetObjectPosition_cpp.md)
- [`simSetObjectQuaternion`](sim-2/simSetObjectQuaternion_cpp.md)
- [`simSetObjectSel`](sim-2/simSetObjectSel_cpp.md)
- [`simSetReferencedHandles`](sim-2/simSetReferencedHandles_cpp.md)

## <a id="functions_shape"></a><a id="shapeObject"></a>[shape](shapes.md) (C-functions)

- [`simAddForce`](sim-2/simAddForce_cpp.md)
- [`simAddForceAndTorque`](sim-2/simAddForceAndTorque_cpp.md)
- [`simAlignShapeBB`](sim-2/simAlignShapeBB_cpp.md)
- [`simApplyTexture`](sim-2/simApplyTexture_cpp.md)
- [`simComputeMassAndInertia`](sim-2/simComputeMassAndInertia_cpp.md)
- [`simConvexDecompose`](sim-2/simConvexDecompose_cpp.md)
- [`simCreateHeightfieldShape`](sim-2/simCreateHeightfieldShape_cpp.md)
- [`simCreatePrimitiveShape`](sim-2/simCreatePrimitiveShape_cpp.md)
- [`simCreateShape`](sim-2/simCreateShape_cpp.md)
- [`simGenerateShapeFromPath`](sim-2/simGenerateShapeFromPath_cpp.md)
- [`simGetDecimatedMesh`](sim-2/simGetDecimatedMesh_cpp.md)
- [`simGetExtensionString`](sim-2/simGetExtensionString_cpp.md)
- [`simGetQHull`](sim-2/simGetQHull_cpp.md)
- [`simGetShapeColor`](sim-2/simGetShapeColor_cpp.md)
- [`simGetShapeGeomInfo`](sim-2/simGetShapeGeomInfo_cpp.md)
- [`simGetShapeInertia`](sim-2/simGetShapeInertia_cpp.md)
- [`simGetShapeMass`](sim-2/simGetShapeMass_cpp.md)
- [`simGetShapeMesh`](sim-2/simGetShapeMesh_cpp.md)
- [`simGetShapeTextureId`](sim-2/simGetShapeTextureId_cpp.md)
- [`simGetShapeViz`](sim-2/simGetShapeViz_cpp.md)
- [`simGetVelocity`](sim-2/simGetVelocity_cpp.md)
- [`simGroupShapes`](sim-2/simGroupShapes_cpp.md)
- [`simImportShape`](sim-2/simImportShape_cpp.md)
- [`simRelocateShapeFrame`](sim-2/simRelocateShapeFrame_cpp.md)
- [`simSetShapeColor`](sim-2/simSetShapeColor_cpp.md)
- [`simSetShapeInertia`](sim-2/simSetShapeInertia_cpp.md)
- [`simSetShapeMass`](sim-2/simSetShapeMass_cpp.md)
- [`simSetShapeTexture`](sim-2/simSetShapeTexture_cpp.md)
- [`simUngroupShape`](sim-2/simUngroupShape_cpp.md)

## <a id="functions_joint"></a><a id="jointObject"></a>[joint](joints.md) (C-functions)

- [`simCreateJoint`](sim-2/simCreateJoint_cpp.md)
- [`simGetJointDependency`](sim-2/simGetJointDependency_cpp.md)
- [`simGetJointForce`](sim-2/simGetJointForce_cpp.md)
- [`simGetJointInterval`](sim-2/simGetJointInterval_cpp.md)
- [`simGetJointMode`](sim-2/simGetJointMode_cpp.md)
- [`simGetJointPosition`](sim-2/simGetJointPosition_cpp.md)
- [`simGetJointTargetForce`](sim-2/simGetJointTargetForce_cpp.md)
- [`simGetJointTargetPosition`](sim-2/simGetJointTargetPosition_cpp.md)
- [`simGetJointTargetVelocity`](sim-2/simGetJointTargetVelocity_cpp.md)
- [`simGetJointType`](sim-2/simGetJointType_cpp.md)
- [`simGetJointVelocity`](sim-2/simGetJointVelocity_cpp.md)
- [`simGetObjectChildPose`](sim-2/simGetObjectChildPose_cpp.md)
- [`simSetJointDependency`](sim-2/simSetJointDependency_cpp.md)
- [`simSetJointInterval`](sim-2/simSetJointInterval_cpp.md)
- [`simSetJointMode`](sim-2/simSetJointMode_cpp.md)
- [`simSetJointPosition`](sim-2/simSetJointPosition_cpp.md)
- [`simSetJointTargetForce`](sim-2/simSetJointTargetForce_cpp.md)
- [`simSetJointTargetPosition`](sim-2/simSetJointTargetPosition_cpp.md)
- [`simSetJointTargetVelocity`](sim-2/simSetJointTargetVelocity_cpp.md)
- [`simSetObjectChildPose`](sim-2/simSetObjectChildPose_cpp.md)

## <a id="functions_dummy"></a><a id="dummyObject"></a>[dummy](dummies.md) (C-functions)

- [`simCreateDummy`](sim-2/simCreateDummy_cpp.md)
- [`simGetLinkDummy`](sim-2/simGetLinkDummy_cpp.md)
- [`simSetLinkDummy`](sim-2/simSetLinkDummy_cpp.md)

## <a id="functions_camera"></a><a id="cameraObject"></a>[camera](cameras.md) (C-functions)

- [`simAdjustView`](sim-2/simAdjustView_cpp.md)
- [`simCameraFitToView`](sim-2/simCameraFitToView_cpp.md)
- [`simGetExtensionString`](sim-2/simGetExtensionString_cpp.md)

## <a id="functions_light"></a><a id="lightObject"></a>[light](lights.md) (C-functions)

```cpp
simGetExtensionString
```

## <a id="functions_graph"></a><a id="graphs"></a>[graph](graphs.md) (C-functions)

- [`simAddGraphCurve`](sim-2/simAddGraphCurve_cpp.md)
- [`simAddGraphStream`](sim-2/simAddGraphStream_cpp.md)
- [`simDestroyGraphCurve`](sim-2/simDestroyGraphCurve_cpp.md)
- [`simDuplicateGraphCurveToStatic`](sim-2/simDuplicateGraphCurveToStatic_cpp.md)
- [`simHandleGraph`](sim-2/simHandleGraph_cpp.md)
- [`simResetGraph`](sim-2/simResetGraph_cpp.md)
- [`simSetGraphStreamTransformation`](sim-2/simSetGraphStreamTransformation_cpp.md)
- [`simSetGraphStreamValue`](sim-2/simSetGraphStreamValue_cpp.md)

## <a id="functions_proximitySensor"></a>[proximitySensor](proximitySensors.md) (C-functions)

- [`simCheckProximitySensor`](sim-2/simCheckProximitySensor_cpp.md)
- [`simCreateProximitySensor`](sim-2/simCreateProximitySensor_cpp.md)
- [`simHandleProximitySensor`](sim-2/simHandleProximitySensor_cpp.md)
- [`simReadProximitySensor`](sim-2/simReadProximitySensor_cpp.md)
- [`simResetProximitySensor`](sim-2/simResetProximitySensor_cpp.md)

## <a id="functions_visionSensor"></a>[visionSensor](visionSensors.md) (C-functions)

- [`simAdjustView`](sim-2/simAdjustView_cpp.md)
- [`simCheckVisionSensor`](sim-2/simCheckVisionSensor_cpp.md)
- [`simCheckVisionSensorEx`](sim-2/simCheckVisionSensorEx_cpp.md)
- [`simCreateVisionSensor`](sim-2/simCreateVisionSensor_cpp.md)
- [`simGetExtensionString`](sim-2/simGetExtensionString_cpp.md)
- [`simGetVisionSensorDepth`](sim-2/simGetVisionSensorDepth_cpp.md)
- [`simGetVisionSensorImg`](sim-2/simGetVisionSensorImg_cpp.md)
- [`simGetVisionSensorRes`](sim-2/simGetVisionSensorRes_cpp.md)
- [`simHandleVisionSensor`](sim-2/simHandleVisionSensor_cpp.md)
- [`simReadVisionSensor`](sim-2/simReadVisionSensor_cpp.md)
- [`simResetVisionSensor`](sim-2/simResetVisionSensor_cpp.md)
- [`simSetVisionSensorImg`](sim-2/simSetVisionSensorImg_cpp.md)

## <a id="functions_forceSensor"></a>[forceSensor](forceSensors.md) (C-functions)

- [`simCreateForceSensor`](sim-2/simCreateForceSensor_cpp.md)
- [`simReadForceSensor`](sim-2/simReadForceSensor_cpp.md)

## <a id="functions_pointCloud"></a>[pointCloud](pointClouds.md) (C-functions)

- [`simCreatePointCloud`](sim-2/simCreatePointCloud_cpp.md)
- [`simGetPointCloudOptions`](sim-2/simGetPointCloudOptions_cpp.md)
- [`simGetPointCloudPoints`](sim-2/simGetPointCloudPoints_cpp.md)
- [`simInsertObjectIntoPointCloud`](sim-2/simInsertObjectIntoPointCloud_cpp.md)
- [`simInsertPointsIntoPointCloud`](sim-2/simInsertPointsIntoPointCloud_cpp.md)
- [`simIntersectPointsWithPointCloud`](sim-2/simIntersectPointsWithPointCloud_cpp.md)
- [`simRemovePointsFromPointCloud`](sim-2/simRemovePointsFromPointCloud_cpp.md)
- [`simSetPointCloudOptions`](sim-2/simSetPointCloudOptions_cpp.md)
- [`simSubtractObjectFromPointCloud`](sim-2/simSubtractObjectFromPointCloud_cpp.md)

## <a id="functions_ocTree"></a><a id="octree"></a>[ocTree](octrees.md) (C-functions)

- [`simCheckOctreePointOccupancy`](sim-2/simCheckOctreePointOccupancy_cpp.md)
- [`simCreateOctree`](sim-2/simCreateOctree_cpp.md)
- [`simGetOctreeVoxels`](sim-2/simGetOctreeVoxels_cpp.md)
- [`simInsertObjectIntoOctree`](sim-2/simInsertObjectIntoOctree_cpp.md)
- [`simInsertVoxelsIntoOctree`](sim-2/simInsertVoxelsIntoOctree_cpp.md)
- [`simRemoveVoxelsFromOctree`](sim-2/simRemoveVoxelsFromOctree_cpp.md)
- [`simSubtractObjectFromOctree`](sim-2/simSubtractObjectFromOctree_cpp.md)

## <a id="functions_Path"></a><a id="paths"></a>[Path](paths.md) (C-functions)

- [`simGenerateShapeFromPath`](sim-2/simGenerateShapeFromPath_cpp.md)
- [`simGetClosestPosOnPath`](sim-2/simGetClosestPosOnPath_cpp.md)

## <a id="functions_file"></a><a id="fileOperations"></a>File operations (C-functions)

- [`simCloseScene`](sim-2/simCloseScene_cpp.md)
- [`simCreateTexture`](sim-2/simCreateTexture_cpp.md)
- [`simDoesFileExist`](sim-2/simDoesFileExist_cpp.md)
- [`simExportMesh`](sim-2/simExportMesh_cpp.md)
- [`simImportMesh`](sim-2/simImportMesh_cpp.md)
- [`simImportShape`](sim-2/simImportShape_cpp.md)
- [`simLoadModel`](sim-2/simLoadModel_cpp.md)
- [`simLoadScene`](sim-2/simLoadScene_cpp.md)
- [`simSaveModel`](sim-2/simSaveModel_cpp.md)
- [`simSaveScene`](sim-2/simSaveScene_cpp.md)

## <a id="functions_main"></a><a id="mainFunctionalityHandling"></a>General functionality handling (C-functions)

- [`simGetCollectionObjects`](sim-2/simGetCollectionObjects_cpp.md)
- [`simGetObject`](sim-2/simGetObject_cpp.md)
- [`simGetObjects`](sim-2/simGetObjects_cpp.md)
- [`simGetObjectsInTree`](sim-2/simGetObjectsInTree_cpp.md)
- [`simGetReferencedHandles`](sim-2/simGetReferencedHandles_cpp.md)
- [`simIsHandle`](sim-2/simIsHandle_cpp.md)
- [`simSetReferencedHandles`](sim-2/simSetReferencedHandles_cpp.md)

## <a id="functions_dynamics"></a><a id="dynamicsFunctionality"></a>[Dynamics](dynamicsModule.md) (C-functions)

- [`simAddForce`](sim-2/simAddForce_cpp.md)
- [`simAddForceAndTorque`](sim-2/simAddForceAndTorque_cpp.md)
- [`simComputeMassAndInertia`](sim-2/simComputeMassAndInertia_cpp.md)
- [`simConvexDecompose`](sim-2/simConvexDecompose_cpp.md)
- [`simCreateForceSensor`](sim-2/simCreateForceSensor_cpp.md)
- [`simGetContactInfo`](sim-2/simGetContactInfo_cpp.md)
- [`simGetDecimatedMesh`](sim-2/simGetDecimatedMesh_cpp.md)
- [`simGetJointForce`](sim-2/simGetJointForce_cpp.md)
- [`simGetJointTargetForce`](sim-2/simGetJointTargetForce_cpp.md)
- [`simGetLinkDummy`](sim-2/simGetLinkDummy_cpp.md)
- [`simGetQHull`](sim-2/simGetQHull_cpp.md)
- [`simGetShapeInertia`](sim-2/simGetShapeInertia_cpp.md)
- [`simGetShapeMass`](sim-2/simGetShapeMass_cpp.md)
- [`simGetVelocity`](sim-2/simGetVelocity_cpp.md)
- [`simHandleDynamics`](sim-2/simHandleDynamics_cpp.md)
- [`simIsDynamicallyEnabled`](sim-2/simIsDynamicallyEnabled_cpp.md)
- [`simReadForceSensor`](sim-2/simReadForceSensor_cpp.md)
- [`simResetDynamicObject`](sim-2/simResetDynamicObject_cpp.md)
- [`simSetJointTargetForce`](sim-2/simSetJointTargetForce_cpp.md)
- [`simSetJointTargetPosition`](sim-2/simSetJointTargetPosition_cpp.md)
- [`simSetJointTargetVelocity`](sim-2/simSetJointTargetVelocity_cpp.md)
- [`simSetLinkDummy`](sim-2/simSetLinkDummy_cpp.md)
- [`simSetShapeInertia`](sim-2/simSetShapeInertia_cpp.md)
- [`simSetShapeMass`](sim-2/simSetShapeMass_cpp.md)

## <a id="functions_collision"></a><a id="collisionDetection"></a>[Collision detection](collisionDetection.md) (C-functions)

```cpp
simCheckCollision
```

## <a id="functions_distance"></a><a id="distanceCalculation"></a>[Distance calculation](distanceCalculation.md) (C-functions)

```cpp
simCheckDistance
```

## <a id="functions_rendering"></a>[Rendering](dataVisualizationAndOutput.md) (C-functions)

- [`simGetObjectColor`](sim-2/simGetObjectColor_cpp.md)
- [`simGetShapeColor`](sim-2/simGetShapeColor_cpp.md)
- [`simSetObjectColor`](sim-2/simSetObjectColor_cpp.md)
- [`simSetShapeColor`](sim-2/simSetShapeColor_cpp.md)

## <a id="functions_model"></a><a id="modelFunctionality"></a>[Models](models.md) (C-functions)

- [`simLoadModel`](sim-2/simLoadModel_cpp.md)
- [`simSaveModel`](sim-2/simSaveModel_cpp.md)

## <a id="functions_selection"></a><a id="sceneObjectSelectionFunctionality"></a>Selection (C-functions)

- [`simGetObjectSel`](sim-2/simGetObjectSel_cpp.md)
- [`simSetObjectSel`](sim-2/simSetObjectSel_cpp.md)

## <a id="functions_creation"></a><a id="sceneObjectCreationFunctionality"></a>Object creation (C-functions)

- [`simCreateDummy`](sim-2/simCreateDummy_cpp.md)
- [`simCreateForceSensor`](sim-2/simCreateForceSensor_cpp.md)
- [`simCreateHeightfieldShape`](sim-2/simCreateHeightfieldShape_cpp.md)
- [`simCreateJoint`](sim-2/simCreateJoint_cpp.md)
- [`simCreateOctree`](sim-2/simCreateOctree_cpp.md)
- [`simCreatePointCloud`](sim-2/simCreatePointCloud_cpp.md)
- [`simCreatePrimitiveShape`](sim-2/simCreatePrimitiveShape_cpp.md)
- [`simCreateProximitySensor`](sim-2/simCreateProximitySensor_cpp.md)
- [`simCreateScript`](sim-2/simCreateScript_cpp.md)
- [`simCreateShape`](sim-2/simCreateShape_cpp.md)
- [`simCreateTexture`](sim-2/simCreateTexture_cpp.md)
- [`simCreateVisionSensor`](sim-2/simCreateVisionSensor_cpp.md)
- [`simGenerateShapeFromPath`](sim-2/simGenerateShapeFromPath_cpp.md)

## <a id="functions_scriptRelated"></a>[Script related](scripts.md) (C-functions)

- [`simCallScriptFunctionEx`](sim-2/simCallScriptFunctionEx_cpp.md)
- [`simCreateScript`](sim-2/simCreateScript_cpp.md)
- [`simExecuteScriptString`](sim-2/simExecuteScriptString_cpp.md)
- [`simGetApiFunc`](sim-2/simGetApiFunc_cpp.md)
- [`simGetApiInfo`](sim-2/simGetApiInfo_cpp.md)
- [`simGetScriptHandleEx`](sim-2/simGetScriptHandleEx_cpp.md)
- [`simInitScript`](sim-2/simInitScript_cpp.md)
- [`simIsHandle`](sim-2/simIsHandle_cpp.md)
- [`simRegisterScriptCallbackFunction`](sim-2/simRegisterScriptCallbackFunction_cpp.md)
- [`simRegisterScriptFuncHook`](sim-2/simRegisterScriptFuncHook_cpp.md)
- [`simRegisterScriptVariable`](sim-2/simRegisterScriptVariable_cpp.md)
- [`simResetScript`](sim-2/simResetScript_cpp.md)

## <a id="functions_simulation"></a><a id="SimulationFunctionality"></a>[Simulation](simulation.md) (C-functions)

- [`simGetSimulationState`](sim-2/simGetSimulationState_cpp.md)
- [`simGetSimulationTime`](sim-2/simGetSimulationTime_cpp.md)
- [`simGetSimulationTimeStep`](sim-2/simGetSimulationTimeStep_cpp.md)
- [`simPauseSimulation`](sim-2/simPauseSimulation_cpp.md)
- [`simStartSimulation`](sim-2/simStartSimulation_cpp.md)
- [`simStopSimulation`](sim-2/simStopSimulation_cpp.md)

## <a id="functions_transformation"></a><a id="pose"></a><a id="transformations"></a><a id="coordinatesAndTransformations"></a>[Coordinates and transformations](positionOrientationTransformation.md) (C-functions)

- [`simAlignShapeBB`](sim-2/simAlignShapeBB_cpp.md)
- [`simBuildMatrix`](sim-2/simBuildMatrix_cpp.md)
- [`simBuildPose`](sim-2/simBuildPose_cpp.md)
- [`simGetEulerAnglesFromMatrix`](sim-2/simGetEulerAnglesFromMatrix_cpp.md)
- [`simGetObjectChildPose`](sim-2/simGetObjectChildPose_cpp.md)
- [`simGetObjectMatrix`](sim-2/simGetObjectMatrix_cpp.md)
- [`simGetObjectOrientation`](sim-2/simGetObjectOrientation_cpp.md)
- [`simGetObjectPose`](sim-2/simGetObjectPose_cpp.md)
- [`simGetObjectPosition`](sim-2/simGetObjectPosition_cpp.md)
- [`simGetObjectQuaternion`](sim-2/simGetObjectQuaternion_cpp.md)
- [`simGetObjectVelocity`](sim-2/simGetObjectVelocity_cpp.md)
- [`simGetRotationAxis`](sim-2/simGetRotationAxis_cpp.md)
- [`simInvertMatrix`](sim-2/simInvertMatrix_cpp.md)
- [`simInvertPose`](sim-2/simInvertPose_cpp.md)
- [`simMatrixToPose`](sim-2/simMatrixToPose_cpp.md)
- [`simMultiplyMatrices`](sim-2/simMultiplyMatrices_cpp.md)
- [`simMultiplyPoses`](sim-2/simMultiplyPoses_cpp.md)
- [`simPoseToMatrix`](sim-2/simPoseToMatrix_cpp.md)
- [`simRelocateShapeFrame`](sim-2/simRelocateShapeFrame_cpp.md)
- [`simRotateAroundAxis`](sim-2/simRotateAroundAxis_cpp.md)
- [`simSetObjectChildPose`](sim-2/simSetObjectChildPose_cpp.md)
- [`simSetObjectMatrix`](sim-2/simSetObjectMatrix_cpp.md)
- [`simSetObjectOrientation`](sim-2/simSetObjectOrientation_cpp.md)
- [`simSetObjectPose`](sim-2/simSetObjectPose_cpp.md)
- [`simSetObjectPosition`](sim-2/simSetObjectPosition_cpp.md)
- [`simSetObjectQuaternion`](sim-2/simSetObjectQuaternion_cpp.md)
- [`simTransformVector`](sim-2/simTransformVector_cpp.md)

## <a id="functions_messaging"></a>[Messaging](meansOfCommunication.md) (C-functions)

- [`simAddLog`](sim-2/simAddLog_cpp.md)
- [`simCallScriptFunctionEx`](sim-2/simCallScriptFunctionEx_cpp.md)
- [`simExecuteScriptString`](sim-2/simExecuteScriptString_cpp.md)
- [`simGetLastError`](sim-2/simGetLastError_cpp.md)
- [`simGetObjectUid`](sim-2/simGetObjectUid_cpp.md)
- [`simGetSimulatorMessage`](sim-2/simGetSimulatorMessage_cpp.md)
- [`simSetLastError`](sim-2/simSetLastError_cpp.md)

## <a id="functions_importExport"></a><a id="importExportFunctions"></a>[Import/export](importExport.md) (C-functions)

- [`simCreateTexture`](sim-2/simCreateTexture_cpp.md)
- [`simExportMesh`](sim-2/simExportMesh_cpp.md)
- [`simImportMesh`](sim-2/simImportMesh_cpp.md)
- [`simImportShape`](sim-2/simImportShape_cpp.md)
- [`simLoadImage`](sim-2/simLoadImage_cpp.md)
- [`simSaveImage`](sim-2/simSaveImage_cpp.md)

## <a id="functions_Motion"></a><a id="rml"></a><a id="ruckig"></a>Motion functionality (C-functions)

- [`simRuckigPos`](sim-2/simRuckigPos_cpp.md)
- [`simRuckigRemove`](sim-2/simRuckigRemove_cpp.md)
- [`simRuckigStep`](sim-2/simRuckigStep_cpp.md)
- [`simRuckigVel`](sim-2/simRuckigVel_cpp.md)

## <a id="functions_packing"></a>Packing/unpacking (C-functions)

- [`simGetBufferProperty`](sim-2/simGetBufferProperty_cpp.md)
- [`simPackTable`](sim-2/simPackTable_cpp.md)
- [`simSetBufferProperty`](sim-2/simSetBufferProperty_cpp.md)
- [`simUnpackTable`](sim-2/simUnpackTable_cpp.md)

## <a id="functions_other"></a>Other (C-functions)

- [`simAnnounceSceneContentChange`](sim-2/simAnnounceSceneContentChange_cpp.md)
- [`simCreateBuffer`](sim-2/simCreateBuffer_cpp.md)
- [`simFloatingViewAdd`](sim-2/simFloatingViewAdd_cpp.md)
- [`simFloatingViewRemove`](sim-2/simFloatingViewRemove_cpp.md)
- [`simGetExplicitHandling`](sim-2/simGetExplicitHandling_cpp.md)
- [`simGetLastError`](sim-2/simGetLastError_cpp.md)
- [`simGetLastInfo`](sim-2/simGetLastInfo_cpp.md)
- [`simGetMainWindow`](sim-2/simGetMainWindow_cpp.md)
- [`simGetNavigationMode`](sim-2/simGetNavigationMode_cpp.md)
- [`simGetObjectfromUid`](sim-2/simGetObjectfromUid_cpp.md)
- [`simGetPage`](sim-2/simGetPage_cpp.md)
- [`simGetPluginInfo`](sim-2/simGetPluginInfo_cpp.md)
- [`simModuleEntry`](sim-2/simModuleEntry_cpp.md)
- [`simOpenTextEditor`](sim-2/simOpenTextEditor_cpp.md)
- [`simQuitSimulator`](sim-2/simQuitSimulator_cpp.md)
- [`simRefreshDialogs`](sim-2/simRefreshDialogs_cpp.md)
- [`simReleaseBuffer`](sim-2/simReleaseBuffer_cpp.md)
- [`simSetExplicitHandling`](sim-2/simSetExplicitHandling_cpp.md)
- [`simSetLastError`](sim-2/simSetLastError_cpp.md)
- [`simSetNavigationMode`](sim-2/simSetNavigationMode_cpp.md)
- [`simSetPage`](sim-2/simSetPage_cpp.md)
- [`simSetPluginInfo`](sim-2/simSetPluginInfo_cpp.md)
