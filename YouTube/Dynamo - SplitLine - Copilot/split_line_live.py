# Take a line and split it into multiple lines in Revit Dynamo BIM.

import clr
clr.AddReference('ProtoGeometry')
import Autodesk.DesignScript.Geometry as pt

lines = IN[0]

def split_line(line):
    start = line.StartPoint
    end = line.EndPoint
    def get_midpoint(start, end):
        x = (start.X + end.X) / 2
        y = (start.Y + end.Y) / 2
        return pt.Point.ByCoordinates(x, y, 0)
    mid = get_midpoint(start, end)
    return [pt.Line.ByStartPointEndPoint(start, mid), pt.Line.ByStartPointEndPoint(mid, end)]

OUT = [split_line(line) for line in IN[0]]
 