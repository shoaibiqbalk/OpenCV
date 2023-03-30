# Reading an Image and Displaying it
# library import
import cv2 as cv

img = cv.imread('resources/image-1.jpg')

cv.imshow('First Image', img)

cv.waitKey(0)