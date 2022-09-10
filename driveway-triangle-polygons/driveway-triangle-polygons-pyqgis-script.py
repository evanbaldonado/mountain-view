# IMPORTS
# Note that installing packages/libaries within QGIS might be a separate process on your computer. For me, I have to run: /Applications/QGIS-LTR.app/Contents/MacOS/bin/python3 -m pip install PACKAGENAME
import geopy
import geopy.distance
from geographiclib.geodesic import Geodesic # Needed to get bearing (angle) from two coordinates (geopy cannot do this itself)
import math
from qgis.gui import QgsMapToolEmitPoint # For user input

# CONFIG
LEG_LENGTH_IN_FEET = 25
HYPOTENUSE_LENGTH_IN_FEET = 25 * math.sqrt(2)

global userDefinedPoints
userDefinedPoints = [] # First point will be the center point, second will be along the sidewalk (to determine bearing only; exact distance will be auto-calculated).

# Function that is called when the user clicks the map using the point tool.
def clickFunction(qgisPoint):

    # Select the current layer.
    layer = iface.activeLayer()
    layer.selectAll()

    # Store the clicked point.
    layerPoint = pointTool.toLayerCoordinates(layer, qgisPoint)
    userDefinedPoints.append((layerPoint.x(), layerPoint.y())) # Add point to our list.

    if (len(userDefinedPoints) == 1):
        # Ask the user to input a second point.
        print("Please click a point along the sidewalk. This is to angle the triangle.")
    elif (len(userDefinedPoints) >= 2):
        # Draw the triangles.
        if layer.dataProvider().capabilities() and QgsVectorDataProvider.AddFeatures:

            # Calculate the angle with the two provided points.
            initial_bearing = Geodesic.WGS84.Inverse(userDefinedPoints[0][1], userDefinedPoints[0][0], userDefinedPoints[1][1], userDefinedPoints[1][0])['azi1']

            # Set up the center point.
            centerPoint = userDefinedPoints[0]
            centerGeopyPoint = geopy.Point(centerPoint[1], centerPoint[0])

            # Draw the four triangles.
            for i in range(4):
                secondCornerGeopyPoint = geopy.distance.geodesic(feet=LEG_LENGTH_IN_FEET).destination(centerGeopyPoint, initial_bearing)
                secondCorner = (secondCornerGeopyPoint.longitude, secondCornerGeopyPoint.latitude)

                thirdCornerGeopyPoint = geopy.distance.geodesic(feet=HYPOTENUSE_LENGTH_IN_FEET).destination(secondCornerGeopyPoint, initial_bearing + 135)
                thirdCorner = (thirdCornerGeopyPoint.longitude, thirdCornerGeopyPoint.latitude)

                newTriangle = QgsFeature()
                newTriangle.setGeometry(QgsGeometry.fromPolygonXY( [[ QgsPointXY( pair[0], pair[1] ) for pair in [centerPoint, secondCorner, thirdCorner, centerPoint] ]] ) )
                layer.dataProvider().addFeatures([newTriangle])

                initial_bearing += 90

        # Start over (prepare for a new set of triangles).
        userDefinedPoints.clear()
        print("Please click the main vertex (center of driveway/sidewalk).")

# Obtain a reference to the canvas.
global canvas
canvas = iface.mapCanvas()

# Set up the point tool.
global pointTool
pointTool = QgsMapToolEmitPoint(canvas)
pointTool.canvasClicked.connect(clickFunction)

# Connect the point tool to the canvas.
canvas.setMapTool(pointTool)

# Get started!
print("This tool is designed to help you draw driveway triangles. Please contact mountainview@evanbaldonado.com with any questions.")
print("Please click the main vertex (center of driveway/sidewalk).")
