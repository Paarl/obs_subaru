import lsst.afw.cameraGeom.cameraConfig
assert type(config) == lsst.afw.cameraGeom.cameraConfig.CameraConfig, 'config is of type %s.%s instead of lsst.afw.cameraGeom.cameraConfig.CameraConfig' % (
    type(config).__module__, type(config).__name__)
config.plateScale = 1.0
config.transformDict.nativeSys = 'FocalPlane'
config.transformDict.transforms = {}
config.transformDict.transforms['Focal_Plane_Pixels'] = lsst.afw.geom.transformConfig.TransformConfig()
config.transformDict.transforms['Focal_Plane_Pixels'].transform['multi'].transformDict = None
config.transformDict.transforms['Focal_Plane_Pixels'].transform['affine'].translation = [0.0, 0.0]
config.transformDict.transforms['Focal_Plane_Pixels'].transform['affine'].linear = [1.0, 0.0, 0.0, 1.0]
config.transformDict.transforms['Focal_Plane_Pixels'].transform['radial'].coeffs = None
config.transformDict.transforms['Focal_Plane_Pixels'].transform.name = 'affine'
config.transformDict.transforms['Pupil'] = lsst.afw.geom.transformConfig.TransformConfig()
config.transformDict.transforms['Pupil'].transform['multi'].transformDict = None
config.transformDict.transforms['Pupil'].transform['affine'].translation = [0.0, 0.0]
config.transformDict.transforms['Pupil'].transform['affine'].linear = [1.0, 0.0, 0.0, 1.0]
config.transformDict.transforms['Pupil'].transform['radial'].coeffs = None
config.transformDict.transforms['Pupil'].transform.name = 'identity'
config.detectorList = {}
config.detectorList[0] = lsst.afw.cameraGeom.cameraConfig.DetectorConfig()
config.detectorList[0].bbox_y0 = 0
config.detectorList[0].bbox_y1 = 4176
config.detectorList[0].bbox_x1 = 2047
config.detectorList[0].bbox_x0 = 0
config.detectorList[0].name = 'Ponyo'
config.detectorList[0].pixelSize_x = 1.0
config.detectorList[0].transformDict.nativeSys = None
config.detectorList[0].transformDict.transforms = None
config.detectorList[0].refpos_x = 1023.5
config.detectorList[0].refpos_y = 2088.0
config.detectorList[0].pixelSize_y = 1.0
config.detectorList[0].detectorType = 0
config.detectorList[0].offset_x = -4242.1
config.detectorList[0].offset_y = -2123.13
config.detectorList[0].transposeDetector = None
config.detectorList[0].yawDeg = 0.0
config.detectorList[0].rollDeg = 0.0
config.detectorList[0].serial = '8'
config.detectorList[0].pitchDeg = 0.0
config.detectorList[0].id = 8
config.detectorList[1] = lsst.afw.cameraGeom.cameraConfig.DetectorConfig()
config.detectorList[1].bbox_y0 = 0
config.detectorList[1].bbox_y1 = 4176
config.detectorList[1].bbox_x1 = 2047
config.detectorList[1].bbox_x0 = 0
config.detectorList[1].name = 'Chihiro'
config.detectorList[1].pixelSize_x = 1.0
config.detectorList[1].transformDict.nativeSys = None
config.detectorList[1].transformDict.transforms = None
config.detectorList[1].refpos_x = 1023.5
config.detectorList[1].refpos_y = 2088.0
config.detectorList[1].pixelSize_y = 1.0
config.detectorList[1].detectorType = 0
config.detectorList[1].offset_x = -4245.1
config.detectorList[1].offset_y = 2127.3
config.detectorList[1].transposeDetector = None
config.detectorList[1].yawDeg = 0.0
config.detectorList[1].rollDeg = 0.0
config.detectorList[1].serial = '6'
config.detectorList[1].pitchDeg = 0.0
config.detectorList[1].id = 6
config.detectorList[2] = lsst.afw.cameraGeom.cameraConfig.DetectorConfig()
config.detectorList[2].bbox_y0 = 0
config.detectorList[2].bbox_y1 = 4176
config.detectorList[2].bbox_x1 = 2047
config.detectorList[2].bbox_x0 = 0
config.detectorList[2].name = 'San'
config.detectorList[2].pixelSize_x = 1.0
config.detectorList[2].transformDict.nativeSys = None
config.detectorList[2].transformDict.transforms = None
config.detectorList[2].refpos_x = 1023.5
config.detectorList[2].refpos_y = 2088.0
config.detectorList[2].pixelSize_y = 1.0
config.detectorList[2].detectorType = 0
config.detectorList[2].offset_x = -2120.4
config.detectorList[2].offset_y = -2122.0
config.detectorList[2].transposeDetector = None
config.detectorList[2].yawDeg = 0.0
config.detectorList[2].rollDeg = 0.0
config.detectorList[2].serial = '9'
config.detectorList[2].pitchDeg = 0.0
config.detectorList[2].id = 9
config.detectorList[3] = lsst.afw.cameraGeom.cameraConfig.DetectorConfig()
config.detectorList[3].bbox_y0 = 0
config.detectorList[3].bbox_y1 = 4176
config.detectorList[3].bbox_x1 = 2047
config.detectorList[3].bbox_x0 = 0
config.detectorList[3].name = 'Clarisse'
config.detectorList[3].pixelSize_x = 1.0
config.detectorList[3].transformDict.nativeSys = None
config.detectorList[3].transformDict.transforms = None
config.detectorList[3].refpos_x = 1023.5
config.detectorList[3].refpos_y = 2088.0
config.detectorList[3].pixelSize_y = 1.0
config.detectorList[3].detectorType = 0
config.detectorList[3].offset_x = -2121.2
config.detectorList[3].offset_y = 2129.6
config.detectorList[3].transposeDetector = None
config.detectorList[3].yawDeg = 0.0
config.detectorList[3].rollDeg = 0.0
config.detectorList[3].serial = '7'
config.detectorList[3].pitchDeg = 0.0
config.detectorList[3].id = 7
config.detectorList[4] = lsst.afw.cameraGeom.cameraConfig.DetectorConfig()
config.detectorList[4].bbox_y0 = 0
config.detectorList[4].bbox_y1 = 4176
config.detectorList[4].bbox_x1 = 2047
config.detectorList[4].bbox_x0 = 0
config.detectorList[4].name = 'Satsuki'
config.detectorList[4].pixelSize_x = 1.0
config.detectorList[4].transformDict.nativeSys = None
config.detectorList[4].transformDict.transforms = None
config.detectorList[4].refpos_x = 1023.5
config.detectorList[4].refpos_y = 2088.0
config.detectorList[4].pixelSize_y = 1.0
config.detectorList[4].detectorType = 0
config.detectorList[4].offset_x = 0.0
config.detectorList[4].offset_y = -2126.7
config.detectorList[4].transposeDetector = None
config.detectorList[4].yawDeg = 0.0
config.detectorList[4].rollDeg = 0.0
config.detectorList[4].serial = '5'
config.detectorList[4].pitchDeg = 0.0
config.detectorList[4].id = 5
config.detectorList[5] = lsst.afw.cameraGeom.cameraConfig.DetectorConfig()
config.detectorList[5].bbox_y0 = 0
config.detectorList[5].bbox_y1 = 4176
config.detectorList[5].bbox_x1 = 2047
config.detectorList[5].bbox_x0 = 0
config.detectorList[5].name = 'Fio'
config.detectorList[5].pixelSize_x = 1.0
config.detectorList[5].transformDict.nativeSys = None
config.detectorList[5].transformDict.transforms = None
config.detectorList[5].refpos_x = 1023.5
config.detectorList[5].refpos_y = 2088.0
config.detectorList[5].pixelSize_y = 1.0
config.detectorList[5].detectorType = 0
config.detectorList[5].offset_x = 2.1
config.detectorList[5].offset_y = 2130.3
config.detectorList[5].transposeDetector = None
config.detectorList[5].yawDeg = 0.0
config.detectorList[5].rollDeg = 0.0
config.detectorList[5].serial = '2'
config.detectorList[5].pitchDeg = 0.0
config.detectorList[5].id = 2
config.detectorList[6] = lsst.afw.cameraGeom.cameraConfig.DetectorConfig()
config.detectorList[6].bbox_y0 = 0
config.detectorList[6].bbox_y1 = 4176
config.detectorList[6].bbox_x1 = 2047
config.detectorList[6].bbox_x0 = 0
config.detectorList[6].name = 'Sheeta'
config.detectorList[6].pixelSize_x = 1.0
config.detectorList[6].transformDict.nativeSys = None
config.detectorList[6].transformDict.transforms = None
config.detectorList[6].refpos_x = 1023.5
config.detectorList[6].refpos_y = 2088.0
config.detectorList[6].pixelSize_y = 1.0
config.detectorList[6].detectorType = 0
config.detectorList[6].offset_x = 2129.9
config.detectorList[6].offset_y = -2120.9
config.detectorList[6].transposeDetector = None
config.detectorList[6].yawDeg = 0.0
config.detectorList[6].rollDeg = 0.0
config.detectorList[6].serial = '4'
config.detectorList[6].pitchDeg = 0.0
config.detectorList[6].id = 4
config.detectorList[7] = lsst.afw.cameraGeom.cameraConfig.DetectorConfig()
config.detectorList[7].bbox_y0 = 0
config.detectorList[7].bbox_y1 = 4176
config.detectorList[7].bbox_x1 = 2047
config.detectorList[7].bbox_x0 = 0
config.detectorList[7].name = 'Kiki'
config.detectorList[7].pixelSize_x = 1.0
config.detectorList[7].transformDict.nativeSys = None
config.detectorList[7].transformDict.transforms = None
config.detectorList[7].refpos_x = 1023.5
config.detectorList[7].refpos_y = 2088.0
config.detectorList[7].pixelSize_y = 1.0
config.detectorList[7].detectorType = 0
config.detectorList[7].offset_x = 2123.8
config.detectorList[7].offset_y = 2129.7
config.detectorList[7].transposeDetector = None
config.detectorList[7].yawDeg = 0.0
config.detectorList[7].rollDeg = 0.0
config.detectorList[7].serial = '1'
config.detectorList[7].pitchDeg = 0.0
config.detectorList[7].id = 1
config.detectorList[8] = lsst.afw.cameraGeom.cameraConfig.DetectorConfig()
config.detectorList[8].bbox_y0 = 0
config.detectorList[8].bbox_y1 = 4176
config.detectorList[8].bbox_x1 = 2047
config.detectorList[8].bbox_x0 = 0
config.detectorList[8].name = 'Sophie'
config.detectorList[8].pixelSize_x = 1.0
config.detectorList[8].transformDict.nativeSys = None
config.detectorList[8].transformDict.transforms = None
config.detectorList[8].refpos_x = 1023.5
config.detectorList[8].refpos_y = 2088.0
config.detectorList[8].pixelSize_y = 1.0
config.detectorList[8].detectorType = 0
config.detectorList[8].offset_x = 4247.4
config.detectorList[8].offset_y = -2122.7
config.detectorList[8].transposeDetector = None
config.detectorList[8].yawDeg = 0.0
config.detectorList[8].rollDeg = 0.0
config.detectorList[8].serial = '3'
config.detectorList[8].pitchDeg = 0.0
config.detectorList[8].id = 3
config.detectorList[9] = lsst.afw.cameraGeom.cameraConfig.DetectorConfig()
config.detectorList[9].bbox_y0 = 0
config.detectorList[9].bbox_y1 = 4176
config.detectorList[9].bbox_x1 = 2047
config.detectorList[9].bbox_x0 = 0
config.detectorList[9].name = 'Nausicaa'
config.detectorList[9].pixelSize_x = 1.0
config.detectorList[9].transformDict.nativeSys = None
config.detectorList[9].transformDict.transforms = None
config.detectorList[9].refpos_x = 1023.5
config.detectorList[9].refpos_y = 2088.0
config.detectorList[9].pixelSize_y = 1.0
config.detectorList[9].detectorType = 0
config.detectorList[9].offset_x = 4245.5
config.detectorList[9].offset_y = 2130.0
config.detectorList[9].transposeDetector = None
config.detectorList[9].yawDeg = 0.0
config.detectorList[9].rollDeg = 0.0
config.detectorList[9].serial = '0'
config.detectorList[9].pitchDeg = 0.0
config.detectorList[9].id = 0
config.radialCoeffs = None
config.name = 'Subaru SuprimeCam'
