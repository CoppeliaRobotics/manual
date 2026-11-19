# Object Parameter IDs

Note: object parameters are deprecated and have been replaced by [properties](properties.md).

## <a id="sceneObjects"></a>Scene objects (preferably, use [scene object related methods and properties](apiFunctions.md#methodsAndProperties_sceneObject))

- `sim.objintparam_visibility_layer`
  int32 parameter: object visibility layer
- `sim.objfloatparam_abs_x_velocity`
  float parameter (can only be read): object absolute x velocity. This is a calculated value.
- `sim.objfloatparam_abs_y_velocity`
  float parameter (can only be read): object absolute y velocity. This is a calculated value.
- `sim.objfloatparam_abs_z_velocity`
  float parameter (can only be read): object absolute z velocity. This is a calculated value.
- `sim.objfloatparam_abs_rot_velocity`
  float parameter (can only be read): object absolute rotational velocity. This is a calculated value.
- `sim.objfloatparam_objbbox_min_x`
  float parameter (can only be read): object bounding box, min. x position
- `sim.objfloatparam_objbbox_min_y`
  float parameter (can only be read): object bounding box, min. y position
- `sim.objfloatparam_objbbox_min_z`
  float parameter (can only be read): object bounding box, min. z position
- `sim.objfloatparam_objbbox_max_x`
  float parameter (can only be read): object bounding box, max. x position
- `sim.objfloatparam_objbbox_max_y`
  float parameter (can only be read): object bounding box, max. y position
- `sim.objfloatparam_objbbox_max_z`
  float parameter (can only be read): object bounding box, max. z position
- `sim.objfloatparam_modelbbox_min_x`
  float parameter (can only be read): model bounding box, min. x position. Object needs to be flagged as model base.
- `sim.objfloatparam_modelbbox_min_y`
  float parameter (can only be read): model bounding box, min. y position. Object needs to be flagged as model base.
- `sim.objfloatparam_modelbbox_min_z`
  float parameter (can only be read): model bounding box, min. z position. Object needs to be flagged as model base.
- `sim.objfloatparam_modelbbox_max_x`
  float parameter (can only be read): model bounding box, max. x position. Object needs to be flagged as model base.
- `sim.objfloatparam_modelbbox_max_y`
  float parameter (can only be read): model bounding box, max. y position. Object needs to be flagged as model base.
- `sim.objfloatparam_modelbbox_max_z`
  float parameter (can only be read): model bounding box, max. z position. Object needs to be flagged as model base.
- `sim.objintparam_collection_self_collision_indicator`
  int32 parameter: collection self-collision indicator.
- `sim.objfloatparam_transparency_offset`
  float parameter: transparent object distance offset. When rendering transparent objects, they are ordered from back to front for rendering. With this value you can influence the ordering a bit.
- `sim.objintparam_manipulation_permissions`
  int32 parameter: object manipulation permissions, bit-coded: bit0 set (1) --> object can be translated during non-simulation, bit1 set (2) --> object can be translated during simulation, bit2 set (4) --> object can be rotated during non-simulation, bit3 set (8) --> object can be rotated during simulation, bit4 set (16) --> object manual shift settings are locked, bit5 set (32) --> object manual rotation settings are locked.
- `sim.objintparam_illumination_handle`
  int32 parameter: -1 if object should be illuminated by all light objects, otherwise a light handle (or collection handle) for the light object(s) that should illuminate the object.
- `sim.objfloatparam_size_factor`
  float parameter: a size factor that will be automatically scaled when the object gets scaled.
- `sim.objstringparam_unique_id`
  string parameter: a string that uniquely and persistently identifies an object. Can only be read.
- `sim.objintparam_visible`
  int32 parameter: 0 if the shape is not visible. Can only be read.

## <a id="visionSensors"></a>Vision sensors (preferably, use [vision sensor related properties](apiFunctions.md#visionSensor))

- `sim.visionfloatparam_near_clipping`
  float parameter: near clipping plane
- `sim.visionfloatparam_far_clipping`
  float parameter: far clipping plane
- `sim.visionintparam_resolution_x`
  int32 parameter: resolution x
- `sim.visionintparam_resolution_y`
  int32 parameter: resolution y
