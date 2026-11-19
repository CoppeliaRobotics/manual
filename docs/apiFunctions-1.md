# Regular API reference (sim-1)

This page lists all constants/enums related to the regular API, version 1 (version 2 can be found [here](apiConstants.md))

## <a id="fileOperations"></a>File operations

- [`sim.closeScene`](sim-1/simCloseScene.htm)
- [`sim.saveScene`](sim-1/simSaveScene.htm)
- [`sim.loadScene`](sim-1/simLoadScene.htm)
- [`sim.saveModel`](sim-1/simSaveModel.htm)
- [`sim.loadModel`](sim-1/simLoadModel.htm)
- [`sim.importShape`](sim-1/simImportShape.htm)
- [`sim.importMesh`](sim-1/simImportMesh.htm)
- [`sim.exportMesh`](sim-1/simExportMesh.htm)
- [`sim.launchExecutable`](sim-1/simLaunchExecutable.htm)
- [`sim.createTexture`](sim-1/simCreateTexture.htm)

- [simCloseScene](sim-1/simCloseScene_cpp.htm)
- [simSaveScene](sim-1/simSaveScene_cpp.htm)
- [simLoadScene](sim-1/simLoadScene_cpp.htm)
- [simSaveModel](sim-1/simSaveModel_cpp.htm)
- [simLoadModel](sim-1/simLoadModel_cpp.htm)
- [simDoesFileExist](sim-1/simDoesFileExist_cpp.htm)
- [simImportShape](sim-1/simImportShape_cpp.htm)
- [simImportMesh](sim-1/simImportMesh_cpp.htm)
- [simExportMesh](sim-1/simExportMesh_cpp.htm)
- [simCreateTexture](sim-1/simCreateTexture_cpp.htm)

## <a id="HandleRetrieval"></a>General object handle retrieval

- [`sim.getObject`](sim-1/simGetObject.htm)
- [`sim.getObjectFromUid`](sim-1/simGetObjectFromUid.htm)
- [`sim.isHandle`](sim-1/simIsHandle.htm)
- [`sim.getObjects`](sim-1/simGetObjects.htm)
- [`sim.getObjectsInTree`](sim-1/simGetObjectsInTree.htm)
- [`sim.getCollectionObjects`](sim-1/simGetCollectionObjects.htm)
- [`sim.setReferencedHandles`](sim-1/simSetReferencedHandles.htm)
- [`sim.getReferencedHandles`](sim-1/simGetReferencedHandles.htm)
- [`sim.getReferencedHandlesTags`](sim-1/simGetReferencedHandlesTags.htm)

- [simGetObject](sim-1/simGetObject_cpp.htm)
- [simGetObjectFromUid](sim-1/simGetObjectFromUid_cpp.htm)
- [simIsHandle](sim-1/simIsHandle_cpp.htm)
- [simGetObjects](sim-1/simGetObjects_cpp.htm)
- [simGetObjectsInTree](sim-1/simGetObjectsInTree_cpp.htm)
- [simGetCollectionObjects](sim-1/simGetCollectionObjects_cpp.htm)
- [simSetReferencedHandles](sim-1/simSetReferencedHandles_cpp.htm)
- [simGetReferencedHandles](sim-1/simGetReferencedHandles_cpp.htm)

## <a id="mainFunctionalityHandling"></a>General functionality handling

- [`sim.handleSimulationScripts`](sim-1/simHandleSimulationScripts.htm)
- [`sim.handleEmbeddedScripts`](sim-1/simHandleEmbeddedScripts.htm)
- [`sim.handleAddOnScripts`](sim-1/simHandleAddOnScripts.htm)
- [`sim.handleSandboxScript`](sim-1/simHandleSandboxScript.htm)

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

- [`sim.handleDynamics`](sim-1/simHandleDynamics.htm)
- [`sim.setJointTargetPosition`](sim-1/simSetJointTargetPosition.htm)
- [`sim.setJointTargetVelocity`](sim-1/simSetJointTargetVelocity.htm)
- [`sim.readForceSensor`](sim-1/simReadForceSensor.htm)
- [`sim.getJointForce`](sim-1/simGetJointForce.htm)
- [`sim.getJointTargetForce`](sim-1/simGetJointTargetForce.htm)
- [`sim.setJointTargetForce`](sim-1/simSetJointTargetForce.htm)
- [`sim.addForce`](sim-1/simAddForce.htm)
- [`sim.addForceAndTorque`](sim-1/simAddForceAndTorque.htm)
- [`sim.getVelocity`](sim-1/simGetVelocity.htm)
- [`sim.getLinkDummy`](sim-1/simGetLinkDummy.htm)
- [`sim.setLinkDummy`](sim-1/simSetLinkDummy.htm)
- [`sim.resetDynamicObject`](sim-1/simResetDynamicObject.htm)
- [`sim.addParticleObject`](sim-1/simAddParticleObject.htm)
- [`sim.addParticleObjectItem`](sim-1/simAddParticleObjectItem.htm)
- [`sim.removeParticleObject`](sim-1/simRemoveParticleObject.htm)
- [`sim.getContactInfo`](sim-1/simGetContactInfo.htm)
- [`sim.getShapeMass`](sim-1/simGetShapeMass.htm)
- [`sim.setShapeMass`](sim-1/simSetShapeMass.htm)
- [`sim.getShapeInertia`](sim-1/simGetShapeInertia.htm)
- [`sim.setShapeInertia`](sim-1/simSetShapeInertia.htm)
- [`sim.computeMassAndInertia`](sim-1/simComputeMassAndInertia.htm)
- [`sim.createForceSensor`](sim-1/simCreateForceSensor.htm)
- [`sim.isDynamicallyEnabled`](sim-1/simIsDynamicallyEnabled.htm)
- See also:
- [properties](properties.md)

- [simHandleDynamics](sim-1/simHandleDynamics_cpp.htm)
- [simSetJointTargetPosition](sim-1/simSetJointTargetPosition_cpp.htm)
- [simSetJointTargetVelocity](sim-1/simSetJointTargetVelocity_cpp.htm)
- [simReadForceSensor](sim-1/simReadForceSensor_cpp.htm)
- [simGetJointForce](sim-1/simGetJointForce_cpp.htm)
- [simGetJointTargetForce](sim-1/simGetJointTargetForce_cpp.htm)
- [simSetJointTargetForce](sim-1/simSetJointTargetForce_cpp.htm)
- [simAddForce](sim-1/simAddForce_cpp.htm)
- [simAddForceAndTorque](sim-1/simAddForceAndTorque_cpp.htm)
- [simGetVelocity](sim-1/simGetVelocity_cpp.htm)
- [simGetLinkDummy](sim-1/simGetLinkDummy_cpp.htm)
- [simSetLinkDummy](sim-1/simSetLinkDummy_cpp.htm)
- [simResetDynamicObject](sim-1/simResetDynamicObject_cpp.htm)
- [simGetContactInfo](sim-1/simGetContactInfo_cpp.htm)
- [simGetShapeMass](sim-1/simGetShapeMass_cpp.htm)
- [simSetShapeMass](sim-1/simSetShapeMass_cpp.htm)
- [simGetShapeInertia](sim-1/simGetShapeInertia_cpp.htm)
- [simSetShapeInertia](sim-1/simSetShapeInertia_cpp.htm)
- [simComputeMassAndInertia](sim-1/simComputeMassAndInertia_cpp.htm)
- [simCreateForceSensor](sim-1/simCreateForceSensor_cpp.htm)
- [simConvexDecompose](sim-1/simConvexDecompose_cpp.htm)
- [simGetQHull](sim-1/simGetQHull_cpp.htm)
- [simGetDecimatedMesh](sim-1/simGetDecimatedMesh_cpp.htm)
- [simIsDynamicallyEnabled](sim-1/simIsDynamicallyEnabled_cpp.htm)
- See also:
- [properties](properties.md)

## <a id="dummyObject"></a>Dummies

- [`sim.createDummy`](sim-1/simCreateDummy.htm)
- [`sim.getLinkDummy`](sim-1/simGetLinkDummy.htm)
- [`sim.setLinkDummy`](sim-1/simSetLinkDummy.htm)
- See also:
- [properties](properties.md)

- [simCreateDummy](sim-1/simCreateDummy_cpp.htm)
- [simGetLinkDummy](sim-1/simGetLinkDummy_cpp.htm)
- [simSetLinkDummy](sim-1/simSetLinkDummy_cpp.htm)
- See also:
- [properties](properties.md)

## <a id="customizingLuaFunctions"></a><a id="customScriptFunctions"></a>Scripts

- [`sim.createScript`](sim-1/simCreateScript.htm)
- [`sim.getScript`](sim-1/simGetScript.htm)
- [`sim.isHandle`](sim-1/simIsHandle.htm)
- [`sim.initScript`](sim-1/simInitScript.htm)
- [`sim.callScriptFunction`](sim-1/simCallScriptFunction.htm)
- [`sim.getScriptFunctions`](sim-1/simGetScriptFunctions.htm)
- [`sim.executeScriptString`](sim-1/simExecuteScriptString.htm)
- [`sim.getApiFunc`](sim-1/simGetApiFunc.htm)
- [`sim.getApiInfo`](sim-1/simGetApiInfo.htm)
- [`sim.handleSimulationScripts`](sim-1/simHandleSimulationScripts.htm)
- [`sim.handleEmbeddedScripts`](sim-1/simHandleEmbeddedScripts.htm)
- [`sim.handleAddOnScripts`](sim-1/simHandleAddOnScripts.htm)
- [`sim.handleSandboxScript`](sim-1/simHandleSandboxScript.htm)
- [`sim.registerScriptFuncHook`](sim-1/simRegisterScriptFuncHook.htm)
- [`sim.getStackTraceback`](sim-1/simGetStackTraceback.htm)
- [`sim.setEventFilters`](sim-1/simSetEventFilters.htm)
- See also:
- [properties](properties.md)

