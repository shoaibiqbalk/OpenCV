## Copying & Pasting Parts of the image


import cv2 as cv
import random

img = cv.imread('resources/image-9.jpg')
img = cv.resize(img, (800, 600)) 
cv.imshow('Image', img)

tag = img[500:400, 600:300] # Copy a square of given pixel
# img[100:300, 650:350] = tag



cv.imshow('Manipulated image', tag)        
cv.waitKey(0)
cv.destroyAllWindows()