- `sim.visionfloatparam_perspective_angle`
  float parameter: perspective projection angle
- `sim.visionfloatparam_ortho_size`
  float parameter: orthographic projection size
- `sim.visionintparam_disabled_light_components`
  int32 parameter: mask of disabled light components (ambient, diffuse, specular)
- `sim.visionintparam_rendering_attributes`
  int32 parameter: a combination of rendering attributes. Use with care.
- `sim.visionintparam_entity_to_render`
  int32 parameter: entity handle of the entity to render, or -1 to render all renderable objects.
- `sim.visionintparam_windowed_size_x`
  int32 parameter: size X of external windowed rendering. 0 for full-screen.
- `sim.visionintparam_windowed_size_y`
  int32 parameter: size Y of external windowed rendering. 0 for full-screen.
- `sim.visionintparam_windowed_pos_x`
  int32 parameter: pos X of external windowed rendering.
- `sim.visionintparam_windowed_pos_y`
  int32 parameter: pos Y of external windowed rendering.
- `sim.visionintparam_pov_focal_blur`
  int32 parameter: POV-Ray focal blur enabled flag.
- `sim.visionfloatparam_pov_blur_distance`
  float parameter: POV-Ray focal blur distance.
- `sim.visionfloatparam_pov_aperture`
  float parameter: POV-Ray aperture.
- `sim.visionintparam_pov_blur_sampled`
  int32 parameter: POV-Ray blur samples.
- `sim.visionintparam_render_mode`
  int32 parameter: Render mode. Use with care. 0=normal, 1=aux. channels, 2=object handles, 3=POV-Ray.
- `sim.visionintparam_perspective_operation`
  int32 parameter: whether the vision sensor is operated in perspective mode (1) or orthogonal mode (0).
- `sim.visionfarrayparam_viewfrustum`
  float array parameter: 2 3D vectors, for the near and far view frustum corners.
- `sim.visionintparam_rgbignored`
  int parameter: whether RGB info is ignored
- `sim.visionintparam_depthignored`
  int parameter: whether depth info is ignored

## <a id="joints"></a>Joints (preferably, use [joint related properties](apiFunctions.md#joint))

- `sim.jointfloatparam_intrinsic_x`
  float parameter (can only be read): joint transformation, position X
- `sim.jointfloatparam_intrinsic_y`
  float parameter (can only be read): joint transformation, position Y
- `sim.jointfloatparam_intrinsic_z`
  float parameter (can only be read): joint transformation, position Z
- `sim.jointfloatparam_intrinsic_qx`
  float parameter (can only be read): joint transformation, quaternion X
- `sim.jointfloatparam_intrinsic_qy`
  float parameter (can only be read): joint transformation, quaternion Y
- `sim.jointfloatparam_intrinsic_qz`
  float parameter (can only be read): joint transformation, quaternion Z
- `sim.jointfloatparam_intrinsic_qw`
  float parameter (can only be read): joint transformation, quaternion W
- `sim.jointfloatparam_velocity`
  float parameter (can only be read): joint velocity. This is a calculated value.
- `sim.jointfloatparam_spherical_qx`
  float parameter (can only be written): spherical joint quaternion (X part). Value is buffered (quaternion will only be written when float parameter 2016 is written).
- `sim.jointfloatparam_spherical_qy`
  float parameter (can only be written): spherical joint quaternion (Y part). Value is buffered (quaternion will only be written when float parameter 2016 is written).
- `sim.jointfloatparam_spherical_qz`
  float parameter (can only be written): spherical joint quaternion (Z part). Value is buffered (quaternion will only be written when float parameter 2016 is written).
- `sim.jointfloatparam_spherical_qw`
  float parameter (can only be written): spherical joint quaternion (W part). Writes a quaternion also using buffered values (see parameters 2013-2015).
- `sim.jointfloatparam_upper_limit`
  float parameter: joint upper velocity limit. May only have an effect after simulation restart, or after resetting the joint.
- `sim.jointfloatparam_kc_k`
  float parameter: dynamic motor spring control K parameter
- `sim.jointfloatparam_kc_c`
  float parameter: dynamic motor spring control C parameter
- `sim.jointfloatparam_error_x`
  float parameter: joint internal position error X (when joint is dynamically enabled). Can only be read.
