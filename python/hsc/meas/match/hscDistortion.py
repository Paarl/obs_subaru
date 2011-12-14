import lsst.afw.geom as afwGeom
import lsst.afw.image as afwImage
import lsst.pipette.distortion as pipDist
import hsc.meas.match.distest as distest

class HscDistortion(pipDist.CameraDistortion):
    """ Adapter class for the pipette framework. """
    
    def __init__(self, ccd, config):
        """Constructor

        @param ccd Ccd for distortion (sets position relative to center)
        @param config Configuration for distortion
        """
        self.ccd = ccd
        self.pixelSize = ccd.getPixelSize()
        self.transform = ccd.getGlobalTransform()
        self.inverseTransform = self.transform.invert()

    def _distortPosition(self, x, y, direction=None, elevation=60.0, copy=True):
        """Distort/undistort a position.

        @param x X coordinate to distort. pixels from focal plane center.
        @param y Y coordinate to distort
        @param direction "toIdeal" or "toActual"
        @returns Copy of input source with distorted/undistorted coordinates
        """

        if direction == "toIdeal":
            point = self.transform(afwGeom.makePoint(x, y))
            x, y = point.getX() / self.pixelSize, point.getY() / self.pixelSize
            distX, distY = distest.getUndistortedPosition(x, y, elevation)
            return distX, disty

        if direction == "toActual":
            undistX, undistY = distEst.getDistortedPosition(x, y, elevation)
            point = afwGeom.makePoint(undistX * self.pixelSize, undistY * self.pixelSize)
            point = self.inverseTransform(point)
            return point.getX(), point.getY()

        raise RuntimeError("unknown distortion direction: %s" % (direction))
    
    # Need to get elevation in here -- CPL
    def actualToIdeal(self, sources, copy=True):
        return self._distortSources(sources, direction="toIdeal", copy=copy)

    def idealToActual(self, sources, copy=True):
        return self._distortSources(sources, direction="toActual",  copy=copy)