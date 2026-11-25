# Regular API reference (sim-1)

This page lists all constants/enums related to the regular API, version 1 (version 2 can be found [here](apiConstants.md))

## <a id="fileOperations"></a>File operations

- [`sim.closeScene`](sim-1/simCloseScene.md)
- [`sim.saveScene`](sim-1/simSaveScene.md)
- [`sim.loadScene`](sim-1/simLoadScene.md)
- [`sim.saveModel`](sim-1/simSaveModel.md)
- [`sim.loadModel`](sim-1/simLoadModel.md)
- [`sim.importShape`](sim-1/simImportShape.md)
- [`sim.importMesh`](sim-1/simImportMesh.md)
- [`sim.exportMesh`](sim-1/simExportMesh.md)
- [`sim.launchExecutable`](sim-1/simLaunchExecutable.md)
- [`sim.createTexture`](sim-1/simCreateTexture.md)

- [simCloseScene](sim-1/simCloseScene_cpp.md)
- [simSaveScene](sim-1/simSaveScene_cpp.md)
- [simLoadScene](sim-1/simLoadScene_cpp.md)
- [simSaveModel](sim-1/simSaveModel_cpp.md)
- [simLoadModel](sim-1/simLoadModel_cpp.md)
- [simDoesFileExist](sim-1/simDoesFileExist_cpp.md)
- [simImportShape](sim-1/simImportShape_cpp.md)
- [simImportMesh](sim-1/simImportMesh_cpp.md)
- [simExportMesh](sim-1/simExportMesh_cpp.md)
- [simCreateTexture](sim-1/simCreateTexture_cpp.md)

## <a id="HandleRetrieval"></a>General object handle retrieval

- [`sim.getObject`](sim-1/simGetObject.md)
- [`sim.getObjectFromUid`](sim-1/simGetObjectFromUid.md)
- [`sim.isHandle`](sim-1/simIsHandle.md)
- [`sim.getObjects`](sim-1/simGetObjects.md)
- [`sim.getObjectsInTree`](sim-1/simGetObjectsInTree.md)
- [`sim.getCollectionObjects`](sim-1/simGetCollectionObjects.md)
- [`sim.setReferencedHandles`](sim-1/simSetReferencedHandles.md)
- [`sim.getReferencedHandles`](sim-1/simGetReferencedHandles.md)
- [`sim.getReferencedHandlesTags`](sim-1/simGetReferencedHandlesTags.md)

- [simGetObject](sim-1/simGetObject_cpp.md)
- [simGetObjectFromUid](sim-1/simGetObjectFromUid_cpp.md)
- [simIsHandle](sim-1/simIsHandle_cpp.md)
- [simGetObjects](sim-1/simGetObjects_cpp.md)
- [simGetObjectsInTree](sim-1/simGetObjectsInTree_cpp.md)
- [simGetCollectionObjects](sim-1/simGetCollectionObjects_cpp.md)
- [simSetReferencedHandles](sim-1/simSetReferencedHandles_cpp.md)
- [simGetReferencedHandles](sim-1/simGetReferencedHandles_cpp.md)

## <a id="mainFunctionalityHandling"></a>General functionality handling

- [`sim.handleSimulationScripts`](sim-1/simHandleSimulationScripts.md)
- [`sim.handleEmbeddedScripts`](sim-1/simHandleEmbeddedScripts.md)
- [`sim.handleAddOnScripts`](sim-1/simHandleAddOnScripts.md)
- [`sim.handleSandboxScript`](sim-1/simHandleSandboxScript.md)

## <a id="collisionDetection"></a>Collision detection

```
sim.checkCollision
```

```cpp
simCheckCollision
```

## <a id="distanceCalculation"></a>Minimum distance calculation

```
sim.checkDistance
```

```cpp
simCheckDistance
```

## <a id="dynamicsFunctionality"></a>Dynamics

- [`sim.handleDynamics`](sim-1/simHandleDynamics.md)
- [`sim.setJointTargetPosition`](sim-1/simSetJointTargetPosition.md)
- [`sim.setJointTargetVelocity`](sim-1/simSetJointTargetVelocity.md)
- [`sim.readForceSensor`](sim-1/simReadForceSensor.md)
- [`sim.getJointForce`](sim-1/simGetJointForce.md)
- [`sim.getJointTargetForce`](sim-1/simGetJointTargetForce.md)
- [`sim.setJointTargetForce`](sim-1/simSetJointTargetForce.md)
- [`sim.addForce`](sim-1/simAddForce.md)
- [`sim.addForceAndTorque`](sim-1/simAddForceAndTorque.md)
- [`sim.getVelocity`](sim-1/simGetVelocity.md)
- [`sim.getLinkDummy`](sim-1/simGetLinkDummy.md)
- [`sim.setLinkDummy`](sim-1/simSetLinkDummy.md)
- [`sim.resetDynamicObject`](sim-1/simResetDynamicObject.md)
- [`sim.addParticleObject`](sim-1/simAddParticleObject.md)
- [`sim.addParticleObjectItem`](sim-1/simAddParticleObjectItem.md)
- [`sim.removeParticleObject`](sim-1/simRemoveParticleObject.md)
- [`sim.getContactInfo`](sim-1/simGetContactInfo.md)
- [`sim.getShapeMass`](sim-1/simGetShapeMass.md)
- [`sim.setShapeMass`](sim-1/simSetShapeMass.md)
- [`sim.getShapeInertia`](sim-1/simGetShapeInertia.md)
- [`sim.setShapeInertia`](sim-1/simSetShapeInertia.md)
- [`sim.computeMassAndInertia`](sim-1/simComputeMassAndInertia.md)
- [`sim.createForceSensor`](sim-1/simCreateForceSensor.md)
- [`sim.isDynamicallyEnabled`](sim-1/simIsDynamicallyEnabled.md)
- See also:
- [properties](properties.md)

- [simHandleDynamics](sim-1/simHandleDynamics_cpp.md)
- [simSetJointTargetPosition](sim-1/simSetJointTargetPosition_cpp.md)
- [simSetJointTargetVelocity](sim-1/simSetJointTargetVelocity_cpp.md)
- [simReadForceSensor](sim-1/simReadForceSensor_cpp.md)
- [simGetJointForce](sim-1/simGetJointForce_cpp.md)
- [simGetJointTargetForce](sim-1/simGetJointTargetForce_cpp.md)
- [simSetJointTargetForce](sim-1/simSetJointTargetForce_cpp.md)
- [simAddForce](sim-1/simAddForce_cpp.md)
- [simAddForceAndTorque](sim-1/simAddForceAndTorque_cpp.md)
- [simGetVelocity](sim-1/simGetVelocity_cpp.md)
- [simGetLinkDummy](sim-1/simGetLinkDummy_cpp.md)
- [simSetLinkDummy](sim-1/simSetLinkDummy_cpp.md)
- [simResetDynamicObject](sim-1/simResetDynamicObject_cpp.md)
- [simGetContactInfo](sim-1/simGetContactInfo_cpp.md)
- [simGetShapeMass](sim-1/simGetShapeMass_cpp.md)
- [simSetShapeMass](sim-1/simSetShapeMass_cpp.md)
- [simGetShapeInertia](sim-1/simGetShapeInertia_cpp.md)
- [simSetShapeInertia](sim-1/simSetShapeInertia_cpp.md)
- [simComputeMassAndInertia](sim-1/simComputeMassAndInertia_cpp.md)
- [simCreateForceSensor](sim-1/simCreateForceSensor_cpp.md)
- [simConvexDecompose](sim-1/simConvexDecompose_cpp.md)
- [simGetQHull](sim-1/simGetQHull_cpp.md)
- [simGetDecimatedMesh](sim-1/simGetDecimatedMesh_cpp.md)
- [simIsDynamicallyEnabled](sim-1/simIsDynamicallyEnabled_cpp.md)
- See also:
- [properties](properties.md)

## <a id="dummyObject"></a>Dummies

- [`sim.createDummy`](sim-1/simCreateDummy.md)
- [`sim.getLinkDummy`](sim-1/simGetLinkDummy.md)
- [`sim.setLinkDummy`](sim-1/simSetLinkDummy.md)
- See also:
- [properties](properties.md)

- [simCreateDummy](sim-1/simCreateDummy_cpp.md)
- [simGetLinkDummy](sim-1/simGetLinkDummy_cpp.md)
- [simSetLinkDummy](sim-1/simSetLinkDummy_cpp.md)
- See also:
- [properties](properties.md)

## <a id="customizingLuaFunctions"></a><a id="customScriptFunctions"></a>Scripts

- [`sim.createScript`](sim-1/simCreateScript.md)
- [`sim.getScript`](sim-1/simGetScript.md)
- [`sim.isHandle`](sim-1/simIsHandle.md)
- [`sim.initScript`](sim-1/simInitScript.md)
- [`sim.callScriptFunction`](sim-1/simCallScriptFunction.md)
- [`sim.getScriptFunctions`](sim-1/simGetScriptFunctions.md)
- [`sim.executeScriptString`](sim-1/simExecuteScriptString.md)
- [`sim.getApiFunc`](sim-1/simGetApiFunc.md)
- [`sim.getApiInfo`](sim-1/simGetApiInfo.md)
- [`sim.handleSimulationScripts`](sim-1/simHandleSimulationScripts.md)
- [`sim.handleEmbeddedScripts`](sim-1/simHandleEmbeddedScripts.md)
- [`sim.handleAddOnScripts`](sim-1/simHandleAddOnScripts.md)
- [`sim.handleSandboxScript`](sim-1/simHandleSandboxScript.md)
- [`sim.registerScriptFuncHook`](sim-1/simRegisterScriptFuncHook.md)
- [`sim.getStackTraceback`](sim-1/simGetStackTraceback.md)
- [`sim.setEventFilters`](sim-1/simSetEventFilters.md)
- See also:
- [properties](properties.md)