- `sim.jointfloatparam_error_y`
  float parameter: joint internal position error Y (when joint is dynamically enabled). Can only be read.
- `sim.jointfloatparam_error_z`
  float parameter: joint internal position error Z (when joint is dynamically enabled). Can only be read.
- `sim.jointfloatparam_error_a`
  float parameter: joint internal orientation error alpha (euler(0)) (when joint is dynamically enabled). Can only be read.
- `sim.jointfloatparam_error_b`
  float parameter: joint internal orientation error beta (euler(1)) (when joint is dynamically enabled). Can only be read.
- `sim.jointfloatparam_error_g`
  float parameter: joint internal orientation error gamma (euler(2)) (when joint is dynamically enabled). Can only be read.
- `sim.jointfloatparam_error_pos`
  float parameter: joint internal position error (when joint is dynamically enabled). Can only be read.
- `sim.jointfloatparam_error_angle`
  float parameter: joint internal angular error (when joint is dynamically enabled). Can only be read.
- `sim.jointintparam_vortex_dep_handle`
  int32 parameter: Vortex joint dependency, dependent joint handle. When written, the joint might have to be reset for the change to take effect.
- `sim.jointfloatparam_vortex_dep_multiplication`
  float parameter: Vortex joint dependency, multiplication factor. When written, the joint might have to be reset for the change to take effect.
- `sim.jointfloatparam_vortex_dep_offset`
  float parameter: Vortex joint dependency, offset. When written, the joint might have to be reset for the change to take effect.
- `sim.jointfloatparam_screwlead`
  float parameter: the joint screw lead, if the joint is a revolute joint
- `sim.jointfloatparam_maxvel`
  float parameter: the maximum allowed velocity, when motion controlled
- `sim.jointfloatparam_maxaccel`
  float parameter: the maximum allowed acceleration, when motion controlled
- `sim.jointfloatparam_maxjerk`
  float parameter: the maximum allowed jerk, when motion controlled
- `sim.jointintparam_dynctrlmode`
  int32 parameter: the dynamic control mode of the joint
- `sim.jointintparam_dynvelctrltype`
  int32 parameter: the dynamic velocity control type of the joint: 0=none, 1=motion profile
- `sim.jointintparam_dynposctrltype`
  int32 parameter: the dynamic position control type of the joint: 0=built-in, 1=motion profile

## <a id="shapes"></a>Shapes (preferably, use [shape related properties](apiFunctions.md#shape))

- `sim.shapefloatparam_init_velocity_x`
  float parameter: x-component of the initial dynamic linear velocity of a dynamically enabled shape (static or non-static). The shape might have to be reset
- `sim.shapefloatparam_init_velocity_y`
  float parameter: y-component of the initial dynamic linear velocity of a dynamically enabled shape (static or non-static). The shape might have to be reset
- `sim.shapefloatparam_init_velocity_z`
  float parameter: z-component of the initial dynamic linear velocity of a dynamically enabled shape (static or non-static). The shape might have to be reset[sim/simResetDynamicObject.htm](sim/simResetDynamicObject.htm)
- `sim.shapeintparam_static`
  int32 parameter: static state (0 or!=0). Use with care when setting this parameter during simulation (the shape might have to be reset)
- `sim.shapeintparam_kinematic`
  int32 parameter: kinematic state (0 or!=0), mainly to indicate mobile static shapes with the MuJoCo engine.
- `sim.shapeintparam_respondable`
  int32 parameter: respondable state (0 or!=0). Use with care when setting this parameter during simulation (the shape might have to be reset)
- `sim.shapeintparam_respondablesuspendcnt`
  int32 parameter: number of simulation steps to temporarily suspend the respondable flag of this shape. Can only be written.
- `sim.shapefloatparam_mass`
  float parameter: mass of the shape. Use with care when setting this parameter during simulation (the shape might have to be reset)
- `sim.shapefloatparam_texture_x`
  float parameter: texture x-coordinate. Has no effect when imported texture coordinates are used
- `sim.shapefloatparam_texture_y`
  float parameter: texture y-coordinate. Has no effect when imported texture coordinates are used
