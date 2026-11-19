# Coppelia Kinematics Routines, API reference

All units, unless otherwise indicated, are specified in meters and radians.

- [ikAddElement](#ikAddElement)
- [ikComputeGroupJacobian](#ikComputeGroupJacobian)
- [ikComputeJacobian](#ikComputeJacobian)
- [ikCreateDummy](#ikCreateDummy)
- [ikCreateEnvironment](#ikCreateEnvironment)
- [ikCreateGroup](#ikCreateGroup)
- [ikCreateJoint](#ikCreateJoint)
- [ikDoesGroupExist](#ikDoesGroupExist)
- [ikDoesObjectExist](#ikDoesObjectExist)
- [ikDuplicateEnvironment](#ikDuplicateEnvironment)
- [ikEraseEnvironment](#ikEraseEnvironment)
- [ikEraseObject](#ikEraseObject)
- [ikFindConfig](#ikFindConfig)
- [ikGetElementBase](#ikGetElementBase)
- [ikGetElementConstraints](#ikGetElementConstraints)
- [ikGetElementFlags](#ikGetElementFlags)
- [ikGetElementPrecision](#ikGetElementPrecision)
- [ikGetElementWeights](#ikGetElementWeights)
- [ikGetGroupCalculation](#ikGetGroupCalculation)
- [ikGetGroupFlags](#ikGetGroupFlags)
- [ikGetGroupHandle](#ikGetGroupHandle)
- [ikGetGroupJointLimitHits](#ikGetGroupJointLimitHits)
- [ikGetGroupJoints](#ikGetGroupJoints)
- [ikGetJointDependency](#ikGetJointDependency)
- [ikGetJointInterval](#ikGetJointInterval)
- [ikGetJointLimitMargin](#ikGetJointLimitMargin)
- [ikGetJointMatrix](#ikGetJointMatrix)
- [ikGetJointMaxStepSize](#ikGetJointMaxStepSize)
- [ikGetJointMode](#ikGetJointMode)
- [ikGetJointPosition](#ikGetJointPosition)
- [ikGetJointScrewLead](#ikGetJointScrewLead)
- [ikGetJointTransformation](#ikGetJointTransformation)
- [ikGetJointType](#ikGetJointType)
- [ikGetJointWeight](#ikGetJointWeight)
- [ikGetLastError](#ikGetLastError)
- [ikGetObjectHandle](#ikGetObjectHandle)
- [ikGetObjectMatrix](#ikGetObjectMatrix)
- [ikGetObjectParent](#ikGetObjectParent)
- [ikGetObjects](#ikGetObjects)
- [ikGetObjectTransformation](#ikGetObjectTransformation)
- [ikGetObjectType](#ikGetObjectType)
- [ikGetTargetDummy](#ikGetTargetDummy)
- [ikHandleGroups](#ikHandleGroups)
- [ikLoad](#ikLoad)
- [ikReleaseBuffer](#ikReleaseBuffer)
- [ikSave](#ikSave)
- [ikSetElementBase](#ikSetElementBase)
- [ikSetElementConstraints](#ikSetElementConstraints)
- [ikSetElementFlags](#ikSetElementFlags)
- [ikSetElementPrecision](#ikSetElementPrecision)
- [ikSetElementWeights](#ikSetElementWeights)
- [ikSetGroupCalculation](#ikSetGroupCalculation)
- [ikSetGroupFlags](#ikSetGroupFlags)
- [ikSetJointDependency](#ikSetJointDependency)
- [ikSetJointInterval](#ikSetJointInterval)
- [ikSetJointLimitMargin](#ikSetJointLimitMargin)
- [ikSetJointMaxStepSize](#ikSetJointMaxStepSize)
- [ikSetJointMode](#ikSetJointMode)
- [ikSetJointPosition](#ikSetJointPosition)
- [ikSetJointScrewLead](#ikSetJointScrewLead)
- [ikSetJointWeight](#ikSetJointWeight)
- [ikSetObjectMatrix](#ikSetObjectMatrix)
- [ikSetObjectParent](#ikSetObjectParent)
- [ikSetObjectTransformation](#ikSetObjectTransformation)
- [ikSetSphericalJointMatrix](#ikSetSphericalJointMatrix)
- [ikSetSphericalJointQuaternion](#ikSetSphericalJointQuaternion)
- [ikSetTargetDummy](#ikSettargetDummy)
- [ikSwitchEnvironment](#ikSwitchEnvironment)

## <a id="environment"></a>Environment functions and helpers

- [ikCreateEnvironment](#ikCreateEnvironment)
- [ikEraseEnvironment](#ikEraseEnvironment)
- [ikDuplicateEnvironment](#ikDuplicateEnvironment)
- [ikSave](#ikSave)
- [ikLoad](#ikLoad)
- [ikSwitchEnvironment](#ikSwitchEnvironment)
- [ikGetLastError](#ikGetLastError)
- [ikReleaseBuffer](#ikReleaseBuffer)

## <a id="objects"></a>Objects

- [ikGetObjects](#ikGetObjects)
- [ikGetObjectHandle](#ikGetObjectHandle)
- [ikDoesObjectExist](#ikDoesObjectExist)
- [ikEraseObject](#ikEraseObject)
- [ikGetObjectParent](#ikGetObjectParent)
- [ikSetObjectParent](#ikSetObjectParent)
- [ikGetObjectTransformation](#ikGetObjectTransformation)
- [ikSetObjectTransformation](#ikSetObjectTransformation)
- [ikGetObjectType](#ikGetObjectType)
- [ikGetObjectMatrix](#ikGetObjectMatrix)
- [ikSetObjectMatrix](#ikSetObjectMatrix)

## <a id="dummies"></a>Dummies

- [ikCreateDummy](#ikCreateDummy)
- [ikEraseObject](#ikEraseObject)
- [ikGetTargetDummy](#ikGetTargetDummy)
- [ikSetTargetDummy](#ikSetTargetDummy)

## <a id="joints"></a>Joints

- [ikCreateJoint](#ikCreateJoint)
- [ikEraseObject](#ikEraseObject)
- [ikGetJointPosition](#ikGetJointPosition)
- [ikSetJointPosition](#ikSetJointPosition)
- [ikGetJointMode](#ikGetJointMode)
- [ikSetJointMode](#ikSetJointMode)
- [ikGetJointInterval](#ikGetJointInterval)
- [ikSetJointInterval](#ikSetJointInterval)
- [ikGetJointDependency](#ikGetJointDependency)
- [ikSetJointDependency](#ikSetJointDependency)
- [ikGetJointWeight](#ikGetJointWeight)
- [ikSetJointWeight](#ikSetJointWeight)
- [ikGetJointLimitMargin](#ikGetJointLimitMargin)
- [ikSetJointLimitMargin](#ikSetJointLimitMargin)
- [ikGetJointMaxStepSize](#ikGetJointMaxStepSize)
- [ikSetJointMaxStepSize](#ikSetJointMaxStepSize)
- [ikGetJointScrewLead](#ikGetJointScrewLead)
- [ikSetJointScrewLead](#ikSetJointScrewLead)
- [ikGetJointTransformation](#ikGetJointTransformation)
- [ikSetSphericalJointQuaternion](#ikSetSphericalJointQuaternion)
- [ikGetJointType](#ikGetJointType)
- [ikGetJointMatrix](#ikGetJointMatrix)
- [ikSetSphericalJointMatrix](#ikSetSphericalJointMatrix)
- [ikGetGroupJoints](#ikGetGroupJoints)

## <a id="ikGroups"></a>IK groups

- [ikCreateGroup](#ikCreateGroup)
- [ikGetGroupHandle](#ikGetGroupHandle)
- [ikDoesGroupExist](#ikDoesGroupExist)
- [ikGetGroupFlags](#ikGetGroupFlags)
- [ikSetGroupFlags](#ikSetGroupFlags)
- [ikGetGroupCalculation](#ikGetGroupCalculation)
- [ikGetGroupJointLimitHits](#ikGetGroupJointLimitHits)
- [ikGetGroupJoints](#ikGetGroupJoints)
- [ikSetGroupCalculation](#ikSetGroupCalculation)

## <a id="ikElements"></a>IK elements

- [ikAddElement](#ikAddElement)
- [ikGetElementFlags](#ikGetElementFlags)
- [ikSetElementFlags](#ikSetElementFlags)
- [ikGetElementConstraints](#ikGetElementConstraints)
- [ikSetElementConstraints](#ikSetElementConstraints)
- [ikGetElementBase](#ikGetElementBase)
- [ikSetElementBase](#ikSetElementBase)
- [ikGetElementPrecision](#ikGetElementPrecision)
- [ikSetElementPrecision](#ikSetElementPrecision)
- [ikGetElementWeights](#ikGetElementWeights)
- [ikSetElementWeights](#ikSetElementWeights)

## <a id="ikCalculation"></a>IK calculation

- [ikHandleGroups](#ikHandleGroups)
- [ikFindConfig](#ikFindConfig)
- [ikComputeGroupJacobian](#ikComputeGroupJacobian)
- [ikComputeJacobian](#ikComputeJacobian)

### <a id="ikAddIkElement"></a><a id="ikAddElement"></a>ikAddElement

**Description**: Adds a new IK element to an IK group.

**Synopsis**: `bool ikAddElement(int ikGroupHandle,int tipHandle,int* ikElementHandle)`

**Arguments**:

- **ikGroupHandle**: the handle of the IK group.
- **tipHandle**: the handle of the dummy object that should act as the tip in the IK element.
- **ikElementHandle**: the IK element handle in the IK group, in return.

**Return value**: true in case of success.

**See also**: [ikGetGroupHandle](#ikGetGroupHandle), [ikGetObjectHandle](#ikGetObjectHandle)

### <a id="ikComputeGroupJacobian"></a>ikComputeGroupJacobian

**Description**: Computes the Jacobian and error vector for an IK group.

**Synopsis**: `bool ikComputeGroupJacobian(int ikGroupHandle,std::vector<double>* jacobian,std::vector<double>* errorVect)`

**Arguments**:

- **ikGroupHandle**: the handle of the IK group
- **jacobian**: the jacobian in return (row major order). Each row corresponds to one constraint in the following order: x, y, z, alpha, beta, gamma. Each column corresponds to one joint, from base to tip. Can be nullptr
- **errorVect**: the error vector between the target and the tip. Can be nullptr

**Return value**: true in case of success.

**See also**: [ikComputeJacobian](#ikComputeJacobian), [ikHandleGroups](#ikHandleGroups)

### <a id="ikComputeJacobian"></a>ikComputeJacobian

**Description**: Computes the Jacobian and error vector for a kinematic chain.

**Synopsis**: `bool ikComputeJacobian(int baseHandle,int jointHandle,int constraints,const CPose* tipPose,const CPose* targetPose,const CPose* constrBasePose,std::vector<double>* jacobian,std::vector<double>* errorVect)`

**Arguments**:

- **baseHandle**: the handle of the base of the kinematic chain, or -1 for the world
- **jointHandle**: the handle of the last joint in the kinematic chain, when going from base to tip
- **constraints**: a combination of the following is possible: ik_constraint_x, ik_constraint_y, ik_constraint_z, ik_constraint_alpha_beta, ik_constraint_gamma. For convenience we also have ik_constraint_position=ik_constraint_x|ik_constraint_y|ik_constraint_z, ik_constraint_orientation=ik_constraint_alpha_beta|ik_constraint_gamma, and ik_constraint_pose=ik_constraint_position|ik_constraint_orientation.
- **tipPose**: the pose of the tip object, relative to the world
- **targetPose**: the pose of the target object, relative to the world. Can be nullptr, in which case the targetPose is the same as the tipPose
- **constrBasePose**: the pose that should serve as the reference frame for positional constraints, or nullptr to use the base object instead
- **jacobian**: the jacobian in return (row major order). Each row corresponds to one constraint in the following order: x, y, z, alpha, beta, gamma. Each column corresponds to one joint, from base to tip. Can be nullptr
- **errorVect**: the error vector between the target and the tip. Can be nullptr

**Return value**: true in case of success.

**See also**: [ikComputeGroupJacobian](#ikComputeGroupJacobian), [ikHandleGroups](#ikHandleGroups)

### <a id="ikCreateEnvironment"></a>ikCreateEnvironment

**Description**: Creates a new IK environment, and switches to it.

**Synopsis**: `bool ikCreateEnvironment(int* environmentHandle=nullptr,int flags=0)`

**Arguments**:

- **environmentHandle**: the handle of the newly created environment.
- **flags**: keep at 0

**Return value**: true in case of success.

**See also**: [ikEraseEnvironment](#ikEraseEnvironment), [ikSwitchEnvironment](#ikSwitchEnvironment), [ikDuplicateEnvironment](#ikDuplicateEnvironment), [ikLoad](#ikLoad)

### <a id="ikCreateDummy"></a>ikCreateDummy

**Description**: Creates a dummy object.

**Synopsis**: `bool ikCreateDummy(const char* dummyName/*=nullptr*/,int* dummyHandle)`

**Arguments**:

- **dummyName**: the name of the dummy.
- **dummyHandle**: the handle of the dummy, in return.

**Return value**: true in case of success.

**See also**: [ikDoesObjectExist](#ikDoesObjectExist), [ikCreateJoint](#ikCreateJoint), [ikEraseObject](#ikEraseObject)

### <a id="ikCreateIkGroup"></a><a id="ikCreateGroup"></a>ikCreateGroup

**Description**: Creates an IK group.

**Synopsis**: `bool ikCreateGroup(const char* ikGroupName/*=nullptr*/,int* ikGroupHandle)`

**Arguments**:

- **ikGroupName**: the name of the IK group.
- **ikGroupHandle**: the handle of the IK group, in return.

**Return value**: true in case of success.

**See also**: [ikDoesGroupExist](#ikDoesGroupExist)

### <a id="ikCreateJoint"></a>ikCreateJoint

**Description**: Creates a joint object.

**Synopsis**: `bool ikCreateJoint(const char* jointName/*=nullptr*/,int jointType,int* jointHandle)`

**Arguments**:

- **jointName**: the name of the joint.
- **jointType**: the type of the joint. Supported types are ik_jointtype_revolute, ik_jointtype_prismatic and ik_jointtype_spherical.
- **jointHandle**: the handle of the joint, in return.

**Return value**: true in case of success.

**See also**: [ikDoesObjectExist](#ikDoesObjectExist), [ikCreateDummy](#ikCreateJoint), [ikEraseObject](#ikEraseObject)

### <a id="ikDoesObjectExist"></a>ikDoesObjectExist

**Description**: Checks whether an object exists, based on its name.

**Synopsis**: `bool ikDoesObjectExist(const char* objectName)`

**Arguments**:

- **objectName**: the name of the object.

**Return value**: true if the object exists.

**See also**: [ikGetObjectHandle](#ikGetObjectHandle)

### <a id="ikDoesIkGroupExist"></a><a id="ikDoesGroupExist"></a>ikDoesGroupExist

**Description**: Checks whether an IK group exists, based on its name.

**Synopsis**: `bool ikDoesGroupExist(const char* ikGroupName)`

**Arguments**:

- **ikGroupName**: the name of the IK group.

**Return value**: true if the IK group exists.

**See also**: [ikGetGroupHandle](#ikGetGroupHandle)

### <a id="ikDuplicateEnvironment"></a>ikDuplicateEnvironment

**Description**: Duplicates the current IK environment. Can be used to operate on an environment without modifying the original environment.

**Synopsis**: `bool ikDuplicateEnvironment(int* newEnvironmentHandle)`

**Arguments**:

- **newEnvironmentHandle**: the handle of the newly created environment.

**Return value**: true in case of success.

**See also**: [ikEraseEnvironment](#ikEraseEnvironment), [ikSwitchEnvironment](#ikSwitchEnvironment), [ikDuplicateEnvironment](#ikDuplicateEnvironment), [ikCreateEnvironment](#ikCreateEnvironment)

### <a id="ikEraseEnvironment"></a>ikEraseEnvironment

**Description**: Erases an IK environment, and switches to another environment, if available.

**Synopsis**: `bool ikEraseEnvironment(int* switchedEnvironmentHandle=nullptr)`

**Arguments**:

- **switchedEnvironmentHandle**: the handle of the environment that was switched to, or -1 if there is no environment left.

**Return value**: true in case of success.

**See also**: [ikCreateEnvironment](#ikCreateEnvironment), [ikSwitchEnvironment](#ikSwitchEnvironment)

### <a id="ikEraseObject"></a>ikEraseObject

**Description**: Erases an object.

**Synopsis**: `bool ikEraseObject(int objectHandle)`

**Arguments**:

- **objectHandle**: handle of the object.

**Return value**: true in case of success.

**See also**: [ikGetObjectHandle](#ikGetObjectHandle), [ikCreateDummy](#ikCreateDummy), [ikCreateJoint](#ikCreateJoint)

### <a id="ikFindConfig"></a>ikFindConfig

**Description**: Searches for a manipulator configuration that matches a given end-effector position/orientation in space. Search is randomized.

**Synopsis**: `int ikFindConfig(int ikGroupHandle,size_t jointCnt,const int* jointHandles,double thresholdDist,int maxSearchTimeInMs,double* retConfig,const double* metric=nullptr,bool(*validationCallback)(double*)=nullptr)`

**Arguments**:

- **ikGroupHandle**: the handle of the IK group.
- **jointCnt**: the number of joint handles provided in the jointHandles array.
- **jointHandles**: an array with jointCnt entries that specifies the joint handles for the joints we wish to retrieve the values calculated by the IK.
- **thresholdDist**: a distance indicating when IK should be computed to try to bring the tip onto the target: since the search algorithm proceeds by generating random configurations, many of them produce a tip pose that is too far from the target pose to run IK successfully. Choosing a large value will result in slow calculations, choosing a small value might produce a smaller subset of solutions. Distance between two poses is calculated using a metric (see metric argument below).
- **maxSearchTimeInMs**: the maximum time in milliseconds before this function returns.
- **retConfig**: an array with jointCnt entries that will receive the IK calculated joint values, as specified by the jointHandles array.
- **metric**: an array of 4 values indicating a metric used to compute pose-pose distances: distance=sqrt((dx\*metric[0])^2+(dy\*metric[1])^2+(dz\*metric[2])^2+(angle\*metric[3])^2).
- **validationCallback**: a callback function taking as input argument the proposed joint values (i.e. a configuration), and as return value whether the configuration is valid (e.g. is not colliding).

**Return value**: \-1 in case of an error, 0 if no valid configuration was found, 1 otherwise.

**See also**: [ikComputeJacobian](#ikComputeJacobian), [ikDuplicateEnvironment](#ikDuplicateEnvironment)

### <a id="ikGetConfigForTipPose"></a>ikGetConfigForTipPose

**Description**: Deprecated. Use ikFindConfig instead.

**Synopsis**: `int ikGetConfigForTipPose(int ikGroupHandle,size_t jointCnt,const int* jointHandles,double thresholdDist,int maxIterations,double* retConfig,const double* metric=nullptr,bool(*validationCallback)(double*)=nullptr,const int* jointOptions=nullptr,const double* lowLimits=nullptr,const double* ranges=nullptr)`

**Arguments**:

- **ikGroupHandle**: the handle of the IK group.
- **jointCnt**: the number of joint handles provided in the jointHandles array.
- **jointHandles**: an array with jointCnt entries that specifies the joint handles for the joints we wish to retrieve the values calculated by the IK.
- **thresholdDist**: a distance indicating when IK should be computed to try to bring the tip onto the target: since the search algorithm proceeds by generating random configurations, many of them produce a tip pose that is too far from the target pose to run IK successfully. Choosing a large value will result in slow calculations, choosing a small value might produce a smaller subset of solutions. Distance between two poses is calculated using a metric (see metric argument below).
- **maxIterations**: the maximum number of iterations before this function returns. Alternatively, you can specify an upper time limit, in milliseconds, after which the function returns with maxIterations=-timeLimitInMs.
- **retConfig**: an array with jointCnt entries that will receive the IK calculated joint values, as specified by the jointHandles array.
- **metric**: an array of 4 values indicating a metric used to compute pose-pose distances: distance=sqrt((dx\*metric[0])^2+(dy\*metric[1])^2+(dz\*metric[2])^2+(angle\*metric[3])^2).
- **validationCallback**: a callback function taking as input argument the proposed joint values (i.e. a configuration), and as return value whether the configuration is valid (e.g. is not colliding).
- **jointOptions**: a bit-coded value corresponding to each specified joint handle. Bit 0 (i.e. 1) indicates the corresponding joint is dependent of another joint.
- **lowLimits**: an optional array pointing to different low limit values for each specified joint. This can be useful when you wish to explore a sub-set of the joint's intervals.
- **ranges**: an optional array pointing to different range values for each specified joint. This can be useful when you wish to explore a sub-set of the joint's intervals. If the range value is 0, then the lowLimit and range values are taken from the joint's properties. If the range value is negative, then the search interval will be centered around the current joint linear/angular position, with an extent of (-range).

**Return value**: \-1 in case of an error, 0 if no valid configuration was found, 1 otherwise.

**See also**: [ikComputeJacobian](#ikComputeJacobian), [ikDuplicateEnvironment](#ikDuplicateEnvironment)

### <a id="ikGetIkElementBase"></a><a id="ikGetElementBase"></a>ikGetElementBase

**Description**: Retrieves the base object of an IK element.

**Synopsis**: `bool ikGetElementBase(int ikGroupHandle,int ikElementHandle,int* baseHandle,int* constraintsBaseHandle)`

**Arguments**:

- **ikGroupHandle**: the handle of the IK group.
- **ikElementHandle**: the IK element handle, or X, where X=handleOfTipDummy|ik_handleflag_tipdummy (if several IK elements with the same tip dummy exist, then the first encountered will be selected).
- **baseHandle**: the handle of the base object, in return, or -1 if the world is the base.
- **constraintsBaseHandle**: the handle of the constraints base object, in return, relative to which the constraints are specified. Returns -1 if the constraints are relative to the base object.

**Return value**: true in case of success.

**See also**: [ikSetElementBase](#ikSetElementBase), [ikGetGroupHandle](#ikGetGroupHandle), [ikGetObjectHandle](#ikGetObjectHandle)

### <a id="ikGetIkElementConstraints"></a><a id="ikGetElementConstraints"></a>ikGetElementConstraints

**Description**: Retrieves the constraints of an IK element.

**Synopsis**: `bool ikGetElementConstraints(int ikGroupHandle,int ikElementHandle,int* constraints)`

**Arguments**:

- **ikGroupHandle**: the handle of the IK group.
- **ikElementHandle**: the IK element handle, or X, where X=handleOfTipDummy|ik_handleflag_tipdummy (if several IK elements with the same tip dummy exist, then the first encountered will be selected).
- **constraints**: the constraints, in return. A combination of the following is possible: ik_constraint_x, ik_constraint_y, ik_constraint_z, ik_constraint_alpha_beta, ik_constraint_gamma. For convenience we also have ik_constraint_position=ik_constraint_x|ik_constraint_y|ik_constraint_z, ik_constraint_orientation=ik_constraint_alpha_beta|ik_constraint_gamma, and ik_constraint_pose=ik_constraint_position|ik_constraint_orientation.

**Return value**: true in case of success.

**See also**: [ikSetElementConstraints](#ikSetElementConstraints), [ikGetGroupHandle](#ikGetGroupHandle), [ikGetObjectHandle](#ikGetObjectHandle)

### <a id="ikGetIkElementFlags"></a><a id="ikGetElementFlags"></a>ikGetElementFlags

**Description**: Retrieves various flags of an IK element.

**Synopsis**: `bool ikGetElementFlags(int ikGroupHandle,int ikElementHandle,int* flags)`

**Arguments**:

- **ikGroupHandle**: the handle of the IK group.
- **ikElementHandle**: the IK element handle, or X, where X=handleOfTipDummy|ik_handleflag_tipdummy (if several IK elements with the same tip dummy exist, then the first encountered will be selected).
- **flags**: bit-coded flags, in return: bit0 set (1): the enabled state of the IK element.

**Return value**: true in case of success.

**See also**: [ikSetElementFlags](#ikSetElementFlags), [ikGetGroupHandle](#ikGetGroupHandle), [ikGetObjectHandle](#ikGetObjectHandle)

### <a id="ikGetIkElementPrecision"></a><a id="ikGetElementPrecision"></a>ikGetElementPrecision

**Description**: Retrieves the precision settings of an IK element.

**Synopsis**: `bool ikGetElementPrecision(int ikGroupHandle,int ikElementHandle,double* linearPrecision,double* angularPrecision)`

**Arguments**:

- **ikGroupHandle**: the handle of the IK group.
- **ikElementHandle**: the IK element handle, or X, where X=handleOfTipDummy|ik_handleflag_tipdummy (if several IK elements with the same tip dummy exist, then the first encountered will be selected).
- **linearPrecision**: the required linear precision, in return.
- **angularPrecision**: the required angular precision, in return.

**Return value**: true in case of success.

**See also**: [ikSetElementPrecision](#ikSetElementPrecision), [ikGetGroupHandle](#ikGetGroupHandle), [ikGetObjectHandle](#ikGetObjectHandle)

### <a id="ikGetIkElementWeights"></a><a id="ikGetElementWeights"></a>ikGetElementWeights

**Description**: Retrieves the desired linear and angular resolution weights of an IK element.

**Synopsis**: `bool ikGetElementWeights(int ikGroupHandle,int ikElementHandle,double* linearWeight,double* angularWeight,double* elementWeight=nullptr)`

**Arguments**:

- **ikGroupHandle**: the handle of the IK group.
- **ikElementHandle**: the IK element handle, or X, where X=handleOfTipDummy|ik_handleflag_tipdummy (if several IK elements with the same tip dummy exist, then the first encountered will be selected).
- **linearWeight**: the linear resolution weight, in return.
- **angularWeight**: the angular resolution weight, in return.
- **elementWeight**: the overall weight for that IK element, in return.

**Return value**: true in case of success.

**See also**: [ikSetElementWeights](#ikSetElementWeights), [ikGetGroupHandle](#ikGetGroupHandle), [ikGetObjectHandle](#ikGetObjectHandle)

### <a id="ikGetIkGroupCalculation"></a><a id="ikGetGroupCalculation"></a>ikGetGroupCalculation

**Description**: Retrieves calculation properties for an IK group.

**Synopsis**: `bool ikGetGroupCalculation(int ikGroupHandle,int* method,double* damping,int* maxIterations)`

**Arguments**:

- **ikGroupHandle**: the handle of the IK group.
- **method**: the resolution method, in return. Possible values are ik_method_pseudo_inverse (features a tiny bit of hard-coded damping), ik_method_undamped_pseudo_inverse, ik_method_damped_least_squares and ik_method_jacobian_transpose.
- **damping**: the damping, in case the resolution method is ik_method_damped_least_squares, in return.
- **maxIterations**: the maximum number of iterations, in return.

**Return value**: true in case of success.

**See also**: [ikSetGroupCalculation](#ikSetGroupCalculation), [ikGetGroupHandle](#ikGetGroupHandle)

### <a id="ikGetIkGroupFlags"></a><a id="ikGetGroupFlags"></a>ikGetGroupFlags

**Description**: Retrieves flags of an IK group.

**Synopsis**: `bool ikGetGroupFlags(int ikGroupHandle,int* flags)`

**Arguments**:

**ikGroupHandle**: the handle of the IK group.

**flags**: the flags of the IK group, in return, bit-coded:

ik_group_enabled: the group's enabled state

ik_group_ignoremaxsteps: the joints' max step sizes are ignored. Otherwise, when detected, an interpolation factor (originally at 1.0) is successively divided by 2.0 until the max. step sizes are respected

ik_group_restoreonbadlintol: the IK world state is left untouched if the linear precision is not reached

ik_group_restoreonbadangtol: the IK world state is left untouched if the angular precision is not reached

ik_group_avoidlimits: joint limits are actively avoided

ik_group_stoponlimithit: calculation ends when a joint limit is hit

**Return value**: true in case of success.

**See also**: [ikSetGroupFlags](#ikSetGroupFlags), [ikGetGroupHandle](#ikGetGroupHandle)

### <a id="ikGetIkGroupHandle"></a><a id="ikGetGroupHandle"></a>ikGetGroupHandle

**Description**: Retrieves the handle of an IK group based on its name.

**Synopsis**: `bool ikGetGroupHandle(const char* ikGroupName,int* ikGroupHandle)`

**Arguments**:

- **ikGroupName**: the name of the IK group.
- **ikGroupHandle**: the returned IK group handle.

**Return value**: true in case of success.

**See also**: [ikDoesGroupExist](#ikDoesGroupExist), [ikCreateGroup](#ikCreateGroup)

### <a id="ikGetIkGroupJointLimitHits"></a><a id="ikGetGroupJointLimitHits"></a>ikGetGroupJointLimitHits

**Description**: Checks which joints of an IK group hit a limit the last time the IK group was handled.

**Synopsis**: `bool ikGetGroupJointLimitHits(int ikGroupHandle,std::vector<int>* jointHandles,std::vector<double>* underOrOvershots)`

**Arguments**:

- **ikGroupHandle**: the handle of the IK group.
- **jointHandles**: the joint handles that had joint limits under- or overshot. Can be null
- **underOrOvershots**: the corresponding under- or overshots for each of the jointHandles. Can be null

**Return value**: true in case of success.

**See also**: [ikSetGroupFlags](#ikSetGroupFlags)

### <a id="ikGetGroupJoints"></a>ikGetGroupJoints

**Description**: Returns the joint handles involved in the IK group calculation, i.e. one handle per Jacobian column (except for revolute joints, which have 3 corresponding Jacobian columns).

**Synopsis**: `bool ikGetGroupJoints(int ikGroupHandle,std::vector<int>* jointHandles)`

**Arguments**:

- **ikGroupHandle**: the handle of the IK group.
- **jointHandles**: the joint handles.

**Return value**: true in case of success.

### <a id="ikGetJointDependency"></a>ikGetJointDependency

**Description**: Retrieves information about a possible joint dependency.

**Synopsis**: `bool ikGetJointDependency(int jointHandle,int* dependencyJointHandle,double* offset,double* mult)`

**Arguments**:

- **jointHandle**: the handle of the joint.
- **dependencyJointHandle**: the handle of the dependency joint, in return.
- **offset**: the offset, in return. We have joint linear/angular position = dependency joint linear/angular position \* mult + offset.
- **mult**: the multiplication factor, in return. We have joint linear/angular position = dependency joint linear/angular position \* mult + offset.

**Return value**: true in case of success.

**See also**: [ikSetJointDependency](#ikSetJointDependency), [ikGetObjectHandle](#ikGetObjectHandle)

### <a id="ikGetJointIkWeight"></a><a id="ikGetJointWeight"></a>ikGetJointWeight

**Description**: Retrieves the IK weight of a joint, i.e. the weight it has during IK resolution.

**Synopsis**: `bool ikGetJointWeight(int jointHandle,double* ikWeight)`

**Arguments**:

- **jointHandle**: the handle of the joint.
- **ikWeight**: the IK weight, in return.

**Return value**: true in case of success.

**See also**: [ikSetJointWeight](#ikSetJointWeight), [ikGetObjectHandle](#ikGetObjectHandle)

### <a id="ikGetJointInterval"></a>ikGetJointInterval

**Description**: Retrieves the joint limits.

**Synopsis**: `bool ikGetJointInterval(int jointHandle,bool* cyclic,double* intervalMinAndRange)`

**Arguments**:

- **jointHandle**: the handle of the joint.
- **cyclic**: whether the joint is cyclic (has no limits).
- **intervalMinAndRange**: a pointer to two values: the joint lower limit and the joint range (i.e. joint upper limit = joint lower limit + joint range)

**Return value**: true in case of success.

**See also**: [ikSetJointInterval](#ikSetJointInterval), [ikGetObjectHandle](#ikGetObjectHandle)

### <a id="ikGetJointLimitMargin"></a>ikGetJointLimitMargin

**Description**: Retrieves the limit margin of a joint, i.e. the threshold that will be used to counteract joint limit violation during IK resolution, if the appropriate IK group flag was set.

**Synopsis**: `bool ikGetJointLimitMargin(int jointHandle,double* margin)`

**Arguments**:

- **jointHandle**: the handle of the joint.
- **margin**: the margin, in return.

**Return value**: true in case of success.

**See also**: [ikSetJointLimitMargin](#ikSetJointLimitMargin), [ikGetGroupFlags](#ikGetGroupFlags)

### <a id="ikGetJointMatrix"></a>ikGetJointMatrix

**Description**: Retrieves the intrinsic transformation matrix of a joint.

**Synopsis**: `bool ikGetJointMatrix(int jointHandle,C4X4Matrix* matrix)`

**Arguments**:

- **jointHandle**: the handle of the joint.
- **matrix**: the transformation matrix, in return.

**Return value**: true in case of success.

**See also**: [ikSetSphericalJointMatrix](#ikSetSphericalJointMatrix), [ikGetJointPosition](#ikGetJointPosition), [ikGetJointTransformation](#ikGetJointTransformation), [ikGetObjectHandle](#ikGetObjectHandle)

### <a id="ikGetJointMaxStepSize"></a>ikGetJointMaxStepSize

**Description**: Retrieves the maximum step size of a joint.

**Synopsis**: `bool ikGetJointMaxStepSize(int jointHandle,double* maxStepSize)`

**Arguments**:

- **jointHandle**: the handle of the joint.
- **maxStepSize**: the maximum step size, in return.

**Return value**: true in case of success.

**See also**: [ikSetJointMaxStepSize](#ikSetJointMaxStepSize), [ikGetObjectHandle](#ikGetObjectHandle)

### <a id="ikGetJointMode"></a>ikGetJointMode

**Description**: Retrieves the joint mode.

**Synopsis**: `bool ikGetJointMode(int jointHandle,int* mode)`

**Arguments**:

- **jointHandle**: the handle of the joint.
- **mode**: the joint mode, in return. Possible values are: ik_jointmode_passive, ik_jointmode_ik

**Return value**: true in case of success.

**See also**: [ikSetJointMode](#ikSetJointMode), [ikGetObjectHandle](#ikGetObjectHandle)

### <a id="ikGetJointPosition"></a>ikGetJointPosition

**Description**: Retrieves the position (linear or angular) of a joint.

**Synopsis**: `bool ikGetJointPosition(int jointHandle,double* position)`

**Arguments**:

- **jointHandle**: the handle of the joint.
- **position**: the position, in return.

**Return value**: true in case of success.

**See also**: [ikSetJointPosition](#ikSetJointPosition), [ikGetJointMatrix](#ikGetJointMatrix), [ikGetJointTransformation](#ikGetJointTransformation), [ikGetObjectHandle](#ikGetObjectHandle)

### <a id="ikGetJointScrewLead"></a><a id="ikGetJointScrewPitch"></a>ikGetJointScrewLead

**Description**: Retrieves the screw lead of a revolute joint.

**Synopsis**: `bool ikGetJointScrewLead(int jointHandle,double* lead)`

**Arguments**:

- **jointHandle**: the handle of the joint.
- **lead**: the screw lead of the joint, in return. A lead value of zero represents a revolute joint, while a value different from zero represents a screw.

**Return value**: true in case of success.

**See also**: [ikSetJointScrewLead](#ikSetJointScrewLead), [ikGetObjectHandle](#ikGetObjectHandle)

### <a id="ikGetJointTransformation"></a>ikGetJointTransformation

**Description**: Retrieves the intrinsic transformation of a joint.

**Synopsis**: `bool ikGetJointTransformation(int jointHandle,CPose* transf)`

**Arguments**:

- **jointHandle**: the handle of the joint.
- **transf**: the transformation, in return.

**Return value**: true in case of success.

**See also**: [ikSetSphericalJointQuaternion](#ikSetSphericalJointQuaternion), [ikGetJointPosition](#ikGetJointPosition), [ikGetJointMatrix](#ikGetJointMatrix), [ikGetObjectHandle](#ikGetObjectHandle)

### <a id="ikGetJointType"></a>ikGetJointType

**Description**: Retrieves the joint type.

**Synopsis**: `bool ikGetJointType(int jointHandle,int* jointType)`

**Arguments**:

- **jointHandle**: the handle of the joint.
- **jointType**: the joint type, in return. Possible values are: ik_jointtype_revolute, ik_jointtype_prismatic and ik_jointtype_spherical.

**Return value**: true in case of success.

**See also**: [ikCreateJoint](#ikCreateJoint)

### <a id="ikGetLastError"></a>ikGetLastError

**Description**: Retrieves and clears the last error string.

**Synopsis**: `std::string ikGetLastError()`

**Return value**: The error string.

### <a id="ikGetLinkedDummy"></a>ikGetLinkedDummy

**Description**: Deprecated. Use [ikGetTargetDummy](#ikGetTargetDummy) instead.

**Synopsis**: `bool ikGetLinkedDummy(int dummyHandle,int* linkedDummyHandle)`

**Arguments**:

- **dummyHandle**: the handle of the dummy object.
- **linkedDummyHandle**: the handle of the linked dummy object, in return. Is -1 if no dummy object is linked to this one.

**Return value**: true in case of success.

**See also**: [ikSetLinkedDummy](#ikSetLinkedDummy), [ikGetObjectHandle](#ikGetObjectHandle)

### <a id="ikGetObjectHandle"></a>ikGetObjectHandle

**Description**: Retrieves the handle of an object based on its name.

**Synopsis**: `bool ikGetObjectHandle(const char* objectName,int* objectHandle)`

**Arguments**:

- **objectName**: the name of the object.
- **objectHandle**: the returned object handle.

**Return value**: true in case of success.

**See also**: [ikDoesObjectExist](#ikDoesObjectExist), [ikCreateDummy](#ikCreateDummy), [ikCreateJoint](#ikCreateJoint)

### <a id="ikGetObjectMatrix"></a>ikGetObjectMatrix

**Description**: Retrieves the transformation matrix of an object. If the object is a joint object, the matrix does not include the joint's intrinsic transformation.

**Synopsis**: `bool ikGetObjectMatrix(int objectHandle,int relativeToObjectHandle,C4X4Matrix* matrix)`

**Arguments**:

- **objectHandle**: the handle of the object.
- **relativeToObjectHandle**: the handle of an object relative to which we want the matrix expressed. Otherwise, specify ik_handle_world if you want the absolute matrix, or ik_handle_parent if you want the matrix relative to the parent object.
- **matrix**: a pointer to 12 values representing the transformation matrix (the last row of the 4x4 matrix (0,0,0,1) is omitted).

**Return value**: true in case of success.

**See also**: [ikSetObjectMatrix](#ikSetObjectMatrix), [ikGetObjectTransformation](#ikGetObjectTransformation), [ikGetJointTransformation](#ikGetJointTransformation), [ikGetObjectHandle](#ikGetObjectHandle)

### <a id="ikGetObjectParent"></a>ikGetObjectParent

**Description**: Retrieves an object's parent handle.

**Synopsis**: `bool ikGetObjectParent(int objectHandle,int* parentObjectHandle)`

**Arguments**:

- **objectHandle**: the handle of the object.
- **parentObjectHandle**: the returned handle of the parent, or -1 if the object has no parent.

**Return value**: true in case of success.

**See also**: [ikSetObjectParent](#ikSetObjectParent), [ikGetObjectHandle](#ikGetObjectHandle)

### <a id="ikGetObjects"></a>ikGetObjects

**Description**: Allows you to loop through all objects in the environment.

**Synopsis**: `bool ikGetObjects(size_t index,int* objectHandle=nullptr,std::string* objectName=nullptr,bool* isJoint=nullptr,int* jointType=nullptr)`

**Arguments**:

- **index**: the zero-based index. Start at 0, and increment until the return value is false, to loop through all objects in the environment.
- **objectHandle**: the handle of the object, in return.
- **objectName**: the name of the object, in return.
- **isJoint**: whether the object is a joint, in return.
- **jointType**: the type of joint, in return, if the object at the specified index is a joint. Possible values are ik_jointtype_revolute, ik_jointtype_prismatic or ik_jointtype_spherical.

**Return value**: false in case of an error, or if no object exists at the specified index.

**See also**: [ikGetObjectHandle](#ikGetObjectHandle), [ikDoesObjectExist](#ikDoesObjectExist)

### <a id="ikGetObjectTransformation"></a>ikGetObjectTransformation

**Description**: Retrieves the transformation (position and quaternion) of an object. If the object is a joint object, the transformation does not include the joint's intrinsic transformation.

**Synopsis**: `bool ikGetObjectTransformation(int objectHandle,int relativeToObjectHandle,CPose* transf)`

**Arguments**:

- **objectHandle**: the handle of the object.
- **relativeToObjectHandle**: the handle of an object relative to which we want the transformation expressed. Otherwise, specify ik_handle_world if you want the absolute transformation, or ik_handle_parent if you want the transformation relative to the parent object.
- **transf**: a pointer to the transformation that will be returned.

**Return value**: true in case of success.

**See also**: [ikSetObjectTransformation](#ikSetObjectTransformation), [ikGetObjectMatrix](#ikGetObjectMatrix), [ikGetJointTransformation](#ikGetJointTransformation), [ikGetObjectHandle](#ikGetObjectHandle)

### <a id="ikGetObjectType"></a>ikGetObjectType

**Description**: Retrieves the type of an object.

**Synopsis**: `bool ikGetObjectType(int objectHandle,int* objectType)`

**Arguments**:

- **objectHandle**: the handle of the object.
- **objectType**: the returned type of the object.

**Return value**: true in case of success.

### <a id="ikGetTargetDummy"></a>ikGetTargetDummy

**Description**: Retrieves the handle of the target dummy associated with a tip dummy.

**Synopsis**: `bool ikGetTargetDummy(int tipDummyHandle,int* targetDummyHandle)`

**Arguments**:

- **tipDummyHandle**: the handle of the tip dummy.
- **targetDummyHandle**: the handle of the target dummy, in return. Is -1 if no target is associated with the tip dummy.

**Return value**: true in case of success.

**See also**: [ikSetTargetDummy](#ikSetTargetDummy), [ikGetObjectHandle](#ikGetObjectHandle)

### <a id="ikHandleIkGroup"></a><a id="ikHandleGroups"></a>ikHandleGroups

**Description**: Handles (i.e. computes/resolves) one or several IK groups.

**Synopsis**: `bool ikHandleGroups(const std::vector<int>* ikGroupHandles,int* result=nullptr,double* precision,int(*cb)(const int*,double*,const int*,const int*,const int*,const int*,double*,double*,double*)=nullptr)`

**Arguments**:

**ikGroupHandles**: the handles of the IK groups. If one handle is specified, then a simple IK calculation is performed. If more than one handle is specified, then a projected IK computation is performed, where each group calculation result is projected into the previous group's null space, i.e. dq=dq0+NP0\*(dq1+NP1\*(dq2+NP2\*(...))), where dqi is the result of the i-th task's IK (i.e. typically J#\*e), and NPi is the i-th task's I-J#\*J.

**result**: the bit-coded execution result, in return. Possible values are ik_calc_notperformed, ik_calc_cannotinvert, ik_calc_notwithintolerance, ik_calc_stepstoobig, ik_calc_limithit. Can be nullptr

**precision**: a pointer to 2 values, receiving the largest linear and angular distance between all tip-target pairs. Can be nullptr

**cb**: an optional callback address that allows you to inspect and manipulate the generated jacobians and error vector:

int jacobianCallback(const int jacobianSize[2],double\* jacobian,const int\* rowConstraints,const int\* rowIkElements,const int\* colHandles,const int\* colStages,double\* errorVector,double\* qVector,double\* jacobianPseudoinverse)

The return value is bit-coded: bit0=qVector is provided, bit1=jacobianPseudoinverse is provided. jacobian and errorVector can be modified, and qVector can be set (set also return bit0 in that case). If jacobianPseudoinverse is provided (set also return bit1 in that case), then if qVector is not provided, qVector will be computed simply like: qVector=jacobianPseudoinverse\*errorVector. If qVector and jacobianPseudoinverse are not provided, then internal calculations are used.

**Return value**: true in case of execution success.

**See also**: [ikComputeJacobian](#ikComputeJacobian), [ikFindConfig](#ikFindConfig)

### <a id="ikLoad"></a>ikLoad

**Description**: Loads kinematic content previously exported with [ikSave](#ikSave). Make sure that the environment is empty before calling this function.

**Synopsis**: `bool ikLoad(const unsigned char* data,size_t dataLength)`

**Arguments**:

- **data**: a pointer to a buffer with the kinematic content.
- **dataLength**: the size of the kinematic content buffer.

**Return value**: true in case of success.

**See also**: [ikSave](#ikSave), [ikCreateEnvironment](#ikCreateEnvironment), [ikEraseEnvironment](#ikEraseEnvironment)

### <a id="ikReleaseBuffer"></a>ikReleaseBuffer

**Description**: Releases a buffer allocated by the specific API functions.

**Synopsis**: `void ikReleaseBuffer(void* buffer)`

**Arguments**:

- **buffer**: the buffer to release.

### <a id="ikSave"></a>ikSave

**Description**: Saves the kinematic content in the current environment.

**Synopsis**: `unsigned char* ikSave(size_t* dataLength)`

**Arguments**:

- **dataLength**: the size of the kinematic content buffer.

**Return value**: a pointer to a buffer with the kinematic content. The user is in charge of releasing the buffer with [ikReleaseBuffer](#ikReleaseBuffer)

**See also**: [ikLoad](#ikLoad)

### <a id="ikSetIkElementBase"></a><a id="ikSetElementBase"></a>ikSetElementBase

**Description**: Sets the base object of an IK element.

**Synopsis**: `bool ikSetElementBase(int ikGroupHandle,int ikElementHandle,int baseHandle,int constraintsBaseHandle=-1)`

**Arguments**:

- **ikGroupHandle**: the handle of the IK group.
- **ikElementHandle**: the IK element handle, or X, where X=handleOfTipDummy|ik_handleflag_tipdummy (if several IK elements with the same tip dummy exist, then the first encountered will be selected).
- **baseHandle**: the handle of the base object, or -1 if the world is the base.
- **constraintsBaseHandle**: the handle of the constraints base object, relative to which the constraints are specified. Set to -1 to have the constraints relative to the base object.

**Return value**: true in case of success.

**See also**: [ikGetElementBase](#ikGetElementBase), [ikGetGroupHandle](#ikGetGroupHandle), [ikGetObjectHandle](#ikGetObjectHandle)

### <a id="ikSetIkElementConstraints"></a><a id="ikSetElementConstraints"></a>ikSetElementConstraints

**Description**: Sets the constraints of an IK element.

**Synopsis**: `bool ikSetElementConstraints(int ikGroupHandle,int ikElementHandle,int constraints)`

**Arguments**:

- **ikGroupHandle**: the handle of the IK group.
- **ikElementHandle**: the IK element handle, or X, where X=handleOfTipDummy|ik_handleflag_tipdummy (if several IK elements with the same tip dummy exist, then the first encountered will be selected).
- **constraints**: the constraints. Combine following: ik_constraint_x, ik_constraint_y, ik_constraint_z, ik_constraint_alpha_beta, ik_constraint_gamma (ik_constraint_gamma should only be set if ik_constraint_alpha_beta is also set). For convenience we also have ik_constraint_position=ik_constraint_x|ik_constraint_y|ik_constraint_z, ik_constraint_orientation=ik_constraint_alpha_beta|ik_constraint_gamma, and ik_constraint_pose=ik_constraint_position|ik_constraint_orientation.

**Return value**: true in case of success.

**See also**: [ikGetElementConstraints](#ikGetElementConstraints), [ikGetGroupHandle](#ikGetGroupHandle), [ikGetObjectHandle](#ikGetObjectHandle)

### <a id="ikSetIkElementFlags"></a><a id="ikSetElementFlags"></a>ikSetElementFlags

**Description**: Sets various flags for an IK element.

**Synopsis**: `bool ikSetElementFlags(int ikGroupHandle,int ikElementHandle,int flags)`

**Arguments**:

- **ikGroupHandle**: the handle of the IK group.
- **ikElementHandle**: the IK element handle, or X, where X=handleOfTipDummy|ik_handleflag_tipdummy (if several IK elements with the same tip dummy exist, then the first encountered will be selected).
- **flags**: bit-coded flags: bit0 set (1): the enabled state of the IK element.

**Return value**: true in case of success.

**See also**: [ikGetElementFlags](#ikGetElementFlags), [ikGetGroupHandle](#ikGetGroupHandle), [ikGetObjectHandle](#ikGetObjectHandle)

### <a id="ikSetIkElementPrecision"></a><a id="ikSetElementPrecision"></a>ikSetElementPrecision

**Description**: Sets the desired precision of an IK element.

**Synopsis**: `bool ikSetElementPrecision(int ikGroupHandle,int ikElementHandle,double linearPrecision,double angularPrecision)`

**Arguments**:

- **ikGroupHandle**: the handle of the IK group.
- **ikElementHandle**: the IK element handle, or X, where X=handleOfTipDummy|ik_handleflag_tipdummy (if several IK elements with the same tip dummy exist, then the first encountered will be selected).
- **linearPrecision**: the required linear precision.
- **angularPrecision**: the required angular precision.

**Return value**: true in case of success.

**See also**: [ikGetElementPrecision](#ikGetElementPrecision), [ikGetGroupHandle](#ikGetGroupHandle), [ikGetObjectHandle](#ikGetObjectHandle)

### <a id="ikSetIkElementWeights"></a><a id="ikSetElementWeights"></a>ikSetElementWeights

**Description**: Sets the desired linear and angular resolution weights of an IK element.

**Synopsis**: `bool ikSetElementWeights(int ikGroupHandle,int ikElementHandle,double linearWeight,double angularWeight,double elementWeight)`

**Arguments**:

- **ikGroupHandle**: the handle of the IK group.
- **ikElementHandle**: the IK element handle, or X, where X=handleOfTipDummy|ik_handleflag_tipdummy (if several IK elements with the same tip dummy exist, then the first encountered will be selected).
- **linearWeight**: the desired linear resolution weight.
- **angularWeight**: the desired angular resolution weight.
- **elementWeight**: the desired overall weight for that IK element.

**Return value**: true in case of success.

**See also**: [ikGetElementWeights](#ikGetElementWeights), [ikGetGroupHandle](#ikGetGroupHandle), [ikGetObjectHandle](#ikGetObjectHandle)

### <a id="ikSetIkGroupCalculation"></a><a id="ikSetGroupCalculation"></a>ikSetGroupCalculation

**Description**: Sets calculation properties for an IK group.

**Synopsis**: `bool ikSetGroupCalculation(int ikGroupHandle,int method,double damping,int maxIterations)`

**Arguments**:

- **ikGroupHandle**: the handle of the IK group.
- **method**: the resolution method. Possible values are ik_method_pseudo_inverse (features a tiny bit of hard-coded damping), ik_method_undamped_pseudo_inverse, ik_method_damped_least_squares and ik_method_jacobian_transpose.
- **damping**: the damping, in case the resolution method is ik_method_damped_least_squares.
- **maxIterations**: the maximum number of iterations.

**Return value**: true in case of success.

**See also**: [ikGetGroupCalculation](#ikGetGroupCalculation), [ikGetGroupHandle](#ikGetGroupHandle)

### <a id="ikSetIkGroupFlags"></a><a id="ikSetGroupFlags"></a>ikSetGroupFlags

**Description**: Sets flags of an IK group.

**Synopsis**: `bool ikSetGroupFlags(int ikGroupHandle,int flags)`

**Arguments**:

**ikGroupHandle**: the handle of the IK group.

**flags**: the flags of the IK group bit-coded:

ik_group_enabled: the group's enabled state

ik_group_ignoremaxsteps: the joints' max step sizes are ignored. Otherwise, when detected, an interpolation factor (originally at 1.0) is successively divided by 2.0 until the max. step sizes are respected

ik_group_restoreonbadlintol: the IK world state is left untouched if the linear precision is not reached

ik_group_restoreonbadangtol: the IK world state is left untouched if the angular precision is not reached

ik_group_avoidlimits: joint limits are actively avoided

ik_group_stoponlimithit: calculation ends when a joint limit is hit

**Return value**: true in case of success.

**See also**: [ikGetGroupFlags](#ikGetGroupFlags), [ikGetGroupHandle](#ikGetGroupHandle)

### <a id="ikSetJointDependency"></a>ikSetJointDependency

**Description**: Sets information about a possible dependent joint.

**Synopsis**: `bool ikSetJointDependency(int jointHandle,int dependencyJointHandle,double offset=0.0,double mult=1.0,double(*cb)(int ikEnv,int slaveJoint,double masterPos)=nullptr)`

**Arguments**:

**jointHandle**: the handle of the joint.

**dependencyJointHandle**: the handle of the joint that this joint is dependent of. -1 to disable.

**offset**: the offset. We have joint linear/angular position = dependency joint linear/angular position \* mult + offset

**mult**: the multiplication factor. We have joint linear/angular position = dependency joint linear/angular position \* mult + offset

**cb**: an optional callback address that allows you to provide a custom dependency function:

double dependencyCallback(int ikEnv,int slaveJointHandle,double masterJointPosition)

**Return value**: true in case of success.

**See also**: [ikGetJointDependency](#ikGetJointDependency), [ikGetObjectHandle](#ikGetObjectHandle)

### <a id="ikSetJointIkWeight"></a><a id="ikSetJointWeight"></a>ikSetJointWeight

**Description**: Sets the IK weight of a joint, i.e. the weight it has during IK resolution.

**Synopsis**: `bool ikSetJointWeight(int jointHandle,double ikWeight)`

**Arguments**:

- **jointHandle**: the handle of the joint.
- **ikWeight**: the IK weight.

**Return value**: true in case of success.

**See also**: [ikGetJointWeight](#ikGetJointWeight), [ikGetObjectHandle](#ikGetObjectHandle)

### <a id="ikSetJointInterval"></a>ikSetJointInterval

**Description**: Sets the joint limits.

**Synopsis**: `bool ikSetJointInterval(int jointHandle,bool cyclic,const double* intervalMinAndRange=nullptr)`

**Arguments**:

- **jointHandle**: the handle of the joint.
- **cyclic**: whether the joint is cyclic (has no limits). Only revolute joints can be cyclic.
- **intervalMinAndRange**: a pointer to two values: the joint lower limit, and the joint range (i.e. joint upper limit = joint lower limit + joint range)

**Return value**: true in case of success.

**See also**: [ikGetJointInterval](#ikGetJointInterval), [ikGetObjectHandle](#ikGetObjectHandle)

### <a id="ikSetJointLimitMargin"></a>ikSetJointLimitMargin

**Description**: Sets the limit margin of a joint, i.e. the threshold that will be used to counteract joint limit violation during IK resolution, if the appropriate IK group flag was set.

**Synopsis**: `bool ikSetJointLimitMargin(int jointHandle,double margin)`

**Arguments**:

- **jointHandle**: the handle of the joint.
- **margin**: the margin.

**Return value**: true in case of success.

**See also**: [ikGetJointLimitMargin](#ikGetJointLimitMargin), [ikGetGroupFlags](#ikGetGroupFlags)

### <a id="ikSetJointMaxStepSize"></a>ikSetJointMaxStepSize

**Description**: Sets the maximum step size of a joint.

**Synopsis**: `bool ikSetJointMaxStepSize(int jointHandle,double maxStepSize)`

**Arguments**:

- **jointHandle**: the handle of the joint.
- **maxStepSize**: the maximum step size.

**Return value**: true in case of success.

**See also**: [ikGetJointMaxStepSize](#ikGetJointMaxStepSize), [ikGetObjectHandle](#ikGetObjectHandle)

### <a id="ikSetJointMode"></a>ikSetJointMode

**Description**: Sets the joint mode.

**Synopsis**: `bool ikSetJointMode(int jointHandle,int jointMode)`

**Arguments**:

- **jointHandle**: the handle of the joint.
- **jointMode**: the joint mode. Allowed values are: ik_jointmode_passive, ik_jointmode_ik

**Return value**: true in case of success.

**See also**: [ikGetJointMode](#ikGetJointMode), [ikGetObjectHandle](#ikGetObjectHandle)

### <a id="ikSetJointPosition"></a>ikSetJointPosition

**Description**: Sets the position (linear or angular) of a joint.

**Synopsis**: `bool ikSetJointPosition(int jointHandle,double position)`

**Arguments**:

- **jointHandle**: the handle of the joint.
- **position**: the position.

**Return value**: true in case of success.

**See also**: [ikGetJointPosition](#ikGetJointPosition), [ikSetSphericalJointMatrix](#ikSetSphericalJointMatrix), [ikSetSphericalJointQuaternion](#ikSetSphericalJointQuaternion), [ikGetObjectHandle](#ikGetObjectHandle)

### <a id="ikSetJointScrewLead"></a><a id="ikSetJointScrewPitch"></a>ikSetJointScrewLead

**Description**: Sets the screw lead, in case of a revolute joint.

**Synopsis**: `bool ikSetJointScrewLead(int jointHandle,double lead)`

**Arguments**:

- **jointHandle**: the handle of the joint.
- **lead**: the screw lead of the joint. A lead value of zero represents a revolute joint, while a value different from zero represents a screw.

**Return value**: true in case of success.

**See also**: [ikGetJointScrewLead](#ikGetJointScrewLead), [ikGetObjectHandle](#ikGetObjectHandle)

### <a id="ikSetLinkedDummy"></a>ikSetLinkedDummy

**Description**: Deprecated. Use [ikSetTargetDummy instead](#ikSetTargetDummy)

**Synopsis**: `bool ikSetLinkedDummy(int dummyHandle,int linkedDummyHandle)`

**Arguments**:

- **dummyHandle**: the handle of the dummy object.
- **linkedDummyHandle**: the handle of the dummy object to be linked, or -1 to detach this dummy object from a linked dummy object.

**Return value**: true in case of success.

**See also**: [ikGetLinkedDummy](#ikGetLinkedDummy), [ikGetObjectHandle](#ikGetObjectHandle)

### <a id="ikSetObjectMatrix"></a>ikSetObjectMatrix

**Description**: Sets the transformation matrix of an object. If the object is a joint object, the matrix does not include the joint's intrinsic transformation.

**Synopsis**: `bool ikSetObjectMatrix(int objectHandle,int relativeToObjectHandle,const C4X4Matrix* matrix)`

**Arguments**:

- **objectHandle**: the handle of the object.
- **relativeToObjectHandle**: the handle of an object relative to which the matrix is expressed. Otherwise, specify ik_handle_world if you specify the absolute matrix, or ik_handle_parent if you specify the matrix relative to the parent object.
- **matrix**: the transformation matrix.

**Return value**: true in case of success.

**See also**: [ikGetObjectMatrix](#ikGetObjectMatrix), [ikSetObjectTransformation](#ikSetObjectTransformation), [ikSetJointPosition](#ikSetJointPosition), [ikGetObjectHandle](#ikGetObjectHandle)

### <a id="ikSetObjectParent"></a>ikSetObjectParent

**Description**: Sets the parent of an object.

**Synopsis**: `bool ikSetObjectParent(int objectHandle,int parentObjectHandle,bool keepInPlace)`

**Arguments**:

- **objectHandle**: the handle of the object.
- **parentObjectHandle**: the desired parent object. Set -1 for no parent.
- **keepInPlace**: if true, the object will stay in place, otherwise, it will keep its local transformation.

**Return value**: true in case of success.

**See also**: [ikGetObjectParent](#ikGetObjectParent), [ikGetObjectHandle](#ikGetObjectHandle)

### <a id="ikSetObjectTransformation"></a>ikSetObjectTransformation

**Description**: Sets the transformation (position and quaternion) of an object. If the object is a joint object, the transformation does not include the joint's intrinsic transformation.

**Synopsis**: `bool ikSetObjectTransformation(int objectHandle,int relativeToObjectHandle,const CPose* transf)`

**Arguments**:

- **objectHandle**: the handle of the object.
- **relativeToObjectHandle**: the handle of an object relative to which the transformation is expressed. Otherwise, specify ik_handle_world if you specify the absolute transformation, or ik_handle_parent if you specify the transformation relative to the parent object.
- **transf**: the transformation.

**Return value**: true in case of success.

**See also**: [ikGetObjectTransformation](#ikGetObjectTransformation), [ikSetObjectMatrix](#ikSetObjectMatrix), [ikSetJointPosition](#ikSetJointPosition), [ikGetObjectHandle](#ikGetObjectHandle)

### <a id="ikSetSphericalJointMatrix"></a>ikSetSphericalJointMatrix

**Description**: Sets the rotation transformation matrix of a spherical joint.

**Synopsis**: `bool ikSetSphericalJointMatrix(int jointHandle,const C3X3Matrix* rotMatrix)`

**Arguments**:

- **jointHandle**: the handle of the joint.
- **rotMatrix**: the rotation transformation matrix to apply.

**Return value**: true in case of success.

**See also**: [ikGetJointMatrix](#ikGetJointMatrix), [ikSetJointPosition](#ikSetJointPosition), [ikSetSphericalJointQuaternion](#ikSetSphericalJointQuaternion), [ikGetObjectHandle](#ikGetObjectHandle)

### <a id="ikSetSphericalJointQuaternion"></a>ikSetSphericalJointQuaternion

**Description**: Sets the rotation transformation of a spherical joint.

**Synopsis**: `bool ikSetSphericalJointQuaternion(int jointHandle,const CQuaternion* quaternion)`

**Arguments**:

- **jointHandle**: the handle of the joint.
- **quaternion**: the rotation transformation to apply.

**Return value**: true in case of success.

**See also**: [ikGetJointTransformation](#ikGetJointTransformation), [ikSetSphericalJointMatrix](#ikSetSphericalJointMatrix), [ikSetJointPosition](#ikSetJointPosition), [ikGetObjectHandle](#ikGetObjectHandle)

### <a id="ikSetTargetDummy"></a>ikSetTargetDummy

**Description**: Associates a tip dummy with a target dummy, or removes that association. If the tip dummy is already associated with another target dummy, then first remove that association before setting another one.

**Synopsis**: `bool ikSetTargetDummy(int tipDummyHandle,int targetDummyHandle)`

**Arguments**:

- **tipDummyHandle**: the handle of the tip dummy.
- **targetDummyHandle**: the handle of the dummy to become the target of the tip, or -1 to remove an existing target association from the tip dummy.

**Return value**: true in case of success.

**See also**: [ikGetTargetDummy](#ikGetTargetDummy), [ikGetObjectHandle](#ikGetObjectHandle)

### <a id="ikSwitchEnvironment"></a>ikSwitchEnvironment

**Description**: Switches to another environment, and all function calls will be directed to that environment.

**Synopsis**: `bool ikSwitchEnvironment(int handle,bool allowAlsoProtectedEnvironment=false)`

**Arguments**:

- **handle**: the handle of the environment to switch to.
- **allowAlsoProtectedEnvironment**: set to false.

**Return value**: true in case of success.

**See also**: [ikCreateEnvironment](#ikCreateEnvironment), [ikEraseEnvironment](#ikEraseEnvironment)
