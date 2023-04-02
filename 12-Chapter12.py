# Corner Detection

import cv2 as cv
import numpy as np

img = cv.imread('resources/chessboard.png')
img = cv.resize(img, (0, 0), fx=0.5, fy=0.5)
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


cv.imshow('Image', img)


cv.waitKey(0)
cv.destroyAllWindows()