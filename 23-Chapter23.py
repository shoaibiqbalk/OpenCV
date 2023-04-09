# Detecting Specific Colors inside python

import cv2 as cv
import numpy as np

img = cv.imread('resources/image-1.jpg') 


cv.imshow('Image', img)
cv.waitKey(0)
cv.destroyAllWindows()