- [simCreateScript](sim-1/simCreateScript_cpp.htm)
- [simGetScriptHandleEx](sim-1/simGetScriptHandleEx_cpp.htm)
- [simIsHandle](sim-1/simIsHandle_cpp.htm)
- [simInitScript](sim-1/simInitScript_cpp.htm)
- [simCallScriptFunctionEx](sim-1/simCallScriptFunctionEx_cpp.htm)
- [simExecuteScriptString](sim-1/simExecuteScriptString_cpp.htm)
- [simGetApiFunc](sim-1/simGetApiFunc_cpp.htm)
- [simGetApiInfo](sim-1/simGetApiInfo_cpp.htm)
- [simResetScript](sim-1/simResetScript_cpp.htm)
- [simRegisterScriptCallbackFunction](sim-1/simRegisterScriptCallbackFunction_cpp.htm)
- [simRegisterScriptVariable](sim-1/simRegisterScriptVariable_cpp.htm)
- [simRegisterScriptFuncHook](sim-1/simRegisterScriptFuncHook_cpp.htm)
- See also:
- [properties](properties.md)

## <a id="jointObject"></a>Joints

- [`sim.setJointPosition`](sim-1/simSetJointPosition.htm)
- [`sim.getJointPosition`](sim-1/simGetJointPosition.htm)
- [`sim.setJointTargetPosition`](sim-1/simSetJointTargetPosition.htm)
- [`sim.getJointTargetPosition`](sim-1/simGetJointTargetPosition.htm)
- [`sim.setJointTargetVelocity`](sim-1/simSetJointTargetVelocity.htm)
- [`sim.getJointTargetVelocity`](sim-1/simGetJointTargetVelocity.htm)
- [`sim.getJointVelocity`](sim-1/simGetJointVelocity.htm)
- [`sim.getObjectChildPose`](sim-1/simGetObjectChildPose.htm)
- [`sim.setObjectChildPose`](sim-1/simSetObjectChildPose.htm)
- [`sim.setJointInterval`](sim-1/simSetJointInterval.htm)
- [`sim.getJointInterval`](sim-1/simGetJointInterval.htm)
- [`sim.getJointType`](sim-1/simGetJointType.htm)
- [`sim.createJoint`](sim-1/simCreateJoint.htm)
- [`sim.setJointMode`](sim-1/simSetJointMode.htm)
- [`sim.getJointMode`](sim-1/simGetJointMode.htm)
- [`sim.setJointDependency`](sim-1/simSetJointDependency.htm)
- [`sim.getJointDependency`](sim-1/simGetJointDependency.htm)
- [`sim.getJointForce`](sim-1/simGetJointForce.htm)
- [`sim.getJointTargetForce`](sim-1/simGetJointTargetForce.htm)
- [`sim.setJointTargetForce`](sim-1/simSetJointTargetForce.htm)
- See also:
- [properties](properties.md)

- [simSetJointPosition](sim-1/simSetJointPosition_cpp.htm)
- [simGetJointPosition](sim-1/simGetJointPosition_cpp.htm)
- [simSetJointTargetPosition](sim-1/simSetJointTargetPosition_cpp.htm)
- [simGetJointTargetPosition](sim-1/simGetJointTargetPosition_cpp.htm)
- [simSetJointTargetVelocity](sim-1/simSetJointTargetVelocity_cpp.htm)
- [simGetJointTargetVelocity](sim-1/simGetJointTargetVelocity_cpp.htm)
- [simGetJointVelocity](sim-1/simGetJointVelocity_cpp.htm)
- [simGetObjectChildPose](sim-1/simGetObjectChildPose_cpp.htm)
- [simSetObjectChildPose](sim-1/simSetObjectChildPose_cpp.htm)
- [simSetJointInterval](sim-1/simSetJointInterval_cpp.htm)
- [simGetJointInterval](sim-1/simGetJointInterval_cpp.htm)
- [simGetJointType](sim-1/simGetJointType_cpp.htm)
- [simCreateJoint](sim-1/simCreateJoint_cpp.htm)
- [simSetJointMode](sim-1/simSetJointMode_cpp.htm)
- [simGetJointMode](sim-1/simGetJointMode_cpp.htm)
- [simSetJointDependency](sim-1/simSetJointDependency_cpp.htm)
- [simGetJointDependency](sim-1/simGetJointDependency_cpp.htm)
- [simGetJointForce](sim-1/simGetJointForce_cpp.htm)
- [simGetJointTargetForce](sim-1/simGetJointTargetForce_cpp.htm)
- [simSetJointTargetForce](sim-1/simsetJointTargetForce_cpp.htm)
- See also:
- [properties](properties.md)

## <a id="shapeObject"></a>Shapes

- [`sim.addForce`](sim-1/simAddForce.htm)
- [`sim.addForceAndTorque`](sim-1/simAddForceAndTorque.htm)
- [`sim.getVelocity`](sim-1/simGetVelocity.htm)
- [`sim.getShapeColor`](sim-1/simGetShapeColor.htm)
- [`sim.setShapeColor`](sim-1/simSetShapeColor.htm)
- [`sim.getShapeTextureId`](sim-1/simGetShapeTextureId.htm)
- [`sim.setShapeTexture`](sim-1/simSetShapeTexture.htm)
- [`sim.createShape`](sim-1/simCreateShape.htm)
- [`sim.createPrimitiveShape`](sim-1/simCreatePrimitiveShape.htm)
- [`sim.createHeightfieldShape`](sim-1/simCreateHeightfieldShape.htm)
- [`sim.getShapeMesh`](sim-1/simGetShapeMesh.htm)
- [`sim.getShapeViz`](sim-1/simGetShapeViz.htm)
- [`sim.getShapeGeomInfo`](sim-1/simGetShapeGeomInfo.htm)
- [`sim.getShapeMass`](sim-1/simGetShapeMass.htm)
- [`sim.setShapeMass`](sim-1/simSetShapeMass.htm)
- [`sim.getShapeInertia`](sim-1/simGetShapeInertia.htm)
- [`sim.setShapeInertia`](sim-1/simSetShapeInertia.htm)
- [`sim.computeMassAndInertia`](sim-1/simComputeMassAndInertia.htm)
- [`sim.groupShapes`](sim-1/simGroupShapes.htm)
- [`sim.ungroupShape`](sim-1/simUngroupShape.htm)
- [`sim.importShape`](sim-1/simImportShape.htm)
- [`sim.alignShapeBB`](sim-1/simAlignShapeBB.htm)
- [`sim.relocateShapeFrame`](sim-1/simRelocateShapeFrame.htm)
- [`sim.getShapeBB`](sim-1/simGetShapeBB.htm)
- [`sim.setShapeBB`](sim-1/simSetShapeBB.htm)
- [`sim.getExtensionString`](sim-1/simGetExtensionString.htm)
- [`sim.generateTextShape`](sim-1/simGenerateTextShape.htm)
- See also:
- [properties](properties.md)

- [simAddForce](sim-1/simAddForce_cpp.htm)
- [simAddForceAndTorque](sim-1/simAddForceAndTorque_cpp.htm)
- [simGetVelocity](sim-1/simGetVelocity_cpp.htm)
- [simGetShapeColor](sim-1/simGetShapeColor_cpp.htm)
- [simSetShapeColor](sim-1/simSetShapeColor_cpp.htm)
- [simGetShapeTextureId](sim-1/simGetShapeTextureId_cpp.htm)
- [simSetShapeTexture](sim-1/simSetShapeTexture_cpp.htm)
- [simCreateShape](sim-1/simCreateShape_cpp.htm)
- [simCreatePrimitiveShape](sim-1/simCreatePrimitiveShape_cpp.htm)
- [simCreateHeightfieldShape](sim-1/simCreateHeightfieldShape_cpp.htm)
- [simGetShapeMesh](sim-1/simGetShapeMesh_cpp.htm)
- [simGetShapeViz](sim-1/simGetShapeViz_cpp.htm)
- [simApplyTexture](sim-1/simApplyTexture_cpp.htm)
- [simGetShapeGeomInfo](sim-1/simGetShapeGeomInfo_cpp.htm)
- [simGetShapeMass](sim-1/simGetShapeMass_cpp.htm)
- [simSetShapeMass](sim-1/simSetShapeMass_cpp.htm)
- [simGetShapeInertia](sim-1/simGetShapeInertia_cpp.htm)
- [simSetShapeInertia](sim-1/simSetShapeInertia_cpp.htm)
- [simComputeMassAndInertia](sim-1/simComputeMassAndInertia_cpp.htm)
- [simGroupShapes](sim-1/simGroupShapes_cpp.htm)
- [simUngroupShape](sim-1/simUngroupShape_cpp.htm)
- [simImportShape](sim-1/simImportShape_cpp.htm)
- [simConvexDecompose](sim-1/simConvexDecompose_cpp.htm)
- [simGetQHull](sim-1/simGetQHull_cpp.htm)
- [simGetDecimatedMesh](sim-1/simGetDecimatedMesh_cpp.htm)
- [simAlignShapeBB](sim-1/simAlignShapeBB_cpp.htm)
- [simRelocateShapeFrame](sim-1/simRelocateShapeFrame_cpp.htm)
- [simGetExtensionString](sim-1/simGetExtensionString_cpp.htm)
- See also:
- [properties](properties.md)

