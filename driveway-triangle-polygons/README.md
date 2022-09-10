# Driveway triangle polygons

## Overview
[driveway-triangle-polygons-pyqgis-script.py](driveway-triangle-polygons-pyqgis-script.py) is a PyQGIS script to assist with drawing driveway sight triangles with PyQGIS. This allows for accurate and precise drawings.

## Configuration
Configure the program by editing the first few lines of [driveway-triangle-polygons-pyqgis-script.py](driveway-triangle-polygons-pyqgis-script.py).

- LEG_LENGTH_IN_FEET is the size of the driveway triangle. Currently, the program only supports right isosceles triangles.

## Setup/usage
1. Download [QGIS](https://www.qgis.org/en/site/) and start/open a project.
2. From the top menu, open Plugins > Python Console.
3. Within the console, open the editor and paste in the contents of [driveway-triangle-polygons-pyqgis-script.py](driveway-triangle-polygons-pyqgis-script.py).
4. Within QGIS, open a polygon layer, select it, and enable editing if it is not already enabled.
5. Click to run the script.
6. Click to mark the center of the triangle cluster (the right angle corner).
7. Click again to angle and place the triangle cluster.
8. Repeat as many times as necessary.
9. Use the delete tool from the advanced digitizing toolbar to delete extra triangles, leaving an appropriate driveway triangle(s). Note that, if you use the delete tool, you will have to click to run the script again.

## Notes
- See [demo.mov](demo.mov) for a demo.