- [simCreateScript](sim-1/simCreateScript_cpp.md)
- [simGetScriptHandleEx](sim-1/simGetScriptHandleEx_cpp.md)
- [simIsHandle](sim-1/simIsHandle_cpp.md)
- [simInitScript](sim-1/simInitScript_cpp.md)
- [simCallScriptFunctionEx](sim-1/simCallScriptFunctionEx_cpp.md)
- [simExecuteScriptString](sim-1/simExecuteScriptString_cpp.md)
- [simGetApiFunc](sim-1/simGetApiFunc_cpp.md)
- [simGetApiInfo](sim-1/simGetApiInfo_cpp.md)
- [simResetScript](sim-1/simResetScript_cpp.md)
- [simRegisterScriptCallbackFunction](sim-1/simRegisterScriptCallbackFunction_cpp.md)
- [simRegisterScriptVariable](sim-1/simRegisterScriptVariable_cpp.md)
- [simRegisterScriptFuncHook](sim-1/simRegisterScriptFuncHook_cpp.md)
- See also:
- [properties](properties.md)

## <a id="jointObject"></a>Joints

- [`sim.setJointPosition`](sim-1/simSetJointPosition.md)
- [`sim.getJointPosition`](sim-1/simGetJointPosition.md)
- [`sim.setJointTargetPosition`](sim-1/simSetJointTargetPosition.md)
- [`sim.getJointTargetPosition`](sim-1/simGetJointTargetPosition.md)
- [`sim.setJointTargetVelocity`](sim-1/simSetJointTargetVelocity.md)
- [`sim.getJointTargetVelocity`](sim-1/simGetJointTargetVelocity.md)
- [`sim.getJointVelocity`](sim-1/simGetJointVelocity.md)
- [`sim.getObjectChildPose`](sim-1/simGetObjectChildPose.md)
- [`sim.setObjectChildPose`](sim-1/simSetObjectChildPose.md)
- [`sim.setJointInterval`](sim-1/simSetJointInterval.md)
- [`sim.getJointInterval`](sim-1/simGetJointInterval.md)
- [`sim.getJointType`](sim-1/simGetJointType.md)
- [`sim.createJoint`](sim-1/simCreateJoint.md)
- [`sim.setJointMode`](sim-1/simSetJointMode.md)
- [`sim.getJointMode`](sim-1/simGetJointMode.md)
- [`sim.setJointDependency`](sim-1/simSetJointDependency.md)
- [`sim.getJointDependency`](sim-1/simGetJointDependency.md)
- [`sim.getJointForce`](sim-1/simGetJointForce.md)
- [`sim.getJointTargetForce`](sim-1/simGetJointTargetForce.md)
- [`sim.setJointTargetForce`](sim-1/simSetJointTargetForce.md)
- See also:
- [properties](properties.md)

- [simSetJointPosition](sim-1/simSetJointPosition_cpp.md)
- [simGetJointPosition](sim-1/simGetJointPosition_cpp.md)
- [simSetJointTargetPosition](sim-1/simSetJointTargetPosition_cpp.md)
- [simGetJointTargetPosition](sim-1/simGetJointTargetPosition_cpp.md)
- [simSetJointTargetVelocity](sim-1/simSetJointTargetVelocity_cpp.md)
- [simGetJointTargetVelocity](sim-1/simGetJointTargetVelocity_cpp.md)
- [simGetJointVelocity](sim-1/simGetJointVelocity_cpp.md)
- [simGetObjectChildPose](sim-1/simGetObjectChildPose_cpp.md)
- [simSetObjectChildPose](sim-1/simSetObjectChildPose_cpp.md)
- [simSetJointInterval](sim-1/simSetJointInterval_cpp.md)
- [simGetJointInterval](sim-1/simGetJointInterval_cpp.md)
- [simGetJointType](sim-1/simGetJointType_cpp.md)
- [simCreateJoint](sim-1/simCreateJoint_cpp.md)
- [simSetJointMode](sim-1/simSetJointMode_cpp.md)
- [simGetJointMode](sim-1/simGetJointMode_cpp.md)
- [simSetJointDependency](sim-1/simSetJointDependency_cpp.md)
- [simGetJointDependency](sim-1/simGetJointDependency_cpp.md)
- [simGetJointForce](sim-1/simGetJointForce_cpp.md)
- [simGetJointTargetForce](sim-1/simGetJointTargetForce_cpp.md)
- [simSetJointTargetForce](sim-1/simSetJointTargetForce_cpp.md)
- See also:
- [properties](properties.md)

## <a id="shapeObject"></a>Shapes

- [`sim.addForce`](sim-1/simAddForce.md)
- [`sim.addForceAndTorque`](sim-1/simAddForceAndTorque.md)
- [`sim.getVelocity`](sim-1/simGetVelocity.md)
- [`sim.getShapeColor`](sim-1/simGetShapeColor.md)
- [`sim.setShapeColor`](sim-1/simSetShapeColor.md)
- [`sim.getShapeTextureId`](sim-1/simGetShapeTextureId.md)
- [`sim.setShapeTexture`](sim-1/simSetShapeTexture.md)
- [`sim.createShape`](sim-1/simCreateShape.md)
- [`sim.createPrimitiveShape`](sim-1/simCreatePrimitiveShape.md)
- [`sim.createHeightfieldShape`](sim-1/simCreateHeightfieldShape.md)
- [`sim.getShapeMesh`](sim-1/simGetShapeMesh.md)
- [`sim.getShapeViz`](sim-1/simGetShapeViz.md)
- [`sim.getShapeGeomInfo`](sim-1/simGetShapeGeomInfo.md)
- [`sim.getShapeMass`](sim-1/simGetShapeMass.md)
- [`sim.setShapeMass`](sim-1/simSetShapeMass.md)
- [`sim.getShapeInertia`](sim-1/simGetShapeInertia.md)
- [`sim.setShapeInertia`](sim-1/simSetShapeInertia.md)
- [`sim.computeMassAndInertia`](sim-1/simComputeMassAndInertia.md)
- [`sim.groupShapes`](sim-1/simGroupShapes.md)
- [`sim.ungroupShape`](sim-1/simUngroupShape.md)
- [`sim.importShape`](sim-1/simImportShape.md)
- [`sim.alignShapeBB`](sim-1/simAlignShapeBB.md)
- [`sim.relocateShapeFrame`](sim-1/simRelocateShapeFrame.md)
- [`sim.getShapeBB`](sim-1/simGetShapeBB.md)
- [`sim.setShapeBB`](sim-1/simSetShapeBB.md)
- [`sim.getExtensionString`](sim-1/simGetExtensionString.md)
- [`sim.generateTextShape`](sim-1/simGenerateTextShape.md)
- See also:
- [properties](properties.md)

- [simAddForce](sim-1/simAddForce_cpp.md)
- [simAddForceAndTorque](sim-1/simAddForceAndTorque_cpp.md)
- [simGetVelocity](sim-1/simGetVelocity_cpp.md)
- [simGetShapeColor](sim-1/simGetShapeColor_cpp.md)
- [simSetShapeColor](sim-1/simSetShapeColor_cpp.md)
- [simGetShapeTextureId](sim-1/simGetShapeTextureId_cpp.md)
- [simSetShapeTexture](sim-1/simSetShapeTexture_cpp.md)
- [simCreateShape](sim-1/simCreateShape_cpp.md)
- [simCreatePrimitiveShape](sim-1/simCreatePrimitiveShape_cpp.md)
- [simCreateHeightfieldShape](sim-1/simCreateHeightfieldShape_cpp.md)
- [simGetShapeMesh](sim-1/simGetShapeMesh_cpp.md)
- [simGetShapeViz](sim-1/simGetShapeViz_cpp.md)
- [simApplyTexture](sim-1/simApplyTexture_cpp.md)
- [simGetShapeGeomInfo](sim-1/simGetShapeGeomInfo_cpp.md)
- [simGetShapeMass](sim-1/simGetShapeMass_cpp.md)
- [simSetShapeMass](sim-1/simSetShapeMass_cpp.md)
- [simGetShapeInertia](sim-1/simGetShapeInertia_cpp.md)
- [simSetShapeInertia](sim-1/simSetShapeInertia_cpp.md)
- [simComputeMassAndInertia](sim-1/simComputeMassAndInertia_cpp.md)
- [simGroupShapes](sim-1/simGroupShapes_cpp.md)
- [simUngroupShape](sim-1/simUngroupShape_cpp.md)
- [simImportShape](sim-1/simImportShape_cpp.md)
- [simConvexDecompose](sim-1/simConvexDecompose_cpp.md)
- [simGetQHull](sim-1/simGetQHull_cpp.md)
- [simGetDecimatedMesh](sim-1/simGetDecimatedMesh_cpp.md)
- [simAlignShapeBB](sim-1/simAlignShapeBB_cpp.md)
- [simRelocateShapeFrame](sim-1/simRelocateShapeFrame_cpp.md)
- [simGetExtensionString](sim-1/simGetExtensionString_cpp.md)
- See also:
- [properties](properties.md)