## <a id="proximitySensor"></a>Proximity sensors

- [`sim.handleProximitySensor`](sim-1/simHandleProximitySensor.htm)
- [`sim.readProximitySensor`](sim-1/simReadProximitySensor.htm)
- [`sim.resetProximitySensor`](sim-1/simResetProximitySensor.htm)
- [`sim.checkProximitySensor`](sim-1/simCheckProximitySensor.htm)
- [`sim.createProximitySensor`](sim-1/simCreateProximitySensor.htm)
- See also:
- [properties](properties.md)

- [simHandleProximitySensor](sim-1/simHandleProximitySensor_cpp.htm)
- [simReadProximitySensor](sim-1/simReadProximitySensor_cpp.htm)
- [simResetProximitySensor](sim-1/simResetProximitySensor_cpp.htm)
- [simCheckProximitySensor](sim-1/simCheckProximitySensor_cpp.htm)
- [simCreateProximitySensor](sim-1/simCreateProximitySensor_cpp.htm)
- See also:
- [properties](properties.md)

## <a id="visionSensor"></a>Vision sensors

- [`sim.handleVisionSensor`](sim-1/simHandleVisionSensor.htm)
- [`sim.readVisionSensor`](sim-1/simReadVisionSensor.htm)
- [`sim.resetVisionSensor`](sim-1/simResetVisionSensor.htm)
- [`sim.checkVisionSensor`](sim-1/simCheckVisionSensor.htm)
- [`sim.checkVisionSensorEx`](sim-1/simCheckVisionSensorEx.htm)
- [`sim.getVisionSensorDepth`](sim-1/simGetVisionSensorDepth.htm)
- [`sim.getVisionSensorImg`](sim-1/simGetVisionSensorImg.htm)
- [`sim.setVisionSensorImg`](sim-1/simSetVisionSensorImg.htm)
- [`sim.getVisionSensorRes`](sim-1/simGetVisionSensorRes.htm)
- [`sim.adjustView`](sim-1/simAdjustView.htm)
- [`sim.createVisionSensor`](sim-1/simCreateVisionSensor.htm)
- [`sim.getExtensionString`](sim-1/simGetExtensionString.htm)
- See also:
- [properties](properties.md)

- [simHandleVisionSensor](sim-1/simHandleVisionSensor_cpp.htm)
- [simReadVisionSensor](sim-1/simReadVisionSensor_cpp.htm)
- [simResetVisionSensor](sim-1/simResetVisionSensor_cpp.htm)
- [simCheckVisionSensor](sim-1/simCheckVisionSensor_cpp.htm)
- [simCheckVisionSensorEx](sim-1/simCheckVisionSensorEx_cpp.htm)
- [simGetVisionSensorDepth](sim-1/simGetVisionSensorDepth_cpp.htm)
- [simGetVisionSensorImg](sim-1/simGetVisionSensorImg_cpp.htm)
- [simSetVisionSensorImg](sim-1/simSetVisionSensorImg_cpp.htm)
- [simGetVisionSensorRes](sim-1/simGetVisionSensorRes_cpp.htm)
- [simAdjustView](sim-1/simAdjustView_cpp.htm)
- [simCreateVisionSensor](sim-1/simCreateVisionSensor_cpp.htm)
- [simGetExtensionString](sim-1/simGetExtensionString_cpp.htm)
- See also:
- [properties](properties.md)

## <a id="forceSensor"></a>Force sensors

- [`sim.readForceSensor`](sim-1/simReadForceSensor.htm)
- [`sim.createForceSensor`](sim-1/simCreateForceSensor.htm)
- See also:
- [properties](properties.md)

- [simReadForceSensor](sim-1/simReadForceSensor_cpp.htm)
- [simCreateForceSensor](sim-1/simCreateForceSensor_cpp.htm)
- See also:
- [properties](properties.md)

## <a id="graphs"></a>Graphs

- [`sim.addGraphStream`](sim-1/simAddGraphStream.htm)
- [`sim.setGraphStreamTransformation`](sim-1/simSetGraphStreamTransformation.htm)
- [`sim.setGraphStreamValue`](sim-1/simSetGraphStreamValue.htm)
- [`sim.addGraphCurve`](sim-1/simAddGraphCurve.htm)
- [`sim.destroyGraphCurve`](sim-1/simDestroyGraphCurve.htm)
- [`sim.duplicateGraphCurveToStatic`](sim-1/simDuplicateGraphCurveToStatic.htm)
- [`sim.handleGraph`](sim-1/simHandleGraph.htm)
- [`sim.resetGraph`](sim-1/simResetGraph.htm)
- See also:
- [properties](properties.md)

- [simAddGraphStream](sim-1/simAddGraphStream_cpp.htm)
- [simSetGraphStreamTransformation](sim-1/simSetGraphStreamTransformation_cpp.htm)
- [simSetGraphStreamValue](sim-1/simSetGraphStreamValue_cpp.htm)
- [simAddGraphCurve](sim-1/simAddGraphCurve_cpp.htm)
- [simDestroyGraphCurve](sim-1/simDestroyGraphCurve_cpp.htm)
- [simDuplicateGraphCurveToStatic](sim-1/simDuplicateGraphCurveToStatic_cpp.htm)
- [simHandleGraph](sim-1/simHandleGraph_cpp.htm)
- [simResetGraph](sim-1/simResetGraph_cpp.htm)
- See also:
- [properties](properties.md)

## <a id="lightObject"></a>Lights

- [`sim.getExtensionString`](sim-1/simGetExtensionString.htm)
- See also:
- [properties](properties.md)

- [simGetExtensionString](sim-1/simGetExtensionString_cpp.htm)
- See also:
- [properties](properties.md)

## <a id="cameraObject"></a>Cameras

- [`sim.cameraFitToView`](sim-1/simCameraFitToView.htm)
- [`sim.adjustView`](sim-1/simAdjustView.htm)
- [`sim.getExtensionString`](sim-1/simGetExtensionString.htm)
- See also:
- [properties](properties.md)

- [simCameraFitToView](sim-1/simCameraFitToView_cpp.htm)
- [simAdjustView](sim-1/simAdjustView_cpp.htm)
- [simGetExtensionString](sim-1/simGetExtensionString_cpp.htm)
- See also:
- [properties](properties.md)

## <a id="octree"></a>OC trees

- [`sim.createOctree`](sim-1/simCreateOctree.htm)
- [`sim.insertVoxelsIntoOctree`](sim-1/simInsertVoxelsIntoOctree.htm)
- [`sim.removeVoxelsFromOctree`](sim-1/simRemoveVoxelsFromOctree.htm)
- [`sim.insertObjectIntoOctree`](sim-1/simInsertObjectIntoOctree.htm)
- [`sim.subtractObjectFromOctree`](sim-1/simSubtractObjectFromOctree.htm)
- [`sim.getOctreeVoxels`](sim-1/simGetOctreeVoxels.htm)
- [`sim.checkOctreePointOccupancy`](sim-1/simCheckOctreePointOccupancy.htm)
- See also:
- [properties](properties.md)

- [simCreateOctree](sim-1/simCreateOctree_cpp.htm)
- [simInsertVoxelsIntoOctree](sim-1/simInsertVoxelsIntoOctree_cpp.htm)
- [simRemoveVoxelsFromOctree](sim-1/simRemoveVoxelsFromOctree_cpp.htm)
- [simInsertObjectIntoOctree](sim-1/simInsertObjectIntoOctree_cpp.htm)
- [simSubtractObjectFromOctree](sim-1/simSubtractObjectFromOctree_cpp.htm)
- [simGetOctreeVoxels](sim-1/simGetOctreeVoxels_cpp.htm)
- [simCheckOctreePointOccupancy](sim-1/simCheckOctreePointOccupancy_cpp.htm)
- See also:
- [properties](properties.md)

## <a id="pointCloud"></a>Point clouds

- [`sim.createPointCloud`](sim-1/simCreatePointCloud.htm)
- [`sim.getPointCloudOptions`](sim-1/simGetPointCloudOptions.htm)
- [`sim.setPointCloudOptions`](sim-1/simSetPointCloudOptions.htm)
- [`sim.insertPointsIntoPointCloud`](sim-1/simInsertPointsIntoPointCloud.htm)
- [`sim.removePointsFromPointCloud`](sim-1/simRemovePointsFromPointCloud.htm)
- [`sim.subtractObjectFromPointCloud`](sim-1/simSubtractObjectFromPointCloud.htm)
- [`sim.intersectPointsWithPointCloud`](sim-1/simIntersectPointsWithPointCloud.htm)
- [`sim.insertObjectIntoPointCloud`](sim-1/simInsertObjectIntoPointCloud.htm)
- [`sim.getPointCloudPoints`](sim-1/simGetPointCloudPoints.htm)
- See also:
- [properties](properties.md)

- [simCreatePointCloud](sim-1/simCreatePointCloud_cpp.htm)
- [simGetPointCloudOptions](sim-1/simGetPointCloudOptions_cpp.htm)
- [simSetPointCloudOptions](sim-1/simSetPointCloudOptions_cpp.htm)
- [simInsertPointsIntoPointCloud](sim-1/simInsertPointsIntoPointCloud_cpp.htm)
- [simRemovePointsFromPointCloud](sim-1/simRemovePointsFromPointCloud_cpp.htm)
- [simSubtractObjectFromPointCloud](sim-1/simSubtractObjectFromPointCloud_cpp.htm)
- [simIntersectPointsWithPointCloud](sim-1/simIntersectPointsWithPointCloud_cpp.htm)
- [simInsertObjectIntoPointCloud](sim-1/simInsertObjectIntoPointCloud_cpp.htm)
- [simGetPointCloudPoints](sim-1/simGetPointCloudPoints_cpp.htm)
- See also:
- [properties](properties.md)

