
wb_usr = {
   langs = {"en"},
   start_size = "400",
   contact = "info@coppeliarobotics.com",
   copyright_link = "http://www.coppeliarobotics.com",
   search_link = "http://www.tecgraf.puc-rio.br/webbook",
   copyright_name = "Coppelia Robotics AG",
   title_bgcolor = "midnightblue",
   file_title = "wb",
   start_open = "1"
}

wb_usr.messages = {
  en = {
     title = "CoppeliaSim User Manual",
     bar_title = "User Manual"
  }
}

wb_usr.tree =
{
    name={en="CoppeliaSim User Manual"},
    link="welcome.htm",
    folder=
    {
        {
            name={en="Main features"},
            link="coppeliaSimFeatures.htm",
            folder=
            {
                {
                    name={en="Overview in other languages"},
                    link="overviewTranslations.htm",
                },
            }
        },
        {
            name={en="Version history"},
            link="versionInfo.htm",
        },
        {
            name={en="Licensing"},
            link="licensing.htm",
        },
        {
            name={en="Acknowledgments"},
            link="acknowledgments.htm",
        },
        {
            name={en="User interface"},
            link="userInterface.htm",
            folder=
            {
                {
                    name={en="Pages and views"},
                    link="pagesAndViews.htm"
                },
                {
                    name={en="Position/orientation manipulation"},
                    link="coordinateDialog.htm",
                    folder=
                    {
                        {
                            name={en="Position dialog"},
                            link="positionDialog.htm"
                        },
                        {
                            name={en="Orientation dialog"},
                            link="orientationDialog.htm"
                        },
                        {
                            name={en="Object movement via the mouse"},
                            link="objectMovement.htm"
                        },
                    }
                },
                {
                    name={en="On positions and orientations"},
                    link="positionOrientationTransformation.htm"
                },
                {
                    name={en="User settings"},
                    link="settings.htm"
                },
                {
                    name={en="Shortcuts"},
                    link="shortcuts.htm"
                },
            }
        },
        {
            name={en="Scenes and models"},
            link="scenesAndModels.htm",
            folder=
            {
                {
                    name={en="Scenes"},
                    link="scenes.htm"
                },
                {
                    name={en="Models"},
                    link="models.htm",
                    folder=
                    {
                        {
                            name={en="Model dialog"},
                            link="modelDialog.htm"
                        },
                    }
                },
            }
        },
        {
            name={en="Environment"},
            link="environment.htm",
            folder=
            {
                {
                    name={en="Environment dialog"},
                    link="environmentPropertiesDialog.htm"
                },
                {
                    name={en="Texture dialog"},
                    link="textureDialog.htm"
                },
            }
        },
        {
            name={en="Scene objects"},
            link="objects.htm",
            folder=
            {
                {
                    name={en="Entities"},
                    link="entities.htm",
                    folder=
                    {
                        {
                            name={en="Collections"},
                            link="collections.htm",
                        },
                    }
                },
                {
                    name={en="Scene object dialog"},
                    link="sceneObjectPropertiesDialog.htm",
                    folder=
                    {
                        {
                            name={en="General scene object properties dialog"},
                            link="commonPropertiesDialog.htm"
                        },
                    }
                },
                {
                    name={en="Collidable objects"},
                    link="collidableObjects.htm"
                },
                {
                    name={en="Measurable objects"},
                    link="measurableObjects.htm"
                },
                {
                    name={en="Detectable objects"},
                    link="detectableObjects.htm"
                },
                {
                    name={en="Viewable objects"},
                    link="viewableObjects.htm"
                },
                {
                    name={en="Layer selection dialog"},
                    link="layerSelectionDialog.htm"
                },
                {
                    name={en="Cameras"},
                    link="cameras.htm",
                    folder=
                    {
                        {
                            name={en="Camera dialog"},
                            link="cameraPropertiesDialog.htm"
                        },
                    }
                },
                {
                    name={en="Lights"},
                    link="lights.htm",
                    folder=
                    {
                        {
                            name={en="Light dialog"},
                            link="lightPropertiesDialog.htm"
                        },
                    }
                },
                {
                    name={en="Shapes"},
                    link="shapes.htm",
                    folder=
                    {
                        {
                            name={en="Shape coordinate frame"},
                            link="shapeReferenceFrames.htm"
                        },
                        {
                            name={en="Primitive shapes"},
                            link="primitiveShapes.htm"
                        },
                        {
                            name={en="Shape dialog"},
                            link="shapeProperties.htm",
                            folder=
                            {
                                {
                                    name={en="Shape dynamics dialog"},
                                    link="shapeDynamicsProperties.htm"
                                },
                                {
                                    name={en="Shape geometry dialog"},
                                    link="geometryDialog.htm"
                                },
                            }
                        },
                        {
                            name={en="Shape edit modes"},
                            link="shapeEditModes.htm",
                            folder=
                            {
                                {
                                    name={en="Triangle edit mode"},
                                    link="triangleEditMode.htm"
                                },
                                {
                                    name={en="Vertex edit mode"},
                                    link="vertexEditMode.htm"
                                },
                                {
                                    name={en="Edge edit mode"},
                                    link="edgeEditMode.htm"
                                },
                                {
                                    name={en="Edit mode for compound shapes"},
                                    link="groupedShapeEditMode.htm"
                                },
                            }
                        },
                    }
                },
                {
                    name={en="Joints"},
                    link="joints.htm",
                    folder=
                    {
                        {
                            name={en="Joint modes"},
                            link="jointModes.htm"
                        },
                        {
                            name={en="Joint dialog"},
                            link="jointProperties.htm",
                            folder=
                            {
                                {
                                    name={en="Joint dynamics dialog"},
                                    link="jointDynamicsProperties.htm"
                                },
                            }
                        },
                    }
                },
                {
                    name={en="Dummies"},
                    link="dummies.htm",
                    folder=
                    {
                        {
                            name={en="Dummy dialog"},
                            link="dummyPropertiesDialog.htm"
                        },
                    }
                },
                {
                    name={en="Graphs"},
                    link="graphs.htm",
                    folder=
                    {
                        {
                            name={en="Graph dialog"},
                            link="graphPropertiesDialog.htm"
                        },
                    }
                },
                {
                    name={en="Proximity sensors"},
                    link="proximitySensors.htm",
                    folder=
                    {
                        {
                            name={en="Proximity sensor types and mode of operation"},
                            link="proximitySensorDescription.htm"
                        },
                        {
                            name={en="Proximity sensor dialog"},
                            link="proximitySensorPropertiesDialog.htm",
                            folder=
                            {
                                {
                                    name={en="Proximity sensor volume dialog"},
                                    link="proximitySensorVolumeDialog.htm"
                                },
                                {
                                    name={en="Proximity sensor detection parameter dialog"},
                                    link="proximitySensorDetectionParameterDialog.htm"
                                },
                            }
                        },
                    }
                },
                {
                    name={en="Vision sensors"},
                    link="visionSensors.htm",
                    folder=
                    {
                        {
                            name={en="Vision sensor types and mode of operation"},
                            link="visionSensorDescription.htm"
                        },
                        {
                            name={en="Vision sensor dialog"},
                            link="visionSensorPropertiesDialog.htm"
                        },
                    }
                },
                {
                    name={en="Force sensors"},
                    link="forceSensors.htm",
                    folder=
                    {
                        {
                            name={en="Force sensor dialog"},
                            link="forceSensorPropertiesDialog.htm"
                        },
                    }
                },
                {
                    name={en="OC trees"},
                    link="octrees.htm",
                    folder=
                    {
                        {
                            name={en="OC tree dialog"},
                            link="octreePropertiesDialog.htm"
                        },
                    }
                },
                {
                    name={en="Point clouds"},
                    link="pointClouds.htm",
                    folder=
                    {
                        {
                            name={en="Point cloud dialog"},
                            link="pointCloudPropertiesDialog.htm"
                        },
                    }
                },
                {
                    name={en="Paths"},
                    link="paths.htm"
                },
                {
                    name={en="Script objects"},
                    link="scriptObjects.htm",
                    folder=
                    {
                        {
                            name={en="Simulation scripts"},
                            link="simulationScripts.htm",
                        },
                        {
                            name={en="Customization scripts"},
                            link="customizationScripts.htm"
                        },
                        {
                            name={en="Script editor"},
                            link="scriptEditor.htm"
                        },
                        {
                            name={en="Script dialog"},
                            link="scriptPropertiesDialog.htm"
                        },
                    }
                },
            }
        },
        {
            name={en="Functionality"},
            link="functionality.htm",
            folder=
            {
                {
                    name={en="Geometry / mesh"},
                    link="geometricCalculations.htm",
                    folder=
                    {
                        {
                            name={en="Collision detection"},
                            link="collisionDetection.htm"
                        },
                        {
                            name={en="Distance calculation"},
                            link="distanceCalculation.htm"
                        },
                        {
                            name={en="Geometric plugin"},
                            link="geometricPlugin.htm",
                            folder=
                            {
                                {
                                    name={en="simGeom API reference"},
                                    link="simGeom.htm?view=category"
                                },
                            }
                        },
                        {
                            name={en="Coppelia geometric routines"},
                            link="coppeliaGeometricRoutines.htm",
                            folder=
                            {
                                {
                                    name={en="API reference"},
                                    link="coppeliaGeometricRoutines-api.htm?view=category"
                                },
                            }
                        },
                        {
                            name={en="simConvex API reference"},
                            link="simConvex.htm?view=alphabetical",
                            folder=
                            {
                                {
                                    name={en="Convex hull"},
                                    link="convexHull.htm"
                                },
                                {
                                    name={en="Convex decomposition"},
                                    link="convexDecomposition.htm"
                                },
                            }
                        },
                        {
                            name={en="simOpenMesh API reference"},
                            link="simOpenMesh.htm?view=alphabetical"
                        },
                        {
                            name={en="simIGL API reference"},
                            link="simIGL.htm?view=alphabetical"
                        },
                    }
                },
                {
                    name={en="Kinematics"},
                    link="kinematics.htm",
                    folder=
                    {
                        {
                            name={en="Solving IK and FK tasks"},
                            link="solvingIkAndFk.htm"
                        },
                        {
                            name={en="Kinematics plugin"},
                            link="kinematicsPlugin.htm",
                            folder=
                            {
                                {
                                    name={en="simIK API reference"},
                                    link="simIK.htm?view=category"
                                },
                            }
                        },
                        {
                            name={en="Coppelia kinematics routines"},
                            link="coppeliaKinematicsRoutines.htm",
                            folder=
                            {
                                {
                                    name={en="API reference"},
                                    link="coppeliaKinematicsRoutines-api.htm?view=category"
                                },
                            }
                        },
                    }
                },
                {
                    name={en="Dynamics"},
                    link="dynamicsModule.htm",
                    folder=
                    {
                        {
                            name={en="Designing dynamic simulations"},
                            link="designingDynamicSimulations.htm"
                        },
                        {
                            name={en="Physics engine differences"},
                            link="physicsEngineDifferences.htm",
                            folder=
                            {
                                {
                                    name={en="simMujoco API reference"},
                                    link="simMujoco.htm"
                                },
                            }
                        },
                    }
                },
				{
					name={en="Data visualization/output"},
					link="dataVisualizationAndOutput.htm",
                    folder=
                    {
                        {
                            name={en="Web-browser based front-end"},
                            link="externalFrontEnd.htm"
                        },
                    }
				},
				{
					name={en="Data manipulation/transformation"},
					link="dataTransformation.htm"
				},
				{
					name={en="Messaging/interfaces/connectivity"},
					link="meansOfCommunication.htm",
                    folder=
                    {
                        {
                            name={en="Remote API"},
                            link="remoteApiOverview.htm",
                            folder=
                            {
                                {
                                    name={en="ZeroMQ remote API"},
                                    link="zmqRemoteApiOverview.htm",
                                },
                                {
                                    name={en="WebSocket remote API"},
                                    link="wsRemoteApiOverview.htm",
                                },
                            }
                        },
                        {
                            name={en="ROS Interfaces"},
                            link="rosInterfaces.htm",
                            folder=
                            {
                                {
                                    name={en="ROS Interface"},
                                    link="rosInterf.htm",
                                    folder=
                                    {
                                        {
                                            name={en="simROS API reference"},
                                            link="simROS.htm?view=alphabetical"
                                        },
                                    }
                                },
                                {
                                    name={en="ROS 2 Interface"},
                                    link="ros2Interface.htm",
                                    folder=
                                    {
                                        {
                                            name={en="simROS2 API reference"},
                                            link="simROS2.htm?view=alphabetical"
                                        },
                                    }
                                },
                            }
                        },
                        {
                            name={en="simZMQ API reference"},
                            link="simZMQ.htm?view=alphabetical",
                        },
                        {
                            name={en="simWS API reference"},
                            link="simWS.htm?view=alphabetical",
                        },
                    }
				},
				{
					name={en="Paths/trajectories"},
					link="pathsAndTrajectories.htm"
				},
                {
                    name={en="Path planning"},
                    link="pathAndMotionPlanningModules.htm",
                    folder=
                    {
                        {
                            name={en="simOMPL API reference"},
                            link="simOMPL.htm?view=alphabetical"
                        },
                    }
                },
                {
                    name={en="Synthetic vision"},
                    link="syntheticVision.htm",
                    folder=
                    {
                        {
                            name={en="simIM API reference"},
                            link="simIM.htm?view=alphabetical"
                        },
                        {
                            name={en="simVision API reference"},
                            link="simVision.htm?view=category"
                        },
                    }
                },
                {
                    name={en="Custom user interfaces"},
                    link="customUIPlugin.htm",
                    folder=
                    {
                        {
                            name={en="simUI API reference"},
                            link="simUI.htm?view=alphabetical"
                        },
                        {
                            name={en="simUI XML syntax"},
                            link="simUI-widgets.htm"
                        },
                        {
                            name={en="simQML API reference"},
                            link="simQML.htm?view=alphabetical"
                        },
                    }
                },
                {
                    name={en="Import/export"},
                    link="importExport.htm",
                    folder=
                    {
                        {
                            name={en="XML format"},
                            link="xmlFormat.htm"
                        },
                        {
                            name={en="URDF format"},
                            link="urdfPlugin.htm",
                            folder=
                            {
                                {
                                    name={en="simURDF API reference"},
                                    link="simURDF.htm?view=alphabetical"
                                },
                            }
                        },
                        {
                            name={en="SDF format"},
                            link="sdfPlugin.htm",
                            folder=
                            {
                                {
                                    name={en="simSDF API reference"},
                                    link="simSDF.htm?view=alphabetical"
                                },
                            }
                        },
                        {
                            name={en="Video exporter"},
                            link="aviRecorder.htm"
                        },
                        {
                            name={en="simAssimp API reference"},
                            link="simAssimp.htm?view=alphabetical"
                        },
                        {
                            name={en="simGLTF API reference"},
                            link="simGLTF.htm?view=alphabetical"
                        },
                        {
                            name={en="simLDraw API reference"},
                            link="simLDraw.htm?view=alphabetical"
                        },
                    }
                },
                {
                    name={en="Commands/setting"},
                    link="commandLine.htm",
                    folder=
                    {
                        {
                            name={en="simCmd API reference"},
                            link="simCmd.htm?view=alphabetical"
                        },
                    }
                },
                {
                    name={en="Miscellaneous"},
                    link="miscellaneousFunctionality.htm",
                    folder=
                    {
                        {
                            name={en="simSurfRec API reference"},
                            link="simSurfRec.htm?view=alphabetical"
                        },
                        {
                            name={en="simICP API reference"},
                            link="simICP.htm?view=alphabetical"
                        },
                        {
                            name={en="simSubprocess API reference"},
                            link="simSubprocess.htm?view=alphabetical"
                        },
                        {
                            name={en="simEigen API reference"},
                            link="simEigen.htm?view=alphabetical"
                        },
                    }
                },
            }
        },
        {
            name={en="Writing code"},
            link="writingCode.htm",
            folder=
            {
                {
                    name={en="Scripting"},
                    link="scripts.htm",
                    folder=
                    {
                        {
                            name={en="Embedded scripts"},
                            link="embeddedScripts.htm",
                            folder=
                            {
                                {
                                    name={en="The main script"},
                                    link="mainScript.htm"
                                },
                            }
                        },
                        {
                            name={en="Add-ons"},
                            link="addOns.htm"
                        },
                        {
                            name={en="The sandbox"},
                            link="sandboxScript.htm"
                        },
                        {
                            name={en="Threaded and non-threaded script code"},
                            link="threadedAndNonThreadedCode.htm"
                        },
                        {
                            name={en="Callback functions"},
                            link="callbackFunctions.htm",
                            folder=
                            {
                                {
                                    name={en="Dynamics callback functions"},
                                    link="dynCallbackFunctions.htm"
                                },
                                {
                                    name={en="Joint callback functions"},
                                    link="jointCallbackFunctions.htm"
                                },
                                {
                                    name={en="Contact callback function"},
                                    link="contactCallbackFunction.htm"
                                },
                                {
                                    name={en="Vision callback functions"},
                                    link="visionCallbackFunctions.htm"
                                },
                                {
                                    name={en="Trigger callback functions"},
                                    link="triggerCallbackFunctions.htm"
                                },
                                {
                                    name={en="User config callback functions"},
                                    link="userConfigCallbackFunctions.htm"
                                },
                            }
                        },
                        {
                            name={en="Script execution order"},
                            link="scriptExecution.htm"
                        },                                
                        {
                            name={en="Buffers"},
                            link="buffers.htm"
                        },                                
                        {
                            name={en="Lua vs Python scripts"},
                            link="luaPythonDifferences.htm"
                        },
                        {
                            name={en="Lua crash course"},
                            link="luaCrashCourse.htm"
                        },
                    }
                },
                {
                    name={en="Plugins"},
                    link="plugins.htm"
                },
                {
                    name={en="CoppeliaSim's library"},
                    link="coppeliaSimLibrary.htm"
                },
                {
                    name={en="Accessing scene objects programmatically"},
                    link="accessingSceneObjects.htm"
                },
                {
                    name={en="Explicit and non-explicit calls"},
                    link="explicitHandling.htm"
                },
                {
                    name={en="CoppeliaSim API framework"},
                    link="apisOverview.htm",
                    folder=
                    {
                        {
                            name={en="Regular API reference"},
                            link="apiFunctions.htm"
                        },
                        {
                            name={en="Regular API constants"},
                            link="apiConstants.htm"
                        },
                        {
                            name={en="Properties"},
                            link="properties.htm",
                            folder=
                            {
                                {
                                    name={en="Properties reference"},
                                    link="propertiesReference.htm"
                                },
                            }
                        },
                    }
                },
            }
        },
        {
            name={en="Simulation"},
            link="simulation.htm",
            folder=
            {
                {
                    name={en="Simulation dialog"},
                    link="simulationPropertiesDialog.htm"
                },
            }
        },
        {
            name={en="Tutorials"},
            link="tutorials.htm",
            folder=
            {
                {
                    name={en="BubbleRob tutorial"},
                    link="bubbleRobTutorial.htm"
                },
                {
                    name={en="Building a clean model tutorial"},
                    link="buildingAModelTutorial.htm"
                },
                {
                    name={en="Line following BubbleRob tutorial"},
                    link="lineFollowingBubbleRobTutorial.htm"
                },
                {
                    name={en="Inverse kinematics tutorial"},
                    link="inverseKinematicsTutorial.htm"
                },
                {
                    name={en="External controller tutorial"},
                    link="externalControllerTutorial.htm"
                },
                {
                    name={en="Plugin tutorial"},
                    link="pluginTutorial.htm"
                },
                {
                    name={en="Robot language interpreter integration tutorial"},
                    link="robotLanguageIntegrationTutorial.htm"
                },
                {
                    name={en="ROS tutorials"},
                    link="rosTutorial.htm",
                    folder=
                    {
                        {
                            name={en="ROS tutorial"},
                            link="ros1Tutorial.htm"
                        },
                        {
                            name={en="ROS 2 tutorial"},
                            link="ros2Tutorial.htm"
                        },
                    }
                },
            }
        },
        {
            name={en="Compiling CoppeliaSim"},
            link="compilingCoppeliaSim.htm",
        },
    }
}