## <a id="proximitySensor"></a>Proximity sensors

- [`sim.handleProximitySensor`](sim-1/simHandleProximitySensor.md)
- [`sim.readProximitySensor`](sim-1/simReadProximitySensor.md)
- [`sim.resetProximitySensor`](sim-1/simResetProximitySensor.md)
- [`sim.checkProximitySensor`](sim-1/simCheckProximitySensor.md)
- [`sim.createProximitySensor`](sim-1/simCreateProximitySensor.md)
- See also:
- [properties](properties.md)

- [simHandleProximitySensor](sim-1/simHandleProximitySensor_cpp.md)
- [simReadProximitySensor](sim-1/simReadProximitySensor_cpp.md)
- [simResetProximitySensor](sim-1/simResetProximitySensor_cpp.md)
- [simCheckProximitySensor](sim-1/simCheckProximitySensor_cpp.md)
- [simCreateProximitySensor](sim-1/simCreateProximitySensor_cpp.md)
- See also:
- [properties](properties.md)

## <a id="visionSensor"></a>Vision sensors

- [`sim.handleVisionSensor`](sim-1/simHandleVisionSensor.md)
- [`sim.readVisionSensor`](sim-1/simReadVisionSensor.md)
- [`sim.resetVisionSensor`](sim-1/simResetVisionSensor.md)
- [`sim.checkVisionSensor`](sim-1/simCheckVisionSensor.md)
- [`sim.checkVisionSensorEx`](sim-1/simCheckVisionSensorEx.md)
- [`sim.getVisionSensorDepth`](sim-1/simGetVisionSensorDepth.md)
- [`sim.getVisionSensorImg`](sim-1/simGetVisionSensorImg.md)
- [`sim.setVisionSensorImg`](sim-1/simSetVisionSensorImg.md)
- [`sim.getVisionSensorRes`](sim-1/simGetVisionSensorRes.md)
- [`sim.adjustView`](sim-1/simAdjustView.md)
- [`sim.createVisionSensor`](sim-1/simCreateVisionSensor.md)
- [`sim.getExtensionString`](sim-1/simGetExtensionString.md)
- See also:
- [properties](properties.md)

- [simHandleVisionSensor](sim-1/simHandleVisionSensor_cpp.md)
- [simReadVisionSensor](sim-1/simReadVisionSensor_cpp.md)
- [simResetVisionSensor](sim-1/simResetVisionSensor_cpp.md)
- [simCheckVisionSensor](sim-1/simCheckVisionSensor_cpp.md)
- [simCheckVisionSensorEx](sim-1/simCheckVisionSensorEx_cpp.md)
- [simGetVisionSensorDepth](sim-1/simGetVisionSensorDepth_cpp.md)
- [simGetVisionSensorImg](sim-1/simGetVisionSensorImg_cpp.md)
- [simSetVisionSensorImg](sim-1/simSetVisionSensorImg_cpp.md)
- [simGetVisionSensorRes](sim-1/simGetVisionSensorRes_cpp.md)
- [simAdjustView](sim-1/simAdjustView_cpp.md)
- [simCreateVisionSensor](sim-1/simCreateVisionSensor_cpp.md)
- [simGetExtensionString](sim-1/simGetExtensionString_cpp.md)
- See also:
- [properties](properties.md)

## <a id="forceSensor"></a>Force sensors

- [`sim.readForceSensor`](sim-1/simReadForceSensor.md)
- [`sim.createForceSensor`](sim-1/simCreateForceSensor.md)
- See also:
- [properties](properties.md)

- [simReadForceSensor](sim-1/simReadForceSensor_cpp.md)
- [simCreateForceSensor](sim-1/simCreateForceSensor_cpp.md)
- See also:
- [properties](properties.md)

## <a id="graphs"></a>Graphs

- [`sim.addGraphStream`](sim-1/simAddGraphStream.md)
- [`sim.setGraphStreamTransformation`](sim-1/simSetGraphStreamTransformation.md)
- [`sim.setGraphStreamValue`](sim-1/simSetGraphStreamValue.md)
- [`sim.addGraphCurve`](sim-1/simAddGraphCurve.md)
- [`sim.destroyGraphCurve`](sim-1/simDestroyGraphCurve.md)
- [`sim.duplicateGraphCurveToStatic`](sim-1/simDuplicateGraphCurveToStatic.md)
- [`sim.handleGraph`](sim-1/simHandleGraph.md)
- [`sim.resetGraph`](sim-1/simResetGraph.md)
- See also:
- [properties](properties.md)

- [simAddGraphStream](sim-1/simAddGraphStream_cpp.md)
- [simSetGraphStreamTransformation](sim-1/simSetGraphStreamTransformation_cpp.md)
- [simSetGraphStreamValue](sim-1/simSetGraphStreamValue_cpp.md)
- [simAddGraphCurve](sim-1/simAddGraphCurve_cpp.md)
- [simDestroyGraphCurve](sim-1/simDestroyGraphCurve_cpp.md)
- [simDuplicateGraphCurveToStatic](sim-1/simDuplicateGraphCurveToStatic_cpp.md)
- [simHandleGraph](sim-1/simHandleGraph_cpp.md)
- [simResetGraph](sim-1/simResetGraph_cpp.md)
- See also:
- [properties](properties.md)

## <a id="lightObject"></a>Lights

- [`sim.getExtensionString`](sim-1/simGetExtensionString.md)
- See also:
- [properties](properties.md)

- [simGetExtensionString](sim-1/simGetExtensionString_cpp.md)
- See also:
- [properties](properties.md)

## <a id="cameraObject"></a>Cameras

- [`sim.cameraFitToView`](sim-1/simCameraFitToView.md)
- [`sim.adjustView`](sim-1/simAdjustView.md)
- [`sim.getExtensionString`](sim-1/simGetExtensionString.md)
- See also:
- [properties](properties.md)

- [simCameraFitToView](sim-1/simCameraFitToView_cpp.md)
- [simAdjustView](sim-1/simAdjustView_cpp.md)
- [simGetExtensionString](sim-1/simGetExtensionString_cpp.md)
- See also:
- [properties](properties.md)

## <a id="octree"></a>OC trees

- [`sim.createOctree`](sim-1/simCreateOctree.md)
- [`sim.insertVoxelsIntoOctree`](sim-1/simInsertVoxelsIntoOctree.md)
- [`sim.removeVoxelsFromOctree`](sim-1/simRemoveVoxelsFromOctree.md)
- [`sim.insertObjectIntoOctree`](sim-1/simInsertObjectIntoOctree.md)
- [`sim.subtractObjectFromOctree`](sim-1/simSubtractObjectFromOctree.md)
- [`sim.getOctreeVoxels`](sim-1/simGetOctreeVoxels.md)
- [`sim.checkOctreePointOccupancy`](sim-1/simCheckOctreePointOccupancy.md)
- See also:
- [properties](properties.md)

- [simCreateOctree](sim-1/simCreateOctree_cpp.md)
- [simInsertVoxelsIntoOctree](sim-1/simInsertVoxelsIntoOctree_cpp.md)
- [simRemoveVoxelsFromOctree](sim-1/simRemoveVoxelsFromOctree_cpp.md)
- [simInsertObjectIntoOctree](sim-1/simInsertObjectIntoOctree_cpp.md)
- [simSubtractObjectFromOctree](sim-1/simSubtractObjectFromOctree_cpp.md)
- [simGetOctreeVoxels](sim-1/simGetOctreeVoxels_cpp.md)
- [simCheckOctreePointOccupancy](sim-1/simCheckOctreePointOccupancy_cpp.md)
- See also:
- [properties](properties.md)

## <a id="pointCloud"></a>Point clouds

- [`sim.createPointCloud`](sim-1/simCreatePointCloud.md)
- [`sim.getPointCloudOptions`](sim-1/simGetPointCloudOptions.md)
- [`sim.setPointCloudOptions`](sim-1/simSetPointCloudOptions.md)
- [`sim.insertPointsIntoPointCloud`](sim-1/simInsertPointsIntoPointCloud.md)
- [`sim.removePointsFromPointCloud`](sim-1/simRemovePointsFromPointCloud.md)
- [`sim.subtractObjectFromPointCloud`](sim-1/simSubtractObjectFromPointCloud.md)
- [`sim.intersectPointsWithPointCloud`](sim-1/simIntersectPointsWithPointCloud.md)
- [`sim.insertObjectIntoPointCloud`](sim-1/simInsertObjectIntoPointCloud.md)
- [`sim.getPointCloudPoints`](sim-1/simGetPointCloudPoints.md)
- See also:
- [properties](properties.md)

- [simCreatePointCloud](sim-1/simCreatePointCloud_cpp.md)
- [simGetPointCloudOptions](sim-1/simGetPointCloudOptions_cpp.md)
- [simSetPointCloudOptions](sim-1/simSetPointCloudOptions_cpp.md)
- [simInsertPointsIntoPointCloud](sim-1/simInsertPointsIntoPointCloud_cpp.md)
- [simRemovePointsFromPointCloud](sim-1/simRemovePointsFromPointCloud_cpp.md)
- [simSubtractObjectFromPointCloud](sim-1/simSubtractObjectFromPointCloud_cpp.md)
- [simIntersectPointsWithPointCloud](sim-1/simIntersectPointsWithPointCloud_cpp.md)
- [simInsertObjectIntoPointCloud](sim-1/simInsertObjectIntoPointCloud_cpp.md)
- [simGetPointCloudPoints](sim-1/simGetPointCloudPoints_cpp.md)
- See also:
- [properties](properties.md)