## <a id="paths"></a>Paths

- [`sim.createPath`](sim-1/simCreatePath.htm)
- [`sim.getConfigDistance`](sim-1/simGetConfigDistance.htm)
- [`sim.getPathLengths`](sim-1/simGetPathLengths.htm)
- [`sim.getPathInterpolatedConfig`](sim-1/simGetPathInterpolatedConfig.htm)
- [`sim.resamplePath`](sim-1/simResamplePath.htm)
- [`sim.generateTimeOptimalTrajectory`](sim-1/simGenerateTimeOptimalTrajectory.htm)
- [`sim.generateShapeFromPath`](sim-1/simGenerateShapeFromPath.htm)
- [`sim.getClosestPosOnPath`](sim-1/simGetClosestPosOnPath.htm)

- [simGenerateShapeFromPath](sim-1/simGenerateShapeFromPath_cpp.htm)
- [simGetClosestPosOnPath](sim-1/simGetClosestPosOnPath_cpp.htm)

## <a id="sceneObjectFunctionality"></a>Scene objects

- [`sim.getObject`](sim-1/simGetObject.htm)
- [`sim.getObjectUid`](sim-1/simGetObjectUid.htm)
- [`sim.isHandle`](sim-1/simIsHandle.htm)
- [`sim.removeObjects`](sim-1/simRemoveObjects.htm)
- [`sim.removeModel`](sim-1/simRemoveModel.htm)
- [`sim.getObjectAlias`](sim-1/simGetObjectAlias.htm)
- [`sim.setObjectAlias`](sim-1/simSetObjectAlias.htm)
- [`sim.getObjects`](sim-1/simGetObjects.htm)
- [`sim.getObjectsInTree`](sim-1/simGetObjectsInTree.htm)
- [`sim.getObjectParent`](sim-1/simGetObjectParent.htm)
- [`sim.setObjectParent`](sim-1/simSetObjectParent.htm)
- [`sim.getObjectHierarchyOrder`](sim-1/simGetObjectHierarchyOrder.htm)
- [`sim.setObjectHierarchyOrder`](sim-1/simSetObjectHierarchyOrder.htm)
- [`sim.getObjectChild`](sim-1/simGetObjectChild.htm)
- [`sim.getObjectMatrix`](sim-1/simGetObjectMatrix.htm)
- [`sim.setObjectMatrix`](sim-1/simSetObjectMatrix.htm)
- [`sim.getObjectPose`](sim-1/simGetObjectPose.htm)
- [`sim.setObjectPose`](sim-1/simSetObjectPose.htm)
- [`sim.getObjectPosition`](sim-1/simGetObjectPosition.htm)
- [`sim.setObjectPosition`](sim-1/simSetObjectPosition.htm)
- [`sim.getObjectOrientation`](sim-1/simGetObjectOrientation.htm)
- [`sim.setObjectOrientation`](sim-1/simSetObjectOrientation.htm)
- [`sim.getObjectQuaternion`](sim-1/simGetObjectQuaternion.htm)
- [`sim.setObjectQuaternion`](sim-1/simSetObjectQuaternion.htm)
- [`sim.getObjectType`](sim-1/simGetObjectType.htm)
- [`sim.getObjectSel`](sim-1/simGetObjectSel.htm)
- [`sim.setObjectSel`](sim-1/simSetObjectSel.htm)
- [`sim.getObjectSizeFactor`](sim-1/simGetObjectSizeFactor.htm)
- [`sim.copyPasteObjects`](sim-1/simCopyPasteObjects.htm)
- [`sim.scaleObject`](sim-1/simScaleObject.htm)
- [`sim.scaleObjects`](sim-1/simScaleObjects.htm)
- [`sim.getObjectVelocity`](sim-1/simGetObjectVelocity.htm)
- [`sim.setReferencedHandles`](sim-1/simSetReferencedHandles.htm)
- [`sim.getReferencedHandles`](sim-1/simGetReferencedHandles.htm)
- [`sim.getReferencedHandlesTags`](sim-1/simGetReferencedHandlesTags.htm)
- [`sim.isDynamicallyEnabled`](sim-1/simIsDynamicallyEnabled.htm)
- [`sim.getObjectColor`](sim-1/simGetObjectColor.htm)
- [`sim.setObjectColor`](sim-1/simSetObjectColor.htm)
- See also:
- [properties](properties.md)

- [simGetObject](sim-1/simGetObject_cpp.htm)
- [simGetObjectUid](sim-1/simGetObjectUid_cpp.htm)
- [simIsHandle](sim-1/simIsHandle_cpp.htm)
- [simRemoveObjects](sim-1/simRemoveObjects_cpp.htm)
- [simRemoveModel](sim-1/simRemoveModel_cpp.htm)
- [simGetObjectAlias](sim-1/simGetObjectAlias_cpp.htm)
- [simSetObjectAlias](sim-1/simSetObjectAlias_cpp.htm)
- [simGetObjects](sim-1/simGetObjects_cpp.htm)
- [simGetObjectsInTree](sim-1/simGetObjectsInTree_cpp.htm)
- [simGetObjectParent](sim-1/simGetObjectParent_cpp.htm)
- [simSetObjectParent](sim-1/simSetObjectParent_cpp.htm)
- [simGetObjectHierarchyOrder](sim-1/simGetObjectHierarchyOrder_cpp.htm)
- [simSetObjectHierarchyOrder](sim-1/simSetObjectHierarchyOrder_cpp.htm)
- [simGetObjectChild](sim-1/simGetObjectChild_cpp.htm)
- [simGetObjectMatrix](sim-1/simGetObjectMatrix_cpp.htm)
- [simSetObjectMatrix](sim-1/simSetObjectMatrix_cpp.htm)
- [simGetObjectPose](sim-1/simGetObjectPose_cpp.htm)
- [simSetObjectPose](sim-1/simSetObjectPose_cpp.htm)
- [simGetObjectPosition](sim-1/simGetObjectPosition_cpp.htm)
- [simSetObjectPosition](sim-1/simSetObjectPosition_cpp.htm)
- [simGetObjectOrientation](sim-1/simGetObjectOrientation_cpp.htm)
- [simSetObjectOrientation](sim-1/simSetObjectOrientation_cpp.htm)
- [simGetObjectQuaternion](sim-1/simGetObjectQuaternion_cpp.htm)
- [simSetObjectQuaternion](sim-1/simSetObjectQuaternion_cpp.htm)
- [simGetObjectType](sim-1/simGetObjectType_cpp.htm)
- [simGetObjectSel](sim-1/simGetObjectSel_cpp.htm)
- [simSetObjectSel](sim-1/simSetObjectSel_cpp.htm)
- [simGetObjectSizeFactor](sim-1/simGetObjectSizeFactor_cpp.htm)
- [simCopyPasteObjects](sim-1/simCopyPasteObjects_cpp.htm)
- [simScaleObject](sim-1/simScaleObject_cpp.htm)
- [simScaleObjects](sim-1/simScaleObjects_cpp.htm)
- [simGetObjectVelocity](sim-1/simGetObjectVelocity_cpp.htm)
- [simSetReferencedHandles](sim-1/simSetReferencedHandles_cpp.htm)
- [simGetReferencedHandles](sim-1/simGetReferencedHandles_cpp.htm)
- [simIsDynamicallyEnabled](sim-1/simIsDynamicallyEnabled_cpp.htm)
- [simGetObjectColor](sim-1/simGetObjectColor_cpp.htm)
- [simSetObjectColor](sim-1/simSetObjectColor_cpp.htm)
- See also:
- [properties](properties.md)

## <a id="properties"></a>Properties

