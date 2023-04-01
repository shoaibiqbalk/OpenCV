## Image manipulation using pixels

import cv2 as cv
import random

img = cv.imread('resources/image-2.jpg')
img = cv.resize(img, (800, 600)) 
cv.imshow('Image', img)

for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

cv.imshow('Manipulated image', img)        
cv.waitKey(0)
cv.destroyAllWindows()
