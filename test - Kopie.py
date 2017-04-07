import numpy as np
import cv2
from matplotlib import pyplot as plt

# Load an color image in grayscale
img = cv2.imread('Download5.jpg')
height,width = img.shape[:2]
img = img[round(height/2):height,0:width]


img1_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img2 =  cv2.pyrMeanShiftFiltering(img, 5, 70, 50);
edges = cv2.Canny(img1_g,300,200)
edges2 = cv2.Canny(img2,300,200)

ied = edges - edges2

kernel = np.ones((3,3),np.float32)/10
dst = cv2.filter2D(ied,-1,kernel)

ret, thresh = cv2.threshold(dst,100,255,cv2.THRESH_BINARY_INV)


plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(thresh,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()


#cv2.imshow('image',img)
#cv2.waitKey(0)