- `sim.shapefloatparam_texture_z`
  float parameter: texture z-coordinate. Has no effect when imported texture coordinates are used
- `sim.shapefloatparam_texture_a`
  float parameter: texture alpha-coordinate (Euler angle). Has no effect when imported texture coordinates are used
- `sim.shapefloatparam_texture_b`
  float parameter: texture beta-coordinate (Euler angle). Has no effect when imported texture coordinates are used
- `sim.shapefloatparam_texture_g`
  float parameter: texture gamma-coordinate (Euler angle). Has no effect when imported texture coordinates are used
- `sim.shapefloatparam_texture_scaling_x`
  float parameter: texture scaling along x. Has no effect when imported texture coordinates are used
- `sim.shapefloatparam_texture_scaling_y`
  float parameter: texture scaling along y. Has no effect when imported texture coordinates are used
- `sim.shapeintparam_culling`
  int32 parameter: culling state (0 or!=0)
- `sim.shapeintparam_wireframe`
  int32 parameter: wireframe state (0 or!=0)
- `sim.shapeintparam_compound`
  int32 parameter: shape compound state (0 if shape is a simple shape,!=0 if shape is a compound shape)
- `sim.shapeintparam_convex`
  int32 parameter: shape convex state (!=0 if shape mesh(es) is/are convex). This is just a flag. Be very careful when setting this value (make sure the mesh(es) is/are closed and perfectly convex). The flag is used to select special and faster collision calculation routines for the physics engines. See also next item
- `sim.shapeintparam_convex_check`
  int32 parameter: triggers a convexity check for the given shape. Can only be set (parameter can be any value). The shape's convex state will be set. Normally not needed because done automatically.
- `sim.shapeintparam_respondable_mask`
  int32 parameter: respondable mask. Use with care when setting this parameter during simulation (the shape might have to be reset)
- `sim.shapefloatparam_init_velocity_a`
  float parameter: alpha-component of the initial dynamic angular velocity of a dynamically enabled shape (static or non-static). The shape might have to be reset
- `sim.shapefloatparam_init_velocity_b`
  float parameter: beta-component of the initial dynamic angular velocity of a dynamically enabled shape (static or non-static). The shape might have to be reset
- `sim.shapefloatparam_init_velocity_g`
  float parameter: gamma-component of the initial dynamic angular velocity of a dynamically enabled shape (static or non-static). The shape might have to be reset
- `sim.shapestringparam_colorname`
  string parameter: the color name(s) contained in the shape. If several color strings are contained, they are separated by a space character. Unnamed colors are represented by '\*'. This parameter can only be written for shapes that are not compound shapes.
- `sim.shapeintparam_edge_visibility`
  int32 parameter: edge visibility state (0 or!=0).
- `sim.shapefloatparam_shading_angle`
  float parameter: shading angle.
- `sim.shapefloatparam_edge_angle`
  float parameter: edge threshold angle.
- `sim.shapeintparam_edge_borders_hidden`
  int32 parameter: hide edge borders (0 or!=0).
- `sim.shapeintparam_component_cnt`
  int32 parameter: the number of items in a compound shape, or 1 otherwise.
- `sim.shapeintparam_sleepmodestart`
  int32 parameter: 1 if the dynamic shape starts in sleep mode.

## <a id="proximitySensors"></a>Proximity sensors (preferably, use [proximity sensor related properties](apiFunctions.md#proximitySensor))

- `sim.proxintparam_ray_invisibility`
  int32 parameter: detection ray invisibility state (0 or!=0)
- `sim.proxintparam_volume_type`
  int32 parameter: the volume type of the proximity sensor. Can only be read.
- `sim.proxintparam_entity_to_detect`
  int32 parameter: entity handle of the entity to detect, or -1 to detect all detectable objects.

## <a id="forceSensors"></a>Force sensors (preferably, use [force sensor related properties](apiFunctions.md#forceSensor))

- `sim.forcefloatparam_error_x`
  float parameter: force sensor internal position error X. Can only be read.
- `sim.forcefloatparam_error_y`
  float parameter: force sensor internal position error Y. Can only be read.
- `sim.forcefloatparam_error_z`
  float parameter: force sensor internal position error Z. Can only be read.
