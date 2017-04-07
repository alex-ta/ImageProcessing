import numpy as np
import cv2
from matplotlib import pyplot as plt

class Point:
    def __init__(self, xV, yV):
        self.x = xV
        self.y = yV

def pointMean(points):
    point = Point(points[0].x, points[0].y);
    for p in range(0,len(points)):
        point.x += points[p].x;
        point.y += points[p].y;
    point.x = int(round(point.x/(len(points)+1)));
    point.y = int(round(point.y/(len(points)+1)));
    return point;



# Load an color image in grayscale
img = cv2.imread('Download.jpg')
height, width = img.shape[:2]
img = img[round(height/2):height,0:width]
img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_g,120,255,cv2.THRESH_BINARY_INV)
allWhite = np.where(thresh == 255)
y = allWhite[0]
x = allWhite[1]
pArray = [[],[]]
mid = width/2

for c in range(0,len(y)):
    if x[c] > mid:
        pArray[0].append(Point(x[c],y[c]))
    else:
        pArray[1].append(Point(x[c],y[c]))

pArray[0].sort(key=lambda x1 : x1.x)
pArray[1].sort(key=lambda x2 : x2.x)

#ymax
#      ymax
#    xmax|xmin
#        0
#0          xmax

p1 = pointMean(pArray[0][0:170])
p2 = pointMean(pArray[0][-170:-1])
p3 = pointMean(pArray[1][0:170])
p4 = pointMean(pArray[1][-170:-1])
#p2 = pArray[1][0]
p3.y = p2.y

print (p1.x)
print (p1.y)
print (p2.x)
print (p2.y)

cv2.line(img,(p1.x,p1.y),(p2.x,p2.y),(255,0,0),5)
cv2.line(img,(p3.x,p3.y),(p4.x,p4.y),(255,0,0),5)


plt.subplot(121),plt.imshow(img)
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(thresh)
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()


#cv2.imshow('image',img)
#cv2.waitKey(0)