- [`sim.setBoolProperty`](sim-1/simSetBoolProperty.htm)
- [`sim.getBoolProperty`](sim-1/simGetBoolProperty.htm)
- [`sim.setIntProperty`](sim-1/simSetIntProperty.htm)
- [`sim.getIntProperty`](sim-1/simGetIntProperty.htm)
- [`sim.setLongProperty`](sim-1/simSetLongProperty.htm)
- [`sim.getLongProperty`](sim-1/simGetLongProperty.htm)
- [`sim.setFloatProperty`](sim-1/simSetFloatProperty.htm)
- [`sim.getFloatProperty`](sim-1/simGetFloatProperty.htm)
- [`sim.setStringProperty`](sim-1/simSetStringProperty.htm)
- [`sim.getStringProperty`](sim-1/simGetStringProperty.htm)
- [`sim.setBufferProperty`](sim-1/simSetBufferProperty.htm)
- [`sim.getBufferProperty`](sim-1/simGetBufferProperty.htm)
- [`sim.setIntArrayProperty`](sim-1/simSetIntArrayProperty.htm)
- [`sim.getIntArrayProperty`](sim-1/simGetIntArrayProperty.htm)
- [`sim.setIntArray2Property`](sim-1/simSetIntArray2Property.htm)
- [`sim.getIntArray2Property`](sim-1/simGetIntArray2Property.htm)
- [`sim.setFloatArrayProperty`](sim-1/simSetFloatArrayProperty.htm)
- [`sim.getFloatArrayProperty`](sim-1/simGetFloatArrayProperty.htm)
- [`sim.setVector2Property`](sim-1/simSetVector2Property.htm)
- [`sim.getVector2Property`](sim-1/simGetVector2Property.htm)
- [`sim.setVector3Property`](sim-1/simSetVector3Property.htm)
- [`sim.getVector3Property`](sim-1/simGetVector3Property.htm)
- [`sim.setQuaternionProperty`](sim-1/simSetQuaternionProperty.htm)
- [`sim.getQuaternionProperty`](sim-1/simGetQuaternionProperty.htm)
- [`sim.setPoseProperty`](sim-1/simSetPoseProperty.htm)
- [`sim.getPoseProperty`](sim-1/simGetPoseProperty.htm)
- [`sim.setColorProperty`](sim-1/simSetColorProperty.htm)
- [`sim.getColorProperty`](sim-1/simGetColorProperty.htm)
- [`sim.removeProperty`](sim-1/simRemoveProperty.htm)
- [`sim.getPropertyName`](sim-1/simGetPropertyName.htm)
- [`sim.getPropertyInfo`](sim-1/simGetPropertyInfo.htm)
- [`sim.getProperty`](sim-1/simGetProperty.htm)
- [`sim.setProperty`](sim-1/simSetProperty.htm)
- [`sim.getProperties`](sim-1/simGetProperties.htm)
- [`sim.setProperties`](sim-1/simSetProperties.htm)
- [`sim.getPropertiesInfos`](sim-1/simGetPropertiesInfos.htm)
- See also:
- [packing/unpacking functions](#packing)
- [properties](properties.md)

- [simSetBoolProperty](sim-1/simSetBoolProperty_cpp.htm)
- [simGetBoolProperty](sim-1/simGetBoolProperty_cpp.htm)
- [simSetIntProperty](sim-1/simSetIntProperty_cpp.htm)
- [simGetIntProperty](sim-1/simGetIntProperty_cpp.htm)
- [simSetLongProperty](sim-1/simSetLongProperty_cpp.htm)
- [simGetLongProperty](sim-1/simGetLongProperty_cpp.htm)
- [simSetFloatProperty](sim-1/simSetFloatProperty_cpp.htm)
- [simGetFloatProperty](sim-1/simGetFloatProperty_cpp.htm)
- [simSetStringProperty](sim-1/simSetStringProperty_cpp.htm)
- [simGetStringProperty](sim-1/simGetStringProperty_cpp.htm)
- [simSetBufferProperty](sim-1/simSetBufferProperty_cpp.htm)
- [simGetBufferProperty](sim-1/simGetBufferProperty_cpp.htm)
- [simSetIntArrayProperty](sim-1/simSetIntArrayProperty_cpp.htm)
- [simGetIntArrayProperty](sim-1/simGetIntArrayProperty_cpp.htm)
- [simSetIntArray2Property](sim-1/simSetIntArray2Property_cpp.htm)
- [simGetIntArray2Property](sim-1/simGetIntArray2Property_cpp.htm)
- [simSetFloatArrayProperty](sim-1/simSetFloatArrayProperty_cpp.htm)
- [simGetFloatArrayProperty](sim-1/simGetFloatArrayProperty_cpp.htm)
- [simSetVector2Property](sim-1/simSetVector2Property_cpp.htm)
- [simGetVector2Property](sim-1/simGetVector2Property_cpp.htm)
- [simSetVector3Property](sim-1/simSetVector3Property_cpp.htm)
- [simGetVector3Property](sim-1/simGetVector3Property_cpp.htm)
- [simSetQuaternionProperty](sim-1/simSetQuaternionProperty_cpp.htm)
- [simGetQuaternionProperty](sim-1/simGetQuaternionProperty_cpp.htm)
- [simSetPoseProperty](sim-1/simSetPoseProperty_cpp.htm)
- [simGetPoseProperty](sim-1/simGetPoseProperty_cpp.htm)
- [simSetColorProperty](sim-1/simSetColorProperty_cpp.htm)
- [simGetColorProperty](sim-1/simGetColorProperty_cpp.htm)
- [simRemoveProperty](sim-1/simRemoveProperty_cpp.htm)
- [simGetPropertyName](sim-1/simGetPropertyName_cpp.htm)
- [simGetPropertyInfo](sim-1/simGetPropertyInfo_cpp.htm)
- See also:
- [properties](properties.md)

## <a id="collections"></a>Collections

- [`sim.createCollection`](sim-1/simCreateCollection.htm)
- [`sim.destroyCollection`](sim-1/simDestroyCollection.htm)
- [`sim.addItemToCollection`](sim-1/simAddItemToCollection.htm)
- [`sim.getCollectionObjects`](sim-1/simGetCollectionObjects.htm)

- [simCreateCollectionEx](sim-1/simCreateCollection_cpp.htm)
- [simDestroyCollection](sim-1/simDestroyCollection_cpp.htm)
- [simAddItemToCollection](sim-1/simAddItemToCollection_cpp.htm)
- [simGetCollectionObjects](sim-1/simGetCollectionObjects_cpp.htm)

## <a id="serialCommunicationFunctionality"></a><a id="serialPort"></a>Serial port

- [`sim.serialCheck`](sim-1/simSerialCheck.htm)
- [`sim.serialClose`](sim-1/simSerialClose.htm)
- [`sim.serialOpen`](sim-1/simSerialOpen.htm)
- [`sim.serialRead`](sim-1/simSerialRead.htm)
- [`sim.serialSend`](sim-1/simSerialSend.htm)

- [simSerialCheck](sim-1/simSerialCheck_cpp.htm)
- [simSerialClose](sim-1/simSerialClose_cpp.htm)
- [simSerialOpen](sim-1/simSerialOpen_cpp.htm)
- [simSerialRead](sim-1/simSerialRead_cpp.htm)
- [simSerialSend](sim-1/simSerialSend_cpp.htm)

## <a id="serialCommunicationFunctionality-2"></a><a id="serialPort-2"></a>Serial port

- [`sim.serialCheck`](sim-1/simSerialCheck.htm)
- [`sim.serialClose`](sim-1/simSerialClose.htm)
- [`sim.serialOpen`](sim-1/simSerialOpen.htm)
- [`sim.serialRead`](sim-1/simSerialRead.htm)
- [`sim.serialSend`](sim-1/simSerialSend.htm)

- [simSerialCheck](sim-1/simSerialCheck_cpp.htm)
- [simSerialClose](sim-1/simSerialClose_cpp.htm)
- [simSerialOpen](sim-1/simSerialOpen_cpp.htm)
- [simSerialRead](sim-1/simSerialRead_cpp.htm)
- [simSerialSend](sim-1/simSerialSend_cpp.htm)

## <a id="drawingObject"></a><a id="rendering"></a>Rendering

- [`sim.addDrawingObject`](sim-1/simAddDrawingObject.htm)
- [`sim.addDrawingObjectItem`](sim-1/simAddDrawingObjectItem.htm)
- [`sim.removeDrawingObject`](sim-1/simRemoveDrawingObject.htm)
- [`sim.getShapeColor`](sim-1/simGetShapeColor.htm)
- [`sim.setShapeColor`](sim-1/simSetShapeColor.htm)
- [`sim.getObjectColor`](sim-1/simGetObjectColor.htm)
- [`sim.setObjectColor`](sim-1/simSetObjectColor.htm)
- [`sim.changeEntityColor`](sim-1/simChangeEntityColor.htm)
- [`sim.restoreEntityColor`](sim-1/simRestoreEntityColor.htm)
- [`sim.getGenesisEvents`](sim-1/simGetGenesisEvents.htm)

- [simAddDrawingObject](sim-1/simAddDrawingObject_cpp.htm)
- [simAddDrawingObjectItem](sim-1/simAddDrawingObjectItem_cpp.htm)
- [simRemoveDrawingObject](sim-1/simRemoveDrawingObject_cpp.htm)
- [simGetShapeColor](sim-1/simGetShapeColor_cpp.htm)
- [simSetShapeColor](sim-1/simSetShapeColor_cpp.htm)
- [simGetObjectColor](sim-1/simGetObjectColor_cpp.htm)
- [simSetObjectColor](sim-1/simSetObjectColor_cpp.htm)

## <a id="particleObject"></a>Particle objects

- [`sim.addParticleObject`](sim-1/simAddParticleObject.htm)
- [`sim.addParticleObjectItem`](sim-1/simAddParticleObjectItem.htm)
- [`sim.removeParticleObject`](sim-1/simRemoveParticleObject.htm)

## <a id="modelFunctionality"></a>Models

- [`sim.saveModel`](sim-1/simSaveModel.htm)
- [`sim.loadModel`](sim-1/simLoadModel.htm)
- See also:
- [properties](properties.md)

- [simSaveModel](sim-1/simSaveModel_cpp.htm)
- [simLoadModel](sim-1/simLoadModel_cpp.htm)
- See also:
- [properties](properties.md)

## <a id="sceneObjectSelectionFunctionality"></a>Object selection

- [`sim.getObjectSel`](sim-1/simGetObjectSel.htm)
- [`sim.setObjectSel`](sim-1/simSetObjectSel.htm)
- See also:
- [properties](properties.md)

- [simGetObjectSel](sim-1/simGetObjectSel_cpp.htm)
- [simSetObjectSel](sim-1/simSetObjectSel_cpp.htm)
- See also:
- [properties](properties.md)

## <a id="sceneObjectCreationFunctionality"></a>Object creation

- [`sim.createDummy`](sim-1/simCreateDummy.htm)
- [`sim.createScript`](sim-1/simCreateScript.htm)
- [`sim.createForceSensor`](sim-1/simCreateForceSensor.htm)
- [`sim.createHeightfieldShape`](sim-1/simCreateHeightfieldShape.htm)
- [`sim.createJoint`](sim-1/simCreateJoint.htm)
- [`sim.createShape`](sim-1/simCreateShape.htm)
- [`sim.createProximitySensor`](sim-1/simCreateProximitySensor.htm)
- [`sim.createPrimitiveShape`](sim-1/simCreatePrimitiveShape.htm)
- [`sim.createVisionSensor`](sim-1/simCreateVisionSensor.htm)
- [`sim.createOctree`](sim-1/simCreateOctree.htm)
- [`sim.createPointCloud`](sim-1/simCreatePointCloud.htm)
- [`sim.createTexture`](sim-1/simCreateTexture.htm)
- [`sim.generateTextShape`](sim-1/simGenerateTextShape.htm)
- [`sim.generateShapeFromPath`](sim-1/simGenerateShapeFromPath.htm)

- [simCreateDummy](sim-1/simCreateDummy_cpp.htm)
- [simCreateScript](sim-1/simCreateScript_cpp.htm)
- [simCreateForceSensor](sim-1/simCreateForceSensor_cpp.htm)
- [simCreateHeightfieldShape](sim-1/simCreateHeightfieldShape_cpp.htm)
- [simCreateJoint](sim-1/simCreateJoint_cpp.htm)
- [simCreateShape](sim-1/simCreateShape_cpp.htm)
- [simCreateProximitySensor](sim-1/simCreateProximitySensor_cpp.htm)
- [simCreatePrimitiveShape](sim-1/simCreatePrimitiveShape_cpp.htm)
- [simCreateVisionSensor](sim-1/simCreateVisionSensor_cpp.htm)
- [simCreateOctree](sim-1/simCreateOctree_cpp.htm)
- [simCreatePointCloud](sim-1/simCreatePointCloud_cpp.htm)
- [simCreateTexture](sim-1/simCreateTexture_cpp.htm)
- [simGenerateShapeFromPath](sim-1/simGenerateShapeFromPath_cpp.htm)

## <a id="SimulationFunctionality"></a>Simulation

- [`sim.startSimulation`](sim-1/simStartSimulation.htm)
- [`sim.pauseSimulation`](sim-1/simPauseSimulation.htm)
- [`sim.stopSimulation`](sim-1/simStopSimulation.htm)
- [`sim.getSimulationState`](sim-1/simGetSimulationState.htm)
- [`sim.getSimulationTime`](sim-1/simGetSimulationTime.htm)
- [`sim.getSimulationTimeStep`](sim-1/simGetSimulationTimeStep.htm)
- See also:
- [properties](properties.md)

- [simStartSimulation](sim-1/simStartSimulation_cpp.htm)
- [simPauseSimulation](sim-1/simPauseSimulation_cpp.htm)
- [simStopSimulation](sim-1/simStopSimulation_cpp.htm)
- [simGetSimulationState](sim-1/simGetSimulationState_cpp.htm)
- [simGetSimulationTime](sim-1/simGetSimulationTime_cpp.htm)
- [simGetSimulationTimeStep](sim-1/simGetSimulationTimeStep_cpp.htm)
- See also:
- [properties](properties.md)

## <a id="threads"></a><a id="threadRelatedFunctionality"></a>Threads

- [`sim.setStepping`](sim-1/simSetStepping.htm)
- [`sim.step`](sim-1/simStep.htm)
- [`sim.setAutoYieldDelay`](sim-1/simSetAutoYieldDelay.htm)
- [`sim.acquireLock`](sim-1/simAcquireLock.htm)
- [`sim.releaseLock`](sim-1/simReleaseLock.htm)
- [`sim.getSimulationStopping`](sim-1/simGetSimulationStopping.htm)
- [`sim.handleExtCalls`](sim-1/simHandleExtCalls.htm)

## <a id="pose"></a><a id="transformation"></a><a id="transformations"></a><a id="coordinatesAndTransformations"></a>Transformations

- [`sim.buildMatrix`](sim-1/simBuildMatrix.htm)
- [`sim.buildPose`](sim-1/simBuildPose.htm)
- [`sim.getEulerAnglesFromMatrix`](sim-1/simGetEulerAnglesFromMatrix.htm)
- [`sim.matrixToPose`](sim-1/simMatrixToPose.htm)
- [`sim.poseToMatrix`](sim-1/simPoseToMatrix.htm)
- [`sim.multiplyMatrices`](sim-1/simMultiplyMatrices.htm)
- [`sim.multiplyPoses`](sim-1/simMultiplyPoses.htm)
- [`sim.interpolateMatrices`](sim-1/simInterpolateMatrices.htm)
- [`sim.interpolatePoses`](sim-1/simInterpolatePoses.htm)
- [`sim.getMatrixInverse`](sim-1/simGetMatrixInverse.htm)
- [`sim.getPoseInverse`](sim-1/simGetPoseInverse.htm)
- [`sim.getObjectMatrix`](sim-1/simGetObjectMatrix.htm)
- [`sim.setObjectMatrix`](sim-1/simSetObjectMatrix.htm)
- [`sim.getObjectPose`](sim-1/simGetObjectPose.htm)
- [`sim.setObjectPose`](sim-1/simSetObjectPose.htm)
- [`sim.getObjectPosition`](sim-1/simGetObjectPosition.htm)
- [`sim.setObjectPosition`](sim-1/simSetObjectPosition.htm)
- [`sim.getObjectOrientation`](sim-1/simGetObjectOrientation.htm)
- [`sim.setObjectOrientation`](sim-1/simSetObjectOrientation.htm)
- [`sim.getObjectQuaternion`](sim-1/simGetObjectQuaternion.htm)
- [`sim.setObjectQuaternion`](sim-1/simSetObjectQuaternion.htm)
- [`sim.getObjectChildPose`](sim-1/simGetObjectChildPose.htm)
- [`sim.setObjectChildPose`](sim-1/simSetObjectChildPose.htm)
- [`sim.multiplyVector`](sim-1/simMultiplyVector.htm)
- [`sim.getRotationAxis`](sim-1/simGetRotationAxis.htm)
- [`sim.rotateAroundAxis`](sim-1/simRotateAroundAxis.htm)
- [`sim.getObjectVelocity`](sim-1/simGetObjectVelocity.htm)
- [`sim.alignShapeBB`](sim-1/simAlignShapeBB.htm)
- [`sim.relocateShapeFrame`](sim-1/simRelocateShapeFrame.htm)
- [`sim.abgToYpr`](sim-1/simAbgToYpr.htm)
- [`sim.yprToAbg`](sim-1/simYprToAbg.htm)
- See also:
- [packing/unpacking functions](#packing)

- [simBuildMatrix](sim-1/simBuildMatrix_cpp.htm)
- [simBuildPose](sim-1/simBuildPose_cpp.htm)
- [simGetEulerAnglesFromMatrix](sim-1/simGetEulerAnglesFromMatrix_cpp.htm)
- [simMatrixToPose](sim-1/simMatrixToPose_cpp.htm)
- [simPoseToMatrix](sim-1/simPoseToMatrix_cpp.htm)
- [simMultiplyMatrices](sim-1/simMultiplyMatrices_cpp.htm)
- [simMultiplyPoses](sim-1/simMultiplyPoses_cpp.htm)
- [simInterpolateMatrices](sim-1/simInterpolateMatrices_cpp.htm)
- [simInterpolatePoses](sim-1/simInterpolatePoses_cpp.htm)
- [simInvertMatrix](sim-1/simInvertMatrix_cpp.htm)
- [simInvertPose](sim-1/simInvertPose_cpp.htm)
- [simGetObjectMatrix](sim-1/simGetObjectMatrix_cpp.htm)
- [simSetObjectMatrix](sim-1/simSetObjectMatrix_cpp.htm)
- [simGetObjectPose](sim-1/simGetObjectPose_cpp.htm)
- [simSetObjectPose](sim-1/simSetObjectPose_cpp.htm)
- [simGetObjectPosition](sim-1/simGetObjectPosition_cpp.htm)
- [simSetObjectPosition](sim-1/simSetObjectPosition_cpp.htm)
- [simGetObjectOrientation](sim-1/simGetObjectOrientation_cpp.htm)
- [simSetObjectOrientation](sim-1/simSetObjectOrientation_cpp.htm)
- [simGetObjectQuaternion](sim-1/simGetObjectQuaternion_cpp.htm)
- [simSetObjectQuaternion](sim-1/simSetObjectQuaternion_cpp.htm)
- [simGetObjectChildPose](sim-1/simGetObjectChildPose_cpp.htm)
- [simSetObjectChildPose](sim-1/simSetObjectChildPose_cpp.htm)
- [simTransformVector](sim-1/simTransformVector_cpp.htm)
- [simGetRotationAxis](sim-1/simGetRotationAxis_cpp.htm)
- [simRotateAroundAxis](sim-1/simRotateAroundAxis_cpp.htm)
- [simGetObjectVelocity](sim-1/simGetObjectVelocity_cpp.htm)
- [simAlignShapeBB](sim-1/simAlignShapeBB_cpp.htm)
- [simRelocateShapeFrame](sim-1/simRelocateShapeFrame_cpp.htm)

## Messaging

- [loadPlugin](sim-1/loadPlugin.htm)
- [unloadPlugin](sim-1/unloadPlugin.htm)
- [`sim.addLog`](sim-1/simAddLog.htm)
- [`sim.getSimulatorMessage`](sim-1/simGetSimulatorMessage.htm)
- [`sim.serialCheck`](sim-1/simSerialCheck.htm)
- [`sim.serialClose`](sim-1/simSerialClose.htm)
- [`sim.serialOpen`](sim-1/simSerialOpen.htm)
- [`sim.serialRead`](sim-1/simSerialRead.htm)
- [`sim.serialSend`](sim-1/simSerialSend.htm)
- [`sim.auxiliaryConsoleClose`](sim-1/simAuxiliaryConsoleClose.htm)
- [`sim.auxiliaryConsoleOpen`](sim-1/simAuxiliaryConsoleOpen.htm)
- [`sim.auxiliaryConsolePrint`](sim-1/simAuxiliaryConsolePrint.htm)
- [`sim.callScriptFunction`](sim-1/simCallScriptFunction.htm)
- [`sim.getScriptFunctions`](sim-1/simGetScriptFunctions.htm)
- [`sim.executeScriptString`](sim-1/simExecuteScriptString.htm)
- [`sim.getObjectUid`](sim-1/simGetObjectUid.htm)
- [`sim.getGenesisEvents`](sim-1/simGetGenesisEvents.htm)
- [`sim.broadcastMsg`](sim-1/simBroadcastMsg.htm)
- [`sim.pushUserEvent`](sim-1/simPushUserEvent.htm)
- [`sim.systemSemaphore`](sim-1/simSystemSemaphore.htm)
- See also:
- [signal properties](properties.md#signals)

- [simAddLog](sim-1/simAddLog_cpp.htm)
- [simSetLastError](sim-1/simSetLastError_cpp.htm)
- [simGetSimulatorMessage](sim-1/simGetSimulatorMessage_cpp.htm)
- [simSerialCheck](sim-1/simSerialCheck_cpp.htm)
- [simSerialClose](sim-1/simSerialClose_cpp.htm)
- [simSerialOpen](sim-1/simSerialOpen_cpp.htm)
- [simSerialRead](sim-1/simSerialRead_cpp.htm)
- [simSerialSend](sim-1/simSerialSend_cpp.htm)
- [simAuxiliaryConsoleClose](sim-1/simAuxiliaryConsoleClose_cpp.htm)
- [simAuxiliaryConsoleOpen](sim-1/simAuxiliaryConsoleOpen_cpp.htm)
- [simAuxiliaryConsolePrint](sim-1/simAuxiliaryConsolePrint_cpp.htm)
- [simCallScriptFunctionEx](sim-1/simCallScriptFunctionEx_cpp.htm)
- [simExecuteScriptString](sim-1/simExecuteScriptString_cpp.htm)
- [simGetObjectUid](sim-1/simGetObjectUid_cpp.htm)
- See also:
- [signal properties](properties.md#signals)

## <a id="textures"></a>Textures

- [`sim.getTextureId`](sim-1/simGetTextureId.htm)
- [`sim.getShapeTextureId`](sim-1/simGetShapeTextureId.htm)
- [`sim.readTexture`](sim-1/simReadTexture.htm)
- [`sim.saveImage`](sim-1/simSaveImage.htm)
- [`sim.loadImage`](sim-1/simLoadImage.htm)
- [`sim.getScaledImage`](sim-1/simGetScaledImage.htm)
- [`sim.transformImage`](sim-1/simTransformImage.htm)
- [`sim.writeTexture`](sim-1/simWriteTexture.htm)
- [`sim.createTexture`](sim-1/simCreateTexture.htm)
- [`sim.setShapeTexture`](sim-1/simSetShapeTexture.htm)
- See also:
- [properties](properties.md)

- [simApplyTexture](sim-1/simApplyTExture_cpp.htm)
- [simGetTextureId](sim-1/simGetTextureId_cpp.htm)
- [simGetShapeTextureId](sim-1/simGetShapeTextureId_cpp.htm)
- [simReadTexture](sim-1/simReadTexture_cpp.htm)
- [simSaveImage](sim-1/simSaveImage_cpp.htm)
- [simLoadImage](sim-1/simLoadImage_cpp.htm)
- [simGetScaledImage](sim-1/simGetScaledImage_cpp.htm)
- [simTransformImage](sim-1/simTransformImage_cpp.htm)
- [simWriteTexture](sim-1/simWriteTexture_cpp.htm)
- [simCreateTexture](sim-1/simCreateTexture_cpp.htm)
- [simSetShapeTexture](sim-1/simSetShapeTexture_cpp.htm)
- See also:
- [properties](properties.md)

## <a id="blockingFunctions"></a>Blocking functions

- [`sim.wait`](sim-1/simWait.htm)
- [`sim.moveToConfig`](sim-1/simMoveToConfig.htm)
- [`sim.moveToPose`](sim-1/simMoveToPose.htm)
- [`sim.serialRead`](sim-1/simSerialRead.htm)
- [`sim.systemSemaphore`](sim-1/simSystemSemaphore.htm)

## <a id="auxiliaryConsoles"></a><a id="auxiliaryConsoleFunctions"></a>Auxiliary consoles

- [`sim.auxiliaryConsoleClose`](sim-1/simAuxiliaryConsoleClose.htm)
- [`sim.auxiliaryConsoleOpen`](sim-1/simAuxiliaryConsoleOpen.htm)
- [`sim.auxiliaryConsolePrint`](sim-1/simAuxiliaryConsolePrint.htm)
- [`sim.auxiliaryConsoleShow`](sim-1/simAuxiliaryConsoleShow.htm)
- See also:
- [Custom user interfaces](customUIPlugin.md)

- [simAuxiliaryConsoleClose](sim-1/simAuxiliaryConsoleClose_cpp.htm)
- [simAuxiliaryConsoleOpen](sim-1/simAuxiliaryConsoleOpen_cpp.htm)
- [simAuxiliaryConsolePrint](sim-1/simAuxiliaryConsolePrint_cpp.htm)
- [simAuxiliaryConsoleShow](sim-1/simAuxiliaryConsoleShow_cpp.htm)

## <a id="textEditors"></a>Text/code editors

- [`sim.textEditorClose`](sim-1/simTextEditorClose.htm)
- [`sim.textEditorGetInfo`](sim-1/simTextEditorGetInfo.htm)
- [`sim.textEditorOpen`](sim-1/simTextEditorOpen.htm)
- [`sim.textEditorShow`](sim-1/simTextEditorShow.htm)
- See also:
- [Custom user interfaces](customUIPlugin.md)

## <a id="importExport"></a><a id="importExportFunctions"></a>Import/export

- [`sim.importShape`](sim-1/simImportShape.htm)
- [`sim.importMesh`](sim-1/simImportMesh.htm)
- [`sim.exportMesh`](sim-1/simExportMesh.htm)
- [`sim.createTexture`](sim-1/simCreateTexture.htm)
- [`sim.loadImage`](sim-1/simLoadImage.htm)
- [`sim.saveImage`](sim-1/simSaveImage.htm)
- [`sim.generateTextShape`](sim-1/simGenerateTextShape.htm)
- See also:
- [Assimp plugin API reference](simAssimp/simAssimp.htm)

- [simImportShape](sim-1/simImportShape_cpp.htm)
- [simImportMesh](sim-1/simImportMesh_cpp.htm)
- [simExportMesh](sim-1/simExportMesh_cpp.htm)
- [simCreateTexture](sim-1/simCreateTexture_cpp.htm)
- [simLoadImage](sim-1/simLoadImage_cpp.htm)
- [simSaveImage](sim-1/simSaveImage_cpp.htm)

## <a id="PagesAndViewsFunctions"></a>Pages and views

- [`sim.floatingViewAdd`](sim-1/simFloatingViewAdd.htm)
- [`sim.floatingViewRemove`](sim-1/simFloatingViewRemove.htm)
- [`sim.adjustView`](sim-1/simAdjustView.htm)
- [`sim.cameraFitToView`](sim-1/simCameraFitToView.htm)

- [simFloatingViewAdd](sim-1/simFloatingViewAdd_cpp.htm)
- [simFloatingViewRemove](sim-1/simFloatingViewRemove_cpp.htm)
- [simAdjustView](sim-1/simAdjustView_cpp.htm)
- [simCameraFitToView](sim-1/simCameraFitToView_cpp.htm)

## <a id="rml"></a><a id="ruckig"></a>Motion functionality

- [`sim.moveToConfig`](sim-1/simMoveToConfig.htm)
- [`sim.moveToConfig_init`](sim-1/simMoveToConfig_init.htm)
- [`sim.moveToConfig_step`](sim-1/simMoveToConfig_step.htm)
- [`sim.moveToConfig_cleanup`](sim-1/simMoveToConfig_cleanup.htm)
- [`sim.moveToPose`](sim-1/simMoveToPose.htm)
- [`sim.moveToPose_init`](sim-1/simMoveToPose_init.htm)
- [`sim.moveToPose_step`](sim-1/simMoveToPose_step.htm)
- [`sim.moveToPose_cleanup`](sim-1/simMoveToPose_cleanup.htm)
- [`sim.ruckigPos`](sim-1/simRuckigPos.htm)
- [`sim.ruckigVel`](sim-1/simRuckigVel.htm)
- [`sim.ruckigStep`](sim-1/simRuckigStep.htm)
- [`sim.ruckigRemove`](sim-1/simRuckigRemove.htm)

- [simRuckigPos](sim-1/simRuckigPos_cpp.htm)
- [simRuckigVel](sim-1/simRuckigVel_cpp.htm)
- [simRuckigStep](sim-1/simRuckigStep_cpp.htm)
- [simRuckigRemove](sim-1/simRuckigRemove_cpp.htm)

## <a id="packing"></a>Packing / unpacking

- [`sim.packTable`](sim-1/simPackTable.htm)
- [`sim.unpackTable`](sim-1/simUnpackTable.htm)
- [`sim.packUInt8Table`](sim-1/simPackUInt8Table.htm)
- [`sim.unpackUInt8Table`](sim-1/simUnpackUInt8Table.htm)
- [`sim.packUInt16Table`](sim-1/simPackUInt16Table.htm)
- [`sim.unpackUInt16Table`](sim-1/simUnpackUInt16Table.htm)
- [`sim.packUInt32Table`](sim-1/simPackUInt32Table.htm)
- [`sim.unpackUInt32Table`](sim-1/simUnpackUInt32Table.htm)
- [`sim.packInt32Table`](sim-1/simPackInt32Table.htm)
- [`sim.unpackInt32Table`](sim-1/simUnpackInt32Table.htm)
- [`sim.packFloatTable`](sim-1/simPackFloatTable.htm)
- [`sim.unpackFloatTable`](sim-1/simUnpackFloatTable.htm)
- [`sim.packDoubleTable`](sim-1/simPackDoubleTable.htm)
- [`sim.unpackDoubleTable`](sim-1/simUnpackDoubleTable.htm)
- [`sim.transformBuffer`](sim-1/simTransformBuffer.htm)

- [simPackTable](sim-1/simPackTable_cpp.htm)
- [simUnpackTable](sim-1/simUnpackTable_cpp.htm)

## <a id="stacks"></a>Stacks

- [`sim.packTable`](sim-1/simPackTable.htm)
- [`sim.unpackTable`](sim-1/simUnpackTable.htm)

- [simCreateStack](sim-1/simCreateStack_cpp.htm)
- [simReleaseStack](sim-1/simReleaseStack_cpp.htm)
- [simCopyStack](sim-1/simCopyStack_cpp.htm)
- [simPushNullOntoStack](sim-1/simPushNullOntoStack_cpp.htm)
- [simPushBoolOntoStack](sim-1/simPushBoolOntoStack_cpp.htm)
- [simPushInt32OntoStack](sim-1/simPushInt32OntoStack_cpp.htm)
- [simPushInt64OntoStack](sim-1/simPushInt64OntoStack_cpp.htm)
- [simPushFloatOntoStack](sim-1/simPushFloatOntoStack_cpp.htm)
- [simPushDoubleOntoStack](sim-1/simPushDoubleOntoStack_cpp.htm)
- [simPushTextOntoStack](sim-1/simPushTextOntoStack_cpp.htm)
- [simPushStringOntoStack](sim-1/simPushStringOntoStack_cpp.htm)
- [simPushBufferOntoStack](sim-1/simPushBufferOntoStack_cpp.htm)
- [simPushMatrixOntoStack](sim-1/simPushMatrixOntoStack_cpp.htm)
- [simPushUInt8TableOntoStack](sim-1/simPushUInt8TableOntoStack_cpp.htm)
- [simPushInt32TableOntoStack](sim-1/simPushInt32TableOntoStack_cpp.htm)
- [simPushInt64TableOntoStack](sim-1/simPushInt64TableOntoStack_cpp.htm)
- [simPushFloatTableOntoStack](sim-1/simPushFloatTableOntoStack_cpp.htm)
- [simPushDoubleTableOntoStack](sim-1/simPushDoubleTableOntoStack_cpp.htm)
- [simPushTableOntoStack](sim-1/simPushTableOntoStack_cpp.htm)
- [simInsertDataIntoStackTable](sim-1/simInsertDataIntoStackTable_cpp.htm)
- [simGetStackSize](sim-1/simGetStackSize_cpp.htm)
- [simPopStackItem](sim-1/simPopStackItem_cpp.htm)
- [simGetStackItemType](sim-1/simGetStackItemType_cpp.htm)
- [simGetStackStringType](sim-1/simGetStackStringType_cpp.htm)
- [simMoveStackItemToTop](sim-1/simMoveStackItemToTop_cpp.htm)
- [simGetStackBoolValue](sim-1/simGetStackBoolValue_cpp.htm)
- [simGetStackInt32Value](sim-1/simGetStackInt32Value_cpp.htm)
- [simGetStackInt64Value](sim-1/simGetStackInt64Value_cpp.htm)
- [simGetStackFloatValue](sim-1/simGetStackFloatValue_cpp.htm)
- [simGetStackDoubleValue](sim-1/simGetStackDoubleValue_cpp.htm)
- [simGetStackStringValue](sim-1/simGetStackStringValue_cpp.htm)
- [simGetStackMatrix](sim-1/simGetStackMatrix_cpp.htm)
- [simGetStackTableInfo](sim-1/simGetStackTableInfo_cpp.htm)
- [simGetStackUInt8Table](sim-1/simGetStackUInt8Table_cpp.htm)
- [simGetStackInt32Table](sim-1/simGetStackInt32Table_cpp.htm)
- [simGetStackInt64Table](sim-1/simGetStackInt64Table_cpp.htm)
- [simGetStackFloatTable](sim-1/simGetStackFloatTable_cpp.htm)
- [simGetStackDoubleTable](sim-1/simGetStackDoubleTable_cpp.htm)
- [simUnfoldStackTable](sim-1/simUnfoldStackTable_cpp.htm)
- [simDebugStack](sim-1/simDebugStack_cpp.htm)
- [simPackTable](sim-1/simPackTable_cpp.htm)
- [simUnpackTable](sim-1/simUnpackTable_cpp.htm)

## Other commands

- [`sim.addLog`](sim-1/simAddLog.htm)
- [`sim.announceSceneContentChange`](sim-1/simAnnounceSceneContentChange.htm)
- [`sim.getNavigationMode`](sim-1/simGetNavigationMode.htm)
- [`sim.setNavigationMode`](sim-1/simSetNavigationMode.htm)
- [`sim.getPage`](sim-1/simGetPage.htm)
- [`sim.setPage`](sim-1/simSetPage.htm)
- [`sim.getLastInfo`](sim-1/simGetLastInfo.htm)
- [`sim.getPluginName`](sim-1/simGetPluginName.htm)
- [`sim.getPluginInfo`](sim-1/simGetPluginInfo.htm)
- [`sim.setPluginInfo`](sim-1/simsetPluginInfo.htm)
- [`sim.getNavigationMode`](sim-1/simGetNavigationMode.htm)
- [`sim.getSystemTime`](sim-1/simGetSystemTime.htm)
- [`sim.refreshDialogs`](sim-1/simRefreshDialogs.htm)
- [`sim.setAutoYieldDelay`](sim-1/simSetAutoYieldDelay.htm)
- [`sim.step`](sim-1/simStep.htm)
- [`sim.getExplicitHandling`](sim-1/simGetExplicitHandling.htm)
- [`sim.setExplicitHandling`](sim-1/simSetExplicitHandling.htm)
- [`sim.launchExecutable`](sim-1/simLaunchExecutable.htm)
- [`sim.quitSimulator`](sim-1/simQuitSimulator.htm)
- [`sim.getExtensionString`](sim-1/simGetExtensionString.htm)
- [`sim.textEditorClose`](sim-1/simTextEditorClose.htm)
- [`sim.textEditorGetInfo`](sim-1/simTextEditorGetInfo.htm)
- [`sim.textEditorOpen`](sim-1/simTextEditorOpen.htm)
- [`sim.textEditorShow`](sim-1/simTextEditorShow.htm)
- [`sim.getUserVariables`](sim-1/simGetUserVariables.htm)
- [`sim.moduleEntry`](sim-1/simModuleEntry.htm)
- [`sim.getGenesisEvents`](sim-1/simGetGenesisEvents.htm)
- [`sim.pushUserEvent`](sim-1/simPushUserEvent.htm)
- [`sim.systemSemaphore`](sim-1/simSystemSemaphore.htm)
- [`sim.scheduleExecution`](sim-1/simScheduleExecution.htm)
- [`sim.cancelScheduledExecution`](sim-1/simCancelScheduledExecution.htm)
- See also:
- [properties](properties.md)

- [simAddLog](sim-1/simAddLog_cpp.htm)
- [simAnnounceSceneContentChange](sim-1/simAnnounceSceneContentChange_cpp.htm)
- [simGetNavigationMode](sim-1/simGetNavigationMode_cpp.htm)
- [simSetNavigationMode](sim-1/simSetNavigationMode_cpp.htm)
- [simGetPage](sim-1/simGetPage_cpp.htm)
- [simSetPage](sim-1/simSetPage_cpp.htm)
- [simGetLastInfo](sim-1/simGetLastInfo_cpp.htm)
- [simGetLastError](sim-1/simGetLastError_cpp.htm)
- [simSetLastError](sim-1/simSetLastError_cpp.htm)
- [simGetPluginName](sim-1/simGetPluginName_cpp.htm)
- [simGetPluginInfo](sim-1/simGetPluginInfo_cpp.htm)
- [simSetPluginInfo](sim-1/simsetPluginInfo_cpp.htm)
- [simGetNavigationMode](sim-1/simGetNavigationMode_cpp.htm)
- [simRefreshDialogs](sim-1/simRefreshDialogs_cpp.htm)
- [simGetExplicitHandling](sim-1/simGetExplicitHandling_cpp.htm)
- [simSetExplicitHandling](sim-1/simSetExplicitHandling_cpp.htm)
- [simQuitSimulator](sim-1/simQuitSimulator_cpp.htm)
- [simGetExtensionString](sim-1/simGetExtensionString_cpp.htm)
- [simOpenTextEditor](sim-1/simOpenTextEditor_cpp.htm)
- [simCreateBuffer](sim-1/simCreateBuffer_cpp.htm)
- [simReleaseBuffer](sim-1/simReleaseBuffer_cpp.htm)
- [simModuleEntry](sim-1/simModuleEntry_cpp.htm)
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
