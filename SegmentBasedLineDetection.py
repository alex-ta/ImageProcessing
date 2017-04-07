import numpy as np
import cv2
from matplotlib import pyplot as plt
class Point:
    def __init__(self, xV, yV, color):
        self.x = xV
        self.y = yV
        self.color = color

class Split:
    def __init__(self, xStart, xWidth, yStart, yWidth, points):
        self.xStart = xStart
        self.xWidth = xWidth
        self.yStart = yStart
        self.yWidth = yWidth
        self.points = points

class Grid:
    def __init__(self, imgPath):
        self.path = imgPath
        self.img = cv2.imread(imgPath)
        self.height,self.width = self.img.shape[:2]
        self.rects = rectGrid(self.img,10,10)

def pointMean(points):
    point = Point(0,0,0)
    for p in range(0,len(points)):
        point.x += points[p].x
        point.y += points[p].y
        point.color[0] += points[p].color[0]
        point.color[1] += points[p].color[1]
        point.color[2] += points[p].color[2]
    point.x = int(round(point.x/(len(points)+1)))
    point.y = int(round(point.y/(len(points)+1)))
    point.color[0] = int(round(point.color[0]/(len(points)+1)))
    point.color[1] = int(round(point.color[1]/(len(points)+1)))
    point.color[2] = int(round(point.color[2]/(len(points)+1)))

    return point;

def rectGrid(image, xCount, yCount):
    rects = []
    height, width = image.shape[:2]
    xWidth = int(round(width / xCount));
    yWidth = int(round(height / yCount));
    for h in range(yCount):
        for w in range(xCount):
            for y in range(yWidth):
                for x in range(xWidth):
                    if x%xWidth == 0 and y%yWidth == 0:
                        rects.append(Split(x+w*xWidth, xWidth, y+h*yWidth, yWidth, []))
                    rects[-1].points.append(Point(x,y, image[x,y]));
    return rects

def toImage(grid):
    points = []
    for rect in grid.rects:
        if rect.xStart == 0 :
            points.append([])
        points[-1].append(pointMean(rect.points))
    return points


img = Grid('Download5.jpg')
print (toImage(img))