## <a id="paths"></a>Paths

- [`sim.createPath`](sim-1/simCreatePath.md)
- [`sim.getConfigDistance`](sim-1/simGetConfigDistance.md)
- [`sim.getPathLengths`](sim-1/simGetPathLengths.md)
- [`sim.getPathInterpolatedConfig`](sim-1/simGetPathInterpolatedConfig.md)
- [`sim.resamplePath`](sim-1/simResamplePath.md)
- [`sim.generateTimeOptimalTrajectory`](sim-1/simGenerateTimeOptimalTrajectory.md)
- [`sim.generateShapeFromPath`](sim-1/simGenerateShapefromPath.md)
- [`sim.getClosestPosOnPath`](sim-1/simGetClosestPosOnPath.md)

- [simGenerateShapeFromPath](sim-1/simGenerateShapefromPath_cpp.md)
- [simGetClosestPosOnPath](sim-1/simGetClosestPosOnPath_cpp.md)

## <a id="sceneObjectFunctionality"></a>Scene objects

- [`sim.getObject`](sim-1/simGetObject.md)
- [`sim.getObjectUid`](sim-1/simGetObjectUid.md)
- [`sim.isHandle`](sim-1/simIsHandle.md)
- [`sim.removeObjects`](sim-1/simRemoveObjects.md)
- [`sim.removeModel`](sim-1/simRemoveModel.md)
- [`sim.getObjectAlias`](sim-1/simGetObjectAlias.md)
- [`sim.setObjectAlias`](sim-1/simSetObjectAlias.md)
- [`sim.getObjects`](sim-1/simGetObjects.md)
- [`sim.getObjectsInTree`](sim-1/simGetObjectsInTree.md)
- [`sim.getObjectParent`](sim-1/simGetObjectParent.md)
- [`sim.setObjectParent`](sim-1/simSetObjectParent.md)
- [`sim.getObjectHierarchyOrder`](sim-1/simGetObjectHierarchyOrder.md)
- [`sim.setObjectHierarchyOrder`](sim-1/simSetObjectHierarchyOrder.md)
- [`sim.getObjectChild`](sim-1/simGetObjectChild.md)
- [`sim.getObjectMatrix`](sim-1/simGetObjectMatrix.md)
- [`sim.setObjectMatrix`](sim-1/simSetObjectMatrix.md)
- [`sim.getObjectPose`](sim-1/simGetObjectPose.md)
- [`sim.setObjectPose`](sim-1/simSetObjectPose.md)
- [`sim.getObjectPosition`](sim-1/simGetObjectPosition.md)
- [`sim.setObjectPosition`](sim-1/simSetObjectPosition.md)
- [`sim.getObjectOrientation`](sim-1/simGetObjectOrientation.md)
- [`sim.setObjectOrientation`](sim-1/simSetObjectOrientation.md)
- [`sim.getObjectQuaternion`](sim-1/simGetObjectQuaternion.md)
- [`sim.setObjectQuaternion`](sim-1/simSetObjectQuaternion.md)
- [`sim.getObjectType`](sim-1/simGetObjectType.md)
- [`sim.getObjectSel`](sim-1/simGetObjectSel.md)
- [`sim.setObjectSel`](sim-1/simSetObjectSel.md)
- [`sim.getObjectSizeFactor`](sim-1/simGetObjectSizeFactor.md)
- [`sim.copyPasteObjects`](sim-1/simCopyPasteObjects.md)
- [`sim.scaleObject`](sim-1/simScaleObject.md)
- [`sim.scaleObjects`](sim-1/simScaleObjects.md)
- [`sim.getObjectVelocity`](sim-1/simGetObjectVelocity.md)
- [`sim.setReferencedHandles`](sim-1/simSetReferencedHandles.md)
- [`sim.getReferencedHandles`](sim-1/simGetReferencedHandles.md)
- [`sim.getReferencedHandlesTags`](sim-1/simGetReferencedHandlesTags.md)
- [`sim.isDynamicallyEnabled`](sim-1/simIsDynamicallyEnabled.md)
- [`sim.getObjectColor`](sim-1/simGetObjectColor.md)
- [`sim.setObjectColor`](sim-1/simSetObjectColor.md)
- See also:
- [properties](properties.md)

- [simGetObject](sim-1/simGetObject_cpp.md)
- [simGetObjectUid](sim-1/simGetObjectUid_cpp.md)
- [simIsHandle](sim-1/simIsHandle_cpp.md)
- [simRemoveObjects](sim-1/simRemoveObjects_cpp.md)
- [simRemoveModel](sim-1/simRemoveModel_cpp.md)
- [simGetObjectAlias](sim-1/simGetObjectAlias_cpp.md)
- [simSetObjectAlias](sim-1/simSetObjectAlias_cpp.md)
- [simGetObjects](sim-1/simGetObjects_cpp.md)
- [simGetObjectsInTree](sim-1/simGetObjectsInTree_cpp.md)
- [simGetObjectParent](sim-1/simGetObjectParent_cpp.md)
- [simSetObjectParent](sim-1/simSetObjectParent_cpp.md)
- [simGetObjectHierarchyOrder](sim-1/simGetObjectHierarchyOrder_cpp.md)
- [simSetObjectHierarchyOrder](sim-1/simSetObjectHierarchyOrder_cpp.md)
- [simGetObjectChild](sim-1/simGetObjectChild_cpp.md)
- [simGetObjectMatrix](sim-1/simGetObjectMatrix_cpp.md)
- [simSetObjectMatrix](sim-1/simSetObjectMatrix_cpp.md)
- [simGetObjectPose](sim-1/simGetObjectPose_cpp.md)
- [simSetObjectPose](sim-1/simSetObjectPose_cpp.md)
- [simGetObjectPosition](sim-1/simGetObjectPosition_cpp.md)
- [simSetObjectPosition](sim-1/simSetObjectPosition_cpp.md)
- [simGetObjectOrientation](sim-1/simGetObjectOrientation_cpp.md)
- [simSetObjectOrientation](sim-1/simSetObjectOrientation_cpp.md)
- [simGetObjectQuaternion](sim-1/simGetObjectQuaternion_cpp.md)
- [simSetObjectQuaternion](sim-1/simSetObjectQuaternion_cpp.md)
- [simGetObjectType](sim-1/simGetObjectType_cpp.md)
- [simGetObjectSel](sim-1/simGetObjectSel_cpp.md)
- [simSetObjectSel](sim-1/simSetObjectSel_cpp.md)
- [simGetObjectSizeFactor](sim-1/simGetObjectSizeFactor_cpp.md)
- [simCopyPasteObjects](sim-1/simCopyPasteObjects_cpp.md)
- [simScaleObject](sim-1/simScaleObject_cpp.md)
- [simScaleObjects](sim-1/simScaleObjects_cpp.md)
- [simGetObjectVelocity](sim-1/simGetObjectVelocity_cpp.md)
- [simSetReferencedHandles](sim-1/simSetReferencedHandles_cpp.md)
- [simGetReferencedHandles](sim-1/simGetReferencedHandles_cpp.md)
- [simIsDynamicallyEnabled](sim-1/simIsDynamicallyEnabled_cpp.md)
- [simGetObjectColor](sim-1/simGetObjectColor_cpp.md)
- [simSetObjectColor](sim-1/simSetObjectColor_cpp.md)
- See also:
- [properties](properties.md)

## <a id="properties"></a>Properties

