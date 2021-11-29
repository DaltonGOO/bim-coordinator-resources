# create a circle by best fit through points
import random
import clr
clr.AddReference('ProtoGeometry')
import Autodesk.DesignScript.Geometry as pt


def random_points(n):
    points = []
    for i in range(n):
        x = random.random()
        y = random.random()
        points.append(pt.Point.ByCoordinates(x, y, 0))
    return points
    
def ByBestFitThroughPoints(points):
    return pt.Circle.ByBestFitThroughPoints(points)
    

OUT = ByBestFitThroughPoints(random_points(10))
    