- `sim.forcefloatparam_error_a`
  float parameter: force sensor internal orientation error alpha (euler(0)). Can only be read.
- `sim.forcefloatparam_error_b`
  float parameter: force sensor internal orientation error beta (euler(1)). Can only be read.
- `sim.forcefloatparam_error_g`
  float parameter: force sensor internal orientation error gamma (euler(2)). Can only be read.
- `sim.forcefloatparam_error_pos`
  float parameter: force sensor internal position error. Can only be read.
- `sim.forcefloatparam_error_angle`
  float parameter: force sensor internal angular error. Can only be read.

## <a id="graphs"></a>Graphs (preferably, use [graph related properties](apiFunctions.md#graph))

- `sim.graphintparam_needs_refresh`
  int32 parameter: reads and clears the refresh flag.

## <a id="lights"></a>Lights (preferably, use [light related properties](apiFunctions.md#light))

- `sim.lightintparam_pov_casts_shadows`
  int32 parameter: POV-Ray light casts shadows flag.
- `sim.lightfloatparam_spot_exponent`
  float parameter: light spot exponent.
- `sim.lightfloatparam_spot_cutoff`
  float parameter: light spot cutoff.
- `sim.lightfloatparam_const_attenuation`
  float parameter: light constant attenuation factor.
- `sim.lightfloatparam_lin_attenuation`
  float parameter: light linear attenuation factor.
- `sim.lightfloatparam_quad_attenuation`
  float parameter: light quadratic attenuation factor.

## <a id="cameras"></a>Cameras (preferably, use [camera related properties](apiFunctions.md#camera))

- `sim.cameraintparam_disabled_light_components`
  int32 parameter: mask of disabled light components (ambient, diffuse, specular)
- `sim.camerafloatparam_perspective_angle`
  float parameter: camera perspective angle.
- `sim.camerafloatparam_ortho_size`
  float parameter: camera orthographic size.
- `sim.cameraintparam_rendering_attributes`
  int32 parameter: a combination of rendering attributes. Use with care.
- `sim.cameraintparam_pov_focal_blur`
  int32 parameter: POV-Ray focal blur enabled flag.
- `sim.camerafloatparam_pov_blur_distance`
  float parameter: POV-Ray focal blur distance.
- `sim.camerafloatparam_pov_aperture`
  float parameter: POV-Ray aperture.
- `sim.cameraintparam_pov_blur_samples`
  int32 parameter: POV-Ray blur samples.
- `sim.camerafloatparam_near_clipping`
  float parameter: near clipping plane.
- `sim.camerafloatparam_far_clipping`
  float parameter: far clipping plane.
- `sim.cameraintparam_perspective_operation`
  int32 parameter: whether the camera is operated in perspective mode (1) or orthogonal mode (0).
- `sim.cameraintparam_remotecameramode`
  int32 parameter: the remote camera mode. Remote camera can be free (0), slave (1) or master (2).
- `sim.camerafarrayparam_viewfrustum`
  float array parameter: 2 3D vectors, for the near and far view frustum corners.

## <a id="dummies"></a>Dummies (preferably, use [dummy related properties](apiFunctions.md#dummy))

- `sim.dummyintparam_dummytype`
  int32 parameter: dummy type.
- `sim.dummyfloatparam_size`
  float parameter: the size of the dummy.
- `sim.dummystringparam_assemblytag`
  string parameter: the assembly tag.

## <a id="scripts"></a>Scripts (preferably, use [scriptObject](apiFunctions.md#scriptObject) and [script](apiFunctions.md#script) related properties)

- `sim.scriptintparam_execorder`
  Integer attribute, see the script execution priorities
- `sim.scriptintparam_execcount`
  Integer attribute, cannot be written
- `sim.scriptintparam_type`
  Integer attribute, cannot be written
- `sim.scriptintparam_enabled`
  Integer attribute
- `sim.scriptintparam_autorestartonerror`
  Integer attribute, can only be written and is auto-cleared
- `sim.scriptstringparam_description`
  String attribute, describes the script
- `sim.scriptstringparam_name`
  String attribute
- `sim.scriptstringparam_text`
  String attribute
- `sim.scriptstringparam_namext`
  String attribute
- `sim.scriptstringparam_lang`
  String attribute