- [`sim.setBoolProperty`](sim-1/simSetBoolProperty.md)
- [`sim.getBoolProperty`](sim-1/simGetBoolProperty.md)
- [`sim.setIntProperty`](sim-1/simSetIntProperty.md)
- [`sim.getIntProperty`](sim-1/simGetIntProperty.md)
- [`sim.setLongProperty`](sim-1/simSetLongProperty.md)
- [`sim.getLongProperty`](sim-1/simGetLongProperty.md)
- [`sim.setFloatProperty`](sim-1/simSetFloatProperty.md)
- [`sim.getFloatProperty`](sim-1/simGetFloatProperty.md)
- [`sim.setStringProperty`](sim-1/simSetStringProperty.md)
- [`sim.getStringProperty`](sim-1/simGetStringProperty.md)
- [`sim.setBufferProperty`](sim-1/simSetBufferProperty.md)
- [`sim.getBufferProperty`](sim-1/simGetBufferProperty.md)
- [`sim.setIntArrayProperty`](sim-1/simSetIntArrayProperty.md)
- [`sim.getIntArrayProperty`](sim-1/simGetIntArrayProperty.md)
- [`sim.setIntArray2Property`](sim-1/simSetIntArray2Property.md)
- [`sim.getIntArray2Property`](sim-1/simGetIntArray2Property.md)
- [`sim.setFloatArrayProperty`](sim-1/simSetFloatArrayProperty.md)
- [`sim.getFloatArrayProperty`](sim-1/simGetFloatArrayProperty.md)
- [`sim.setVector2Property`](sim-1/simSetVector2Property.md)
- [`sim.getVector2Property`](sim-1/simGetVector2Property.md)
- [`sim.setVector3Property`](sim-1/simSetVector3Property.md)
- [`sim.getVector3Property`](sim-1/simGetVector3Property.md)
- [`sim.setQuaternionProperty`](sim-1/simSetQuaternionProperty.md)
- [`sim.getQuaternionProperty`](sim-1/simGetQuaternionProperty.md)
- [`sim.setPoseProperty`](sim-1/simSetPoseProperty.md)
- [`sim.getPoseProperty`](sim-1/simGetPoseProperty.md)
- [`sim.setColorProperty`](sim-1/simSetColorProperty.md)
- [`sim.getColorProperty`](sim-1/simGetColorProperty.md)
- [`sim.removeProperty`](sim-1/simRemoveProperty.md)
- [`sim.getPropertyName`](sim-1/simGetPropertyName.md)
- [`sim.getPropertyInfo`](sim-1/simGetPropertyInfo.md)
- [`sim.getProperty`](sim-1/simGetProperty.md)
- [`sim.setProperty`](sim-1/simSetProperty.md)
- [`sim.getProperties`](sim-1/simGetProperties.md)
- [`sim.setProperties`](sim-1/simSetProperties.md)
- [`sim.getPropertiesInfos`](sim-1/simGetPropertiesInfos.md)
- See also:
- [packing/unpacking functions](#packing)
- [properties](properties.md)

- [simSetBoolProperty](sim-1/simSetBoolProperty_cpp.md)
- [simGetBoolProperty](sim-1/simGetBoolProperty_cpp.md)
- [simSetIntProperty](sim-1/simSetIntProperty_cpp.md)
- [simGetIntProperty](sim-1/simGetIntProperty_cpp.md)
- [simSetLongProperty](sim-1/simSetLongProperty_cpp.md)
- [simGetLongProperty](sim-1/simGetLongProperty_cpp.md)
- [simSetFloatProperty](sim-1/simSetFloatProperty_cpp.md)
- [simGetFloatProperty](sim-1/simGetFloatProperty_cpp.md)
- [simSetStringProperty](sim-1/simSetStringProperty_cpp.md)
- [simGetStringProperty](sim-1/simGetStringProperty_cpp.md)
- [simSetBufferProperty](sim-1/simSetBufferProperty_cpp.md)
- [simGetBufferProperty](sim-1/simGetBufferProperty_cpp.md)
- [simSetIntArrayProperty](sim-1/simSetIntArrayProperty_cpp.md)
- [simGetIntArrayProperty](sim-1/simGetIntArrayProperty_cpp.md)
- [simSetIntArray2Property](sim-1/simSetIntArray2Property_cpp.md)
- [simGetIntArray2Property](sim-1/simGetIntArray2Property_cpp.md)
- [simSetFloatArrayProperty](sim-1/simSetFloatArrayProperty_cpp.md)
- [simGetFloatArrayProperty](sim-1/simGetFloatArrayProperty_cpp.md)
- [simSetVector2Property](sim-1/simSetVector2Property_cpp.md)
- [simGetVector2Property](sim-1/simGetVector2Property_cpp.md)
- [simSetVector3Property](sim-1/simSetVector3Property_cpp.md)
- [simGetVector3Property](sim-1/simGetVector3Property_cpp.md)
- [simSetQuaternionProperty](sim-1/simSetQuaternionProperty_cpp.md)
- [simGetQuaternionProperty](sim-1/simGetQuaternionProperty_cpp.md)
- [simSetPoseProperty](sim-1/simSetPoseProperty_cpp.md)
- [simGetPoseProperty](sim-1/simGetPoseProperty_cpp.md)
- [simSetColorProperty](sim-1/simSetColorProperty_cpp.md)
- [simGetColorProperty](sim-1/simGetColorProperty_cpp.md)
- [simRemoveProperty](sim-1/simRemoveProperty_cpp.md)
- [simGetPropertyName](sim-1/simGetPropertyName_cpp.md)
- [simGetPropertyInfo](sim-1/simGetPropertyInfo_cpp.md)
- See also:
- [properties](properties.md)

## <a id="collections"></a>Collections

- [`sim.createCollection`](sim-1/simCreateCollection.md)
- [`sim.destroyCollection`](sim-1/simDestroyCollection.md)
- [`sim.addItemToCollection`](sim-1/simAddItemToCollection.md)
- [`sim.getCollectionObjects`](sim-1/simGetCollectionObjects.md)

- [simCreateCollectionEx](sim-1/simCreateCollection_cpp.md)
- [simDestroyCollection](sim-1/simDestroyCollection_cpp.md)
- [simAddItemToCollection](sim-1/simAddItemToCollection_cpp.md)
- [simGetCollectionObjects](sim-1/simGetCollectionObjects_cpp.md)

## <a id="serialCommunicationFunctionality"></a><a id="serialPort"></a>Serial port

- [`sim.serialCheck`](sim-1/simSerialCheck.md)
- [`sim.serialClose`](sim-1/simSerialClose.md)
- [`sim.serialOpen`](sim-1/simSerialOpen.md)
- [`sim.serialRead`](sim-1/simSerialRead.md)
- [`sim.serialSend`](sim-1/simSerialSend.md)

- [simSerialCheck](sim-1/simSerialCheck_cpp.md)
- [simSerialClose](sim-1/simSerialClose_cpp.md)
- [simSerialOpen](sim-1/simSerialOpen_cpp.md)
- [simSerialRead](sim-1/simSerialRead_cpp.md)
- [simSerialSend](sim-1/simSerialSend_cpp.md)

## <a id="serialCommunicationFunctionality-2"></a><a id="serialPort-2"></a>Serial port

- [`sim.serialCheck`](sim-1/simSerialCheck.md)
- [`sim.serialClose`](sim-1/simSerialClose.md)
- [`sim.serialOpen`](sim-1/simSerialOpen.md)
- [`sim.serialRead`](sim-1/simSerialRead.md)
- [`sim.serialSend`](sim-1/simSerialSend.md)

- [simSerialCheck](sim-1/simSerialCheck_cpp.md)
- [simSerialClose](sim-1/simSerialClose_cpp.md)
- [simSerialOpen](sim-1/simSerialOpen_cpp.md)
- [simSerialRead](sim-1/simSerialRead_cpp.md)
- [simSerialSend](sim-1/simSerialSend_cpp.md)

## <a id="drawingObject"></a><a id="rendering"></a>Rendering

- [`sim.addDrawingObject`](sim-1/simAddDrawingObject.md)
- [`sim.addDrawingObjectItem`](sim-1/simAddDrawingObjectItem.md)
- [`sim.removeDrawingObject`](sim-1/simRemoveDrawingObject.md)
- [`sim.getShapeColor`](sim-1/simGetShapeColor.md)
- [`sim.setShapeColor`](sim-1/simSetShapeColor.md)
- [`sim.getObjectColor`](sim-1/simGetObjectColor.md)
- [`sim.setObjectColor`](sim-1/simSetObjectColor.md)
- [`sim.changeEntityColor`](sim-1/simChangeEntityColor.md)
- [`sim.restoreEntityColor`](sim-1/simRestoreEntityColor.md)
- [`sim.getGenesisEvents`](sim-1/simGetGenesisEvents.md)

- [simAddDrawingObject](sim-1/simAddDrawingObject_cpp.md)
- [simAddDrawingObjectItem](sim-1/simAddDrawingObjectItem_cpp.md)
- [simRemoveDrawingObject](sim-1/simRemoveDrawingObject_cpp.md)
- [simGetShapeColor](sim-1/simGetShapeColor_cpp.md)
- [simSetShapeColor](sim-1/simSetShapeColor_cpp.md)
- [simGetObjectColor](sim-1/simGetObjectColor_cpp.md)
- [simSetObjectColor](sim-1/simSetObjectColor_cpp.md)

## <a id="particleObject"></a>Particle objects

- [`sim.addParticleObject`](sim-1/simAddParticleObject.md)
- [`sim.addParticleObjectItem`](sim-1/simAddParticleObjectItem.md)
- [`sim.removeParticleObject`](sim-1/simRemoveParticleObject.md)

## <a id="modelFunctionality"></a>Models

- [`sim.saveModel`](sim-1/simSaveModel.md)
- [`sim.loadModel`](sim-1/simLoadModel.md)
- See also:
- [properties](properties.md)

- [simSaveModel](sim-1/simSaveModel_cpp.md)
- [simLoadModel](sim-1/simLoadModel_cpp.md)
- See also:
- [properties](properties.md)

## <a id="sceneObjectSelectionFunctionality"></a>Object selection

- [`sim.getObjectSel`](sim-1/simGetObjectSel.md)
- [`sim.setObjectSel`](sim-1/simSetObjectSel.md)
- See also:
- [properties](properties.md)

- [simGetObjectSel](sim-1/simGetObjectSel_cpp.md)
- [simSetObjectSel](sim-1/simSetObjectSel_cpp.md)
- See also:
- [properties](properties.md)

## <a id="sceneObjectCreationFunctionality"></a>Object creation

- [`sim.createDummy`](sim-1/simCreateDummy.md)
- [`sim.createScript`](sim-1/simCreateScript.md)
- [`sim.createForceSensor`](sim-1/simCreateForceSensor.md)
- [`sim.createHeightfieldShape`](sim-1/simCreateHeightfieldShape.md)
- [`sim.createJoint`](sim-1/simCreateJoint.md)
- [`sim.createShape`](sim-1/simCreateShape.md)
- [`sim.createProximitySensor`](sim-1/simCreateProximitySensor.md)
- [`sim.createPrimitiveShape`](sim-1/simCreatePrimitiveShape.md)
- [`sim.createVisionSensor`](sim-1/simCreateVisionSensor.md)
- [`sim.createOctree`](sim-1/simCreateOctree.md)
- [`sim.createPointCloud`](sim-1/simCreatePointCloud.md)
- [`sim.createTexture`](sim-1/simCreateTexture.md)
- [`sim.generateTextShape`](sim-1/simGenerateTextShape.md)
- [`sim.generateShapeFromPath`](sim-1/simGenerateShapefromPath.md)

- [simCreateDummy](sim-1/simCreateDummy_cpp.md)
- [simCreateScript](sim-1/simCreateScript_cpp.md)
- [simCreateForceSensor](sim-1/simCreateForceSensor_cpp.md)
- [simCreateHeightfieldShape](sim-1/simCreateHeightfieldShape_cpp.md)
- [simCreateJoint](sim-1/simCreateJoint_cpp.md)
- [simCreateShape](sim-1/simCreateShape_cpp.md)
- [simCreateProximitySensor](sim-1/simCreateProximitySensor_cpp.md)
- [simCreatePrimitiveShape](sim-1/simCreatePrimitiveShape_cpp.md)
- [simCreateVisionSensor](sim-1/simCreateVisionSensor_cpp.md)
- [simCreateOctree](sim-1/simCreateOctree_cpp.md)
- [simCreatePointCloud](sim-1/simCreatePointCloud_cpp.md)
- [simCreateTexture](sim-1/simCreateTexture_cpp.md)
- [simGenerateShapeFromPath](sim-1/simGenerateShapefromPath_cpp.md)

## <a id="SimulationFunctionality"></a>Simulation

- [`sim.startSimulation`](sim-1/simStartSimulation.md)
- [`sim.pauseSimulation`](sim-1/simPauseSimulation.md)
- [`sim.stopSimulation`](sim-1/simStopSimulation.md)
- [`sim.getSimulationState`](sim-1/simGetSimulationState.md)
- [`sim.getSimulationTime`](sim-1/simGetSimulationTime.md)
- [`sim.getSimulationTimeStep`](sim-1/simGetSimulationTimeStep.md)
- See also:
- [properties](properties.md)

- [simStartSimulation](sim-1/simStartSimulation_cpp.md)
- [simPauseSimulation](sim-1/simPauseSimulation_cpp.md)
- [simStopSimulation](sim-1/simStopSimulation_cpp.md)
- [simGetSimulationState](sim-1/simGetSimulationState_cpp.md)
- [simGetSimulationTime](sim-1/simGetSimulationTime_cpp.md)
- [simGetSimulationTimeStep](sim-1/simGetSimulationTimeStep_cpp.md)
- See also:
- [properties](properties.md)

## <a id="threads"></a><a id="threadRelatedFunctionality"></a>Threads

- [`sim.setStepping`](sim-1/simSetStepping.md)
- [`sim.step`](sim-1/simStep.md)
- [`sim.setAutoYieldDelay`](sim-1/simSetAutoYieldDelay.md)
- [`sim.acquireLock`](sim-1/simAcquireLock.md)
- [`sim.releaseLock`](sim-1/simReleaseLock.md)
- [`sim.getSimulationStopping`](sim-1/simGetSimulationStopping.md)
- [`sim.handleExtCalls`](sim-1/simHandleExtCalls.md)

## <a id="pose"></a><a id="transformation"></a><a id="transformations"></a><a id="coordinatesAndTransformations"></a>Transformations

- [`sim.buildMatrix`](sim-1/simBuildMatrix.md)
- [`sim.buildPose`](sim-1/simBuildPose.md)
- [`sim.getEulerAnglesFromMatrix`](sim-1/simGetEulerAnglesFromMatrix.md)
- [`sim.matrixToPose`](sim-1/simMatrixToPose.md)
- [`sim.poseToMatrix`](sim-1/simPoseToMatrix.md)
- [`sim.multiplyMatrices`](sim-1/simMultiplyMatrices.md)
- [`sim.multiplyPoses`](sim-1/simMultiplyPoses.md)
- [`sim.interpolateMatrices`](sim-1/simInterpolateMatrices.md)
- [`sim.interpolatePoses`](sim-1/simInterpolatePoses.md)
- [`sim.getMatrixInverse`](sim-1/simGetMatrixInverse.md)
- [`sim.getPoseInverse`](sim-1/simGetPoseInverse.md)
- [`sim.getObjectMatrix`](sim-1/simGetObjectMatrix.md)
- [`sim.setObjectMatrix`](sim-1/simSetObjectMatrix.md)
- [`sim.getObjectPose`](sim-1/simGetObjectPose.md)
- [`sim.setObjectPose`](sim-1/simSetObjectPose.md)
- [`sim.getObjectPosition`](sim-1/simGetObjectPosition.md)
- [`sim.setObjectPosition`](sim-1/simSetObjectPosition.md)
- [`sim.getObjectOrientation`](sim-1/simGetObjectOrientation.md)
- [`sim.setObjectOrientation`](sim-1/simSetObjectOrientation.md)
- [`sim.getObjectQuaternion`](sim-1/simGetObjectQuaternion.md)
- [`sim.setObjectQuaternion`](sim-1/simSetObjectQuaternion.md)
- [`sim.getObjectChildPose`](sim-1/simGetObjectChildPose.md)
- [`sim.setObjectChildPose`](sim-1/simSetObjectChildPose.md)
- [`sim.multiplyVector`](sim-1/simMultiplyVector.md)
- [`sim.getRotationAxis`](sim-1/simGetRotationAxis.md)
- [`sim.rotateAroundAxis`](sim-1/simRotateAroundAxis.md)
- [`sim.getObjectVelocity`](sim-1/simGetObjectVelocity.md)
- [`sim.alignShapeBB`](sim-1/simAlignShapeBB.md)
- [`sim.relocateShapeFrame`](sim-1/simRelocateShapeFrame.md)
- [`sim.abgToYpr`](sim-1/simAbgToYpr.md)
- [`sim.yprToAbg`](sim-1/simYprToAbg.md)
- See also:
- [packing/unpacking functions](#packing)

- [simBuildMatrix](sim-1/simBuildMatrix_cpp.md)
- [simBuildPose](sim-1/simBuildPose_cpp.md)
- [simGetEulerAnglesFromMatrix](sim-1/simGetEulerAnglesFromMatrix_cpp.md)
- [simMatrixToPose](sim-1/simMatrixToPose_cpp.md)
- [simPoseToMatrix](sim-1/simPoseToMatrix_cpp.md)
- [simMultiplyMatrices](sim-1/simMultiplyMatrices_cpp.md)
- [simMultiplyPoses](sim-1/simMultiplyPoses_cpp.md)
- [simInterpolateMatrices](sim-1/simInterpolateMatrices_cpp.md)
- [simInterpolatePoses](sim-1/simInterpolatePoses_cpp.md)
- [simInvertMatrix](sim-1/simInvertMatrix_cpp.md)
- [simInvertPose](sim-1/simInvertPose_cpp.md)
- [simGetObjectMatrix](sim-1/simGetObjectMatrix_cpp.md)
- [simSetObjectMatrix](sim-1/simSetObjectMatrix_cpp.md)
- [simGetObjectPose](sim-1/simGetObjectPose_cpp.md)
- [simSetObjectPose](sim-1/simSetObjectPose_cpp.md)
- [simGetObjectPosition](sim-1/simGetObjectPosition_cpp.md)
- [simSetObjectPosition](sim-1/simSetObjectPosition_cpp.md)
- [simGetObjectOrientation](sim-1/simGetObjectOrientation_cpp.md)
- [simSetObjectOrientation](sim-1/simSetObjectOrientation_cpp.md)
- [simGetObjectQuaternion](sim-1/simGetObjectQuaternion_cpp.md)
- [simSetObjectQuaternion](sim-1/simSetObjectQuaternion_cpp.md)
- [simGetObjectChildPose](sim-1/simGetObjectChildPose_cpp.md)
- [simSetObjectChildPose](sim-1/simSetObjectChildPose_cpp.md)
- [simTransformVector](sim-1/simTransformVector_cpp.md)
- [simGetRotationAxis](sim-1/simGetRotationAxis_cpp.md)
- [simRotateAroundAxis](sim-1/simRotateAroundAxis_cpp.md)
- [simGetObjectVelocity](sim-1/simGetObjectVelocity_cpp.md)
- [simAlignShapeBB](sim-1/simAlignShapeBB_cpp.md)
- [simRelocateShapeFrame](sim-1/simRelocateShapeFrame_cpp.md)

## Messaging

- [loadPlugin](sim-1/loadPlugin.md)
- [unloadPlugin](sim-1/unloadPlugin.md)
- [`sim.addLog`](sim-1/simAddLog.md)
- [`sim.getSimulatorMessage`](sim-1/simGetSimulatorMessage.md)
- [`sim.serialCheck`](sim-1/simSerialCheck.md)
- [`sim.serialClose`](sim-1/simSerialClose.md)
- [`sim.serialOpen`](sim-1/simSerialOpen.md)
- [`sim.serialRead`](sim-1/simSerialRead.md)
- [`sim.serialSend`](sim-1/simSerialSend.md)
- [`sim.auxiliaryConsoleClose`](sim-1/simAuxiliaryConsoleClose.md)
- [`sim.auxiliaryConsoleOpen`](sim-1/simAuxiliaryConsoleOpen.md)
- [`sim.auxiliaryConsolePrint`](sim-1/simAuxiliaryConsolePrint.md)
- [`sim.callScriptFunction`](sim-1/simCallScriptFunction.md)
- [`sim.getScriptFunctions`](sim-1/simGetScriptFunctions.md)
- [`sim.executeScriptString`](sim-1/simExecuteScriptString.md)
- [`sim.getObjectUid`](sim-1/simGetObjectUid.md)
- [`sim.getGenesisEvents`](sim-1/simGetGenesisEvents.md)
- [`sim.broadcastMsg`](sim-1/simBroadcastMsg.md)
- [`sim.pushUserEvent`](sim-1/simPushUserEvent.md)
- [`sim.systemSemaphore`](sim-1/simSystemSemaphore.md)
- See also:
- [signal properties](properties.md#signals)

- [simAddLog](sim-1/simAddLog_cpp.md)
- [simSetLastError](sim-1/simSetLastError_cpp.md)
- [simGetSimulatorMessage](sim-1/simGetSimulatorMessage_cpp.md)
- [simSerialCheck](sim-1/simSerialCheck_cpp.md)
- [simSerialClose](sim-1/simSerialClose_cpp.md)
- [simSerialOpen](sim-1/simSerialOpen_cpp.md)
- [simSerialRead](sim-1/simSerialRead_cpp.md)
- [simSerialSend](sim-1/simSerialSend_cpp.md)
- [simAuxiliaryConsoleClose](sim-1/simAuxiliaryConsoleClose_cpp.md)
- [simAuxiliaryConsoleOpen](sim-1/simAuxiliaryConsoleOpen_cpp.md)
- [simAuxiliaryConsolePrint](sim-1/simAuxiliaryConsolePrint_cpp.md)
- [simCallScriptFunctionEx](sim-1/simCallScriptFunctionEx_cpp.md)
- [simExecuteScriptString](sim-1/simExecuteScriptString_cpp.md)
- [simGetObjectUid](sim-1/simGetObjectUid_cpp.md)
- See also:
- [signal properties](properties.md#signals)

## <a id="textures"></a>Textures

- [`sim.getTextureId`](sim-1/simGetTextureId.md)
- [`sim.getShapeTextureId`](sim-1/simGetShapeTextureId.md)
- [`sim.readTexture`](sim-1/simReadTexture.md)
- [`sim.saveImage`](sim-1/simSaveImage.md)
- [`sim.loadImage`](sim-1/simLoadImage.md)
- [`sim.getScaledImage`](sim-1/simGetScaledImage.md)
- [`sim.transformImage`](sim-1/simTransformImage.md)
- [`sim.writeTexture`](sim-1/simWriteTexture.md)
- [`sim.createTexture`](sim-1/simCreateTexture.md)
- [`sim.setShapeTexture`](sim-1/simSetShapeTexture.md)
- See also:
- [properties](properties.md)

- [simApplyTexture](sim-1/simApplyTexture_cpp.md)
- [simGetTextureId](sim-1/simGetTextureId_cpp.md)
- [simGetShapeTextureId](sim-1/simGetShapeTextureId_cpp.md)
- [simReadTexture](sim-1/simReadTexture_cpp.md)
- [simSaveImage](sim-1/simSaveImage_cpp.md)
- [simLoadImage](sim-1/simLoadImage_cpp.md)
- [simGetScaledImage](sim-1/simGetScaledImage_cpp.md)
- [simTransformImage](sim-1/simTransformImage_cpp.md)
- [simWriteTexture](sim-1/simWriteTexture_cpp.md)
- [simCreateTexture](sim-1/simCreateTexture_cpp.md)
- [simSetShapeTexture](sim-1/simSetShapeTexture_cpp.md)
- See also:
- [properties](properties.md)

## <a id="blockingFunctions"></a>Blocking functions

- [`sim.wait`](sim-1/simWait.md)
- [`sim.moveToConfig`](sim-1/simMoveToConfig.md)
- [`sim.moveToPose`](sim-1/simMoveToPose.md)
- [`sim.serialRead`](sim-1/simSerialRead.md)
- [`sim.systemSemaphore`](sim-1/simSystemSemaphore.md)

## <a id="auxiliaryConsoles"></a><a id="auxiliaryConsoleFunctions"></a>Auxiliary consoles

- [`sim.auxiliaryConsoleClose`](sim-1/simAuxiliaryConsoleClose.md)
- [`sim.auxiliaryConsoleOpen`](sim-1/simAuxiliaryConsoleOpen.md)
- [`sim.auxiliaryConsolePrint`](sim-1/simAuxiliaryConsolePrint.md)
- [`sim.auxiliaryConsoleShow`](sim-1/simAuxiliaryConsoleShow.md)
- See also:
- [Custom user interfaces](customUIPlugin.md)

- [simAuxiliaryConsoleClose](sim-1/simAuxiliaryConsoleClose_cpp.md)
- [simAuxiliaryConsoleOpen](sim-1/simAuxiliaryConsoleOpen_cpp.md)
- [simAuxiliaryConsolePrint](sim-1/simAuxiliaryConsolePrint_cpp.md)
- [simAuxiliaryConsoleShow](sim-1/simAuxiliaryConsoleShow_cpp.md)

## <a id="textEditors"></a>Text/code editors

- [`sim.textEditorClose`](sim-1/simTextEditorClose.md)
- [`sim.textEditorGetInfo`](sim-1/simTextEditorGetInfo.md)
- [`sim.textEditorOpen`](sim-1/simTextEditorOpen.md)
- [`sim.textEditorShow`](sim-1/simTextEditorShow.md)
- See also:
- [Custom user interfaces](customUIPlugin.md)

## <a id="importExport"></a><a id="importExportFunctions"></a>Import/export

- [`sim.importShape`](sim-1/simImportShape.md)
- [`sim.importMesh`](sim-1/simImportMesh.md)
- [`sim.exportMesh`](sim-1/simExportMesh.md)
- [`sim.createTexture`](sim-1/simCreateTexture.md)
- [`sim.loadImage`](sim-1/simLoadImage.md)
- [`sim.saveImage`](sim-1/simSaveImage.md)
- [`sim.generateTextShape`](sim-1/simGenerateTextShape.md)
- See also:
- [Assimp plugin API reference](simAssimp/simAssimp.md)

- [simImportShape](sim-1/simImportShape_cpp.md)
- [simImportMesh](sim-1/simImportMesh_cpp.md)
- [simExportMesh](sim-1/simExportMesh_cpp.md)
- [simCreateTexture](sim-1/simCreateTexture_cpp.md)
- [simLoadImage](sim-1/simLoadImage_cpp.md)
- [simSaveImage](sim-1/simSaveImage_cpp.md)

## <a id="PagesAndViewsFunctions"></a>Pages and views

- [`sim.floatingViewAdd`](sim-1/simFloatingViewAdd.md)
- [`sim.floatingViewRemove`](sim-1/simFloatingViewRemove.md)
- [`sim.adjustView`](sim-1/simAdjustView.md)
- [`sim.cameraFitToView`](sim-1/simCameraFitToView.md)

- [simFloatingViewAdd](sim-1/simFloatingViewAdd_cpp.md)
- [simFloatingViewRemove](sim-1/simFloatingViewRemove_cpp.md)
- [simAdjustView](sim-1/simAdjustView_cpp.md)
- [simCameraFitToView](sim-1/simCameraFitToView_cpp.md)

## <a id="rml"></a><a id="ruckig"></a>Motion functionality

- [`sim.moveToConfig`](sim-1/simMoveToConfig.md)
- [`sim.moveToConfig_init`](sim-1/simMoveToConfig_init.md)
- [`sim.moveToConfig_step`](sim-1/simMoveToConfig_step.md)
- [`sim.moveToConfig_cleanup`](sim-1/simMoveToConfig_cleanup.md)
- [`sim.moveToPose`](sim-1/simMoveToPose.md)
- [`sim.moveToPose_init`](sim-1/simMoveToPose_init.md)
- [`sim.moveToPose_step`](sim-1/simMoveToPose_step.md)
- [`sim.moveToPose_cleanup`](sim-1/simMoveToPose_cleanup.md)
- [`sim.ruckigPos`](sim-1/simRuckigPos.md)
- [`sim.ruckigVel`](sim-1/simRuckigVel.md)
- [`sim.ruckigStep`](sim-1/simRuckigStep.md)
- [`sim.ruckigRemove`](sim-1/simRuckigRemove.md)

- [simRuckigPos](sim-1/simRuckigPos_cpp.md)
- [simRuckigVel](sim-1/simRuckigVel_cpp.md)
- [simRuckigStep](sim-1/simRuckigStep_cpp.md)
- [simRuckigRemove](sim-1/simRuckigRemove_cpp.md)

## <a id="packing"></a>Packing / unpacking

- [`sim.packTable`](sim-1/simPackTable.md)
- [`sim.unpackTable`](sim-1/simUnpackTable.md)
- [`sim.packUInt8Table`](sim-1/simPackUInt8Table.md)
- [`sim.unpackUInt8Table`](sim-1/simUnpackUInt8Table.md)
- [`sim.packUInt16Table`](sim-1/simPackUInt16Table.md)
- [`sim.unpackUInt16Table`](sim-1/simUnpackUInt16Table.md)
- [`sim.packUInt32Table`](sim-1/simPackUInt32Table.md)
- [`sim.unpackUInt32Table`](sim-1/simUnpackUInt32Table.md)
- [`sim.packInt32Table`](sim-1/simPackInt32Table.md)
- [`sim.unpackInt32Table`](sim-1/simUnpackInt32Table.md)
- [`sim.packFloatTable`](sim-1/simPackFloatTable.md)
- [`sim.unpackFloatTable`](sim-1/simUnpackFloatTable.md)
- [`sim.packDoubleTable`](sim-1/simPackDoubleTable.md)
- [`sim.unpackDoubleTable`](sim-1/simUnpackDoubleTable.md)
- [`sim.transformBuffer`](sim-1/simTransformBuffer.md)

- [simPackTable](sim-1/simPackTable_cpp.md)
- [simUnpackTable](sim-1/simUnpackTable_cpp.md)

## <a id="stacks"></a>Stacks

- [`sim.packTable`](sim-1/simPackTable.md)
- [`sim.unpackTable`](sim-1/simUnpackTable.md)

- [simCreateStack](sim-1/simCreateStack_cpp.md)
- [simReleaseStack](sim-1/simReleaseStack_cpp.md)
- [simCopyStack](sim-1/simCopyStack_cpp.md)
- [simPushNullOntoStack](sim-1/simPushNullOntoStack_cpp.md)
- [simPushBoolOntoStack](sim-1/simPushBoolOntoStack_cpp.md)
- [simPushInt32OntoStack](sim-1/simPushInt32OntoStack_cpp.md)
- [simPushInt64OntoStack](sim-1/simPushInt64OntoStack_cpp.md)
- [simPushFloatOntoStack](sim-1/simPushFloatOntoStack_cpp.md)
- [simPushDoubleOntoStack](sim-1/simPushDoubleOntoStack_cpp.md)
- [simPushTextOntoStack](sim-1/simPushTextOntoStack_cpp.md)
- [simPushStringOntoStack](sim-1/simPushStringOntoStack_cpp.md)
- [simPushBufferOntoStack](sim-1/simPushBufferOntoStack_cpp.md)
- [simPushMatrixOntoStack](sim-1/simPushMatrixOntoStack_cpp.md)
- [simPushUInt8TableOntoStack](sim-1/simPushUInt8TableOntoStack_cpp.md)
- [simPushInt32TableOntoStack](sim-1/simPushInt32TableOntoStack_cpp.md)
- [simPushInt64TableOntoStack](sim-1/simPushInt64TableOntoStack_cpp.md)
- [simPushFloatTableOntoStack](sim-1/simPushFloatTableOntoStack_cpp.md)
- [simPushDoubleTableOntoStack](sim-1/simPushDoubleTableOntoStack_cpp.md)
- [simPushTableOntoStack](sim-1/simPushTableOntoStack_cpp.md)
- [simInsertDataIntoStackTable](sim-1/simInsertDataIntoStackTable_cpp.md)
- [simGetStackSize](sim-1/simGetStackSize_cpp.md)
- [simPopStackItem](sim-1/simPopStackItem_cpp.md)
- [simGetStackItemType](sim-1/simGetStackItemType_cpp.md)
- [simGetStackStringType](sim-1/simGetStackStringType_cpp.md)
- [simMoveStackItemToTop](sim-1/simMoveStackItemToTop_cpp.md)
- [simGetStackBoolValue](sim-1/simGetStackBoolValue_cpp.md)
- [simGetStackInt32Value](sim-1/simGetStackInt32Value_cpp.md)
- [simGetStackInt64Value](sim-1/simGetStackInt64Value_cpp.md)
- [simGetStackFloatValue](sim-1/simGetStackFloatValue_cpp.md)
- [simGetStackDoubleValue](sim-1/simGetStackDoubleValue_cpp.md)
- [simGetStackStringValue](sim-1/simGetStackStringValue_cpp.md)
- [simGetStackMatrix](sim-1/simGetStackMatrix_cpp.md)
- [simGetStackTableInfo](sim-1/simGetStackTableInfo_cpp.md)
- [simGetStackUInt8Table](sim-1/simGetStackUInt8Table_cpp.md)
- [simGetStackInt32Table](sim-1/simGetStackInt32Table_cpp.md)
- [simGetStackInt64Table](sim-1/simGetStackInt64Table_cpp.md)
- [simGetStackFloatTable](sim-1/simGetStackFloatTable_cpp.md)
- [simGetStackDoubleTable](sim-1/simGetStackDoubleTable_cpp.md)
- [simUnfoldStackTable](sim-1/simUnfoldStackTable_cpp.md)
- [simDebugStack](sim-1/simDebugStack_cpp.md)
- [simPackTable](sim-1/simPackTable_cpp.md)
- [simUnpackTable](sim-1/simUnpackTable_cpp.md)

## Other commands

- [`sim.addLog`](sim-1/simAddLog.md)
- [`sim.announceSceneContentChange`](sim-1/simAnnounceSceneContentChange.md)
- [`sim.getNavigationMode`](sim-1/simGetNavigationMode.md)
- [`sim.setNavigationMode`](sim-1/simSetNavigationMode.md)
- [`sim.getPage`](sim-1/simGetPage.md)
- [`sim.setPage`](sim-1/simSetPage.md)
- [`sim.getLastInfo`](sim-1/simGetLastInfo.md)
- [`sim.getPluginName`](sim-1/simGetPluginName.md)
- [`sim.getPluginInfo`](sim-1/simGetPluginInfo.md)
- [`sim.setPluginInfo`](sim-1/simSetPluginInfo.md)
- [`sim.getNavigationMode`](sim-1/simGetNavigationMode.md)
- [`sim.getSystemTime`](sim-1/simGetSystemTime.md)
- [`sim.refreshDialogs`](sim-1/simRefreshDialogs.md)
- [`sim.setAutoYieldDelay`](sim-1/simSetAutoYieldDelay.md)
- [`sim.step`](sim-1/simStep.md)
- [`sim.getExplicitHandling`](sim-1/simGetExplicitHandling.md)
- [`sim.setExplicitHandling`](sim-1/simSetExplicitHandling.md)
- [`sim.launchExecutable`](sim-1/simLaunchExecutable.md)
- [`sim.quitSimulator`](sim-1/simQuitSimulator.md)
- [`sim.getExtensionString`](sim-1/simGetExtensionString.md)
- [`sim.textEditorClose`](sim-1/simTextEditorClose.md)
- [`sim.textEditorGetInfo`](sim-1/simTextEditorGetInfo.md)
- [`sim.textEditorOpen`](sim-1/simTextEditorOpen.md)
- [`sim.textEditorShow`](sim-1/simTextEditorShow.md)
- [`sim.getUserVariables`](sim-1/simGetUserVariables.md)
- [`sim.moduleEntry`](sim-1/simModuleEntry.md)
- [`sim.getGenesisEvents`](sim-1/simGetGenesisEvents.md)
- [`sim.pushUserEvent`](sim-1/simPushUserEvent.md)
- [`sim.systemSemaphore`](sim-1/simSystemSemaphore.md)
- [`sim.scheduleExecution`](sim-1/simScheduleExecution.md)
- [`sim.cancelScheduledExecution`](sim-1/simCancelScheduledExecution.md)
- See also:
- [properties](properties.md)

- [simAddLog](sim-1/simAddLog_cpp.md)
- [simAnnounceSceneContentChange](sim-1/simAnnounceSceneContentChange_cpp.md)
- [simGetNavigationMode](sim-1/simGetNavigationMode_cpp.md)
- [simSetNavigationMode](sim-1/simSetNavigationMode_cpp.md)
- [simGetPage](sim-1/simGetPage_cpp.md)
- [simSetPage](sim-1/simSetPage_cpp.md)
- [simGetLastInfo](sim-1/simGetLastInfo_cpp.md)
- [simGetLastError](sim-1/simGetLastError_cpp.md)
- [simSetLastError](sim-1/simSetLastError_cpp.md)
- [simGetPluginName](sim-1/simGetPluginName_cpp.md)
- [simGetPluginInfo](sim-1/simGetPluginInfo_cpp.md)
- [simSetPluginInfo](sim-1/simSetPluginInfo_cpp.md)
- [simGetNavigationMode](sim-1/simGetNavigationMode_cpp.md)
- [simRefreshDialogs](sim-1/simRefreshDialogs_cpp.md)
- [simGetExplicitHandling](sim-1/simGetExplicitHandling_cpp.md)
- [simSetExplicitHandling](sim-1/simSetExplicitHandling_cpp.md)
- [simQuitSimulator](sim-1/simQuitSimulator_cpp.md)
- [simGetExtensionString](sim-1/simGetExtensionString_cpp.md)
- [simOpenTextEditor](sim-1/simOpenTextEditor_cpp.md)
- [simCreateBuffer](sim-1/simCreateBuffer_cpp.md)
- [simReleaseBuffer](sim-1/simReleaseBuffer_cpp.md)
- [simModuleEntry](sim-1/simModuleEntry_cpp.md)
- See also:
- [properties](properties.md)

## <a id="objectParameters"></a>Object parameters

```
See:
properties
```

```cpp
See:
properties
```

## <a id="params"></a>Simulator parameters

```
See:
properties
```

```cpp
See:
properties
```

## <a id="namedParams"></a>Simulator named parameters

```
See:
named parameter properties
```

```cpp
See:
named parameter properties
```

## <a id="engineParameters"></a>Physics engine parameters

```
See:
engine properties
```

```cpp
See:
engine properties
```

## <a id="signals"></a>Signals

```
See:
signal properties
```

```cpp
See:
signal properties
```

## <a id="customData"></a><a id="customDataBlocks"></a><a id="persistentData"></a>Custom data

```
See:
custom data properties
```

```cpp
See:
custom data properties
```
