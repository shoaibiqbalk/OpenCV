## Reading an Image, Resizing and Displaying it

# library import
import cv2 as cv

img = cv.imread('resources/image-1.jpg')
img = cv.resize(img, (800, 600)) 
cv.imshow('First Image', img)

cv.waitKey(0)